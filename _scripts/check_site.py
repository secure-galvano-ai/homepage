"""check_site.py — Self-Check fuer die statische Homepage.

Das "pyright/ruff der Homepage": faengt genau die Fehler ab, die beim Hantieren
mit vielen HTML-Seiten + geteiltem CSS entstehen. Zero-Dependency ausser
tinycss2 (CSS-Parser); fehlt es, wird der CSS-Parse-Check uebersprungen.

Checks (E = Error -> Exit 1, W = Warnung -> Exit 0):
  1. HTML wohlgeformt        (balancierter Tag-Stack, void/opaque-aware)   E
  2. CSS parst sauber        (base.css, leistungen.css, jeder <style>-Block) E
  3. var(--token) aufloesbar (gegen base.css :root + Seiten-eigenes :root)  E
  4. Layout-Marker           (nav/footer vorhanden + nicht leer)           E
  5. Generator-Sync          (Marker-Inhalt == _generate_layout-Ausgabe)   E
  6. Interne Links / Assets  (href/src auf lokale Datei existiert)         E
  7. Transliterations-Reste  (ae/oe/ue in Sichttext, kuratierte Ausnahmen) W

Aufruf:
    py scripts/check_site.py            # alle Root-*.html
    py scripts/check_site.py index.html # gezielt
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
# Transliterierte Staemme (ae/oe/ue statt ä/ö/ü) die im Deutschen fast NIE
# legitim sind -> hoch-signalhaft, im Gegensatz zu einem generischen ue-Scan
# (steuer, dauer, quelle, schauen enthalten legitim "ue"). Nur auf SICHTTEXT.
TRANSLIT_BAD = re.compile(
    r"\b(fuer|ueber|frueh|spaet|moeglich|koenn|muess|loesung|groess|qualitaet|"
    r"waehrend|gemaess|taetig|massnahme|natuerlich|oeffn|verfuegb|zusaetz|"
    r"geschaeft|staerk|faehig|aehnlich|buero|loesch|fuehr|hoeh|gebaeud|"
    r"vertraeg|einfuehr|durchfuehr|ausfuehr|erklaer|gehoer)[a-zäöüß]*",
    re.IGNORECASE)

errors: list[str] = []
warns: list[str] = []


def err(page: str, msg: str) -> None:
    errors.append(f"  [E] {page}: {msg}")


def warn(page: str, msg: str) -> None:
    warns.append(f"  [W] {page}: {msg}")


# ---- 1. HTML well-formedness -------------------------------------------------
class TagStack(HTMLParser):
    def __init__(self, page: str):
        super().__init__(convert_charrefs=True)
        self.page = page
        self.stack: list[tuple[str, int]] = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass  # self-closing -> balanced

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        # pop to the matching open tag (tolerate optional-close tags like <p>,<li>)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return
        err(self.page, f"</{tag}> ohne offenes <{tag}>")


def check_html(page: str, html: str) -> None:
    p = TagStack(page)
    try:
        p.feed(html)
    except Exception as e:  # pragma: no cover - parser rarely throws
        err(page, f"HTML-Parse-Fehler: {e}")
        return
    OPTIONAL = {"p", "li", "dt", "dd", "option", "thead", "tbody", "tr", "td", "th"}
    for tag, line in p.stack:
        if tag not in OPTIONAL:
            err(page, f"<{tag}> (Zeile {line}) nie geschlossen")


# ---- 2. CSS parses -----------------------------------------------------------
def check_css(page: str, css: str, where: str) -> None:
    try:
        import tinycss2
    except ImportError:
        return
    rules = tinycss2.parse_stylesheet(css, skip_whitespace=True)
    for r in rules:
        if r.type == "error":
            err(page, f"CSS-Fehler in {where}: {r.message}")
    if css.count("{") != css.count("}"):
        err(page, f"CSS-Klammern unbalanciert in {where} "
                  f"({css.count('{')} vs {css.count('}')})")


# ---- 3. token resolution -----------------------------------------------------
def defined_tokens(css_texts: list[str]) -> set[str]:
    toks: set[str] = set()
    for css in css_texts:
        for m in re.finditer(r"(--[a-zA-Z0-9-]+)\s*:", css):
            toks.add(m.group(1))
    return toks


# ---- helpers -----------------------------------------------------------------
def style_blocks(html: str) -> list[str]:
    return re.findall(r"<style>(.*?)</style>", html, re.DOTALL)


def marker_content(html: str, name: str):
    m = re.search(re.escape(f"<!-- BEGIN {name} -->") + r"(.*?)"
                  + re.escape(f"<!-- END {name} -->"), html, re.DOTALL)
    return None if m is None else m.group(1)


# ---- main --------------------------------------------------------------------
def main() -> int:
    base_css = (ROOT / "assets/css/base.css").read_text(encoding="utf-8")
    leist_css = (ROOT / "assets/css/leistungen.css").read_text(encoding="utf-8")
    base_tokens = defined_tokens([base_css])

    check_css("base.css", base_css, "base.css")
    check_css("leistungen.css", leist_css, "leistungen.css")

    # generator sync
    sys.path.insert(0, str(ROOT))
    try:
        import _generate_layout as gen
    except Exception as e:  # pragma: no cover
        gen = None
        warn("_generate_layout", f"nicht importierbar ({e}) -> Sync-Check aus")

    args = sys.argv[1:]
    pages = [ROOT / a for a in args] if args else sorted(ROOT.glob("*.html"))

    for path in pages:
        page = path.name
        html = path.read_text(encoding="utf-8")

        check_html(page, html)

        blocks = style_blocks(html)
        for i, css in enumerate(blocks):
            check_css(page, css, f"<style> #{i}")

        # token resolution: base + this page's own :root tokens
        page_tokens = base_tokens | defined_tokens(blocks)
        used = set(re.findall(r"var\((--[a-zA-Z0-9-]+)\)", html))
        for u in sorted(used - page_tokens):
            err(page, f"undefiniertes Token {u}")

        # layout markers + generator sync
        if gen and page in gen.PAGES:
            active = gen.PAGES[page]
            for name, want in [("nav", gen.render_nav(active)),
                               ("footer", gen.render_footer()),
                               ("wa-fab", gen.render_wa_fab()),
                               ("sticky-cta", gen.render_sticky_cta())]:
                have = marker_content(html, name)
                required = name in ("nav", "footer")
                if have is None:
                    if required:
                        err(page, f"Marker '{name}' fehlt")
                    continue
                if not have.strip():
                    err(page, f"Marker '{name}' ist leer -> py _generate_layout.py")
                elif want.strip() not in have:
                    err(page, f"Marker '{name}' nicht in Sync -> py _generate_layout.py")

        # internal links / assets exist
        refs = re.findall(r'(?:href|src)="([^"#?][^"]*?)"', html)
        for ref in refs:
            if re.match(r"^(https?:|mailto:|tel:|data:|//|#)", ref):
                continue
            if "${" in ref or "{{" in ref:  # JS-Template / dynamischer Pfad
                continue
            target = (ROOT / ref.split("#")[0].split("?")[0]).resolve()
            if not target.exists():
                err(page, f"toter Verweis: {ref}")

        # transliteration in visible text (strip comments/scripts/styles/tags;
        # comments + class names are legit ASCII, only user-facing text counts)
        visible = re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)
        visible = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", visible, flags=re.DOTALL)
        visible = re.sub(r"<[^>]+>", " ", visible)
        for m in TRANSLIT_BAD.finditer(visible):
            warn(page, f"moegliche Transliteration: '{m.group(0)}'")

    print(f"check_site: {len(pages)} Seiten geprueft")
    for line in warns:
        print(line)
    if errors:
        print(f"\nFEHLER ({len(errors)}):")
        for line in errors:
            print(line)
        return 1
    print("OK — keine Fehler.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
