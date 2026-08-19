#!/usr/bin/env python3
"""Verify created_with_eee's Pages deployments are actually serving current
content -- a clean `git push` to a `pages` branch is not evidence the site
updated. GitHub's legacy Pages build can get stuck "building" forever after
a transient 503 from GitHub's own deploy API, with zero signal from the push
itself (confirmed 2026-08-18). GitLab deploys via a CI/CD pipeline that has
to be checked separately. Codeberg has no deploy-status API at all -- the
live fetch is the only signal there.

Requires `gh` (GitHub CLI) and `glab` (GitLab CLI), both already
authenticated, for the host-specific checks; falls back to the live fetch
alone if either is unavailable.

Usage:
    python3 verify-pages-deploy.py            # check every known site
    python3 verify-pages-deploy.py odyssey    # only sites whose name matches

The GitLab split-project list is read from the SPLIT_PROJECTS env var
(space-separated bare repo names, same as the Makefile's own SPLIT_PROJECTS)
when set, so `make verify-pages-deploy` stays in sync with the other targets
that already derive from it; falls back to today's 3 known split projects.
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass


@dataclass
class Site:
    name: str
    host: str  # "codeberg" | "github" | "gitlab"
    git_url: str  # for `git ls-remote`
    branch: str
    live_url: str
    api_repo: str | None = None  # "OWNER/REPO", for gh/glab API calls


def _split_site(project: str) -> Site:
    """A GitLab split-project Site, mechanically derived from its bare repo
    name -- git_url/live_url/api_repo all follow the same EEE-project/<name>
    pattern the split projects always use.
    """
    short_name = project.removeprefix("created-with-eee-")
    return Site(f"{short_name} (GitLab split)", "gitlab",
                f"https://gitlab.com/EEE-project/{project}.git", "pages",
                f"https://eee-project.gitlab.io/{project}/",
                api_repo=f"EEE-project/{project}")


_DEFAULT_SPLIT_PROJECTS = "created-with-eee-odyssey created-with-eee-palaestra created-with-eee-b1glc"

SITES = [
    Site("created_with_eee (Codeberg, dev)", "codeberg",
         "https://codeberg.org/EEE-project/created_with_eee.git", "pages",
         "https://eee-project.codeberg.page/created_with_eee/"),
    Site("created_with_eee (GitHub, prod)", "github",
         "https://github.com/EEE-project/created_with_eee.git", "pages",
         "https://eee-project.github.io/created_with_eee/",
         api_repo="EEE-project/created_with_eee"),
    Site("created_with_eee (GitLab, mirror)", "gitlab",
         "https://gitlab.com/EEE-project/created_with_eee.git", "pages",
         "https://eee-project.gitlab.io/created_with_eee/",
         api_repo="EEE-project/created_with_eee"),
    *(_split_site(p) for p in os.environ.get("SPLIT_PROJECTS", _DEFAULT_SPLIT_PROJECTS).split()),
]


def short(sha: "str | None", placeholder: str = "?") -> str:
    return sha[:8] if sha else placeholder


def run_json(cmd: list) -> "tuple[object, str | None]":
    """Run cmd, parse stdout as JSON. Returns (data, None) or (None, error)."""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30, check=True)
        return json.loads(out.stdout), None
    except Exception as e:
        return None, str(e)


def branch_tip(git_url: str, branch: str) -> "str | None":
    out = subprocess.run(["git", "ls-remote", git_url, branch], capture_output=True, text=True, timeout=30)
    line = out.stdout.strip()
    return line.split("\t")[0] if line else None


def fetch_headers(url: str) -> dict:
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"status": resp.status, **{k.lower(): v for k, v in resp.headers.items()}}
    except urllib.error.URLError as e:
        return {"error": str(e)}


def github_status(api_repo: str, expected_sha: "str | None") -> "tuple[str, str]":
    build, err = run_json(["gh", "api", f"repos/{api_repo}/pages/builds/latest"])
    if err:
        return "UNKNOWN", f"gh api call failed: {err}"

    status, commit = build.get("status"), build.get("commit")
    if status == "built" and (not expected_sha or commit == expected_sha):
        return "OK", f"built, commit {short(commit)}"

    detail = f"pages/builds/latest status={status!r} commit={short(commit)}"
    if expected_sha and commit != expected_sha:
        detail += f" (pages branch tip is {short(expected_sha)})"

    # The legacy builds API can show "building" forever after a real failure
    # (confirmed 2026-08-18) -- cross-check the Actions run for that commit.
    try:
        runs = subprocess.run(
            ["gh", "api", f"repos/{api_repo}/actions/runs", "-q",
             '.workflow_runs[] | select(.name=="pages build and deployment") '
             '| [.head_sha,.status,.conclusion] | @tsv'],
            capture_output=True, text=True, timeout=30, check=True,
        )
        for line in runs.stdout.splitlines():
            sha_r, run_status, conclusion = line.split("\t")
            if expected_sha and sha_r == expected_sha:
                detail += f"; Actions run for that commit: status={run_status} conclusion={conclusion}"
                if conclusion == "success":
                    return "WARN", detail + " -- Actions succeeded, legacy builds API entry looks like a stale ghost"
                break
    except Exception:
        pass
    return "FAIL", detail


def gitlab_status(api_repo: str, branch: str, expected_sha: "str | None") -> "tuple[str, str]":
    # No --paginate: GitLab returns pipelines newest-first, and the loop
    # below returns on the first ref==branch match, so page 1 always has it.
    encoded = api_repo.replace("/", "%2F")
    pipelines, err = run_json(["glab", "api", f"projects/{encoded}/pipelines"])
    if err:
        return "UNKNOWN", f"glab api call failed: {err}"

    for p in pipelines:
        if p.get("ref") != branch:
            continue
        status, sha = p.get("status"), p.get("sha")
        detail = f"latest {branch!r} pipeline status={status!r} commit={short(sha)}"
        if status != "success":
            return "FAIL", detail
        if expected_sha and sha != expected_sha:
            return "WARN", detail + f" (pages branch tip is {short(expected_sha)})"
        return "OK", detail
    return "UNKNOWN", f"no pipeline found for ref={branch!r}"


def check_site(site: Site) -> bool:
    """Returns True if this site looks healthy."""
    print(f"\n== {site.name} ==")
    sha = branch_tip(site.git_url, site.branch)
    print(f"  {site.branch} branch tip: {short(sha, 'UNKNOWN')}")

    if site.host == "github" and site.api_repo:
        level, detail = github_status(site.api_repo, sha)
    elif site.host == "gitlab" and site.api_repo:
        level, detail = gitlab_status(site.api_repo, site.branch, sha)
    else:
        level, detail = None, None

    ok = True
    if level is None:
        print("  [--] no deploy-status API for this host -- the live fetch below is the only signal")
    else:
        print(f"  [{level}] {detail}")
        ok = level == "OK"

    headers = fetch_headers(site.live_url)
    if "error" in headers:
        print(f"  [FAIL] live fetch: {headers['error']}")
        return False
    print(f"  live fetch: status={headers.get('status')} last-modified={headers.get('last-modified', '?')} "
          f"x-cache={headers.get('x-cache', '?')} etag={headers.get('etag', '?')}")
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("site_filter", nargs="?",
                         help="Only check sites whose name contains this text (case-insensitive)")
    args = parser.parse_args()

    filt = args.site_filter.lower() if args.site_filter else None
    sites = [s for s in SITES if not filt or filt in s.name.lower()]
    if not sites:
        print(f"No known site matches {filt!r}", file=sys.stderr)
        sys.exit(1)

    all_ok = True
    for site in sites:
        if not check_site(site):
            all_ok = False
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
