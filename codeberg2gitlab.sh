#!/usr/bin/env bash
# Replace Codeberg raw URLs with GitLab raw URLs in all .py files
find . -name "*.py" -not -path "./.git/*" \
    -exec sed -i \
        's|https://codeberg.org/EEE-project/created_with_eee/raw/branch/main|https://gitlab.com/EEE-project/created_with_eee/-/raw/main|g' \
        {} +

# Pin EEE package deps to PyPI releases instead of tracking Codeberg's git main.
# git+... deps track the moving tip of main, so a notebook's calling code can
# silently break when the library's API changes upstream before the notebook
# is updated. Codeberg's canonical copy keeps git+codeberg.org URLs on purpose
# (active development tracks latest unreleased code); mirrors get pinned.
find . -name "*.py" -not -path "./.git/*" \
    -exec sed -i \
        -e 's|"eee-project @ git+https://codeberg.org/EEE-project/eee-project.git"|"eee-project>=1.0.0"|g' \
        -e 's|"ancient-greek-backend-eee @ git+https://codeberg.org/EEE-project/ancient-greek-backend-eee.git"|"ancient-greek-backend-eee>=1.0.0"|g' \
        -e 's|"unimorph-backend-eee @ git+https://codeberg.org/EEE-project/unimorph-backend-eee.git"|"unimorph-backend-eee>=1.0.3"|g' \
        -e 's|"modern-greek-backend-eee @ git+https://codeberg.org/EEE-project/modern-greek-backend-eee.git"|"modern-greek-backend-eee>=1.0.0"|g' \
        -e '/^# \[tool\.uv\.sources\]$/d' \
        -e '/^# eee-project = { git = "https:\/\/codeberg\.org\/EEE-project\/eee-project\.git" }$/d' \
        -e '/^# ancient-greek-backend-eee = { git = "https:\/\/codeberg\.org\/EEE-project\/ancient-greek-backend-eee\.git" }$/d' \
        -e '/^# unimorph-backend-eee = { git = "https:\/\/codeberg\.org\/EEE-project\/unimorph-backend-eee\.git" }$/d' \
        -e '/^# modern-greek-backend-eee = { git = "https:\/\/codeberg\.org\/EEE-project\/modern-greek-backend-eee\.git" }$/d' \
        -e '/^#$/d' \
        {} +
