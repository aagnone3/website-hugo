#!/usr/bin/env bash
set -xeou pipefail

# TODO obtain target branch from github curl
target_branch=master

# reset target branch to its status in origin to create the current diff
git checkout ${target_branch}
git reset --hard origin/${target_branch}
diff_output=$(git diff --diff-filter=D ${CIRCLE_BRANCH}..)

# use a diff to detect and syndicate any new blog posts
[[ ! -z ${diff_output} ]] && {
    # dump blog-specific file additions to a file for reading
    git diff --diff-filter=A ..${CIRCLE_BRANCH} | grep 'diff.*content\/.*index\.md' > /tmp/new_files.lst
    n_new_blogs=$(cat /tmp/new_files.lst | wc -l)

    # return to the active branch to access new content being merged
    git checkout ${CIRCLE_BRANCH}

    # syndicate new blog posts
    [[ ${n_new_blogs} -gt 0 ]] && {
        while read line; do
            name=$(echo ${line} | cut -d ' ' -f4 | rev | cut -d/ -f2 | rev)
            python syndication/src/syndicate.py content/post/${name}/index.md
        done < /tmp/new_files.lst
    }
} || {
    # no new blogs, still need to return to active branch
    git checkout ${CIRCLE_BRANCH}
}

set +e
ssh -F etc/ssh_cfg website ls
