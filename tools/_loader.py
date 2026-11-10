"""The loading overlay of an exported lesson page: the EEE logo and the lesson title on a white screen, until the lesson shows its first text.

A marimo `html-wasm` page is blank or shows marimo's own English spinner for the 10-30 s that Pyodide needs to start. The overlay is drawn by the page's
own HTML, so it shows at once and adds no request except the fonts. It looks like the loader of eee-project's shell (examples/deploy/shell_template.html).
`export-notebooks.py` puts it into every page it exports; `add-loader.py` puts it into pages exported before; `check-loader.py` checks the pages.

The overlay sits before `<div id="root"></div>`. A script looks at the root twice a second and hides the overlay when the root holds more than 100 characters of
text; after 150 s it hides the overlay anyway, so a page that never shows text is not covered for ever.
"""
import html
import pathlib
import re

ROOT = '<div id="root"></div>'
MARKER = 'id="eee-loader"'

LOADER = """<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;700;800&display=swap" media="print" onload="this.media='all'">
<style>
#eee-loader{position:fixed;inset:0;z-index:2147483000;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;transition:opacity .4s ease,visibility .4s ease;font-family:Syne,system-ui,sans-serif}
#eee-loader.eee-ld-hidden{opacity:0;visibility:hidden;pointer-events:none}
.eee-ld-logo{position:relative;width:72px;height:72px}
.eee-ld-ring{position:absolute;inset:0;border-radius:50%;border:2px solid transparent;border-top-color:#003d82;border-right-color:#5f27cd;animation:eee-ld-spin 1.2s linear infinite}
.eee-ld-ring:nth-child(2){inset:8px;border-top-color:#5f27cd;border-right-color:#003d82;animation-direction:reverse;animation-duration:1.8s}
.eee-ld-dot{position:absolute;inset:18px;border-radius:50%;background:linear-gradient(135deg,#003d82,#5f27cd);animation:eee-ld-pulse 2s ease-in-out infinite}
@keyframes eee-ld-spin{to{transform:rotate(360deg)}}
@keyframes eee-ld-pulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(.85);opacity:.7}}
.eee-ld-name{font-size:20px;font-weight:800;letter-spacing:-.02em;background:linear-gradient(90deg,#003d82,#5f27cd);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.eee-ld-title{font-family:"DM Mono",ui-monospace,monospace;font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:#666;text-align:center;padding:0 24px}
@media (prefers-reduced-motion:reduce){.eee-ld-ring,.eee-ld-dot{animation:none}}
</style>
<div id="eee-loader" role="status"><div class="eee-ld-logo"><div class="eee-ld-ring"></div><div class="eee-ld-ring"></div><div class="eee-ld-dot"></div></div><div class="eee-ld-name">EEE</div><div class="eee-ld-title">%%TITLE%%</div></div>
<script>
(function(){var el=document.getElementById("eee-loader");
function done(){clearInterval(t);clearTimeout(g);el.classList.add("eee-ld-hidden");setTimeout(function(){el.remove()},500)}
var t=setInterval(function(){var r=document.getElementById("root");if(r&&r.innerText.trim().length>100)done()},500),g=setTimeout(done,150000)})();
</script>
"""


def add_loader(page: str) -> str:
    """The page with the overlay before its root div; a page that has the overlay is returned as it is. A page without exactly one root div raises ValueError."""
    if MARKER in page:
        return page
    if page.count(ROOT) != 1:
        raise ValueError(f"expected one {ROOT} in the page, found {page.count(ROOT)}")
    m = re.search(r"<title>(.*?)</title>", page, re.S)
    title = html.escape(html.unescape(m.group(1).strip())) if m else "EEE"
    return page.replace(ROOT, LOADER.replace("%%TITLE%%", title) + ROOT)


def add_loader_to_file(path: pathlib.Path) -> None:
    """Put the overlay into one page file, byte for byte otherwise. A file that has the overlay is not written."""
    page = path.read_bytes().decode("utf-8")
    patched = add_loader(page)
    if patched != page:
        path.write_bytes(patched.encode("utf-8"))


def index_pages(root: pathlib.Path) -> "list[pathlib.Path]":
    """Every index.html below a pages checkout."""
    return sorted(root.rglob("index.html"))
