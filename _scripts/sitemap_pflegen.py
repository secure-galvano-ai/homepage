"""sitemap_pflegen.py — zieht jedes <lastmod> in sitemap.xml auf das echte Aenderungsdatum.

Das Datum kommt aus dem letzten Commit der dahinterliegenden Datei
(`git log -1 --format=%ad --date=short -- <datei>`), nicht aus der Dateizeit: die
Dateizeit springt bei jedem Checkout, das Commit-Datum beschreibt den Stand, der
auch wirklich ausgeliefert wurde. Ein veraltetes `lastmod` kostet Crawl-Prioritaet,
ein zu neues verbrennt sie — deshalb kein pauschales "heute".

Nur die `<lastmod>`-Zeilen werden angefasst. URLs kommen NICHT von hier: welche
Seite in die Sitemap gehoert, ist eine inhaltliche Entscheidung. Dass die Liste zu
den Seiten passt (Datei existiert, kein `noindex`, kein Weiterleitungs-Stub),
prueft `check_site.py` Check 8.

Aufruf:
    py _scripts/sitemap_pflegen.py            # schreibt
    py _scripts/sitemap_pflegen.py --pruefen   # meldet nur, Exit 1 bei Abweichung
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
SITE = "https://secure-galvano-ai.com"
SITEMAP = WURZEL / "sitemap.xml"


def datei_zu_url(url: str) -> Path:
    """Pfad der Datei, die GitHub Pages unter dieser URL ausliefert."""
    pfad = url.removeprefix(SITE).lstrip("/")
    if not pfad or pfad.endswith("/"):
        pfad += "index.html"
    return WURZEL / pfad


def commit_datum(datei: Path) -> str | None:
    if not datei.exists():
        return None
    try:
        ausgabe = subprocess.run(
            ["git", "-C", str(WURZEL), "log", "-1", "--format=%ad", "--date=short",
             "--", str(datei.relative_to(WURZEL).as_posix())],
            capture_output=True, text=True, encoding="utf-8", timeout=30, check=True,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None
    return ausgabe or None


def main() -> int:
    nur_pruefen = "--pruefen" in sys.argv[1:]
    text = SITEMAP.read_text(encoding="utf-8")

    # <url>-Bloecke einzeln, damit <loc> und <lastmod> zusammengehoeren
    abweichungen: list[str] = []

    def ersetze(treffer: re.Match[str]) -> str:
        block = treffer.group(0)
        loc = re.search(r"<loc>\s*([^<\s]+)\s*</loc>", block)
        alt = re.search(r"<lastmod>\s*([^<\s]+)\s*</lastmod>", block)
        if not loc or not alt:
            return block
        neu = commit_datum(datei_zu_url(loc.group(1)))
        if neu is None or neu == alt.group(1):
            return block
        abweichungen.append(f"  {loc.group(1)}: {alt.group(1)} -> {neu}")
        return block.replace(f"<lastmod>{alt.group(1)}</lastmod>", f"<lastmod>{neu}</lastmod>")

    neuer_text = re.sub(r"<url>.*?</url>", ersetze, text, flags=re.DOTALL)

    if not abweichungen:
        print("sitemap_pflegen: alle lastmod-Daten stimmen.")
        return 0

    print(f"sitemap_pflegen: {len(abweichungen)} veraltete lastmod-Angabe(n):")
    for zeile in abweichungen:
        print(zeile)
    if nur_pruefen:
        print("\n--pruefen: nichts geschrieben. Ohne den Schalter nachziehen.")
        return 1
    SITEMAP.write_text(neuer_text, encoding="utf-8")
    print("\nsitemap.xml nachgezogen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
