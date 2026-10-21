"""Prueft, ob die englischen Seiten noch zur deutschen Fassung passen.

Warum es die Datei gibt: Seit 12.10.2026 hat die Website eine englische Fassung
(Stefan: internationaler Auftritt, US-Markt). Eine Uebersetzung veraltet lautlos --
die deutsche Seite bekommt einen neuen Preis, einen neuen Abschnitt, und die englische
verspricht weiter das Alte. Nav, Fuss, Sprachverweise und CSS zieht
`_generate_layout.py` ohnehin nach; was kein Generator kann, ist der TEXT. Den
bewacht diese Pruefung.

Wie: Beim Uebersetzen wird der deutsche Inhalt (Metadaten im Kopf + Seiteninhalt ohne
die generierten Bloecke) als Schnappschuss unter `en/_quelle/<seite>.txt` abgelegt.
Weicht die deutsche Seite davon ab, ist die englische veraltet: Exit 1, und der
Unterschied steht als Diff da -- genau die Zeilen, die nachzuziehen sind. Jekyll
liefert `en/_quelle/` wegen des Unterstrichs nicht aus.

Zusaetzlich ein Strukturvergleich, der unabhaengig vom Schnappschuss greift: gleich
viele Abschnitte, Ueberschriften und Funnel-Marker auf beiden Seiten. Er faengt eine
englische Seite, die beim Nachziehen einen Abschnitt verloren hat.

    py _scripts/check_englisch.py                        # pruefen, Exit 1 bei Abweichung
    py _scripts/check_englisch.py --bestaetigen leistungen.html   # nach dem Nachziehen
    py _scripts/check_englisch.py --bestaetigen alle
    py _scripts/check_englisch.py --hook-installieren    # pre-commit im homepage-Repo

Laeuft an drei Stellen: in `check_site.py` (Gate 1 vor jedem Deploy), im pre-commit
des Repos und taeglich im Code-Waechter. Grenze: Die Pruefung sieht, DASS sich das
Deutsche geaendert hat, nicht, ob die englische Nachuebersetzung gut ist.
"""

from __future__ import annotations

import collections
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUELLE = ROOT / "en" / "_quelle"
GENERIERT = ("nav", "footer", "wa-fab", "sticky-cta", "hreflang", "styles")
KOPF_MUSTER = (
    r"<title>.*?</title>",
    r'<meta name="(?:description|keywords)"[^>]*>',
    r'<meta property="og:(?:title|description)"[^>]*>',
    r'<script type="application/ld\+json">.*?</script>',
)
# Woerter, die auf keiner oeffentlichen Seite stehen duerfen (README § Datenwerkstatt-Seite).
GESPERRT = re.compile(r"Regelkarte|control chart", re.I)


def _paare() -> dict[str, str]:
    sys.path.insert(0, str(ROOT))
    import _generate_layout as gen
    return gen.PAIRS


def _ohne_generiertes(text: str) -> str:
    for m in GENERIERT:
        text = re.sub(rf"<!-- BEGIN {m} -->.*?<!-- END {m} -->", "", text, flags=re.S)
    return text


def quelltext(de_html: str) -> str:
    """Der Teil der deutschen Seite, den eine Uebersetzung abbilden muss -- zeilenweise,
    damit der Diff lesbar bleibt."""
    kopf = de_html[: de_html.index("</head>")]
    teile = [m.group(0) for muster in KOPF_MUSTER for m in re.finditer(muster, kopf, re.S)]
    rumpf = _ohne_generiertes(de_html[de_html.index("<body"):])
    zeilen = [z.strip() for z in "\n".join(teile + [rumpf]).splitlines()]
    return "\n".join(z for z in zeilen if z) + "\n"


# Links auf rein deutschsprachiges Material zaehlen nicht mit: Die englische Fassung laesst
# Produktblaetter, Beispiel-Befunde, Musterangebote, Demo und Datenwerkstatt bewusst weg
# (Stefan, 21.10.2026: deutsche Unterlagen auf der englischen Seite wirken unprofessionell).
NUR_DEUTSCH = re.compile(r'href="[^"]*(?:\.pdf|demo\.html|ausbildung\.html)(?:#[^"]*)?"')


def _funnel_marker(rumpf: str) -> int:
    """Zaehlt data-funnel-Marker ohne die auf rein deutschsprachiges Material."""
    gesamt = len(re.findall(r"data-funnel=", rumpf))
    deutsch = sum(1 for tag in re.findall(r"<a\b[^>]*data-funnel=[^>]*>", rumpf)
                  if NUR_DEUTSCH.search(tag))
    return gesamt - deutsch


