"""Render certificate pages from CV PDF into thumbnails + full-size JPGs.

Source: TrustedAIZertifizierung/kompetenznachweise/20251030_Lebenslauf & Nachweise_Stefan Maier.pdf
Output: homepage/credentials/thumbs/<slug>.jpg (~600w) + homepage/credentials/full/<slug>.jpg (~1800w)

Run: py homepage/credentials/_generate_credentials.py
"""
from __future__ import annotations

from pathlib import Path

import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
PDF_PATH = ROOT / "TrustedAIZertifizierung" / "kompetenznachweise" / "20251030_Lebenslauf & Nachweise_Stefan Maier.pdf"
OUT_DIR = Path(__file__).resolve().parent
THUMB_DIR = OUT_DIR / "thumbs"
FULL_DIR = OUT_DIR / "full"

THUMB_WIDTH = 600
FULL_WIDTH = 1800
THUMB_QUALITY = 85
FULL_QUALITY = 90

# (page_num, slug, title, subtitle, year, category)
# page_num is 1-indexed, matching the PDF
CERTIFICATES = [
    (10, "02-msc-bescheid", "Master of Science — Verleihungsurkunde", "Universität Wien", "2016", "akademisch"),
    (12, "03-msc-abschluss", "Master Abschlusszeugnis", "Universität Wien — Notenschnitt 1,1, mit Auszeichnung bestanden", "2016", "akademisch"),
    (13, "04-msc-masterarbeit", "Beurteilung Masterarbeit", "High Pressure Torsion auf CoCrFeMnNi High-Entropy-Alloy", "2016", "akademisch"),

    (26, "06-lehrbrief-oberflaechentechniker", "Lehrbrief Oberflächentechniker", "WKO Vorarlberg", "2006", "galvanik"),
    (15, "07-meisterpruefung", "Meisterprüfung Oberflächentechnik", "WKO Kärnten", "2009", "galvanik"),

    (18, "08-senior-process-manager", "Senior Process Manager (SPüK)", "Zertifizierungsstelle WIFI / Quality Austria", "2017", "management"),
    (16, "09-itil-foundation", "ITIL Foundation in IT Service Management", "APMG International / AXELOS", "2017", "management"),
    (20, "10-projektmanagement-pmi", "Projektmanagement Grundlagen nach PMI®", "EFS Unternehmensberatung", "2016", "management"),
    (21, "11-scrum", "SCRUM Schulung", "EFS Unternehmensberatung", "2017", "management"),
    (17, "12-wertstrom-workshop", "Wertstrom-Expertenworkshop", "IPAL — Wolfgang Gall, Friedrich Dürst", "2023", "management"),
    (27, "13-lehrbrief-industriekaufmann", "Lehrbrief Industriekaufmann (mit Auszeichnung)", "WKO Vorarlberg", "2006", "management"),
    (24, "14-ausbildertraining", "Zeugnis Ausbildertraining", "Lernlabor — Bruno Bereuter, Franz Längle", "2008", "management"),
    (25, "15-sicherheitsvertrauensperson", "Sicherheitstechnisches Seminar (SVP)", "AUVA Landesstelle Salzburg", "2007", "management"),

    (23, "16-psychologischer-berater", "Psychologischer Berater / Personal Coach", "Hamburger Akademie für Fernstudien (Note 1,7)", "2018", "weiterbildung"),
    (22, "17-channel-ausbildung", "Channel-Ausbildung", "Rhiannon Augenthaler", "2024", "weiterbildung"),
]


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

        thumb = render_page(page, THUMB_WIDTH)
        thumb_path = THUMB_DIR / f"{slug}.jpg"
        thumb.save(thumb_path, "JPEG", quality=THUMB_QUALITY, optimize=True)

        full = render_page(page, FULL_WIDTH)
        full_path = FULL_DIR / f"{slug}.jpg"
        full.save(full_path, "JPEG", quality=FULL_QUALITY, optimize=True)

        thumb_kb = thumb_path.stat().st_size // 1024
        full_kb = full_path.stat().st_size // 1024
        print(f"  [{category:14s}] {slug}: thumb {thumb_kb}kb / full {full_kb}kb — {title}")

    doc.close()
    print(f"\nGenerated {len(CERTIFICATES)} certificates -> {THUMB_DIR.parent}")


if __name__ == "__main__":
    main()
