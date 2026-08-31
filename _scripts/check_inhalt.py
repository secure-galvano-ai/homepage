"""Inhalts-, SEO- und Redundanzpruefung ueber alle echten Seiten.

Ergaenzt `check_site.py` (das prueft Dateien, Links und Assets) um die Ebene darueber:
Metadaten, Ueberschriften-Hierarchie, Funnel-Marker, Textdubletten zwischen Seiten und
die Abdeckung der Sitemap.

Warum automatisch: Am 31.08.2026 sind bei einem groesseren Umbau vier Fehler entstanden,
die alle mechanisch auffindbar waren -- eine 278 Zeichen lange Description, zwei
Ueberschriften-Spruenge, wortgleiche Absaetze auf zwei Seiten und eine Seite ohne den
neuen Navigationseintrag. Beim Durchlesen findet ein Mensch so etwas nicht zuverlaessig.

    py _scripts/check_inhalt.py            # Bericht, Exit 1 bei kritischen Befunden
    py _scripts/check_inhalt.py --nur-seo  # nur Metadaten und Ueberschriften

Kritisch (Exit 1): doppelte Titel/Descriptions, fehlendes canonical, mehr als eine H1,
doppelte Funnel-Marker, CTA ohne Marker, tote Anker, Seiten ausserhalb der Sitemap.
Hinweis (Exit 0): Laengen ausserhalb der Zielbereiche, Ueberschriften-Spruenge,
Textdubletten -- die brauchen ein menschliches Urteil.
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TITEL_MIN, TITEL_MAX = 30, 65
DESC_MIN, DESC_MAX = 110, 165
DUBLETTE_AB = 60          # ab wie vielen Zeichen ein Satz als Dublette zaehlt
CTA_MUSTER = re.compile(r"outlook\.office\.com/book|^mailto:|wa\.me/")
# Impressum und Datenschutz muessen eine Kontaktadresse fuehren -- Rechtspflicht,
# kein Conversion-Element, deshalb ohne Funnel-Marker.
OHNE_MARKERPFLICHT = {"impressum.html", "datenschutz.html", "404.html"}
# Bausteine, die _generate_layout.py auf jede Seite schreibt. Sie gehoeren nicht in
# den Textvergleich, sonst meldet die Dublettenpruefung jede Seite gegen jede.
GENERIERTE_BAUSTEINE = ("nav", "footer", "wa-fab", "sticky-cta")


def seiten() -> tuple[dict[str, str], list[str]]:
    """Liefert {Dateiname: Inhalt} der echten Seiten und die Liste der Weiterleitungen."""
    echt: dict[str, str] = {}
    stubs: list[str] = []
    for p in sorted(ROOT.glob("*.html")):
        t = p.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in t:
            stubs.append(p.name)
        else:
            echt[p.name] = t
    return echt, stubs


def _kopf(t: str) -> str:
    return t[: t.index("</head>")] if "</head>" in t else t


def _rumpf(t: str) -> str:
    return t[t.index("<body"):] if "<body" in t else t


def _sichtbar(t: str) -> str:
    """Sichtbarer Fliesstext -- ohne generierte Bausteine, Kommentare, Skripte, Stile.

    Die Bausteine werden ueber ihre BEGIN/END-Marker entfernt, nicht ueber die Tags:
    das ist deterministisch und greift auch, wenn ein Baustein mehrfach vorkommt.
    """
    b = _rumpf(t)
    for marker in GENERIERTE_BAUSTEINE:
        b = re.sub(rf"<!-- BEGIN {marker} -->.*?<!-- END {marker} -->", " ", b, flags=re.S)
    b = re.sub(r"<nav\b.*?</nav>", " ", b, flags=re.S)
    b = re.sub(r"<footer\b.*?</footer>", " ", b, flags=re.S)
    b = re.sub(r"<!--.*?-->", " ", b, flags=re.S)
    b = re.sub(r"<script.*?</script>", " ", b, flags=re.S)
    b = re.sub(r"<style.*?</style>", " ", b, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", b))


def _eins(muster: str, text: str) -> str | None:
    m = re.search(muster, text, re.S | re.I)
    return m.group(1).strip() if m else None


def pruefe(nur_seo: bool = False) -> tuple[list[str], list[str]]:
    echt, _ = seiten()
    kritisch: list[str] = []
    hinweise: list[str] = []
    titel: dict[str, str] = {}
    descs: dict[str, str] = {}

    for name, inhalt in echt.items():
        kopf, rumpf = _kopf(inhalt), _rumpf(inhalt)
        ist_fehlerseite = name == "404.html"

        ti = _eins(r"<title>(.*?)</title>", kopf)
        de = _eins(r'<meta name="description" content="(.*?)">', kopf)
        ca = _eins(r'<link rel="canonical" href="(.*?)">', kopf)

        if ti:
            titel[name] = ti
            if not TITEL_MIN <= len(ti) <= TITEL_MAX:
                hinweise.append(f"{name}: Titel {len(ti)} Zeichen (Ziel {TITEL_MIN}-{TITEL_MAX})")
        else:
            kritisch.append(f"{name}: kein <title>")

        if de:
            descs[name] = de
            if not DESC_MIN <= len(de) <= DESC_MAX:
                hinweise.append(f"{name}: Description {len(de)} Zeichen (Ziel {DESC_MIN}-{DESC_MAX})")
        elif not ist_fehlerseite:
            kritisch.append(f"{name}: keine Description")

        # Eine Fehlerseite fuehrt bewusst weder canonical noch og:image.
        if not ca and not ist_fehlerseite:
            kritisch.append(f"{name}: kein canonical")

        hs = [(int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2)).strip())
              for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", rumpf, re.S)]
        h1 = [x for stufe, x in hs if stufe == 1]
        if len(h1) != 1:
            kritisch.append(f"{name}: {len(h1)} H1-Ueberschriften (genau eine erwartet)")
        letzte = 0
        for stufe, text in hs:
            if letzte and stufe > letzte + 1:
                hinweise.append(f'{name}: Ueberschrift springt h{letzte} -> h{stufe} bei "{text[:40]}"')
            letzte = stufe

        if nur_seo:
            continue

        marker = re.findall(r'data-funnel="([^"]*)"', rumpf)
        doppelt = [m for m, n in collections.Counter(marker).items() if n > 1]
        if doppelt:
            kritisch.append(f"{name}: Funnel-Marker doppelt vergeben: {doppelt}")

        if name not in OHNE_MARKERPFLICHT:
            for m in re.finditer(r"<a\b[^>]*>", rumpf):
                tag = m.group(0)
                href = _eins(r'href="([^"]*)"', tag) or ""
                if CTA_MUSTER.search(href) and "data-funnel=" not in tag:
                    kritisch.append(f"{name}: CTA ohne Funnel-Marker -> {href[:50]}")

        for anker in re.findall(r'href="#([^"]+)"', rumpf):
            if f'id="{anker}"' not in rumpf:
                kritisch.append(f"{name}: toter Anker #{anker}")

    for feld, bezeichnung in ((titel, "Titel"), (descs, "Description")):
        for wert, n in collections.Counter(feld.values()).items():
            if n > 1:
                wo = [s for s, v in feld.items() if v == wert]
                kritisch.append(f"{bezeichnung} doppelt auf {wo}: {wert[:50]}")

    if nur_seo:
        return kritisch, hinweise

    # Textdubletten zwischen Seiten -- Hinweis, nicht kritisch: eine wiederholte
    # Pressezeile oder ein bewusst gespiegelter Beleg ist zulaessig.
    gesehen: dict[str, list[str]] = collections.defaultdict(list)
    for name, inhalt in echt.items():
        for satz in re.split(r"(?<=[.!?])\s+", _sichtbar(inhalt)):
            satz = satz.strip()
            if len(satz) > DUBLETTE_AB:
                gesehen[satz[:70].lower()].append(name)
    for schluessel, wo in gesehen.items():
        eindeutig = sorted(set(wo))
        if len(eindeutig) > 1:
            hinweise.append(f"Textdublette auf {eindeutig}: {schluessel[:58]}...")

    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    in_sm = set(re.findall(r"<loc>https://secure-galvano-ai\.com/(.*?)</loc>", sm))
    for name in echt:
        if name == "404.html":
            continue
        if not (name in in_sm or (name == "index.html" and "" in in_sm)):
            kritisch.append(f"{name}: fehlt in der sitemap.xml")
    for u in in_sm:
        if u and u not in echt:
            kritisch.append(f"sitemap.xml verweist auf {u!r} - keine echte Seite")

    return kritisch, hinweise


def main() -> None:
    nur_seo = "--nur-seo" in sys.argv
    kritisch, hinweise = pruefe(nur_seo)
    echt, stubs = seiten()
    print(f"check_inhalt: {len(echt)} Seiten geprueft, {len(stubs)} Weiterleitungen uebersprungen")

    if hinweise:
        print("\n  HINWEISE (kein Abbruch):")
        for h in hinweise:
            print(f"    - {h}")
    if kritisch:
        print("\n  KRITISCH:")
        for k in kritisch:
            print(f"    - {k}")
        print(f"\n{len(kritisch)} kritische Befunde.")
        sys.exit(1)
    print("\nKeine kritischen Befunde.")


if __name__ == "__main__":
    main()
