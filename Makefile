# created_with_eee -- maintainer tooling for syncing content across hosts.
#
# Trezor-signing steps (commit, push) are meant to be run interactively by a
# human at the keyboard, confirming each physical device prompt yourself --
# no target here invokes trezor-agent on its own.

SPLIT_PROJECTS_DIR ?= $(HOME)/work/greek/git/gitlab/EEE-project
SPLIT_PROJECTS := created-with-eee-odyssey created-with-eee-palaestra created-with-eee-b1glc

.PHONY: help sync-main fix-split-roots

help:
	@echo "Targets:"
	@echo "  sync-main        Sync this repo's main branch to Codeberg, GitHub, and"
	@echo "                   GitLab (wraps ~/work/greek/git/push). Trezor-confirmed"
	@echo "                   per host as you run it."
	@echo "  fix-split-roots  Re-apply the session-page _ROOT fix (see"
	@echo "                   fix-split-session-root.py) to local checkouts of the 3"
	@echo "                   split GitLab projects. Only edits files locally --"
	@echo "                   review with git status/diff, then commit + push each"
	@echo "                   by hand (Trezor-confirmed)."
	@echo ""
	@echo "NOT automated here (still manual -- see README's Maintainer tooling"
	@echo "section): rebuilding the pages branch itself (WASM re-export, hub"
	@echo "regeneration) and splitting a new course off into its own GitLab project."

sync-main:
	$(HOME)/work/greek/git/push

fix-split-roots:
	python3 fix-split-session-root.py $(foreach p,$(SPLIT_PROJECTS),$(SPLIT_PROJECTS_DIR)/$(p))
	@echo ""
	@echo "Local files only -- review with 'git status'/'git diff' in each project"
	@echo "directory above, then commit + push by hand (Trezor-confirmed, one at a"
	@echo "time). This target never commits or pushes."
