---
name: verify-pages
description: Verify created_with_eee's live Pages hosting end-to-end across Codeberg, GitHub, and GitLab -- root hub, category hub, course hub, and a real WASM lesson boot, checked for matching content and zero JS errors on every host. Use this whenever the user asks to verify, check, or test the live site(s) after a change to hub pages, course structure, index.tsv, or the pages branch itself -- not just after a Pages-hosting change specifically, since any structural change to the notebook hierarchy can silently break navigation on one host while looking fine on another.
---

# Verify created_with_eee's Pages hosting

A curl/text check can confirm a page returns 200, but it can't confirm the site actually *works* -- that a hub's cards render, that clicking through navigates same-window into the right place, and that a real lesson's Pyodide/WASM runtime genuinely boots without a JS error. This skill runs that full chain via headless Playwright and reports pass/fail per host.

## Why this needs a script, not ad-hoc navigation

A real lesson page is a marimo/Pyodide export with 200+ asset preloads and takes ~65-75 seconds to boot over a real network. A naive `page.expect_navigation(timeout=10000)` (Playwright's default `wait_until="load"`) times out on that even though the page is loading correctly -- it works fine against a local dev server where everything is instant, and only fails against the real deployed site. `scripts/verify_pages.py` already handles this correctly: it clicks, waits a fixed amount matching the known boot time, then reads content, instead of asserting on the navigation event.

## Running it

```bash
python3 .claude/skills/verify-pages/scripts/verify_pages.py --lesson-path <course>/<lesson-dir>
```

`--lesson-path` is required and should point at a real, currently-published lesson (e.g. `ancient_greek/odyssey/2026_06_01`) -- pick whichever course was just touched, or the known-good reference lesson if the change was structural (hub/index generation, `index.tsv` hierarchy) rather than lesson-specific.

Defaults to all three current hosts (Codeberg, GitHub, GitLab Pages). Override with one or more `--host name=url` if a host's URL has changed or you only want to check one:

```bash
python3 .claude/skills/verify-pages/scripts/verify_pages.py \
    --lesson-path modern_greek/ellinika_b/chapter_01 \
    --host codeberg=https://eee-project.codeberg.page/created_with_eee
```

Uses `~/.venv/eee/bin/python3` if the system Python doesn't have `playwright` installed (it's already set up there with Chromium cached, no additional setup needed).

## Reading the output

Each host prints root card count, each hub-click's URL and card count, then the lesson boot time and rendered text length. `FAIL` lines call out the specific problem (no cards on a hub, JS errors, or suspiciously short lesson content — under 200 characters generally means the WASM boot didn't actually complete). The script exits non-zero if any host failed.

If a host that used to pass now fails while the others are fine, that's a real, host-specific regression worth investigating on its own (mismatched deployment, stale mirror, a host-specific config issue like GitLab's pages_access_level or unique-domain settings) -- not a flaky test to just rerun.
