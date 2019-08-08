#!/usr/bin/env bash
set -eou pipefail

target_branch=master
git checkout ${target_branch}
git reset --hard origin/${target_branch}
git diff --diff-filter=D ${CIRCLE_BRANCH}.. > diffs.txt
diff_output=$(git diff --diff-filter=D ${CIRCLE_BRANCH}..)

[[ ! -z ${diff_output} ]] && {
    git diff --diff-filter=A ..${CIRCLE_BRANCH} | grep 'diff.*\.md' > /tmp/new_files.lst
    for line in $(cat /tmp/new_files.lst); do
        name=$(echo ${line} | cut -d ' ' -f4 | rev | cut -d/ -f2 | rev)
        echo $name >> names.lst
    done
}
