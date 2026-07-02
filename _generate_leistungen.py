"""Generate the Leistungsbausteine cards (catalog + teaser) from one data source.

Single source of truth = the LEISTUNGEN list below. Running this script renders
static HTML into the marked regions of leistungen.html (full catalog) and
index.html (teaser row). The output is committed as plain HTML, so it stays
crawlable and works without JavaScript.

Usage:
    py _generate_leistungen.py

Extend a service = add/edit a dict in LEISTUNGEN, then re-run. Never edit the
generated HTML between the BEGIN/END markers by hand -- it will be overwritten.
"""

from __future__ import annotations

import html
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent

# All Mail-CTAs go to the business address used across the site.
CONTACT_EMAIL = "smaier@rvh.at"

# --- Icons (feather-style inner SVG, reused from the existing site cards) -----
_SVG_OPEN = (
    "<svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" "
    "stroke=\"#2B5EA7\" stroke-width=\"1.6\" stroke-linecap=\"round\" "
    "stroke-linejoin=\"round\">"
)
ICONS = {
    "search": "<circle cx=\"11\" cy=\"11\" r=\"8\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/>",
    "pulse": "<path d=\"M3 12h4l3 9 4-18 3 9h4\"/>",
    "dashboard": "<rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\"/><line x1=\"3\" y1=\"9\" x2=\"21\" y2=\"9\"/><line x1=\"9\" y1=\"21\" x2=\"9\" y2=\"9\"/>",
    "database": "<ellipse cx=\"12\" cy=\"5\" rx=\"9\" ry=\"3\"/><path d=\"M3 5v6c0 1.66 4 3 9 3s9-1.34 9-3V5\"/><path d=\"M3 11v6c0 1.66 4 3 9 3s9-1.34 9-3v-6\"/>",
    "users": "<path d=\"M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2\"/><circle cx=\"12\" cy=\"7\" r=\"4\"/>",
    "shield": "<path d=\"M12 3l8 3v6c0 5-3.4 8.3-8 9-4.6-.7-8-4-8-9V6l8-3z\"/><path d=\"M9 12l2 2 4-4\"/>",
}


def _icon(name: str) -> str:
    return f"{_SVG_OPEN}{ICONS[name]}</svg>"


# --- Single source of truth ---------------------------------------------------
# id       : anchor on leistungen.html + used for #deep-links from the teaser
# title    : card heading
# teaser   : one glanceable sentence ("1. Blick")
# category : label for the chip / future filter (data-cat attribute)
# icon     : key into ICONS
# details  : bullet points shown when the card is expanded ("bei Interesse")
# more     : (label, href) link to the full detail page/section, or None
LEISTUNGEN = [
    {
        "id": "ki-diagnose",
        "title": "KI-Diagnose",
        "teaser": "Findet die Ursache hinter Ausschuss und Reklamationen — mit Ihren vorhandenen Daten.",
        "category": "Diagnose",
        "icon": "search",
        "details": [
            "Ausgewertet wird nur, was Ihre Anlage ohnehin aufzeichnet — kein Eingriff in den Betrieb",
            "Konkret benannt: welche Anlage, welcher Parameter, welche Schicht",
            "Bericht, Management-Foliensatz und KI-Klick-Demo mit Ihren eigenen Daten",
        ],
        "more": ("Zum Einstieg — die Diagnose", "leistungen.html#preise"),
    },
    {
        "id": "live-monitoring",
        "title": "Live-Monitoring",
        "teaser": "Erkennt Auffälligkeiten im laufenden Betrieb — bevor sie beim Kunden landen.",
        "category": "Live-Betrieb",
        "icon": "pulse",
        "details": [
            "Anomalieerkennung auf Bad-, Gleichrichter- und Schichtdaten",
            "Läuft lokal auf abgeschotteter Hardware, kein Cloud-Upload",
            "Meldung rechtzeitig bei der richtigen Person, statt hunderter Fehlalarme",
        ],
        "more": ("Was nach der Diagnose möglich wird", "leistungen.html#folgewege"),
    },
    {
        "id": "kpi-dashboard",
        "title": "KPI-Dashboard & Berichte",
        "teaser": "Auswertungen und Berichte für QM, Behörde und Hauptkunden — verständlich aufbereitet.",
        "category": "Live-Betrieb",
        "icon": "dashboard",
        "details": [
            "KPI-Dashboard auf Ihren eigenen Daten",
            "Berichte für Audits, Reklamationsgespräche und Förderanträge",
            "Kontinuierliches Tracking mit quartalsweiser Verifikation",
        ],
        "more": ("Folgewege ansehen", "leistungen.html#folgewege"),
    },
]


