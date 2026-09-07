"""Render certificate pages from CV PDF into thumbnails + full-size JPGs.

Source: Business Development/resources/credentials/20260512_Lebenslauf & Nachweise_Stefan Maier.pdf
Output: homepage/credentials/thumbs/<slug>.jpg (~600w) + homepage/credentials/full/<slug>.jpg (~1800w)

Run: py homepage/credentials/_generate_credentials.py
"""
from __future__ import annotations

from pathlib import Path

import fitz
from PIL import Image, ImageStat

ROOT = Path(__file__).resolve().parents[2]
PDF_PATH = ROOT / "Business Development" / "resources" / "credentials" / "20260512_Lebenslauf & Nachweise_Stefan Maier.pdf"
OUT_DIR = Path(__file__).resolve().parent
THUMB_DIR = OUT_DIR / "thumbs"
FULL_DIR = OUT_DIR / "full"

THUMB_WIDTH = 600
FULL_WIDTH = 1800
THUMB_QUALITY = 85
FULL_QUALITY = 90

# (page_num, slug, title, subtitle, year, category)
# page_num is 1-indexed, matching the 29-page PDF.
# Page 17 (Startup Vorarlberg "Pre-Inkubation Batch #3") is intentionally omitted
# from the public gallery — it is a program-participation certificate, not a
# personal qualification, so it does not fit the credential categories below.
CERTIFICATES = [
    (10, "02-msc-bescheid", "Master of Science — Verleihungsurkunde", "Universität Wien", "2016", "akademisch"),
    (12, "03-msc-abschluss", "Master Abschlusszeugnis", "Universität Wien — Notenschnitt 1,1, mit Auszeichnung bestanden", "2016", "akademisch"),
    (13, "04-msc-masterarbeit", "Beurteilung Masterarbeit", "High Pressure Torsion auf CoCrFeMnNi High-Entropy-Alloy", "2016", "akademisch"),

    (27, "06-lehrbrief-oberflaechentechniker", "Lehrbrief Oberflächentechniker", "WKO Vorarlberg", "2006", "galvanik"),
    (15, "07-meisterpruefung", "Meisterprüfung Oberflächentechnik", "WKO Kärnten", "2009", "galvanik"),

    (19, "08-senior-process-manager", "Senior Process Manager (SPüK)", "Zertifizierungsstelle WIFI / Quality Austria", "2017", "management"),
    (16, "09-itil-foundation", "ITIL Foundation in IT Service Management", "APMG International / AXELOS", "2017", "management"),
    (21, "10-projektmanagement-pmi", "Projektmanagement Grundlagen nach PMI®", "EFS Unternehmensberatung", "2016", "management"),
    (22, "11-scrum", "SCRUM Schulung", "EFS Unternehmensberatung", "2017", "management"),
    (18, "12-wertstrom-workshop", "Wertstrom-Expertenworkshop", "IPAL Institute for Productivity and applied Leadership", "2023", "management"),
    (28, "13-lehrbrief-industriekaufmann", "Lehrbrief Industriekaufmann (mit Auszeichnung)", "WKO Vorarlberg", "2006", "management"),
    (25, "14-ausbildertraining", "Zeugnis Ausbildertraining", "Lernlabor, Prüfungsort Hohenems", "2008", "management"),
    (26, "15-sicherheitsvertrauensperson", "Sicherheitstechnisches Seminar (SVP)", "AUVA Landesstelle Salzburg", "2007", "management"),

    (24, "16-psychologischer-berater", "Psychologischer Berater / Personal Coach", "Hamburger Akademie für Fernstudien (Note 1,7)", "2018", "weiterbildung"),
    (23, "17-channel-ausbildung", "Channel-Ausbildung", "Rhiannon Augenthaler", "2024", "weiterbildung"),
]


