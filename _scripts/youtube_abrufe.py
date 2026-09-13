"""Zaehlerstand der Video-Abrufe festhalten -- die Zahl, die sonst niemand notiert.

Anlass (10.09.2026): Ein frueher in YouTube Studio abgelesener Wert ("rund 17 Minuten
Wiedergabezeit") stand nirgends. Damit war die einzige Frage, die zaehlt -- ist seither
etwas dazugekommen -- nicht beantwortbar. Ein Zaehlerstand ohne Datum ist kein Befund.

Warum das ohne Anmeldung geht: Die Aufrufzahl steht bei **nicht gelisteten** Videos
genauso in der oeffentlichen Watch-Seite wie bei oeffentlichen. Was dort **nicht** steht
und weiterhin nur YouTube Studio kennt: mittlere Wiedergabedauer, Traffic-Quellen und
Geo-Aufschluesselung.

Anders als bei Clarity geht hier nichts verloren, wenn ein Lauf ausfaellt: Aufrufe sind
ein kumulativer Zaehler, kein Tagesfenster. Das Skript darf deshalb monatlich laufen --
es haengt im Optimierungslauf (`.claude/skills/optimierung/`), nicht im Task Scheduler.

Aufruf:
    py _scripts/youtube_abrufe.py

Ablage der Historie: _analytics/youtube_history.jsonl (gitignored).
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "_analytics" / "youtube_history.jsonl"

# Titel dienen nur der Lesbarkeit der Historie -- massgeblich ist die ID.
# Wird ein Video getauscht, kommt die neue ID dazu; die alte Zeile bleibt stehen,
# sonst bricht die Zeitreihe an der Stelle, an der sie am interessantesten ist.
VIDEOS = [
    ("RStpqzz3r5g", "Anwendung im Ueberblick (demo.html)"),
    ("lLgcKqhHOrU", "Predictive Quality (Startseite)"),
    ("ANMXEK3wz9A", "Prozessdatenauswertung und Predictive Analytics"),
]

KOPF = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
# Beide Schreibweisen kommen in der Seite vor; die reine Zahl ist die verlaesslichere.
MUSTER_AUFRUFE = re.compile(r'"viewCount"\s*:\s*"(\d+)"')
MUSTER_LAENGE = re.compile(r'"lengthSeconds"\s*:\s*"(\d+)"')


def seite_holen(video_id: str) -> str:
    req = urllib.request.Request(
        f"https://www.youtube.com/watch?v={video_id}", headers=KOPF
    )
    with urllib.request.urlopen(req, timeout=30) as antwort:
        return antwort.read().decode("utf-8", errors="replace")


def stand_lesen(video_id: str) -> dict:
    """Zaehlerstand eines Videos. Wirft, wenn das Muster fehlt -- nie stillschweigend 0.

    Ein leeres Ergebnis waere hier kein Befund, sondern ein Messfehler: YouTube haette
    das Seitenformat geaendert, und eine 0 in der Historie sae he aus wie ein Einbruch.
    """
    html = seite_holen(video_id)
    aufrufe = MUSTER_AUFRUFE.search(html)
    if not aufrufe:
        raise RuntimeError(
            f"Aufrufzahl fuer {video_id} nicht gefunden. Wahrscheinlich hat YouTube das "
            "Seitenformat geaendert -- Muster in MUSTER_AUFRUFE pruefen. Es wird bewusst "
            "kein Ersatzwert geschrieben."
        )
    laenge = MUSTER_LAENGE.search(html)
    return {
        "aufrufe": int(aufrufe.group(1)),
        "laenge_s": int(laenge.group(1)) if laenge else None,
        "nicht_gelistet": '"isUnlisted":true' in html,
    }


def bereits_vorhanden() -> set[str]:
    if not HISTORY.exists():
        return set()
    schluessel = set()
    for zeile in HISTORY.read_text(encoding="utf-8").splitlines():
        if not zeile.strip():
            continue
        try:
            schluessel.add(json.loads(zeile)["schluessel"])
        except (json.JSONDecodeError, KeyError):
            continue
    return schluessel


def main() -> None:
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    bekannt = bereits_vorhanden()
    heute = date.today().isoformat()
    neu = 0

    with HISTORY.open("a", encoding="utf-8") as datei:
        for video_id, titel in VIDEOS:
            schluessel = f"{heute}|{video_id}"
            if schluessel in bekannt:
                print(f"{titel}: heute bereits erfasst")
                continue
            try:
                stand = stand_lesen(video_id)
            except (urllib.error.URLError, RuntimeError) as fehler:
                # Ein Video darf den Lauf nicht kippen -- die anderen sind trotzdem wertvoll.
                print(f"FEHLER bei {video_id} ({titel}): {fehler}", file=sys.stderr)
                continue
            zeile = {
                "abgerufen_am": heute,
                "video_id": video_id,
                "titel": titel,
                "schluessel": schluessel,
                **stand,
            }
            datei.write(json.dumps(zeile, ensure_ascii=False) + "\n")
            neu += 1
            print(f"{titel}: {stand['aufrufe']} Aufrufe")

    print(f"\n{neu} Zeile(n) ergaenzt -> {HISTORY}")
    if neu:
        print("Mittlere Wiedergabedauer bleibt manuell: YouTube Studio, nur mit Anmeldung.")


if __name__ == "__main__":
    main()