def _esc(text: str) -> str:
    return html.escape(text, quote=True)


def _mailto(item: dict) -> str:
    """Prefilled mailto: link for one Baustein — direct contact is the goal."""
    subject = f"Anfrage: {item['title']}"
    body = (
        f"Hallo Stefan,\n\n"
        f"ich interessiere mich fuer {item['title']}.\n\n"
        f"Unternehmen:\n"
        f"Standort (PLZ/Ort):\n"
        f"Worum es geht:\n\n"
        f"Vielen Dank!"
    )
    query = urllib.parse.urlencode(
        {"subject": subject, "body": body}, quote_via=urllib.parse.quote
    )
    return f"mailto:{CONTACT_EMAIL}?{query}"


def render_catalog_card(item: dict) -> str:
    """Full card with expandable details ("bei Interesse Details anzeigen")."""
    bullets = "\n".join(
        f"                    <li>{_esc(b)}</li>" for b in item["details"]
    )
    more = ""
    if item.get("more"):
        label, href = item["more"]
        more = (
            f"\n                    <a class=\"leistung-morelink\" href=\"{_esc(href)}\">"
            f"{_esc(label)} →</a>"
        )
    return f"""            <article class="leistung-card" id="{item['id']}" data-cat="{_esc(item['category'])}">
                <div class="leistung-icon">{_icon(item['icon'])}</div>
                <span class="leistung-cat">{_esc(item['category'])}</span>
                <h3>{_esc(item['title'])}</h3>
                <p class="leistung-teaser">{_esc(item['teaser'])}</p>
                <details class="leistung-more">
                    <summary>Details</summary>
                    <ul class="leistung-detaillist">
{bullets}
                    </ul>{more}
                </details>
                <a class="leistung-mailbtn" href="{_esc(_mailto(item))}" data-funnel="mail-baustein">✉ Per Mail anfragen</a>
            </article>"""


def render_home_card(item: dict) -> str:
    """Compact card for the home page: teaser + link to the full entry + mail CTA.

    Keeps the start page scannable (no inline details -> those live on
    leistungen.html), while every Baustein still carries a direct mail button.
    """
    return f"""            <article class="leistung-card" data-cat="{_esc(item['category'])}">
                <div class="leistung-icon">{_icon(item['icon'])}</div>
                <span class="leistung-cat">{_esc(item['category'])}</span>
                <h3>{_esc(item['title'])}</h3>
                <p class="leistung-teaser">{_esc(item['teaser'])}</p>
                <a class="leistung-morelink" href="leistungen.html#{item['id']}">Details ansehen →</a>
                <a class="leistung-mailbtn" href="{_esc(_mailto(item))}" data-funnel="mail-baustein">✉ Per Mail anfragen</a>
            </article>"""


def inject(path: Path, marker: str, inner_html: str) -> None:
    """Replace the content between the BEGIN/END markers for `marker` in `path`."""
    text = path.read_text(encoding="utf-8")
    begin = f"<!-- BEGIN {marker} -->"
    end = f"<!-- END {marker} -->"
    pattern = re.compile(
        re.escape(begin) + r".*?" + re.escape(end), re.DOTALL
    )
    if not pattern.search(text):
        raise SystemExit(f"Marker '{marker}' not found in {path.name}")
    note = "<!-- AUTO-GENERATED by _generate_leistungen.py — do not edit by hand -->"
    replacement = f"{begin}\n            {note}\n{inner_html}\n            {end}"
    path.write_text(pattern.sub(replacement, text), encoding="utf-8")
    print(f"  updated {path.name} [{marker}]")


def main() -> None:
    catalog_html = "\n".join(render_catalog_card(i) for i in LEISTUNGEN)

    print(f"Rendering {len(LEISTUNGEN)} Leistungsbausteine...")
    # leistungen.html = full catalog (expandable details).
    # index.html traegt seit dem Predictive-Quality-Reposition keine Teaser-Karten
    # mehr (eine Treppe statt Kachel-Menue) -> nur noch leistungen.html rendern.
    inject(ROOT / "leistungen.html", "leistungen:catalog", catalog_html)
    print("Done.")


if __name__ == "__main__":
    main()
