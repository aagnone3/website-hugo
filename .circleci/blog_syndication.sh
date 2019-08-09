#!/usr/bin/env bash
set -eou pipefail

# TODO obtain target branch from github curl
target_branch=master
git checkout ${target_branch}
git reset --hard origin/${target_branch}
diff_output=$(git diff --diff-filter=D ${CIRCLE_BRANCH}..)

[[ ! -z ${diff_output} ]] && {
    git diff --diff-filter=A ..${CIRCLE_BRANCH} | grep 'diff.*content\/.*index\.md' > /tmp/new_files.lst
    while read line; do
        name=$(echo ${line} | cut -d ' ' -f4 | rev | cut -d/ -f2 | rev)
        echo $name >> log.txt
        python syndication/src/syndicate.py content/post/${name}/index.md >> log.txt
    done < /tmp/new_files.lst
}
