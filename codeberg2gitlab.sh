#!/usr/bin/env bash
# Replace Codeberg raw URLs with GitLab raw URLs in all .py files
find . -name "*.py" -not -path "./.git/*" \
    -exec sed -i \
        's|https://codeberg.org/EEE-project/created_with_eee/raw/branch/main|https://gitlab.com/EEE-project/created_with_eee/-/raw/main|g' \
        {} +