# --- Schwaerzungen (Stefan, 07.09.2026) -------------------------------------
# Die Galerie ist oeffentlich. Zwei Sorten Angaben gehoeren dort nicht hin:
#
#   1. **Geburtsdatum und Matrikel-/Kandidatennummer.** Zusammen mit Name und
#      Impressumsadresse sind das die Felder, mit denen Identitaetspruefungen am
#      Telefon bestanden werden. Fuer den Nachweis der Qualifikation traegt
#      keines von beiden etwas bei.
#   2. **Unterschriften Dritter.** Sie sind personenbezogene Daten der
#      Unterzeichnenden. Das berechtigte Interesse (Art. 6 Abs. 1 lit. f DSGVO)
#      deckt den Qualifikationsnachweis, aber die Abwaegung fragt nach
#      Erforderlichkeit -- und die Urkunde belegt dasselbe ohne den Schriftzug.
#      Bei den Ausstellern, die Einzelunternehmen sind, ist eine frei kopierbare
#      Unterschrift zudem ein Faelschungsrisiko fuer die Person.
#
# **Diese Liste ist der Grund, warum die Schwaerzung hier steht und nicht in den
# fertigen JPGs.** Wer die Bilder von Hand nachbearbeitet, verliert die Arbeit
# beim naechsten Lauf dieses Skripts -- derselbe Fehlermodus wie bei
# `generate_bmc.py` und `Roadmap Stefan.xlsx` (ZENTRALDOKUMENT.md §1).
#
# Koordinaten sind **relativ** (x0, y0, x1, y1 in 0..1), gelten also fuer Thumb
# und Vollbild gleichermassen. Abgedeckt wird deckend mit der Papierfarbe aus der
# unmittelbaren Umgebung -- nicht weichgezeichnet: Blur laesst Konturen stehen
# und ist bei Schrift teilweise rekonstruierbar.
#
# Namen, Funktionen, Siegel, Aussteller, Datum und Noten bleiben unberuehrt.
REDAKTIONEN: dict[str, list[tuple[float, float, float, float]]] = {
    "02-msc-bescheid": [
        (0.19, 0.391, 0.44, 0.416), (0.575, 0.391, 0.88, 0.416),   # Geburtsdatum de/en
        (0.21, 0.410, 0.40, 0.435), (0.665, 0.410, 0.92, 0.435),   # Matrikelnummer de/en
        (0.44, 0.878, 0.74, 0.932),                               # Unterschrift Studienpraeses
    ],
    "03-msc-abschluss": [
        (0.03, 0.028, 0.32, 0.064),                               # Matrikelnummer (Kaestchen)
        (0.735, 0.206, 0.97, 0.242),                              # Geburtsdatum
    ],
    "04-msc-masterarbeit": [
        (0.03, 0.028, 0.32, 0.064),                               # Matrikelnummer
        (0.66, 0.285, 0.92, 0.327),                               # Unterschrift Studienpraeses
    ],
    "06-lehrbrief-oberflaechentechniker": [
        (0.36, 0.483, 0.72, 0.507),                               # Geburtsdatum und -ort
        (0.36, 0.865, 0.64, 0.928),                               # Unterschrift Lehrlingsstelle
    ],
    "07-meisterpruefung": [
        (0.36, 0.350, 0.65, 0.374),                               # Geburtsdatum
        (0.66, 0.850, 0.93, 0.920),                               # Unterschrift
    ],
    "08-senior-process-manager": [
        (0.33, 0.286, 0.72, 0.308),                               # Geburtsdatum und -ort
        (0.06, 0.770, 0.33, 0.833), (0.76, 0.770, 0.98, 0.833),   # zwei Unterschriften
    ],
    "09-itil-foundation": [
        (0.70, 0.626, 0.95, 0.650),                               # Candidate number
        (0.19, 0.695, 0.47, 0.757), (0.58, 0.695, 0.90, 0.757),   # zwei Unterschriften
    ],
    "10-projektmanagement-pmi": [
        (0.13, 0.730, 0.40, 0.793), (0.58, 0.730, 0.84, 0.793),
    ],
    "11-scrum": [
        (0.13, 0.790, 0.40, 0.848), (0.56, 0.790, 0.82, 0.848),
    ],
    "12-wertstrom-workshop": [
        (0.24, 0.790, 0.47, 0.858), (0.66, 0.790, 0.88, 0.858),
    ],
    "13-lehrbrief-industriekaufmann": [
        (0.36, 0.483, 0.72, 0.507),                               # Geburtsdatum und -ort
        (0.36, 0.865, 0.64, 0.928),                               # Unterschrift
    ],
    "14-ausbildertraining": [
        (0.30, 0.338, 0.72, 0.362),                               # Geburtsdatum
        (0.06, 0.775, 0.25, 0.838), (0.28, 0.775, 0.52, 0.838),
        (0.55, 0.775, 0.80, 0.838), (0.28, 0.845, 0.45, 0.898),   # vier Unterschriften
    ],
    "15-sicherheitsvertrauensperson": [
        (0.25, 0.395, 0.48, 0.420),                               # Geburtsdatum
        (0.16, 0.800, 0.49, 0.888), (0.59, 0.800, 0.95, 0.888),
    ],
    "16-psychologischer-berater": [
        (0.32, 0.276, 0.58, 0.298),                               # Geburtsdatum
        (0.13, 0.868, 0.36, 0.928), (0.55, 0.863, 0.80, 0.928),
    ],
    "17-channel-ausbildung": [
        (0.48, 0.788, 0.94, 0.852),                               # Unterschrift Ausstellerin
    ],
    "18-nisg-2026-wko": [
        (0.02, 0.878, 0.24, 0.942), (0.32, 0.878, 0.55, 0.942),
        (0.63, 0.878, 0.85, 0.942),                               # drei Unterschriften
    ],
    # 19-tuev-inspektionsbericht: reine Textseite, nichts zu schwaerzen.
}

