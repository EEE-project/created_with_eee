#!/usr/bin/env bash
# Propagate Codeberg's complete pages branch to GitHub and GitLab.
#
# GitHub receives the unified tree. GitLab receives both its unified Pages
# project and the three split Pages projects, using the checked-in tools for
# export layout, hub layout, split-course roots/links, and host URLs.
set -Eeuo pipefail

usage() {
    cat <<'EOF'
Usage: tools/propagate-pages.sh [--verbose] [--push] [HOST...]

Synchronize all tracked notebook exports and all generated hubs from
Codeberg's pages worktree into GitHub's unified Pages worktree, GitLab's
unified Pages worktree, and GitLab's split Odyssey/Palaestra/b1glc projects.

Destination worktrees must exist, be clean, and be checked out on pages. The
script commits local changes but does not push unless --push is given. Remote
Git operations use the command configured for each hosting provider.

Options:
  -v, --verbose   print every shell command as it runs
  --push          push changed destination commits after preparation

Hosts (default: all):
  all             GitHub and GitLab, including GitLab split projects
  github          GitHub unified Pages project only
  gitlab          GitLab unified and all GitLab split Pages projects

Environment overrides: GIT_CMD_CODEBERG, GIT_CMD_GITHUB, GIT_CMD_GITLAB,
GITHUB_PAGES_DIR, GITLAB_PAGES_DIR, GITLAB_SPLIT_DIR
EOF
}

verbose=false
push_targets=false
hosts=()

while (($#)); do
    case "$1" in
        -v|--verbose) verbose=true; shift ;;
        --push) push_targets=true; shift ;;
        -h|--help) usage; exit 0 ;;
        all|github|gitlab) hosts+=("$1"); shift ;;
        *) echo "unknown argument: $1" >&2; usage >&2; exit 2 ;;
    esac
done

