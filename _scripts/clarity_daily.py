"""Taeglicher Clarity-Sammler -- baut die Historie auf, die die API nicht hergibt.

Die Clarity Data Export API liefert ausschliesslich die letzten 1-3 Tage und erlaubt
10 Abfragen pro Projekt und Tag. Ein Monatsrueckblick ist darueber nicht abrufbar:
was aelter als drei Tage ist, ist ueber die API endgueltig verloren. Deshalb laeuft
dieses Skript taeglich und haengt den Tagesstand an eine lokale Historie an.

Das 3-Tage-Fenster wird bewusst voll ausgenutzt (numOfDays=3), damit ein bis zwei
ausgefallene Laeufe nachtraeglich aufgeholt werden -- die Dublettenpruefung
verwirft die Ueberschneidung.

Aufruf:
    py _scripts/clarity_daily.py

Token: CLARITY_API_TOKEN aus der Umgebung oder aus .env im Repo-Wurzelverzeichnis.
Erzeugen unter Clarity -> Einstellungen -> Datenexport (nur Projektadmin).
Ablage der Historie: _analytics/clarity_history.jsonl (gitignored).
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "_analytics" / "clarity_history.jsonl"
ENV_FILE = ROOT / ".env"
API_URL = "https://www.clarity.ms/export-data/api/v1/project-live-insights"

# Drei Dimensionen sind das Maximum pro Anfrage. Jede Zeile hier kostet einen der
# zehn Tagesaufrufe -- mehr als drei Abfragen einzutragen ist bei Ausfaellen riskant,
# weil dann kein Kontingent fuer einen Nachholversuch bleibt.
ABFRAGEN = [
    {"label": "gesamt", "dimensions": []},
    {"label": "nach_seite", "dimensions": ["URL"]},
    {"label": "nach_geraet", "dimensions": ["Device"]},
]


def token_lesen() -> str:
    """Token aus der Umgebung, ersatzweise aus .env. Niemals aus einer Git-Datei."""
    tok = os.environ.get("CLARITY_API_TOKEN", "").strip()
    if tok:
        return tok
    if ENV_FILE.exists():
        for zeile in ENV_FILE.read_text(encoding="utf-8").splitlines():
            zeile = zeile.strip()
            if zeile.startswith("CLARITY_API_TOKEN="):
                return zeile.split("=", 1)[1].strip().strip("\"'")
    sys.exit(
        "CLARITY_API_TOKEN fehlt. Token unter Clarity -> Einstellungen -> Datenexport\n"
        f"erzeugen und in {ENV_FILE} ablegen: CLARITY_API_TOKEN=<token>"
    )


def abrufen(token: str, dimensions: list[str]) -> list[dict]:
    """Eine Abfrage gegen die Export-API. Gibt bei aufgebrauchtem Kontingent None zurueck."""
    params = ["numOfDays=3"]
    for i, dim in enumerate(dimensions, start=1):
        params.append(f"dimension{i}={dim}")
    req = urllib.request.Request(
        f"{API_URL}?{'&'.join(params)}",
        headers={"Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as antwort:
            return json.loads(antwort.read().decode("utf-8"))
    except urllib.error.HTTPError as fehler:
        if fehler.code == 429:
            # Tageskontingent erschoepft. Kein Retry -- ein Wiederholungsversuch
            # verbraucht nur den naechsten Aufruf und scheitert genauso.
            print("Kontingent fuer heute aufgebraucht (HTTP 429) -- Abbruch ohne Fehler.")
            return []
        if fehler.code == 401:
            sys.exit("Token abgelehnt (HTTP 401). Neues Token in Clarity erzeugen.")
        raise


def bereits_vorhanden() -> set[str]:
    """Schluessel der schon gespeicherten Zeilen -- das 3-Tage-Fenster ueberlappt."""
    if not HISTORY.exists():
        return set()
    schluessel = set()
    for zeile in HISTORY.read_text(encoding="utf-8").splitlines():
        if not zeile.strip():
            continue
        try:
            schluessel.add(json.loads(zeile)["schluessel"])
        except (json.JSONDecodeError, KeyError):
            continue  # beschaedigte Zeile ueberspringen, nicht den Lauf abbrechen
    return schluessel


def main() -> None:
    token = token_lesen()
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    bekannt = bereits_vorhanden()
    neu = 0

    with HISTORY.open("a", encoding="utf-8") as datei:
        for abfrage in ABFRAGEN:
            for eintrag in abrufen(token, abfrage["dimensions"]):
                schluessel = "|".join([
                    abfrage["label"],
                    str(eintrag.get("metricName", "")),
                    json.dumps(eintrag.get("information", []), sort_keys=True),
                ])
                if schluessel in bekannt:
                    continue
                bekannt.add(schluessel)
                datei.write(json.dumps({
                    "abgerufen_am": date.today().isoformat(),
                    "abfrage": abfrage["label"],
                    "schluessel": schluessel,
                    "daten": eintrag,
                }, ensure_ascii=False) + "\n")
                neu += 1

    print(f"{neu} neue Zeilen -> {HISTORY.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