# **18 und 19 stammen NICHT aus dem Lebenslauf-PDF** und werden von diesem Skript
# nicht erzeugt -- sie wurden spaeter von Hand in die Galerie gelegt. Ihre
# Schwaerzung steckt deshalb bereits in den JPGs. Kommt eine neue Quelle dazu,
# gehoert sie oben in CERTIFICATES und hier in REDAKTIONEN, sonst faellt die
# Schwaerzung beim naechsten Lauf lautlos weg. Fuer den Einzelfall:
#
#     py - <<'EOF'
#     from PIL import Image
#     import sys; sys.path.insert(0, "homepage/credentials")
#     import importlib; g = importlib.import_module("_generate_credentials")
#     for d in ("thumbs", "full"):
#         p = f"homepage/credentials/{d}/18-nisg-2026-wko.jpg"
#         g.redigieren(Image.open(p), "18-nisg-2026-wko").save(p, quality=90)
#     EOF


def _umgebungsfarbe(img: Image.Image, box: tuple[int, int, int, int]) -> tuple[int, int, int]:
    """Mittlere Farbe der Streifen ueber und unter dem Bereich.

    Ein Streifen allein reicht nicht: Bei farbigen Urkunden (Verlauf, Rahmen)
    trifft er sonst die Farbe der falschen Haelfte, und die Abdeckung setzt sich
    als heller Kasten ab.
    """
    x0, y0, x1, y1 = box
    hoehe = img.size[1]
    oben = img.crop((x0, max(0, y0 - 16), x1, max(1, y0 - 4)))
    unten = img.crop((x0, min(hoehe - 2, y1 + 4), x1, min(hoehe - 1, y1 + 16)))
    m1 = ImageStat.Stat(oben).mean[:3]
    m2 = ImageStat.Stat(unten).mean[:3]
    return tuple(int((a + b) / 2) for a, b in zip(m1, m2))


def redigieren(img: Image.Image, slug: str) -> Image.Image:
    """Deckt die in REDAKTIONEN hinterlegten Bereiche deckend ab."""
    breite, hoehe = img.size
    for x0, y0, x1, y1 in REDAKTIONEN.get(slug, []):
        box = (int(x0 * breite), int(y0 * hoehe), int(x1 * breite), int(y1 * hoehe))
        farbe = _umgebungsfarbe(img, box)
        img.paste(Image.new("RGB", (box[2] - box[0], box[3] - box[1]), farbe), box)
    return img


def render_page(page: fitz.Page, target_width: int) -> Image.Image:
    """Render a PDF page to a PIL Image at the given target width in pixels."""
    page_width_pt = page.rect.width
    scale = target_width / page_width_pt
    matrix = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=matrix, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    return img


def main() -> None:
    THUMB_DIR.mkdir(parents=True, exist_ok=True)
    FULL_DIR.mkdir(parents=True, exist_ok=True)

    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    doc = fitz.open(str(PDF_PATH))
    print(f"Source PDF: {PDF_PATH.name} ({len(doc)} pages)")

    for page_num, slug, title, _subtitle, _year, category in CERTIFICATES:
        page = doc[page_num - 1]

        thumb = redigieren(render_page(page, THUMB_WIDTH), slug)
        thumb_path = THUMB_DIR / f"{slug}.jpg"
        thumb.save(thumb_path, "JPEG", quality=THUMB_QUALITY, optimize=True)

        full = redigieren(render_page(page, FULL_WIDTH), slug)
        full_path = FULL_DIR / f"{slug}.jpg"
        full.save(full_path, "JPEG", quality=FULL_QUALITY, optimize=True)

        thumb_kb = thumb_path.stat().st_size // 1024
        full_kb = full_path.stat().st_size // 1024
        print(f"  [{category:14s}] {slug}: thumb {thumb_kb}kb / full {full_kb}kb — {title}")

    doc.close()
    print(f"\nGenerated {len(CERTIFICATES)} certificates -> {THUMB_DIR.parent}")


if __name__ == "__main__":
    main()
