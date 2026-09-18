"""Wochenbericht aus der lokalen Clarity-Historie -- ohne einen einzigen API-Aufruf.

Der taegliche Sammler (`clarity_daily.py`) baut die Historie auf; dieses Skript wertet
sie nur aus. Es geht deshalb **nicht ins Netz** und verbraucht nichts vom Tageskontingent
der Export-API -- ein Wochenbericht laesst sich beliebig oft neu rechnen.

Warum ein Wochenbericht trotz Rauschens: Bei rund 20 Sitzungen je Woche ist eine
Differenz zur Vorwoche **keine Aussage** (OPTIMIERUNG.md §5 sagt das schon fuer
Monatswerte). Der Bericht ist deshalb als **Ueberwachung** gebaut, nicht als
Entscheidungsgrundlage: Laeuft der Sammler lueckenlos? Gibt es einen Ausreisser, der
eine Erklaerung hat? Kommt ein neuer Verweis dazu? Die Trendgroesse ist der rollierende
Vierwochenwert, nicht die einzelne Woche. Entschieden wird weiter im Monatslauf.

Aufruf:
    py _scripts/wochenbericht.py                  # zuletzt abgeschlossene Woche
    py _scripts/wochenbericht.py --woche 2026-W37 # bestimmte Kalenderwoche
    py _scripts/wochenbericht.py --gesamt         # alle gemessenen Wochen auf einmal
    py _scripts/wochenbericht.py --keine-kurzfassung

Ablage: `_analytics/wochen/<JJJJ>-W<NN>.md` (Langfassung, gitignored wie die Historie)
und `~/Desktop/HOMEPAGE-WOCHE.md` (Kurzfassung, wird jede Woche ueberschrieben).
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "_analytics" / "clarity_history.jsonl"
YT_HISTORY = ROOT / "_analytics" / "youtube_history.jsonl"
BERICHTE = ROOT / "_analytics" / "wochen"
PROTOKOLL = ROOT / "_analytics" / "_wochenbericht.log"
KURZFASSUNG = Path.home() / "Desktop" / "HOMEPAGE-WOCHE.md"

# Unterhalb dieser Wochensumme wird jede Differenz zur Vorwoche als Rauschen markiert.
# Herleitung: OPTIMIERUNG.md §5 -- bei ~90 Sitzungen im Monat ist kein Vergleich
# belastbar; ein Viertel davon ist die Wochenentsprechung.
RAUSCH_SCHWELLE = 30

# Frustsignale der Live-Insights-API. Jede Metrik liefert `subTotal` als Anzahl.
FRUSTSIGNALE = {
    "DeadClickCount": "Tote Klicks",
    "RageClickCount": "Wutklicks",
    "QuickbackClick": "Sofort-Zurueck",
    "ErrorClickCount": "Fehlklicks",
    "ScriptErrorCount": "Skriptfehler",
    "ExcessiveScroll": "Uebermaessiges Scrollen",
}

# Vor dem 02.09.2026 lief die lokale Vorschau in die Produktivmessung (OPTIMIERUNG.md §6).
# Seit consent.js den Host prueft, kann nichts Neues dazukommen -- der Filter bleibt
# trotzdem stehen, weil aeltere Wochen nachgerechnet werden koennen.
LOKALE_HOSTS = ("127.0.0.1", "localhost", "::1")

# Die eigene Domain taucht in `ReferrerUrl` auf, sobald jemand intern weiterklickt.
# Diese Zeilen sind **keine** Zulaeufe -- ungetrennt sehen sie in der Tabelle aber genauso
# aus und lassen eine Woche ohne jeden externen Verweis gut besucht wirken.
EIGENE_DOMAIN = "secure-galvano-ai.com"

# `strftime("%a")` haengt an der Locale und liefert hier englische Kuerzel in einem
# deutschen Bericht. Feste Liste statt Locale-Umschaltung: das ist ein Prozesszustand,
# der andere Ausgaben desselben Laufs mit veraendern wuerde.
WOCHENTAGE = ("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")


def zahl(wert: object) -> float:
    """Robuste Zahl aus dem API-Wust. `None` und leere Zeichenketten werden 0.

    Die API liefert dieselbe Groesse mal als Zahl, mal als Zeichenkette (`"16"`), und
    bei leeren Tagen als `null`. Ohne diese Stelle scheitert die Summe am ersten
    besucherlosen Tag -- und das sind rund ein Fuenftel aller Tage.
    """
    if wert is None or wert == "":
        return 0.0
    try:
        return float(wert)
    except (TypeError, ValueError):
        return 0.0


def woche_grenzen(jahr: int, kw: int) -> tuple[date, date]:
    """Montag und Sonntag einer ISO-Kalenderwoche."""
    montag = date.fromisocalendar(jahr, kw, 1)
    return montag, montag + timedelta(days=6)


def letzte_abgeschlossene_woche(heute: date) -> tuple[int, int]:
    """Die Woche, die am letzten Sonntag endete.

    Bewusst nicht die laufende Woche: Der Sammler holt immer den **Vortag**, die
    laufende Woche waere also systematisch unvollstaendig und der Vergleich mit der
    Vorwoche wertlos. Am Montag frueh ist die abgelaufene Woche vollstaendig.
    """
    letzter_sonntag = heute - timedelta(days=heute.isoweekday())
    jahr, kw, _ = letzter_sonntag.isocalendar()
    return jahr, kw


def historie_lesen() -> dict[str, dict[str, dict[str, list]]]:
    """Tageswerte als ``[tag][abfrage][metrik] -> information``.

    Ausgeschlossen werden Zeilen mit ``fenster_tage != 1``: Das sind Erstlauf- und
    Nachhol-Fenster ueber drei Tage. Sie ueberlappen sich und wuerden Sitzungen
    mehrfach zaehlen -- als Summenwert brauchbar, in einer Wochensumme falsch.
    """
    if not HISTORY.exists():
        sys.exit(f"Historie fehlt: {HISTORY}\nLaeuft der Task 'Clarity Daily Pull'?")
    daten: dict[str, dict[str, dict[str, list]]] = defaultdict(lambda: defaultdict(dict))
    for zeile in HISTORY.read_text(encoding="utf-8").splitlines():
        if not zeile.strip():
            continue
        try:
            eintrag = json.loads(zeile)
        except json.JSONDecodeError:
            continue  # beschaedigte Zeile ueberspringen, nicht den Bericht verlieren
        tag = eintrag.get("gilt_fuer")
        if not tag or eintrag.get("fenster_tage") != 1:
            continue
        metrik = (eintrag.get("daten") or {}).get("metricName")
        if not metrik:
            continue
        daten[tag][eintrag.get("abfrage", "")][metrik] = (
            eintrag["daten"].get("information") or []
        )
    return daten


def tage_der_woche(jahr: int, kw: int) -> list[str]:
    montag, _ = woche_grenzen(jahr, kw)
    return [(montag + timedelta(days=i)).isoformat() for i in range(7)]


def woche_rechnen(daten: dict, jahr: int, kw: int) -> dict:
    """Alle Kennzahlen einer Kalenderwoche.

    Wichtig fuer die Lesart: Ein Tag **ohne Eintrag** heisst, der Sammler lief nicht --
    ein Tag **mit** Eintrag und 0 Sitzungen heisst, es war niemand da. Die beiden
    duerfen nie zusammenfallen, sonst sieht ein Sammlerausfall aus wie ein schwacher Tag.
    """
    tage = tage_der_woche(jahr, kw)
    vorhanden = [t for t in tage if t in daten]
    # Der Sammler holt den Vortag -- heute und alles danach kann noch gar nicht
    # dastehen. Ohne diese Schranke meldete ein Lauf ueber die laufende Woche eine
    # Luecke, die keine ist, und der einzige echte Alarm des Berichts waere entwertet.
    letzter_moeglicher = (date.today() - timedelta(days=1)).isoformat()
    fehlend = [t for t in tage if t not in daten and t <= letzter_moeglicher]

    sitzungen = bots = nutzer_tageweise = direkt = intern = 0
    scroll_summe = aktiv_summe = gewicht = 0.0
    frust: dict[str, int] = defaultdict(int)
    geraete: dict[str, int] = defaultdict(int)
    laender: dict[str, int] = defaultdict(int)
    seiten: dict[str, int] = defaultdict(int)
    verweise: dict[str, int] = defaultdict(int)
    tagesreihe: list[tuple[str, int]] = []

    for tag in vorhanden:
        gesamt = daten[tag].get("gesamt", {})
        traffic = (gesamt.get("Traffic") or [{}])[0]
        tages_sitzungen = int(zahl(traffic.get("totalSessionCount")))
        sitzungen += tages_sitzungen
        bots += int(zahl(traffic.get("totalBotSessionCount")))
        nutzer_tageweise += int(zahl(traffic.get("distinctUserCount")))
        tagesreihe.append((tag, tages_sitzungen))

        # Mittelwerte werden mit den Sitzungen des Tages gewichtet. Ungewichtet zaehlte
        # ein Tag mit einer einzigen Sitzung so viel wie ein Tag mit zwanzig.
        if tages_sitzungen:
            scroll = (gesamt.get("ScrollDepth") or [{}])[0]
            engagement = (gesamt.get("EngagementTime") or [{}])[0]
            scroll_summe += zahl(scroll.get("averageScrollDepth")) * tages_sitzungen
            aktiv_summe += zahl(engagement.get("activeTime")) * tages_sitzungen
            gewicht += tages_sitzungen

        for metrik in FRUSTSIGNALE:
            for zeile in gesamt.get(metrik) or []:
                frust[metrik] += int(zahl(zeile.get("subTotal")))

        for zeile in gesamt.get("Device") or []:
            geraete[str(zeile.get("name") or "unbekannt")] += int(zahl(zeile.get("sessionsCount")))
        for zeile in gesamt.get("Country") or []:
            laender[str(zeile.get("name") or "unbekannt")] += int(zahl(zeile.get("sessionsCount")))

        for zeile in gesamt.get("PopularPages") or []:
            url = str(zeile.get("url") or "")
            if any(host in url for host in LOKALE_HOSTS):
                continue  # eigene Vorschau, keine Besucherseite
            seiten[kurz_url(url)] += int(zahl(zeile.get("visitsCount")))

        for zeile in gesamt.get("ReferrerUrl") or []:
            name = str(zeile.get("name") or "")
            anzahl = int(zahl(zeile.get("sessionsCount")))
            if not name:
                direkt += anzahl
            elif EIGENE_DOMAIN in name or any(host in name for host in LOKALE_HOSTS):
                intern += anzahl  # Klick von einer eigenen Seite auf die naechste
            else:
                verweise[name] += anzahl

    montag, sonntag = woche_grenzen(jahr, kw)
    return {
        "jahr": jahr,
        "kw": kw,
        "von": montag,
        "bis": sonntag,
        "tage_vorhanden": len(vorhanden),
        "tage_fehlend": fehlend,
        "sitzungen": sitzungen,
        "bots": bots,
        "nutzer_tageweise": nutzer_tageweise,
        "scrolltiefe": scroll_summe / gewicht if gewicht else None,
        "aktive_zeit": aktiv_summe / gewicht if gewicht else None,
        "frust": dict(frust),
        "geraete": dict(geraete),
        "laender": dict(laender),
        "seiten": dict(seiten),
        "verweise": dict(verweise),
        "direkt": direkt,
        "intern": intern,
        "tagesreihe": tagesreihe,
    }


def vorwoche(jahr: int, kw: int) -> tuple[int, int]:
    montag, _ = woche_grenzen(jahr, kw)
    davor = montag - timedelta(days=7)
    j, k, _ = davor.isocalendar()
    return j, k


def mit_einheit(wert: float | None, einheit: str, stellen: int = 0) -> str:
    """Zahl mit Einheit, oder ein Strich. Fehlender Wert ist nicht dasselbe wie 0 --
    an einer Woche ohne einzige Sitzung gibt es keine Scrolltiefe, und eine 0 dort
    laese sich als „alle brachen sofort ab“ missverstehen."""
    return f"{wert:.{stellen}f}{einheit}" if wert is not None else "—"


def differenz(jetzt: float | None, vorher: float | None, einheit: str = "") -> str:
    """Differenzzeile. Ohne Vergleichswert bewusst ein Strich statt einer 0."""
    if jetzt is None or vorher is None:
        return "—"
    delta = jetzt - vorher
    vorzeichen = "+" if delta > 0 else ""
    return f"{vorzeichen}{delta:.0f}{einheit}" if abs(delta) >= 1 else "±0"


def youtube_stand() -> list[dict]:
    """Letzter und vorletzter Zaehlerstand je Video.

    Aufrufe sind ein kumulativer Zaehler: Interessant ist nur, was seit dem letzten
    Ablesen dazugekommen ist -- und ueber welchen Zeitraum.
    """
    if not YT_HISTORY.exists():
        return []
    staende: dict[str, list[dict]] = defaultdict(list)
    for zeile in YT_HISTORY.read_text(encoding="utf-8").splitlines():
        if not zeile.strip():
            continue
        try:
            eintrag = json.loads(zeile)
        except json.JSONDecodeError:
            continue
        staende[eintrag.get("video_id", "?")].append(eintrag)
    ergebnis = []
    for eintraege in staende.values():
        eintraege.sort(key=lambda e: e.get("abgerufen_am", ""))
        letzter = eintraege[-1]
        vorletzter = eintraege[-2] if len(eintraege) > 1 else None
        ergebnis.append({
            "titel": letzter.get("titel", letzter.get("video_id", "?")),
            "aufrufe": int(zahl(letzter.get("aufrufe"))),
            "stand": letzter.get("abgerufen_am", "?"),
            "zuwachs": (
                int(zahl(letzter.get("aufrufe"))) - int(zahl(vorletzter.get("aufrufe")))
                if vorletzter else None
            ),
            "seit": vorletzter.get("abgerufen_am") if vorletzter else None,
        })
    return sorted(ergebnis, key=lambda e: -e["aufrufe"])


def rangliste(werte: dict[str, int], anzahl: int = 5) -> list[tuple[str, int]]:
    return sorted(werte.items(), key=lambda p: -p[1])[:anzahl]


def kurz_url(url: str) -> str:
    """Domain weg, Startseite vereinheitlicht.

    `/` und `/index.html` sind dieselbe Seite; getrennt gezaehlt halbieren sie die
    meistbesuchte Seite und schieben sie in der Rangliste nach unten.
    """
    gekuerzt = url.split("?")[0]
    for praefix in (f"https://www.{EIGENE_DOMAIN}", f"https://{EIGENE_DOMAIN}"):
        gekuerzt = gekuerzt.replace(praefix, "")
    if gekuerzt in ("", "/index.html"):
        return "/"
    return gekuerzt


def bericht_bauen(w: dict, v: dict, vier_wochen: list[dict], videos: list[dict]) -> str:
    """Die Langfassung. Sie ist Lieferinhalt -- deshalb mit Umlauten, anders als der Code."""
    z: list[str] = []
    a = z.append

    a(f"# Homepage-Woche {w['jahr']}-W{w['kw']:02d} — {w['von']:%d.%m.} bis {w['bis']:%d.%m.%Y}")
    a("")
    a(f"*Erzeugt am {date.today():%d.%m.%Y} von `_scripts/wochenbericht.py` aus der lokalen "
      "Historie. Keine Netzabfrage, jederzeit neu rechenbar.*")
    a("")

    # Die Einordnung steht bewusst vor den Zahlen. Wer sie darunter setzt, liest sie nicht.
    if w["sitzungen"] < RAUSCH_SCHWELLE:
        a(f"> ⚠️ **{w['sitzungen']} Sitzungen — jede Differenz zur Vorwoche ist Rauschen.** "
          f"Belastbar wird ein Vergleich erst ab rund {RAUSCH_SCHWELLE} Sitzungen je Woche "
          "(`OPTIMIERUNG.md` §5). Lies diese Seite als Überwachung: Läuft der Sammler? "
          "Gibt es einen Ausreißer mit Erklärung? Kommt ein neuer Verweis dazu? "
          "**Entschieden wird im Monatslauf, nicht hier.**")
        a("")

    if w["tage_fehlend"]:
        a(f"> 🔴 **Der Sammler hat {len(w['tage_fehlend'])} Tag(e) nicht erfasst:** "
          f"{', '.join(w['tage_fehlend'])}. Das ist **kein** schwacher Tag, sondern eine Lücke — "
          "ein Tag ohne Besucher steht mit 0 in der Historie. Über die API sind diese Tage "
          "nach drei Tagen endgültig verloren (`OPTIMIERUNG.md` §6).")
        a("")

    a("## Auf einen Blick")
    a("")
    a("| Kennzahl | Diese Woche | Vorwoche | Differenz |")
    a("|---|---|---|---|")
    a(f"| **Sitzungen** | **{w['sitzungen']}** | {v['sitzungen']} | "
      f"{differenz(w['sitzungen'], v['sitzungen'])} |")
    a(f"| Ø Scrolltiefe (gewichtet) | {mit_einheit(w['scrolltiefe'], ' %', 1)} | "
      f"{mit_einheit(v['scrolltiefe'], ' %', 1)} | "
      f"{differenz(w['scrolltiefe'], v['scrolltiefe'], ' %')} |")
    a(f"| Ø aktive Zeit (gewichtet) | {mit_einheit(w['aktive_zeit'], ' s')} | "
      f"{mit_einheit(v['aktive_zeit'], ' s')} | "
      f"{differenz(w['aktive_zeit'], v['aktive_zeit'], ' s')} |")
    a(f"| Erfasste Tage | {w['tage_vorhanden']} von 7 | {v['tage_vorhanden']} von 7 | |")
    a(f"| Bot-Sitzungen | {w['bots']} | {v['bots']} | |")
    a("")
    a("> **Die Sitzungszahl ist eine Untergrenze.** Clarity zählt nur, wer im Banner "
      "„Akzeptieren“ klickt, und die lokale Historie untererfasst zusätzlich gegenüber der "
      "Clarity-Oberfläche (belegt 31.08.2026, `OPTIMIERUNG.md` §1). Für den Verlauf gegen "
      "sich selbst taugt sie, für ein Niveau nicht.")
    a("")

    a("## Trend über vier Wochen")
    a("")
    a("| Woche | Zeitraum | Sitzungen | Erfasste Tage |")
    a("|---|---|---|---|")
    for eintrag in vier_wochen:
        marke = " ←" if eintrag["kw"] == w["kw"] and eintrag["jahr"] == w["jahr"] else ""
        a(f"| {eintrag['jahr']}-W{eintrag['kw']:02d}{marke} | "
          f"{eintrag['von']:%d.%m.}–{eintrag['bis']:%d.%m.} | {eintrag['sitzungen']} | "
          f"{eintrag['tage_vorhanden']}/7 |")
    schnitt = sum(e["sitzungen"] for e in vier_wochen) / len(vier_wochen)
    a("")
    a(f"**Rollierender Vierwochenschnitt: {schnitt:.1f} Sitzungen je Woche.** Das ist die "
      "Trendgröße dieses Berichts — sie springt weniger als die einzelne Woche.")
    a("")

    a("## Tagesverlauf")
    a("")
    a("| Tag | Sitzungen |")
    a("|---|---|")
    for tag, anzahl in w["tagesreihe"]:
        wochentag = WOCHENTAGE[date.fromisoformat(tag).weekday()]
        balken = "▇" * min(anzahl, 30)
        a(f"| {wochentag} {tag[8:10]}.{tag[5:7]}. | {anzahl} {balken} |")
    a("")

    if w["seiten"]:
        a("## Meistbesuchte Seiten")
        a("")
        a("| Seite | Aufrufe |")
        a("|---|---|")
        for seite, anzahl in rangliste(w["seiten"]):
            a(f"| `{seite}` | {anzahl} |")
        a("")

    a("## Woher die Besucher kamen")
    a("")
    a(f"**Direkt aufgerufen:** {w['direkt']} · **interne Seitenwechsel:** {w['intern']} "
      "*(kein Zulauf — jemand klickte von einer eigenen Seite auf die nächste)*")
    a("")
    if w["verweise"]:
        a("| Externer Verweis | Sitzungen |")
        a("|---|---|")
        for quelle, anzahl in rangliste(w["verweise"]):
            a(f"| {quelle} | {anzahl} |")
    else:
        a("**Kein einziger externer Verweis diese Woche.** Wer kam, kannte die Adresse "
          "bereits — Verkehr aus Ansprache und Netzwerk, nicht aus Suche oder Fremdseiten.")
    a("")
    a("> **Marken- und Nicht-Marken-Verkehr trennen** (`OPTIMIERUNG.md` §5 Regel 5). Ein "
      "direkter Aufruf ist fast immer Markenverkehr und belegt keine Auffindbarkeit.")
    a("")

    if w["geraete"] or w["laender"]:
        a("## Geräte und Herkunft")
        a("")
        geraete = " · ".join(f"{name} {anzahl}" for name, anzahl in rangliste(w["geraete"]))
        laender = " · ".join(f"{name} {anzahl}" for name, anzahl in rangliste(w["laender"], 4))
        a(f"**Geräte:** {geraete or '—'}")
        a("")
        a(f"**Länder:** {laender or '—'}")
        a("")

    a("## Frustsignale")
    a("")
    gesamt_frust = sum(w["frust"].values())
    if gesamt_frust:
        a("| Signal | Diese Woche | Vorwoche |")
        a("|---|---|---|")
        for metrik, bezeichnung in FRUSTSIGNALE.items():
            jetzt = w["frust"].get(metrik, 0)
            davor = v["frust"].get(metrik, 0)
            if jetzt or davor:
                a(f"| {bezeichnung} | {jetzt} | {davor} |")
        a("")
        a("> **Die API kennt die Anzahl, nicht das Element.** Welcher Knopf einen toten Klick "
          "auslöst, steht nur in der Clarity-Oberfläche (Aufzeichnungen, 28 Tage). Ein Signal "
          "hier ist ein Anlass nachzusehen, kein Befund.")
    else:
        a("Keine — über die ganze Woche kein toter Klick, kein Wutklick, kein Skriptfehler.")
    a("")

    if videos:
        a("## Video-Abrufe")
        a("")
        a("| Video | Aufrufe | Zuwachs |")
        a("|---|---|---|")
        for eintrag in videos:
            zuwachs = (
                f"+{eintrag['zuwachs']} seit {eintrag['seit']}"
                if eintrag["zuwachs"] is not None else f"Erststand {eintrag['stand']}"
            )
            a(f"| {eintrag['titel']} | {eintrag['aufrufe']} | {zuwachs} |")
        a("")

    a("---")
    a("")
    a("## Was hier bewusst fehlt")
    a("")
    a("- **CTA-Klicks, PDF-Abrufe, Scrollmarken** (`data-funnel`, `pdf-*`, `scroll-*`): Custom "
      "Events stehen in **keiner** API-Zeile — eine Produktgrenze von Clarity, kein Mangel am "
      "Sammler (`OPTIMIERUNG.md` §1). Sie werden im Monatslauf aus der Oberfläche gelesen.")
    a("- **Search Console**: bewusst kein API-Zugang (verworfen 11.08.2026, §2). Zwei- bis "
      "dreimal im Jahr von Hand.")
    a("- **LinkedIn**: braucht den XLSX-Export, läuft im Monatslauf über "
      "`linkedin_abholen.py`.")
    a("- **Terminanfragen** — die einzige Zahl, die zählt. Sie steht in Bookings und im "
      "Postfach, nicht in einer Schnittstelle.")
    a("")
    return "\n".join(z) + "\n"


def kurzfassung_bauen(w: dict, v: dict, schnitt: float, pfad: Path) -> str:
    """Zwölf Zeilen für den Desktop. Alles Weitere steht in der Langfassung."""
    z: list[str] = []
    a = z.append
    a(f"# Homepage — Woche {w['jahr']}-W{w['kw']:02d} ({w['von']:%d.%m.}–{w['bis']:%d.%m.})")
    a("")
    # Listenpunkte statt einzelner Zeilen: Ohne sie zieht Markdown die Zeilen beim
    # Rendern zu einem Fliesstext zusammen, und die Kurzfassung verliert genau das,
    # wofuer es sie gibt -- sie auf einen Blick lesen zu koennen.
    a(f"- **{w['sitzungen']} Sitzungen** (Vorwoche {v['sitzungen']}, "
      f"Vierwochenschnitt {schnitt:.1f})")
    if w["scrolltiefe"] is not None:
        a(f"- Scrolltiefe {w['scrolltiefe']:.0f} % · aktive Zeit {w['aktive_zeit']:.0f} s")
    top = rangliste(w["seiten"], 3)
    if top:
        a("- Meistbesucht: " + " · ".join(f"`{seite}` {n}" for seite, n in top))
    if w["verweise"]:
        a("- Externe Verweise: " + " · ".join(
            f"{quelle} {n}" for quelle, n in rangliste(w["verweise"], 2)))
    frust = sum(w["frust"].values())
    a(f"- Frustsignale: {frust}"
      + (" — in der Clarity-Oberfläche nachsehen" if frust else ""))
    a("")
    if w["tage_fehlend"]:
        a(f"🔴 **Sammler-Lücke:** {', '.join(w['tage_fehlend'])} — nicht erfasst, nicht "
          "nachholbar.")
    else:
        a("✅ Sammler lückenlos, 7 von 7 Tagen erfasst.")
    if w["sitzungen"] < RAUSCH_SCHWELLE:
        a("")
        a("⚠️ Bei dieser Menge ist die Differenz zur Vorwoche Rauschen — Überwachung, "
          "keine Entscheidungsgrundlage. Entschieden wird im Monatslauf.")
    a("")
    a(f"Langfassung: `{pfad}`")
    a("")
    return "\n".join(z)


def gesamtuebersicht(daten: dict) -> str:
    """Alle gemessenen Wochen auf einmal -- fuer die Frage „wird es mehr?".

    Bewusst als eigener Aufruf (`--gesamt`) und nicht im Wochenbericht: Dort wuerde die
    Tabelle mit jeder Woche laenger und die Kurzfassung erschlagen. Hier steht sie, wenn
    man sie braucht.
    """
    wochen: dict[tuple[int, int], list[int]] = defaultdict(lambda: [0, 0])
    tagesbeste: list[tuple[int, str]] = []
    verweise: dict[str, int] = defaultdict(int)
    tage_leer = tage_gesamt = 0

    for tag, abfragen in daten.items():
        gesamt = abfragen.get("gesamt", {})
        traffic = (gesamt.get("Traffic") or [{}])[0]
        sitzungen = int(zahl(traffic.get("totalSessionCount")))
        jahr, kw, _ = date.fromisoformat(tag).isocalendar()
        wochen[(jahr, kw)][0] += sitzungen
        wochen[(jahr, kw)][1] += 1
        tagesbeste.append((sitzungen, tag))
        tage_gesamt += 1
        tage_leer += 1 if sitzungen == 0 else 0
        for zeile in gesamt.get("ReferrerUrl") or []:
            name = str(zeile.get("name") or "")
            if name and EIGENE_DOMAIN not in name and not any(h in name for h in LOKALE_HOSTS):
                verweise[name] += int(zahl(zeile.get("sessionsCount")))

    if not wochen:
        return "Keine Tageswerte in der Historie.\n"

    z: list[str] = []
    a = z.append
    tage = sorted(daten)
    summe = sum(w[0] for w in wochen.values())
    a(f"# Homepage — Gesamtverlauf {tage[0]} bis {tage[-1]}")
    a("")
    a(f"*Erzeugt am {date.today():%d.%m.%Y}. {tage_gesamt} gemessene Tage, "
      f"**{summe} Sitzungen**, an {tage_leer} Tagen kam niemand.*")
    a("")
    a("| Woche | Zeitraum | Sitzungen | Ø/Tag | Tage |")
    a("|---|---|---|---|---|")
    for (jahr, kw) in sorted(wochen):
        anzahl, tage_erfasst = wochen[(jahr, kw)]
        montag, sonntag = woche_grenzen(jahr, kw)
        schnitt = anzahl / tage_erfasst if tage_erfasst else 0
        a(f"| {jahr}-W{kw:02d} | {montag:%d.%m.}–{sonntag:%d.%m.} | {anzahl} | "
          f"{schnitt:.1f} | {tage_erfasst}/7 |")
    a("")

    # Einzelne Tage tragen bei dieser Menge ganze Wochen. Wer sie nicht kennt, liest
    # einen Veroeffentlichungstag als Wachstum.
    tagesbeste.sort(reverse=True)
    a("**Stärkste Einzeltage:** " + " · ".join(
        f"{tag} ({anzahl})" for anzahl, tag in tagesbeste[:3]))
    anteil = sum(anzahl for anzahl, _ in tagesbeste[:3]) / summe * 100 if summe else 0
    a("")
    a(f"Diese drei Tage allein tragen **{anteil:.0f} %** aller Sitzungen. Ein Anstieg, der "
      "auf solchen Tagen steht, ist ein Veröffentlichungs- oder Presseeffekt und keine "
      "Optimierungswirkung (`OPTIMIERUNG.md` §5 Regel 6) — erst der Sockel danach zählt.")
    a("")

    a("## Externe Verweise über den gesamten Zeitraum")
    a("")
    if verweise:
        a("| Quelle | Sitzungen |")
        a("|---|---|")
        for quelle, anzahl in sorted(verweise.items(), key=lambda p: -p[1]):
            a(f"| {quelle} | {anzahl} |")
        a("")
        a(f"**Zusammen {sum(verweise.values())} von {summe} Sitzungen.** Alles Übrige wurde "
          "direkt aufgerufen oder war ein interner Seitenwechsel.")
    else:
        a("**Keine.** Jede gemessene Sitzung kam direkt oder über einen internen Wechsel.")
    a("")
    a("> ⚠️ **Diese Zahlen beantworten die Frage „haben wir mehr Verkehr“ nicht allein.** "
      "Clarity zählt nur, wer im Banner „Akzeptieren“ klickt, und die lokale Historie "
      "untererfasst zusätzlich (`OPTIMIERUNG.md` §1). Belegt: Der GSC-Export für August nannte "
      "**60 Suchklicks**, während hier für denselben Zeitraum sechs Google-Verweise stehen. "
      "**Für Verkehrsmengen ist die Search Console die Quelle**, nicht diese Tabelle — sie "
      "zählt ohne Einwilligung und reicht 16 Monate zurück. Hier steht der *Verlauf gegen sich "
      "selbst*, und dafür taugt es.")
    a("")
    return "\n".join(z)


def protokollieren(text: str) -> None:
    """Eine Zeile ans Lauf-Protokoll. Darf den Lauf nie zum Scheitern bringen."""
    try:
        PROTOKOLL.parent.mkdir(parents=True, exist_ok=True)
        stempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with PROTOKOLL.open("a", encoding="utf-8") as datei:
            datei.write(f"{stempel}  {text}\n")
    except OSError:
        pass


def woche_aus_argument(wert: str) -> tuple[int, int]:
    try:
        jahr_text, kw_text = wert.upper().split("-W")
        return int(jahr_text), int(kw_text)
    except ValueError:
        sys.exit(f"--woche erwartet die Form 2026-W37, bekommen: {wert}")


def main() -> None:
    argumente = sys.argv[1:]
    kurzfassung_schreiben = "--keine-kurzfassung" not in argumente
    if "--woche" in argumente:
        jahr, kw = woche_aus_argument(argumente[argumente.index("--woche") + 1])
    else:
        jahr, kw = letzte_abgeschlossene_woche(date.today())

    daten = historie_lesen()

    if "--gesamt" in argumente:
        BERICHTE.mkdir(parents=True, exist_ok=True)
        ziel = BERICHTE / "GESAMTVERLAUF.md"
        ziel.write_text(gesamtuebersicht(daten), encoding="utf-8")
        print(f"Gesamtverlauf ueber {len(daten)} Tage -> {ziel.relative_to(ROOT)}")
        protokollieren(f"Gesamtverlauf ueber {len(daten)} Tage")
        return

    diese = woche_rechnen(daten, jahr, kw)
    vorige = woche_rechnen(daten, *vorwoche(jahr, kw))

    # Vier Wochen aufsteigend: die aelteste zuerst, damit die Tabelle sich wie ein
    # Verlauf liest und nicht wie eine Rangliste.
    vier: list[dict] = []
    j, k = jahr, kw
    for _ in range(4):
        vier.insert(0, woche_rechnen(daten, j, k))
        j, k = vorwoche(j, k)
    schnitt = sum(e["sitzungen"] for e in vier) / len(vier)

    BERICHTE.mkdir(parents=True, exist_ok=True)
    ziel = BERICHTE / f"{jahr}-W{kw:02d}.md"
    ziel.write_text(bericht_bauen(diese, vorige, vier, youtube_stand()), encoding="utf-8")

    if kurzfassung_schreiben:
        try:
            KURZFASSUNG.write_text(
                kurzfassung_bauen(diese, vorige, schnitt, ziel), encoding="utf-8"
            )
        except OSError as fehler:  # Desktop kann umgezogen sein -- kein Grund zum Abbruch
            protokollieren(f"Kurzfassung nicht geschrieben: {fehler}")

    meldung = (
        f"W{kw:02d}/{jahr}: {diese['sitzungen']} Sitzungen, "
        f"{diese['tage_vorhanden']}/7 Tage erfasst"
        + (f", LUECKE {','.join(diese['tage_fehlend'])}" if diese["tage_fehlend"] else "")
    )
    print(f"{meldung} -> {ziel.relative_to(ROOT)}")
    protokollieren(meldung)


if __name__ == "__main__":
    try:
        main()
    except SystemExit as ende:
        if ende.code:
            protokollieren(f"ABBRUCH: {ende.code}")
        raise
    except Exception as fehler:  # noqa: BLE001 - im geplanten Lauf sieht es sonst niemand
        protokollieren(f"FEHLER: {type(fehler).__name__}: {fehler}")
        raise