if ((${#hosts[@]} == 0)) || [[ " ${hosts[*]} " == *" all "* ]]; then
    hosts=(github gitlab)
fi

wants() {
    [[ " ${hosts[*]} " == *" $1 "* ]]
}

if [[ "$verbose" == true ]]; then
    PS4='+ ${BASH_SOURCE##*/}:${LINENO}: '
    set -x
fi

repo_root=$(git rev-parse --show-toplevel)
tool_dir="$repo_root/tools"

# Selected values may come from the repository-root .env (see _dotenv.sh).
env_file="$repo_root/.env"
source "$tool_dir/_dotenv.sh"

for env_name in \
    GIT_CMD_CODEBERG GIT_CMD_GITHUB GIT_CMD_GITLAB \
    GITHUB_PAGES_DIR GITLAB_PAGES_DIR GITLAB_SPLIT_DIR CODEBERG_PAGES_DIR; do
    load_dotenv_value "$env_name"
done

github_dir="${GITHUB_PAGES_DIR:-$HOME/work/greek/git/github/EEE-project/created_with_eee-pages-worktree}"
gitlab_dir="${GITLAB_PAGES_DIR:-$HOME/work/greek/git/gitlab/EEE-project/created_with_eee-pages-worktree}"
split_parent="${GITLAB_SPLIT_DIR:-$HOME/work/greek/git/gitlab/EEE-project}"
git_cmd_codeberg=(git)
git_cmd_github=(git)
git_cmd_gitlab=(git)
[[ -z "${GIT_CMD_CODEBERG:-}" ]] || read -r -a git_cmd_codeberg <<< "$GIT_CMD_CODEBERG"
[[ -z "${GIT_CMD_GITHUB:-}" ]] || read -r -a git_cmd_github <<< "$GIT_CMD_GITHUB"
[[ -z "${GIT_CMD_GITLAB:-}" ]] || read -r -a git_cmd_gitlab <<< "$GIT_CMD_GITLAB"
source_pages_dir="${CODEBERG_PAGES_DIR:-$repo_root/../created_with_eee-pages-worktree}"

github_url=git@github.com:EEE-project/created_with_eee.git
gitlab_url=git@gitlab.com:EEE-project/created_with_eee.git

die() { echo "error: $*" >&2; exit 1; }

# The GitLab split projects come from the one table of split-off courses.
mapfile -t split_projects < <(python3 "$tool_dir/_split_courses.py" projects)
((${#split_projects[@]} > 0)) || die "cannot read the split-course table (tools/_split_courses.py)"
split_repos=()
for project in "${split_projects[@]}"; do
    split_repos+=("$split_parent/$project")
done

run_git() {
    local host=$1
    shift
    case "$host" in
        codeberg) "${git_cmd_codeberg[@]}" "$@" ;;
        github) "${git_cmd_github[@]}" "$@" ;;
        gitlab) "${git_cmd_gitlab[@]}" "$@" ;;
        *) die "unknown Git hosting provider: $host" ;;
    esac
}

is_canonical_gitlab_ci() {
    local file=$1
    [[ -f "$file" ]] || return 1
    cmp -s "$file" "$tool_dir/gitlab-ci-pages.yml"
}

remove_known_generated_files() {
    local dir=$1
    local status
    status=$(git -C "$dir" status --porcelain)
    if [[ "$status" == "?? .gitlab-ci.yml" ]] && is_canonical_gitlab_ci "$dir/.gitlab-ci.yml"; then
        echo "removing known generated untracked file: $dir/.gitlab-ci.yml"
        rm -- "$dir/.gitlab-ci.yml"
    fi
}

require_pages_checkout() {
    local dir=$1 remote=$2
    [[ -d "$dir" ]] || die "missing checkout: $dir"
    git -C "$dir" rev-parse --is-inside-work-tree >/dev/null || die "not a Git checkout: $dir"
    if [[ "$dir" != "$source_pages_dir" ]]; then
        [[ $(git -C "$dir" rev-parse --absolute-git-dir) != $(git -C "$source_pages_dir" rev-parse --absolute-git-dir) ]] ||
            die "$dir shares its git directory with $source_pages_dir (broken .git pointer; run git worktree repair)"
    fi
    [[ $(git -C "$dir" branch --show-current) == pages ]] || die "$dir is not checked out on pages"
    [[ -z $(git -C "$dir" status --porcelain) ]] || die "$dir has uncommitted changes"
    git -C "$dir" remote get-url "$remote" >/dev/null 2>&1 || die "$dir has no $remote remote"
}

public_url() {
    local url=$1
    case "$url" in
        git@*:*) url=${url#git@}; printf 'https://%s/%s' "${url%%:*}" "${url#*:}" ;;
        ssh://git@*/*) url=${url#ssh://git@}; printf 'https://%s/%s' "${url%%/*}" "${url#*/}" ;;
        *) printf '%s' "$url" ;;
    esac
}

# A split project's pages branch refuses force-pushes, so this checkout must already contain the remote's tip.
require_remote_contained() {
    local dir=$1 url out tip
    url=$(public_url "$(git -C "$dir" remote get-url origin)")
    if ! out=$(GIT_TERMINAL_PROMPT=0 timeout 30 git ls-remote "$url" refs/heads/pages); then
        [[ "$push_targets" != true ]] || die "cannot read $url; the remote pages tip is checked before a push"
        echo "warning: cannot read $url; remote pages tip not checked"
        return 0
    fi
    tip=${out%%[[:space:]]*}
    [[ -z "$tip" ]] || git -C "$dir" merge-base --is-ancestor "$tip" pages 2>/dev/null ||
        die "$dir does not contain the remote pages tip ${tip:0:7} (git -C $dir fetch $url +refs/heads/pages:refs/remotes/origin/pages)"
}

# True when the staged tree is exactly what the remote already publishes on pages: a new commit and force-push would change nothing.
matches_published() {
    local dir=$1 url
    url=$(public_url "$2")
    if ! GIT_TERMINAL_PROMPT=0 timeout 60 git -C "$dir" fetch --quiet "$url" +refs/heads/pages:refs/published/pages 2>/dev/null; then
        echo "warning: cannot read $url; not comparing with what it publishes"
        return 1
    fi
    [[ $(git -C "$dir" write-tree) == $(git -C "$dir" rev-parse 'refs/published/pages^{tree}') ]]
}

commit_if_needed() {
    local dir=$1 message=$2 url=${3:-}
    if [[ -z $(git -C "$dir" status --porcelain) ]]; then
        echo "already current: $dir"
        return 1
    fi
    git -C "$dir" add -A
    if [[ -n "$url" ]] && matches_published "$dir" "$url"; then
        echo "already published: $dir has the tree the remote serves"
        git -C "$dir" reset --hard refs/published/pages
        return 1
    fi
    git -C "$dir" commit -m "$message"
    return 0
}

push_pages() {
    local host=$1 dir=$2 url=$3
    echo "pushing $dir -> $url"
    run_git "$host" -C "$dir" push --force "$url" pages:pages
}

[[ -d "$source_pages_dir" ]] || die "missing Codeberg pages worktree: $source_pages_dir"
if wants gitlab; then
    remove_known_generated_files "$gitlab_dir"
fi
require_pages_checkout "$source_pages_dir" origin
if wants github; then
    require_pages_checkout "$github_dir" origin
fi
if wants gitlab; then
    require_pages_checkout "$gitlab_dir" origin
    for split_dir in "${split_repos[@]}"; do
        require_pages_checkout "$split_dir" origin
    done
fi
if wants gitlab; then
    for split_dir in "${split_repos[@]}"; do
        require_remote_contained "$split_dir"
    done
fi

# Fetch Codeberg once from its canonical pages worktree. Mirror worktrees only
# need their own hosting remote (normally `origin`); they do not need a
# Codeberg remote configured locally.
echo "fetching Codeberg pages"
run_git codeberg -C "$source_pages_dir" fetch origin pages
source_pages_ref=$(git -C "$source_pages_dir" rev-parse pages)

# Unified branches can be reset exactly from the fetched Codeberg commit.
if wants github; then
    echo "resetting $github_dir from Codeberg pages ($source_pages_ref)"
    git -C "$github_dir" fetch "$source_pages_dir" "$source_pages_ref"
    git -C "$github_dir" reset --hard "$source_pages_ref"
fi
if wants gitlab; then
    echo "resetting $gitlab_dir from Codeberg pages ($source_pages_ref)"
    git -C "$gitlab_dir" fetch "$source_pages_dir" "$source_pages_ref"
    git -C "$gitlab_dir" reset --hard "$source_pages_ref"
fi

# Copy every tracked notebook export into the unified targets and the
# appropriate flattened split project.
mapfile -t notebooks < <(
    git -C "$repo_root" ls-files '*.py' |
        awk '/(^|\/)(notebook(\.[0-9_]+)?|.*_notebook)\.py$/ { print }'
)
# A course-level notebook has nested lesson notebooks below the same
# directory. Its export directory is a hub/source container; copying it after
# the leaf lesson exports would erase those lesson directories. Hubs are
# synchronized separately by sync-hub-pages.py, so pass only leaf notebooks.
leaf_notebooks=()
for notebook in "${notebooks[@]}"; do
    notebook_dir=${notebook%/*}
    [[ "$notebook_dir" == "$notebook" ]] && notebook_dir=""
    has_descendant=false
    for other in "${notebooks[@]}"; do
        [[ "$other" == "$notebook" ]] && continue
        if [[ -n "$notebook_dir" && "$other" == "$notebook_dir/"* ]] ||
           [[ -z "$notebook_dir" && "$other" == */* ]]; then
            has_descendant=true
            break
        fi
    done
    if [[ "$has_descendant" == false ]]; then
        leaf_notebooks+=("$notebook")
    fi
