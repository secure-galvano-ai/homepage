"""Render the shared layout chrome (nav, footer, WhatsApp-FAB, Sticky-CTA) from
one source into every page.

Single source of truth = the data below (NAV_LINKS, FOOTER_LINKS, the FAB/Sticky
constants). Running this script rewrites the marked regions on each page in
PAGES, so nav and footer can never drift apart again. The output is committed as
plain HTML -> stays crawlable and works without JavaScript.

Usage:
    py _generate_layout.py

Add a nav entry            -> edit NAV_LINKS, re-run.
Bring a page into the set  -> add the four marker pairs to its <body>, list it in
                              PAGES, re-run. The markers are:
    <!-- BEGIN nav -->            <!-- END nav -->
    <!-- BEGIN wa-fab -->         <!-- END wa-fab -->
    <!-- BEGIN sticky-cta -->     <!-- END sticky-cta -->
    <!-- BEGIN footer -->         <!-- END footer -->

Never edit the HTML between the markers by hand -- it is overwritten on the next
run. Styling for all of it lives in assets/css/base.css, behaviour in
assets/js/site.js.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent

BOOKING_URL = "https://outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/"
WHATSAPP_URL = (
    "https://wa.me/4368181483538?text="
    "Hallo%20Stefan%2C%20ich%20habe%20eine%20Frage%20zu%20Ihren%20Leistungen."
)

# --- Nav: one canonical link set; `active` per page highlights the current one -
# (href, label) — the Erstgespraech-CTA is appended separately.
NAV_LINKS = [
    ("leistungen.html", "Leistungen"),
    ("ueber-mich.html", "Über mich"),
    ("forschung.html", "Forschung"),
]

# --- Footer: full cross-link set (label, href, new_tab) ----------------------
FOOTER_LINKS = [
    ("Startseite", "index.html", False),
    ("Leistungen", "leistungen.html", False),
    ("Über mich", "ueber-mich.html", False),
    ("Sicherheit (PDF)", "docs/sicherheit-methoden-standards.pdf", True),
    ("Forschung", "forschung.html", False),
    ("Impressum", "impressum.html", False),
    ("Datenschutz", "datenschutz.html", False),
]
FOOTER_COPY = (
    "Personenbezogene Daten sind gemäß der DSGVO geschützt. "
    "&copy; 2025&ndash;2026 secure-galvano-ai"
)

# --- Pages that carry the layout markers; value = active nav href (or None) ---
PAGES = {
    "index.html": None,
    "leistungen.html": "leistungen.html",
    "ueber-mich.html": "ueber-mich.html",
    "forschung.html": "forschung.html",
    "impressum.html": None,
    "datenschutz.html": None,
}


def render_nav(active: str | None) -> str:
    items = []
    for href, label in NAV_LINKS:
        cls = ' class="active"' if href == active else ""
        items.append(f'            <li><a href="{href}"{cls}>{label}</a></li>')
    links = "\n".join(items)
    return f"""<nav class="nav" id="nav">
    <div class="container nav-inner">
        <a href="index.html" class="nav-logo">
            <img src="assets/img/logo.png" alt="secure galvano ai">
            <span>secure galvano ai</span>
        </a>
        <ul class="nav-links" id="navLinks">
{links}
            <li><a href="{BOOKING_URL}" target="_blank" rel="noopener" class="nav-cta">Erstgespräch</a></li>
        </ul>
        <button class="nav-toggle" id="navToggle" aria-label="Menü" aria-expanded="false">
            <span></span><span></span><span></span>
        </button>
    </div>
</nav>"""


def render_wa_fab() -> str:
    return f"""<a class="wa-fab" href="{WHATSAPP_URL}" target="_blank" rel="noopener" aria-label="Per WhatsApp anfragen">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.247-.694.247-1.289.173-1.413-.074-.124-.272-.198-.57-.347zM12.05 21.785h-.005a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.999-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.002-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884zm8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    <span class="wa-label">Sprechen wir über Ihre Möglichkeiten</span>
</a>"""


def render_sticky_cta() -> str:
    return f"""<div class="sticky-cta" id="stickyCta">
    <a href="{BOOKING_URL}" target="_blank" rel="noopener">Kostenloses Erstgespräch buchen</a>
</div>"""


def render_footer() -> str:
    items = []
    for label, href, new_tab in FOOTER_LINKS:
        attrs = ' target="_blank" rel="noopener"' if new_tab else ""
        items.append(f'                <li><a href="{href}"{attrs}>{label}</a></li>')
    items.append(
        '                <li><a href="#" class="cookie-settings">Cookie-Einstellungen</a></li>'
    )
    links = "\n".join(items)
    return f"""<footer class="footer">
    <div class="container">
        <div class="footer-inner">
            <div class="footer-logo">
                <img src="assets/img/logo.png" alt="secure galvano ai">
                <span>secure galvano ai</span>
            </div>
            <ul class="footer-links">
{links}
            </ul>
            <p class="footer-copy">{FOOTER_COPY}</p>
        </div>
    </div>
</footer>"""


def inject(text: str, marker: str, inner_html: str) -> str:
    """Replace the content between the BEGIN/END markers for `marker`."""
    begin = f"<!-- BEGIN {marker} -->"
    end = f"<!-- END {marker} -->"
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"Marker '{marker}' not found")
    note = "<!-- AUTO-GENERATED by _generate_layout.py -- do not edit by hand -->"
    replacement = f"{begin}\n{note}\n{inner_html}\n{end}"
    return pattern.sub(replacement, text)


def main() -> None:
    print(f"Rendering shared layout into up to {len(PAGES)} pages...")
    updated, skipped = 0, []
    for filename, active in PAGES.items():
        path = ROOT / filename
        if not path.exists():
            raise SystemExit(f"Page not found: {filename}")
        text = path.read_text(encoding="utf-8")
        # A page joins the system once it carries the markers; until then skip it
        # (keeps the rollout incremental instead of failing on un-migrated pages).
        if "<!-- BEGIN nav -->" not in text:
            skipped.append(filename)
            continue
        # nav + footer are on every page; wa-fab + sticky-cta only where the page
        # actually carries that marker (the Sticky-CTA e. g. is start-page-only).
        text = inject(text, "nav", render_nav(active))
        text = inject(text, "footer", render_footer())
        if "<!-- BEGIN wa-fab -->" in text:
            text = inject(text, "wa-fab", render_wa_fab())
        if "<!-- BEGIN sticky-cta -->" in text:
            text = inject(text, "sticky-cta", render_sticky_cta())
        path.write_text(text, encoding="utf-8")
        print(f"  updated {filename}")
        updated += 1
    if skipped:
        print(f"  skipped (no markers yet): {', '.join(skipped)}")
    print(f"Done. {updated} updated, {len(skipped)} skipped.")


if __name__ == "__main__":
    main()
