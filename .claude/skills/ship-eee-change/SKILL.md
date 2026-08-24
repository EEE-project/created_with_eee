---
name: ship-eee-change
description: Ship a change in the created_with_eee repo through the full commit-branch-PR-merge-mirror-sync-verify workflow. Use this whenever the user asks to commit, push, ship, merge, or finish a change here, or to sync the GitHub/GitLab mirrors — the mirror-sync step is easy to forget (it's been missed three separate times on this exact repo) and this skill exists specifically so that stops happening. Trigger it even if the user just says "commit and push" without mentioning mirrors — the mirror sync is part of what "done" means for this repo, not a separate optional step.
---

# Ship an EEE change

This is the full lifecycle for landing a change in `created_with_eee`: branch, push, PR, merge, sync `main` locally, then sync `main` to both mirrors, then verify all three hosts actually agree. The last two steps are the ones that get skipped when shipping a change feels "done" as soon as the PR merges on Codeberg — but Codeberg merging doesn't touch GitHub or GitLab at all, and nothing else does either unless you run it. Treat mirror sync as part of finishing the change, not a follow-up task.

## Trezor confirmation — read this before running any step below

Every command that touches the Trezor key needs its own separate confirmation from the user, asked as an actual question naming the exact command, with a wait for the reply. This applies individually to *each* push below — approving step 2's push does not carry forward to step 5's or step 6's. Retrying a command that just failed (e.g. a transient "Connection closed by ... port 22" drop) still needs a fresh confirmation, not a silent retry. This is a hardware key that physically taps once per action; treat each tap as its own decision point. See `/data/work/sadov/greek/EEE/CLAUDE.md`'s "Git & Codeberg Integration" section for the full rationale — this skill follows that convention, it doesn't invent a new one.

## Steps

### 1. Commit on a topic branch

Never commit directly to `main`. If not already on a topic branch:

```bash
git checkout -b <topic-branch> main
git add <files>
git commit -m "..."
```

### 2. Push the branch

```bash
trezor-agent -v -e ed25519 git@codeberg.org -- git push --set-upstream origin <topic-branch>
```

### 3. Open the PR

```bash
tea pulls create --head <topic-branch> --base main --title "..." --description "..."
```

### 4. Merge via rebase

```bash
tea pr merge -s rebase <PR-number>
```

### 5. Sync local `main` and clean up the branch

```bash
trezor-agent -v -e ed25519 git@codeberg.org -- git fetch origin
git merge --ff-only origin/main   # or: git branch -f main origin/main, if main isn't checked out
git branch -d <topic-branch>
trezor-agent -v -e ed25519 git@codeberg.org -- git push origin --delete <topic-branch>
```

### 6. Sync `main` to the GitHub and GitLab mirrors

This is the step that keeps getting missed — do it now, not later. Repeat for each mirror checkout (`~/work/greek/git/github/EEE-project/created_with_eee/` and `~/work/greek/git/gitlab/EEE-project/created_with_eee/`):

```bash
cd <mirror-checkout>
git fetch codeberg main
git checkout main
git reset --hard codeberg/main
bash ./codeberg2github.sh   # or ./codeberg2gitlab.sh, matching the checkout
git add -A
git commit -m "Switch raw asset URLs and EEE deps from Codeberg to <host> mirror"
```

Then push. GitHub takes a plain force-push:

```bash
trezor-agent -v -e ed25519 git@github.com -- git push --force git@github.com:EEE-project/created_with_eee.git main:main
```

GitLab's `main` is protected against force-push by default — toggle it off, push, then toggle it back on and *verify* the restore actually took (re-`GET` the setting, don't just trust the `PATCH` call succeeding):

```bash
glab api --method PATCH "projects/EEE-project%2Fcreated_with_eee/protected_branches/main" -f allow_force_push=true
trezor-agent -v -e ed25519 git@gitlab.com -- git push --force git@gitlab.com:EEE-project/created_with_eee.git main:main
glab api --method PATCH "projects/EEE-project%2Fcreated_with_eee/protected_branches/main" -f allow_force_push=false
glab api "projects/EEE-project%2Fcreated_with_eee" --jq '.permissions // empty' > /dev/null  # sanity: confirms the API call itself succeeded before trusting the restore
```

### 7. Verify all three hosts agree

```bash
git ls-remote https://codeberg.org/EEE-project/created_with_eee.git main
git ls-remote https://github.com/EEE-project/created_with_eee.git main
git ls-remote https://gitlab.com/EEE-project/created_with_eee.git main
```

The three tips won't be byte-identical hashes (each mirror carries its own conversion commit on top), but Codeberg's tip commit message/content should match what each mirror's *own* conversion produced from it — if a mirror is still showing an old commit from before this change, the sync didn't take and step 6 needs re-running for that host.

## When to skip steps

- If the repo has no `codeberg2github.sh`/`codeberg2gitlab.sh` in its root, step 6 is a plain `git push --mirror` per mirror instead of the fetch/reset/conversion-script dance — check first.
- A change that's `pages`-branch-only (build output, not source) doesn't go through this workflow at all — that branch is synced directly, not via PR against `main`.
