#!/usr/bin/env bash
set -xeou pipefail

# TODO obtain target branch from github curl
target_branch=master

function master_update() {
    echo "Updating $target_branch branch"

    # reset master branch to its previous commit to create the diff with current
    # NOTE: moving to commit t-1 to obtain diffs assumes a consistent squash-and-merge scheme, which
    # therefore only creates one commit per pull request
    git checkout -b temp
    git reset --hard $(git log | grep "^commit [a-zA-Z0-9]*$" | head -n1 | cut -d ' ' -f2)
    diff_output=$(git diff --diff-filter=D ${CIRCLE_BRANCH}..)
}

function pull_request() {
    echo "PR against $target_branch"

    # reset target branch to its status in origin to create the diff with current
    git checkout ${target_branch}
    git reset --hard origin/${target_branch}
    diff_output=$(git diff --diff-filter=D ${CIRCLE_BRANCH}..)
}

[[ "${target_branch}" == "${CIRCLE_BRANCH}" ]] && master_update || pull_request

# use a diff to detect and syndicate any new blog posts
[[ ! -z ${diff_output} ]] && {
    # dump blog-specific file additions to a file for reading
    git diff --diff-filter=A ..${CIRCLE_BRANCH} | grep 'diff.*content\/.*index\.md' > /tmp/new_files.lst
    n_new_blogs=$(cat /tmp/new_files.lst | wc -l)
    echo "Found $n_new_blogs new blog posts to syndicate"

    # return to the active branch to access new content being merged
    git checkout ${CIRCLE_BRANCH}

    # syndicate new blog posts
    [[ ${n_new_blogs} -gt 0 ]] && {
        while read line; do
            name=$(echo ${line} | cut -d ' ' -f4 | rev | cut -d/ -f2 | rev)
            echo $name > log.txt
            echo $name
            # TODO pass extra flag to indicate verify vs deploy
            python syndication/src/syndicate.py content/post/${name}/index.md
        done < /tmp/new_files.lst
    }
} || {
    # no new blogs, still need to return to active branch
    git checkout ${CIRCLE_BRANCH}
}
