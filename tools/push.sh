#!/bin/bash
set -e

for a in "$@"; do
    case "$a" in
        -h|--help)
            cat <<'EOF'
Usage: tools/push.sh [HOST...]

Sync this repo's current branch, tags, and other real branches to Codeberg
and its GitHub/GitLab mirrors. Git runs through GIT_CMD_CODEBERG,
GIT_CMD_GITHUB and GIT_CMD_GITLAB (exported, or set in the repository-root
.env; default: git).

Arguments:
  HOST    One or more of: codeberg, github, gitlab.
          Only the given hosts are synced.
          Default (no args): all three.

Examples:
  tools/push.sh                    # sync all three hosts
  tools/push.sh github             # GitHub only
  tools/push.sh codeberg gitlab    # Codeberg and GitLab, skip GitHub
EOF
            exit 0
            ;;
    esac
done

# Which hosts to sync -- optional positional args (codeberg/github/gitlab),
# default to all three when none are given.
valid_hosts=(codeberg github gitlab)
hosts=("$@")
if [ ${#hosts[@]} -eq 0 ]; then
    hosts=("${valid_hosts[@]}")
else
    for h in "${hosts[@]}"; do
        [[ " ${valid_hosts[*]} " == *" $h "* ]] || { echo "Unknown host: $h (expected: codeberg, github, gitlab)" >&2; exit 1; }
    done
fi
wants() { [[ " ${hosts[*]} " == *" $1 "* ]]; }

# Git command per host: an exported GIT_CMD_* wins, then the repository-root .env, else plain git.
tool_dir="$(dirname "${BASH_SOURCE[0]}")"
env_file="$tool_dir/../.env"
source "$tool_dir/_dotenv.sh"
for env_name in GIT_CMD_CODEBERG GIT_CMD_GITHUB GIT_CMD_GITLAB; do
    load_dotenv_value "$env_name"
done
git_cdb=${GIT_CMD_CODEBERG:-git}
git_hub=${GIT_CMD_GITHUB:-git}
git_lab=${GIT_CMD_GITLAB:-git}

codeberg_root=$(git rev-parse --show-toplevel)
# basename of the remote URL, not of $codeberg_root -- a worktree's own
# directory can be named anything (e.g. "eee-project-pages-worktree"),
# but `git remote get-url origin` resolves correctly from any worktree
# (they share the parent repo's remote config), so this is robust where
# basename-of-checkout-dir isn't.
repo=$(basename "$(git remote get-url origin)" .git)
default_branch=$(git branch --show-current)

# GitLab repo name, when it differs from Codeberg's/GitHub's (rare -- one
# known case so far: an underscore-vs-hyphen mismatch). Everywhere else in
# this script that talks to GitLab uses this instead of $repo.
gitlab_repo="${repo}"
case "$repo" in
    modern_greek_accentuation_eee) gitlab_repo="modern-greek-accentuation-eee" ;;
esac

# Does the host have a mirror of this repo? Ask its API (gh/glab api -i print the
# HTTP status line first): 200 = yes, 404 = no. Anything else -- no connection,
# timeout, login, rate limit, server error -- is NOT "no mirror": say so and stop,
# so a failed check can never pass for a repo without a mirror and push nothing.
mirror_exists() {
    local host=$1 out status detail
    shift
    out=$("$@" 2>&1) || true
    status=$(printf '%s\n' "$out" | sed -n '1s#^HTTP/[0-9.]* \([0-9]*\).*#\1#p')
    case "$status" in
        200) return 0 ;;
        404) return 1 ;;
    esac
    if [ -n "$status" ]; then
        detail="HTTP ${status}"
    else
        detail=$(printf '%s' "$out" | tr -s '[:space:]' ' ' | cut -c1-160)
        detail=${detail# }
    fi
    echo "❌ Could not check whether ${host} has a mirror of ${repo} (${detail:-no answer}) — nothing was pushed to ${host}. Run it again with the host argument ${host,,} once that works." >&2
    exit 1
}

# GitLab's main is a protected branch (no force-push) by default -- only bites when
# history was rewritten (a fast-forward update never trips it), but allow it
# unconditionally for one push since we can't tell in advance. Always switch it off
# again, even if the push reports failure, so a real error never leaves protection
# off. Returns the status of the push (set -e then ends the script with it).
# The arguments are those of `git push`.
gitlab_force_push() {
    local protected_branch_api="projects/EEE-project%2F${gitlab_repo}/protected_branches/main" unprotected=false push_status=0
    if glab api --method PATCH "$protected_branch_api" -f allow_force_push=true > /dev/null 2>&1; then
        unprotected=true
    fi
    # set -e would end the function at a failed push, before the restore below: keep the status, restore, then return it.
    $git_lab push "$@" || push_status=$?
    if [ "$unprotected" = true ]; then
        glab api --method PATCH "$protected_branch_api" -f allow_force_push=false > /dev/null
    fi
    return "$push_status"
}