def struktur(html: str) -> dict[str, int]:
    rumpf = _ohne_generiertes(html[html.index("<body"):])
    zaehler = collections.Counter()
    for name, muster in (("Abschnitte", r"<section\b"), ("h1", r"<h1\b"), ("h2", r"<h2\b"),
                         ("h3", r"<h3\b")):
        zaehler[name] = len(re.findall(muster, rumpf))
    zaehler["Funnel-Marker"] = _funnel_marker(rumpf)
    return dict(zaehler)


def pruefe() -> list[str]:
    """Liefert die Befunde als Zeilen; leer = alles passt."""
    befunde: list[str] = []
    for de, en in _paare().items():
        de_pfad, en_pfad = ROOT / de, ROOT / en
        if not en_pfad.exists():
            befunde.append(f"{en}: fehlt (Gegenstueck zu {de})")
            continue
        de_html = de_pfad.read_text(encoding="utf-8")
        en_html = en_pfad.read_text(encoding="utf-8")
        if '<html lang="en">' not in en_html:
            befunde.append(f'{en}: <html lang="en"> fehlt')
        for treffer in sorted(set(GESPERRT.findall(en_html))):
            befunde.append(f"{en}: gesperrter Begriff '{treffer}'")

        s_de, s_en = struktur(de_html), struktur(en_html)
        for k in s_de:
            if s_de[k] != s_en[k]:
                befunde.append(f"{en}: {k} {s_en[k]} statt {s_de[k]} wie in {de}")

        schnapp = QUELLE / f"{de}.txt"
        jetzt = quelltext(de_html)
        if not schnapp.exists():
            befunde.append(f"{en}: kein Schnappschuss -> nach dem Uebersetzen "
                           f"py _scripts/check_englisch.py --bestaetigen {de}")
            continue
        alt = schnapp.read_text(encoding="utf-8")
        if alt != jetzt:
            diff = list(difflib.unified_diff(alt.splitlines(), jetzt.splitlines(),
                                             f"{de} (Stand der Uebersetzung)", f"{de} (jetzt)",
                                             n=0, lineterm=""))
            kurz = "\n".join("      " + z[:160] for z in diff[:60])
            mehr = f"\n      ... {len(diff) - 60} Zeilen mehr" if len(diff) > 60 else ""
            befunde.append(f"{en}: {de} wurde seit der Uebersetzung geaendert -> {en} "
                           f"nachziehen, dann --bestaetigen {de}\n{kurz}{mehr}")
    return befunde


def bestaetige(was: str) -> None:
    paare = _paare()
    ziele = list(paare) if was == "alle" else [was]
    QUELLE.mkdir(parents=True, exist_ok=True)
    for de in ziele:
        if de not in paare:
            raise SystemExit(f"{de} hat kein englisches Gegenstueck (PAIRS in _generate_layout.py)")
        ziel = QUELLE / f"{de}.txt"
        tmp = ziel.with_suffix(".tmp")
        tmp.write_text(quelltext((ROOT / de).read_text(encoding="utf-8")), encoding="utf-8")
        tmp.replace(ziel)
        print(f"Stand festgeschrieben: {de} -> {paare[de]}")


HOOK = """#!/bin/sh
# Installiert von _scripts/check_englisch.py --hook-installieren (siehe README § Englische Fassung).
# Blockt einen Commit, solange eine englische Seite hinter ihrer deutschen zurueckliegt.
py _scripts/check_englisch.py || {
  echo "Englische Fassung nachziehen (oder bewusst: git commit --no-verify)."
  exit 1
}
"""


def installiere_hook() -> None:
    ziel = ROOT / ".git" / "hooks" / "pre-commit"
    if ziel.exists() and "check_englisch" not in ziel.read_text(encoding="utf-8", errors="replace"):
        raise SystemExit(f"{ziel} existiert schon mit fremdem Inhalt -- nicht ueberschrieben")
    ziel.write_text(HOOK, encoding="utf-8", newline="\n")
    print(f"pre-commit installiert: {ziel}")


def main() -> int:
    if "--hook-installieren" in sys.argv:
        installiere_hook()
        return 0
    if "--bestaetigen" in sys.argv:
        i = sys.argv.index("--bestaetigen")
        if i + 1 >= len(sys.argv):
            raise SystemExit("--bestaetigen <seite.html|alle>")
        bestaetige(sys.argv[i + 1])
        return 0
    befunde = pruefe()
    if befunde:
        print(f"check_englisch: {len(befunde)} Befunde")
        for b in befunde:
            print(f"  - {b}")
        return 1
    print(f"check_englisch: {len(_paare())} Seitenpaare passen zusammen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
