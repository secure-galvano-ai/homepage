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
# WhatsApp-FAB abgeschaltet am 07.09.2026 (Stefan): der Button trug die private
# Mobilnummer im Klartext auf jeder Seite -- maschinell abgreifbar und seither
# Quelle laufender Phishing-Anfragen von unbekannten Nummern. Die Marker bleiben in
# den Seiten stehen, der Block wird leer gerendert; damit ist der Knopf ueber diese
# eine Konstante wieder aktivierbar, ohne dass eine Nummer im Repo liegt.
# Kontaktweg bleibt Erstgespraech-Buchung + mailto.

# --- Nav: one canonical link set; `active` per page highlights the current one -
# (href, label) — the Erstgespraech-CTA is appended separately.
NAV_LINKS = [
    ("leistungen.html", "Leistungen"),
    # "Demo" steht bewusst an zweiter Stelle: Reihenfolge nach der Kaufentscheidung --
    # was macht ihr, wie sieht das aus, wer seid ihr. Vier Eintraege plus CTA liegen im
    # empfohlenen Rahmen von vier bis sechs (31.08.2026).
    ("demo.html", "Demo"),
    # Seit 02.09.2026 wieder in der Navigation (Stefan): das Ausbildungsangebot ist der neue
    # Angebotsschwerpunkt. Label "Datenwerkstatt" -- der naheliegende Name "KI-Werkstatt" ist
    # in derselben Region bereits belegt: die WKO Vorarlberg fuehrt unter diesem Namen ein
    # eigenes Workshop-Programm fuer Vorarlberger KMU (geprueft 02.09.2026). Verwechslung mit
    # einem Verbandsangebot waere doppelt schaedlich -- die WKO ist Netzwerk, kein Wettbewerber.
    # "Daten" statt "KI" trifft zudem die Positionierung genauer. Fuenf Eintraege plus CTA
    # liegen noch im empfohlenen Rahmen von vier bis sechs.
    ("ausbildung.html", "Datenwerkstatt"),
    ("ueber-mich.html", "Über mich"),
    ("forschung.html", "Forschung"),
]

# --- Footer: full cross-link set (label, href, new_tab) ----------------------
FOOTER_LINKS = [
    ("Startseite", "index.html", False),
    ("Leistungen", "leistungen.html", False),
    ("Demo", "demo.html", False),
    ("Datenwerkstatt", "ausbildung.html", False),
    ("Über mich", "ueber-mich.html", False),
    ("Sicherheit (PDF)", "docs/sicherheit-methoden-standards.pdf", True),
    ("Forschung", "forschung.html", False),
    # Seite ist seit 11.08.2026 wieder indexiert: Compliance (NIS2 ab 10/2026, AI Act)
    # ist im Verkauf ein echter Einwand und diese Seite die einzige Antwort darauf.
    # Bewusst nur im Footer, nicht in der Hauptnavigation -- der Fokus-Umbau vom
    # 30.07.2026 soll nicht wieder verwaessert werden.
    ("Sicherheit", "sicherheit.html", False),
    ("Impressum", "impressum.html", False),
    ("Datenschutz", "datenschutz.html", False),
]
# Bewusst ein Verweis statt einer Schutzzusage: "Personenbezogene Daten sind gemaess der
# DSGVO geschuetzt" ist eine pauschale Rechtsaussage im Footer, die niemand pruefen kann und
# die im Streitfall gegen uns ausgelegt wird. Der Verweis auf die Datenschutzerklaerung ist
# rechtlich sauberer und sagt inhaltlich mehr. Geaendert 11.08.2026.
FOOTER_COPY = (
    "Hinweise zur Verarbeitung personenbezogener Daten finden Sie in der "
    '<a href="datenschutz.html">Datenschutzerklärung</a>. '
    "&copy; 2025&ndash;2026 secure-galvano-ai"
)

# --- Pages that carry the layout markers; value = active nav href (or None) ---
PAGES = {
    "index.html": None,
    "leistungen.html": "leistungen.html",
    # Seit 31.08.2026 mit eigenem Nav-Eintrag (Stefan). Die Seite behaelt die
    # Navigation bewusst -- sie ist Teil der Website, keine bezahlte Landingpage,
    # bei der man die Nav entfernen wuerde.
    "demo.html": "demo.html",
    # Seit 31.08.2026 hier statt handgepflegt: die Seite hatte den Demo-Eintrag
    # nicht mitbekommen, weil ihre Navigation als einzige nicht generiert wurde.
    "sicherheit.html": None,
    # Neu aufgebaut am 02.09.2026 -- vorher ein Redirect-Stub auf die Startseite.
    "ausbildung.html": "ausbildung.html",
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
            <li><a href="{BOOKING_URL}" target="_blank" rel="noopener" class="nav-cta" data-funnel="cta-nav">Erstgespräch</a></li>
        </ul>
        <button class="nav-toggle" id="navToggle" aria-label="Menü" aria-expanded="false">
            <span></span><span></span><span></span>
        </button>
    </div>
</nav>"""


def render_wa_fab() -> str:
    """Leerer Block seit 07.09.2026 -- siehe Kommentar bei BOOKING_URL."""
    return "<!-- WhatsApp-Kontakt deaktiviert (07.09.2026) -->"


def render_sticky_cta() -> str:
    return f"""<div class="sticky-cta" id="stickyCta">
    <a href="{BOOKING_URL}" target="_blank" rel="noopener" data-funnel="cta-sticky">Kostenloses Erstgespräch buchen</a>
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