done
notebooks=("${leaf_notebooks[@]}")
(( ${#notebooks[@]} > 0 )) || die "no notebook source files found"

sync_dest_args=(--source-dir "$source_pages_dir")
if wants github; then
    sync_dest_args+=(--github-dir "$github_dir")
fi
if wants gitlab; then
    sync_dest_args+=(--gitlab-unified-dir "$gitlab_dir" --split-projects-dir "$split_parent")
fi
python3 "$tool_dir/sync-pages-export.py" "${sync_dest_args[@]}" "${notebooks[@]}"

# Copy every generated hub index, including split-project hubs.
python3 "$tool_dir/sync-hub-pages.py" "${sync_dest_args[@]}"

if wants github; then
    echo "applying GitHub host fixes"
    (
    cd "$github_dir"
    bash "$repo_root/codeberg2github.sh"
    python3 "$tool_dir/fix-static-footer-host.py" \
        --host https://github.com/EEE-project "$github_dir"
    )
fi

if wants gitlab; then
    echo "applying GitLab unified host fixes"
    (
    cd "$gitlab_dir"
    # The pages tree contains exported HTML, not the source index.tsv files
    # expected by codeberg2gitlab.sh (that script is for main mirrors).
    # Pages-specific scope and split-root tools handle the required rewrites.
    python3 "$tool_dir/fix-gitlab-unified-pages-scope.py" "$gitlab_dir"
    python3 "$tool_dir/fix-static-footer-host.py" \
        --host https://gitlab.com/EEE-project "$gitlab_dir"
    )

    echo "applying GitLab split-project fixes"
    python3 "$tool_dir/fix-split-session-root.py" "${split_repos[@]}"
    b1glc=created-with-eee-b1glc   # the one split project whose hub links to several courses
    b1glc_prefix=$(python3 "$tool_dir/_split_courses.py" prefix "$b1glc")
    python3 "$tool_dir/fix-split-hub-card-links.py" \
        --prefix "$b1glc_prefix" \
        "$split_parent/$b1glc"
    python3 "$tool_dir/fix-static-footer-host.py" \
        --host https://gitlab.com/EEE-project "${split_repos[@]}"
fi

changed_dirs=()
if wants github && commit_if_needed "$github_dir" "Propagate Codeberg pages to GitHub" "$github_url"; then
    changed_dirs+=("github|$github_dir|$github_url")
fi
if wants gitlab && commit_if_needed "$gitlab_dir" "Propagate Codeberg pages to GitLab" "$gitlab_url"; then
    changed_dirs+=("gitlab|$gitlab_dir|$gitlab_url")
fi
if wants gitlab; then
    for split_dir in "${split_repos[@]}"; do
        # Not reset above, so a dry run's commit survives: push whatever pages holds that origin/pages lacks.
        commit_if_needed "$split_dir" "Propagate Codeberg pages to GitLab split hosting" || true
        if [[ $(git -C "$split_dir" rev-parse pages) != $(git -C "$split_dir" rev-parse -q --verify refs/remotes/origin/pages || true) ]]; then
            changed_dirs+=("gitlab|$split_dir|origin")
        fi
    done
fi

if [[ "$push_targets" != true ]]; then
    echo "prepared ${#changed_dirs[@]} local commit(s); no remotes were changed"
    exit 0
fi

for item in "${changed_dirs[@]}"; do
    IFS='|' read -r host dir url <<< "$item"
    push_pages "$host" "$dir" "$url"
done