if wants codeberg; then
    # --tags (not --follow-tags): our tags are lightweight, and
    # --follow-tags only follows annotated tags reachable from what's
    # pushed. Combined into this one push so a new/moved tag doesn't cost
    # a second push.
    $git_cdb push --set-upstream origin "$default_branch" --tags || exit 1
fi

# --- GitHub ---
if wants github; then
    if mirror_exists GitHub gh api -i "repos/EEE-project/${repo}"; then
        conv_script="codeberg2github.sh"
        mirror_dir="$HOME/work/greek/git/github/EEE-project/${repo}"
        if [ ! -f "${codeberg_root}/${conv_script}" ]; then
            # No repo-specific conversion needed: mirror is a passive copy of Codeberg.
            # Explicit refspecs (not --mirror) so only real branches/tags sync --
            # --mirror also copies this checkout's own refs/remotes/* bookkeeping
            # (tracking refs for origin/github/gitlab/etc.), which is meaningless
            # clutter on a host that isn't literally that remote. --prune removes
            # a branch/tag here once it's gone locally, matching --mirror's own
            # cleanup behavior but scoped to refs/heads and refs/tags only.
            $git_hub push --prune --force git@github.com:EEE-project/${repo}.git 'refs/heads/*:refs/heads/*' 'refs/tags/*:refs/tags/*'
        elif [ ! -d "$mirror_dir" ]; then
            echo "⚠️  ${conv_script} exists but ${mirror_dir} is missing — skipping GitHub sync, set up the checkout first"
        else
            (
                cd "$mirror_dir"
                if [ -n "$(git status --short)" ]; then
                    echo "⚠️  ${mirror_dir} has uncommitted changes — skipping GitHub sync, resolve manually first"
                    exit 0
                fi
                git fetch codeberg
                git checkout main
                git reset --hard codeberg/main
                bash "./${conv_script}"
                if [ -z "$(git status --short)" ]; then
                    echo "ℹ️  GitHub conversion produced no changes for ${repo} — nothing to push"
                    exit 0
                fi
                git add -A
                git commit -m "Switch raw asset URLs and EEE deps from Codeberg to GitHub mirror"
                $git_hub push --force git@github.com:EEE-project/${repo}.git main:main
            )
        fi
    else
        echo "ℹ️  No GitHub mirror for ${repo} — skipping"
    fi
fi

# --- GitLab ---
if wants gitlab; then
    if mirror_exists GitLab glab api -i "projects/EEE-project%2F${gitlab_repo}"; then
        conv_script="codeberg2gitlab.sh"
        mirror_dir="$HOME/work/greek/git/gitlab/EEE-project/${repo}"
        if [ ! -f "${codeberg_root}/${conv_script}" ]; then
            # Explicit refspecs (not --mirror) so only real branches/tags sync --
            # --mirror also copies this checkout's own refs/remotes/* bookkeeping
            # (tracking refs for origin/github/gitlab/etc.), which is meaningless
            # clutter on a host that isn't literally that remote (GitLab used to
            # reject it outright as "hidden ref", which is what --mirror's own
            # nonzero exit here used to be from). --prune removes a branch/tag
            # here once it's gone locally, matching --mirror's own cleanup
            # behavior but scoped to refs/heads and refs/tags only.
            gitlab_force_push --prune --force git@gitlab.com:EEE-project/${gitlab_repo}.git 'refs/heads/*:refs/heads/*' 'refs/tags/*:refs/tags/*'
        elif [ ! -d "$mirror_dir" ]; then
            echo "⚠️  ${conv_script} exists but ${mirror_dir} is missing — skipping GitLab sync, set up the checkout first"
        else
            (
                cd "$mirror_dir"
                if [ -n "$(git status --short)" ]; then
                    echo "⚠️  ${mirror_dir} has uncommitted changes — skipping GitLab sync, resolve manually first"
                    exit 0
                fi
                git fetch codeberg
                git checkout main
                git reset --hard codeberg/main
                bash "./${conv_script}"
                if [ -z "$(git status --short)" ]; then
                    echo "ℹ️  GitLab conversion produced no changes for ${repo} — nothing to push"
                    exit 0
                fi
                git add -A
                git commit -m "Switch raw asset URLs and EEE deps from Codeberg to GitLab mirror"
                gitlab_force_push --force git@gitlab.com:EEE-project/${gitlab_repo}.git main:main
            )
        fi
    else
        echo "ℹ️  No GitLab mirror for ${repo} — skipping"
    fi
fi
