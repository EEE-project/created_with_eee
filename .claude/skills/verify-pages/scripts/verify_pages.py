"""Verify created_with_eee's Pages hosting end-to-end: root hub -> category hub ->
course hub -> a real WASM lesson boot, on one or more hosts. Static hub pages load
in ~1s; a real lesson is a marimo/Pyodide export and takes ~65-75s to boot -- this
script waits that long before reading content, since a strict navigation-load
timeout (e.g. Playwright's default expect_navigation) fails on the WASM export's
200+ asset preloads over a real network even though the page is loading correctly.

Usage:
    python3 verify_pages.py --lesson-path ancient_greek/odyssey/2026_06_01 \
        [--host codeberg=https://eee-project.codeberg.page/created_with_eee] \
        [--host github=https://eee-project.github.io/created_with_eee] \
        [--host gitlab=https://eee-project.gitlab.io/created_with_eee] \
        [--boot-wait 70]

Defaults to all three current hosts if none are passed with --host.
"""
import argparse
import time
from playwright.sync_api import sync_playwright

DEFAULT_HOSTS = {
    "codeberg": "https://eee-project.codeberg.page/created_with_eee",
    "github": "https://eee-project.github.io/created_with_eee",
    "gitlab": "https://eee-project.gitlab.io/created_with_eee",
}


def parse_hosts(pairs):
    if not pairs:
        return dict(DEFAULT_HOSTS)
    out = {}
    for pair in pairs:
        name, url = pair.split("=", 1)
        out[name] = url.rstrip("/")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", action="append", dest="hosts", help="name=base_url, repeatable")
    ap.add_argument("--lesson-path", required=True, help="e.g. ancient_greek/odyssey/2026_06_01")
    ap.add_argument("--boot-wait", type=int, default=70, help="seconds to wait for the WASM lesson to boot")
    args = ap.parse_args()

    hosts = parse_hosts(args.hosts)
    lesson_parts = args.lesson_path.strip("/").split("/")
    ok = True

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, base in hosts.items():
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))

            t0 = time.time()
            page.goto(f"{base}/", wait_until="load", timeout=15000)
            page.wait_for_timeout(300)
            cards = page.locator("a.eee-card").count()
            print(f"[{name}] root: {time.time()-t0:.2f}s, cards={cards}")
            if cards == 0:
                print(f"[{name}] FAIL: root hub has no cards")
                ok = False

            # walk down through each path segment except the last (the lesson itself),
            # matching the card whose href contains that segment -- clicking nth=0
            # blindly would always follow the first card regardless of --lesson-path
            for segment in lesson_parts[:-1]:
                card = f'a.eee-card[href*="{segment}"]'
                with page.expect_navigation(timeout=10000):
                    page.click(f"{card} >> nth=0")
                page.wait_for_timeout(300)
                cards = page.locator("a.eee-card").count()
                print(f"[{name}] -> {page.url} cards={cards}")

            # final click into the real lesson: don't wait on "load" (200+ preloads
            # make that exceed 10s over a real network) -- click, confirm the URL
            # changed, then wait out the known WASM boot before reading content.
            t1 = time.time()
            last_segment = lesson_parts[-1]
            page.click(f'a.eee-card[href*="{last_segment}"] >> nth=0', timeout=10000)
            page.wait_for_timeout(1500)
            lesson_url = page.url
            print(f"[{name}] -> {lesson_url} (WASM boot starting)")
            page.wait_for_timeout(args.boot_wait * 1000)
            text = page.locator("body").inner_text()
            elapsed = time.time() - t1
            print(f"[{name}] lesson booted in ~{elapsed:.1f}s, text_len={len(text)}, js_errors={errors}")
            if len(text) < 200 or errors:
                print(f"[{name}] FAIL: lesson content too short or JS errors present")
                ok = False
            page.close()
        browser.close()

    print("\nALL HOSTS OK" if ok else "\nSOME HOSTS FAILED - see above")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
