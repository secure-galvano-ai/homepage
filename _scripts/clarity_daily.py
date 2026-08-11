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
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "_analytics" / "clarity_history.jsonl"
# Der Task laeuft fensterlos (pyw.exe) -- ohne Protokoll waere jeder Fehlschlag unsichtbar.
# Gleiche Konvention wie die uebrigen \SecureGalvano\-Tasks (vgl. _expiry-check.log).
PROTOKOLL = ROOT / "_analytics" / "_sammler.log"
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
        # utf-8-sig, nicht utf-8: Windows-PowerShell schreibt bei `Set-Content -Encoding utf8`
        # ein BOM an den Dateianfang. Ohne das -sig steht es im ersten Schluesselnamen und
        # der Vergleich unten schlaegt fehl -- mit der irrefuehrenden Meldung, das Token fehle.
        for zeile in ENV_FILE.read_text(encoding="utf-8-sig").splitlines():
            zeile = zeile.strip().lstrip("﻿")
            if zeile.startswith("CLARITY_API_TOKEN="):
                tok = zeile.split("=", 1)[1].strip().strip("\"'")
                # Clarity-Token sind lange Zeichenketten. Ein paar Zeichen bedeuten fast
                # immer, dass beim Einfuegen ins Terminal nichts angekommen ist -- das
                # aeussert sich sonst erst weit spaeter als HTTP 403.
                if len(tok) < 20:
                    sys.exit(
                        f"CLARITY_API_TOKEN in {ENV_FILE} ist nur {len(tok)} Zeichen lang "
                        "und damit unbrauchbar.\nBeim Einfuegen ins Terminal ist der Wert "
                        "verloren gegangen. Datei mit einem Editor oeffnen und die Zeile\n"
                        "  CLARITY_API_TOKEN=<vollstaendiges Token>\nvon Hand setzen."
                    )
                return tok
    sys.exit(
        "CLARITY_API_TOKEN fehlt. Token unter Clarity -> Einstellungen -> Datenexport\n"
        f"erzeugen und in {ENV_FILE} ablegen: CLARITY_API_TOKEN=<token>"
    )


def abrufen(token: str, dimensions: list[str], tage: int = 1) -> list[dict]:
    """Eine Abfrage gegen die Export-API. Gibt bei aufgebrauchtem Kontingent [] zurueck.

    ``tage`` ist die Fensterbreite. Standard ist 1: Die API liefert **Summenwerte ueber
    das angefragte Fenster**, keine Tagesaufschluesselung. Nur mit Tagesfenstern entstehen
    ueberschneidungsfreie Werte, die sich zu beliebigen Zeitraeumen aufaddieren lassen.
    Ein 3-Tage-Fenster ueberlappt taeglich und wuerde Sitzungen mehrfach zaehlen.
    """
    params = [f"numOfDays={tage}"]
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
    """Schluessel der schon gespeicherten Zeilen.

    Der Schluessel enthaelt bewusst **den abgedeckten Tag**, nicht die Messwerte. Wuerde
    er ueber die Werte gebildet, verschwaende ein Tag, an dem dieselben Zahlen anfallen
    wie am Vortag -- bei Metriken, die meistens 0 sind, waere das der Regelfall und die
    Zeitreihe haette systematisch Luecken.
    """
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
    heute = date.today()
    # numOfDays=1 liefert den zuletzt abgeschlossenen Tag. Wir schreiben ihn explizit
    # mit, damit spaetere Auswertungen nicht auf den Abrufzeitpunkt schliessen muessen.
    abgedeckt = (heute - timedelta(days=1)).isoformat()
    neu = uebersprungen = 0

    with HISTORY.open("a", encoding="utf-8") as datei:
        for abfrage in ABFRAGEN:
            for eintrag in abrufen(token, abfrage["dimensions"], tage=1):
                schluessel = "|".join([
                    abfrage["label"], abgedeckt, str(eintrag.get("metricName", "")),
                ])
                if schluessel in bekannt:
                    uebersprungen += 1
                    continue
                bekannt.add(schluessel)
                datei.write(json.dumps({
                    "abgerufen_am": heute.isoformat(),
                    "gilt_fuer": abgedeckt,
                    "fenster_tage": 1,
                    "abfrage": abfrage["label"],
                    "schluessel": schluessel,
                    "daten": eintrag,
                }, ensure_ascii=False) + "\n")
                neu += 1

        # Nachhol-Lauf: Fehlt der Vorvortag, war der Task aus (Urlaub, Rechner aus).
        # Die API gibt nur drei Tage zurueck -- mehr als zwei versaeumte Tage sind
        # endgueltig verloren. Das 3-Tage-Fenster wird getrennt und markiert abgelegt:
        # als Summenwert brauchbar, aber bewusst NICHT mit Tageswerten summierbar.
        vorvortag = (heute - timedelta(days=2)).isoformat()
        fehlt = not any(k.split("|")[1] == vorvortag for k in bekannt if "|" in k)
        if fehlt:
            print(f"Luecke erkannt: keine Daten fuer {vorvortag} -- hole 3-Tage-Fenster nach.")
            for abfrage in ABFRAGEN:
                for eintrag in abrufen(token, abfrage["dimensions"], tage=3):
                    schluessel = "|".join([
                        abfrage["label"], f"{vorvortag}_3tage", str(eintrag.get("metricName", "")),
                    ])
                    if schluessel in bekannt:
                        continue
                    bekannt.add(schluessel)
                    datei.write(json.dumps({
                        "abgerufen_am": heute.isoformat(),
                        "gilt_fuer": f"{vorvortag}..{abgedeckt}",
                        "fenster_tage": 3,
                        "luecke": True,
                        "abfrage": abfrage["label"],
                        "schluessel": schluessel,
                        "daten": eintrag,
                    }, ensure_ascii=False) + "\n")
                    neu += 1

    hinweis = f", {uebersprungen} bereits vorhanden" if uebersprungen else ""
    meldung = f"{neu} neue Zeilen fuer {abgedeckt}{hinweis}"
    print(f"{meldung} -> {HISTORY.relative_to(ROOT)}")
    protokollieren(meldung if neu else f"{meldung} -- nichts Neues")


def protokollieren(text: str) -> None:
    """Eine Zeile ans Lauf-Protokoll haengen. Darf den Lauf nie zum Scheitern bringen."""
    try:
        PROTOKOLL.parent.mkdir(parents=True, exist_ok=True)
        stempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with PROTOKOLL.open("a", encoding="utf-8") as f:
            f.write(f"{stempel}  {text}\n")
    except OSError:
        pass


if __name__ == "__main__":
    try:
        main()
    except SystemExit as ende:  # token_lesen() bricht so ab -- der Grund gehoert ins Protokoll
        protokollieren(f"ABBRUCH: {ende.code}" if ende.code else "beendet")
        raise
    except Exception as fehler:  # noqa: BLE001 - im geplanten Lauf gibt es niemanden, der es sieht
        protokollieren(f"FEHLER: {type(fehler).__name__}: {fehler}")
        raise
