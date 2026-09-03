# Monatlicher Optimierungs-Prozess

Ziel: **Terminanfragen erhöhen.** Alles andere (Klicks, Impressionen, Scrolltiefe) ist
Diagnose, kein Ziel. Rhythmus: **einmal im Monat, am ersten Werktag**, für den abgelaufenen
Kalendermonat.

Der Prozess ist so geschnitten, dass Claude ihn weitgehend allein fährt. Stefan wird nur
dort gebraucht, wo Anmeldung, Freigabe oder ein menschliches Urteil nötig ist — diese
Stellen sind mit 👤 markiert.

---

## 1. Datenquellen und was jede wirklich kann

| Quelle | Reichweite | Automatisierbar | Wofür |
|---|---|---|---|
| **Search Console** (Browser) | 16 Monate, Suchanfrage/Seite/Gerät/Land | ❌ bewusst manuell | Wie Leute ankommen — **nur 2–3× im Jahr nötig** |
| **Clarity Data Export API** | **nur 1–3 Tage**, 10 Abfragen/Tag, max. 3 Dimensionen, 1000 Zeilen, keine Pagination | ⚠️ nur mit täglichem Sammler | Aggregierte Kennzahlen + Frustsignale (Anzahl) |
| **Clarity Heatmaps / Aufzeichnungen** | 28 Tage in der Oberfläche | ❌ nicht über API | *Welches* Element tote Klicks auslöst |
| **Clarity Custom Events** (`data-funnel`, `scroll-*`, `pdf-*`) | 28 Tage in der Oberfläche | ❌ **gar nicht über API** | CTA-Klicks je Position, Beleg-Abrufe, Scrollmarken |

**Die Funnel-Events stehen in keiner Zeile der Historie** (geprüft 24.08.2026 über 517
Zeilen). Die Live-Insights-API kennt neun feste Metriken und drei Dimensionen — Custom
Events sind keine davon, unabhängig davon, was der Sammler anfragt. Wer die Zahl der
CTA-Klicks braucht, liest sie in der Clarity-Oberfläche ab; automatisieren lässt sie sich
nicht. Das ist eine Produktgrenze, kein Mangel am Sammler — nicht erneut als Fehler
aufnehmen.

**Die entscheidende Einschränkung:** Die Clarity-API liefert nur die letzten drei Tage.
Wer einmal im Monat abfragt, hat 27 Tage unwiederbringlich verloren — die Daten sind über
die API danach nicht mehr erreichbar. Deshalb läuft ein **täglicher Sammler**
(`_scripts/clarity_daily.py`), der die Historie lokal aufbaut. Das ist keine Bequemlichkeit,
sondern die einzige Möglichkeit, überhaupt an einen Monatsverlauf zu kommen.

**Was dauerhaft manuell bleibt:** Sitzungsaufzeichnungen. Die API kennt die *Anzahl* toter
Klicks, nicht das *Element*, und im Klick-Wärmebild sind die Beschriftungen maskiert. Das
sind 👤 ~5 Minuten pro Monat und der Teil mit dem höchsten Erkenntniswert — nicht
wegrationalisieren.

**Heatmaps und Ereignisliste holt Claude seit 31.08.2026 selbst** über den Browser (Ablauf
im Skill, Schritt 2). Stefan meldet sich einmal je Lauf an, mehr nicht — bewusst **ohne**
gespeicherte Sitzungsdatei, aus demselben Grund, aus dem der GSC-Dienstkonto-Schlüssel
abgelehnt wurde.

> ⚠️ **Die lokale Historie unterzählt** *(belegt 31.08.2026)*. Für 10.–30.08. stehen dort
> 44 Sitzungen, das Dashboard nennt 111 für 28 Tage — für dasselbe Fenster wären rund 75 zu
> erwarten. Dieselbe Richtung bei toten Klicks (1 gegen 6) und Google-Referrern (3 gegen 27).
> **Mittelwerte stimmen** (Scrolltiefe 58,2 % gegen 56,2 %). **Arbeitshypothese, nicht
> belegt:** `numOfDays=1` liefert den *laufenden* Tag bis zum Abruf um 09:15 statt des
> zuletzt abgeschlossenen — dann wäre die Reihe zusätzlich um einen Tag falsch beschriftet.
> Der Kommentar in `_scripts/clarity_daily.py:133` behauptet das Gegenteil ohne Beleg.
> **Test:** Dashboard auf „Letzte 7 Tage" gegen die Summe der Tageswerte derselben Woche.
> Bis dahin: Historie nur für Verhältnisse und Verlauf, jede *Anzahl* aus der Oberfläche.

**LinkedIn gehört seit 31.08.2026 in denselben Monatslauf** — eigener Abschnitt, gemeinsame
Schlussfolgerung. Die Zahlen kommen aus dem XLSX-Export über
`Business Development/scripts/analyse_linkedin.py`, **nicht** über den Browser: automatisierter
Zugriff verstößt dort gegen die Nutzungsbedingungen und riskiert das Konto. Gepflegt wird der
Befund in `projects/linkedin-auftritt/README.md`; hier steht nur, ob ein Beitrag Verkehr auf
die Seite gebracht hat.

---

## 2. Zugänge und Geheimnisse

| Was | Wo | Erneuern |
|---|---|---|
| Clarity-API-Token | `.env` im Repo-Wurzelverzeichnis, Schlüssel `CLARITY_API_TOKEN` — **gitignored** | Clarity → Einstellungen → Datenexport → *Neues API-Token generieren* (nur Projektadmin) |
| — (kein GSC-API-Zugang) | **Verworfen 11.08.2026, nicht erneut vorschlagen.** Der MCP-Server liegt fertig unter `~/.mcp-gsc/` (installiert 10.08.), es fehlt bewusst nur das Dienstkonto. Zwei Gründe: der Dienstkonto-Schlüssel wäre eine Zugangsdatei im Klartext auf der Platte und läuft `25_zugriffs-und-kryptographie.md` §3 zuwider („sämtliche Zugangsdaten im Tresor"); und er hinge am privaten Google-Konto, das über die Anthropic-SSO-Kopplung ohnehin schon geschäftskritisch ist. Gegenwert wären zwei erspartes Copy-Paste im Jahr. | — |
| Clarity-Projekt-ID | `wql3vpgrxl` | — |
| GSC-Property | `https://secure-galvano-ai.com/` | — |

Niemals ein Token in eine Datei schreiben, die in Git landet. Der Sammler liest
ausschließlich aus der Umgebung bzw. `.env`.

**Direktlinks:**
- [Clarity Dashboard](https://clarity.microsoft.com/projects/view/wql3vpgrxl/dashboard)
- [Clarity Heatmaps](https://clarity.microsoft.com/projects/view/wql3vpgrxl/heatmaps)
- [Clarity Aufzeichnungen](https://clarity.microsoft.com/projects/view/wql3vpgrxl/recordings)
- [Clarity Einstellungen → Datenexport](https://clarity.microsoft.com/projects/view/wql3vpgrxl/settings)
- [GSC Leistung](https://search.google.com/search-console/performance/search-analytics?resource_id=https%3A%2F%2Fsecure-galvano-ai.com%2F)
- [GSC Seitenindexierung](https://search.google.com/search-console/index?resource_id=https%3A%2F%2Fsecure-galvano-ai.com%2F)

---

## 3. Ablauf

### Laufend (automatisch, ohne Zutun)
Geplante Aufgabe `\SecureGalvano\Clarity Daily Pull` (täglich 09:15, `StartWhenAvailable`,
akkuunabhängig, nur bei angemeldetem Benutzer) ruft
`pyw.exe _scripts/clarity_daily.py` auf — fensterlos, rund vier Sekunden, kein Dienst
und kein Autostart. Der Lauf hängt **einen Tageswert** (`numOfDays=1`) an
`_analytics/clarity_history.jsonl` an; der Dublettenschlüssel ist
`Abfrage|abgedeckter Tag|Metrik`.

**Warum Tagesfenster und nicht drei Tage:** Die API liefert **Summenwerte über das
angefragte Fenster**, keine Tagesaufschlüsselung. Drei-Tage-Fenster überlappen sich
täglich und lassen sich nicht zu Monatswerten addieren, ohne Sitzungen mehrfach zu
zählen. Ebenso wichtig: Der Schlüssel enthält den **Tag**, nicht die Messwerte —
sonst verschwände ein Tag, an dem dieselben Zahlen anfallen wie am Vortag, und bei
Metriken, die meist 0 sind, wäre das der Regelfall.

**Lückenerkennung:** Fehlt der Vorvortag, holt der Lauf zusätzlich ein 3-Tage-Fenster
nach und legt es getrennt mit `"luecke": true` ab — als Summenwert brauchbar, aber
bewusst nicht mit Tageswerten summierbar. Mehr als zwei versäumte Tage sind endgültig
verloren. Bei HTTP 429 bricht das Skript sauber ab, ohne Retry.

**Protokoll:** je Lauf eine Zeile in `_analytics/_sammler.log`.

### Monatlich

> **Wie eine Aenderung ablaeuft, steht in [`AENDERUNGSPROZESS.md`](AENDERUNGSPROZESS.md)** *(seit 31.08.2026)*. Dieses Dokument hier fuehrt den **Messlauf** — was gemessen wird und welche Entscheidungsregeln gelten. Merksatz: hier steht, **was ist**; dort steht, **wie geaendert wird**.

**Der Ablauf steht im Skill** [`.claude/skills/optimierung/SKILL.md`](../.claude/skills/optimierung/SKILL.md)
und wird mit `/optimierung` gestartet. Er ist bewusst nur dort beschrieben — stünde er
zusätzlich hier, würden die beiden Stände auseinanderdriften.

Die Arbeitsteilung in einem Satz: Claude liest die Historie, rechnet den Funnel durch und
schreibt den Bericht; 👤 Stefan liefert die drei Angaben, die in keiner Schnittstelle
stehen — **Terminanfragen**, das Element hinter den toten Klicks, und die
Heatmap-Auffälligkeiten mobil wie Desktop.

Auslöser ist ein Outlook-Serientermin, erster Werktag im Monat (§7).

---

## 4. Kennzahlen

| Kennzahl | Woher | Stand 03.–31.08.2026 (28 Tage) | Richtung |
|---|---|---|---|
| **Terminanfragen** | 👤 Bookings + Mail | **0** | steigend |
| Sitzungen | Clarity-Dashboard, ohne localhost | **111** (≈ 4/Tag) | steigend |
| Ø Scrolltiefe | Clarity, alle Seiten | **56,2 %** | > 70 % |
| Startseite bis 100 % gelesen | Clarity-Heatmap, je Gerät | **Desktop 35 % · mobil 5 %** | mobil → > 20 % |
| Tote Klicks | Clarity `DeadClickCount` | **6 von 111 ≈ 5,4 %** ⚠️ — Ursache  am 31.08. behoben; alle sechs Faelle vom 6.–10.08. | < 5 % |
| Aktive Zeit | Clarity | 45 s von 1,5 min | — |
| Geräte | Clarity | 59 mobil / 46 Desktop | — |
| **CTA-Klicks je Position** | Clarity, Intelligente Ereignisse | **0** — alle Positionen | > 0 |
| Beleg-Abrufe (PDF/Video) | Clarity `pdf-*`, `video-*` | **18 PDF · 5 Video** | steigend |
| **Demo-Seite: Zulauf und Weiterweg** *(neu 02.09.2026)* | Clarity `link-*` und `cta-demo-seite` | **noch keine Historie** — die Seite trägt erst seit 02.09. ein Video | erstmals im Oktober-Lauf ablesbar |
| **Demo-Einseiter: Weitergabe im Haus** *(neu 02.09.2026)* | Clarity `pdf-anwendung-demo` | **noch keine Historie** | erstmals im Oktober-Lauf ablesbar. Er misst etwas anderes als die übrigen `pdf-*`: nicht Interesse, sondern die Absicht, die Sache **intern weiterzureichen** — Abrufe ohne Terminanfrage sind hier kein Fehlschlag |
| **Datenwerkstatt-Seite: trägt das Angebot?** *(neu 02.09.2026)* | Clarity: Aufrufe `ausbildung.html`, `pdf-flyer-ausbildung`, `cta-ausbildung` | **noch keine Historie** — Seite seit 02.09. live | Erfolgsmaß ist **nicht** die Abrufzahl, sondern **Anfragen mit Ausbildungsbezug: drei binnen zwölf Wochen**. Bei null Anfragen und ≥ 150 Aufrufen ist die Annahme widerlegt — Kriterium und Konsequenz in `BD/projects/ausbildung-und-coaching-2026/zyklus-und-experiment.md` |
| **Trägt das Prozess-Argument?** *(neu 03.09.2026)* | Clarity `link-sicherheit-prozess` | **noch keine Historie** | Der Klick zeigt, ob der standardisierte Entwicklungsablauf als *Kaufgrund* gelesen wird — wer ihn anklickt, sucht den Beleg. **Wenig Klicks widerlegen das Argument nicht** (es steht vollständig auf der Seite); viele Klicks belegen es. Erstmals im Oktober-Lauf ablesbar |
| **Beleg-Foto: trägt die Datenort-Frage?** *(neu 03.09.2026)* | Clarity `link-sicherheit-startseite`, dazu `scroll-75` auf der Startseite | **noch keine Historie** — Foto und Verweis seit 03.09. live | Die Sektion liegt im unteren Drittel; bei Ø 44,6 % Scrolltiefe sieht sie heute nur ein Teil der Besucher. **Erst `scroll-75` lesen, dann die Klicks** — wenige Klicks bei wenig Scrolltiefe widerlegen das Foto nicht, sondern zeigen, dass die Sektion zu weit unten steht. Bei `scroll-75` über ~40 % und weiterhin null Klicks ist der Verweis der falsche Weg, nicht das Bild |
| **Video: mittlere Wiedergabedauer** *(neu 02.09.2026)* | 👤 YouTube Studio, Video `RStpqzz3r5g` | — | **< 2:00 heißt: Kurzfassung schneiden** (Länge ist 4:51, Zielmarke war 2–3 Min) |
| Core Web Vitals | Clarity | 93/100 · LCP 0,44 s · INP 140 ms · CLS 0 | ✅ halten |
| GSC Klicks | 👤 GSC, Export | **60** (+253 %) bei 317 Impressionen | steigend |
| **Nicht-Marken-Klicks** | 👤 GSC, Export | **~3 von 60** (29 davon Markensuche) | steigend |

> **Beim nächsten Monatslauf zu erledigen: Messpunkte auf `leistungen.html` nachrüsten**
> *(beschlossen 03.09.2026, Stefan)*. Am 03.09. sind dort ein Anwendungsfall, drei Fragen, drei
> Abgrenzungssätze und zwei Portfolio-Bausteine dazugekommen — **ohne eigenen Messpunkt**.
> Bewusst aufgeschoben, nicht vergessen: Bei 111 Sitzungen im Monat lieferte ein Klickereignis auf
> eine einzelne Frage einstellige Zahlen, also Rauschen (§5). Zwei Dinge sind dann fällig:
>
> 1. **Scrollmarken für `leistungen.html`** — die Seite hat als einzige lange Seite **gar keine**,
>    obwohl §1 `scroll-*` als Datenquelle führt. Sie ist mobil rund 17.000 px hoch; ohne Marke ist
>    unbekannt, ob die Fragen-Sektion überhaupt erreicht wird. **Das ist die größere Lücke als die
>    fehlenden Klickmarken** und die Voraussetzung dafür, dass diese überhaupt interpretierbar sind.
> 2. **Ein Marker auf die Fragen-Sektion**, nicht acht einzelne. Ein zweiter auf die Frage
>    *„Was ist, wenn eine Sonde falsch misst?"* nur, wenn das Kapitel gezielt beworben wird —
>    per Direktlink auf `#fragen` aus einer Mail oder einem Vortrag.
>
> **Vorzuziehen ist beides, sobald die Sitzungen dauerhaft über ~300 im Monat liegen.**

> ⚠️ **September 2026 trägt keine Wirkungszuordnung** *(Stefan, 03.09.2026)*. An diesem einen Tag
> liefen fünf Änderungsrunden statt der drei erlaubten (§5 Regel 2) — Schnellanalyse, Sensorik-Block,
> Beleg-Foto, Redundanzschnitt, Bannerfix. Das war eine bewusste Entscheidung zugunsten eines
> sauberen Bestands. **Folge für den Oktober-Lauf:** Änderungen an Terminanfragen, Scrolltiefe und
> CTA-Klicks lassen sich keiner einzelnen Maßnahme zuschreiben; der Monat zählt als **neuer
> Ausgangswert**, nicht als Vergleich. Ab Oktober gilt die Dreierregel wieder.

**Ein Monatsvergleich ist erstmals Anfang Oktober möglich** — die Historie beginnt am
10.08.2026. Bis dahin sind alle Zahlen oben Ausgangswerte, keine Entwicklung. **Die Werte
stammen aus der Oberfläche, nicht aus der lokalen Historie** — Begründung im Kasten in §1.

**Clarity ist Opt-in-gated.** Gezählt wird nur, wer im Banner „Akzeptieren" klickt. Jede
Sitzungszahl hier ist eine Untergrenze unbekannter Größe; für Niveauvergleiche mit
Branchenwerten taugt sie nicht, für den Verlauf gegen sich selbst schon.

**Vergleichswerte:** B2B-Websites konvertieren im Mittel bei 2,9 %; Seiten, deren einziges
Angebot ein Gespräch ist, liegen bei 1,5–4 %; Seiten mit Selbstbedienungs-Angebot bei
4–10 %. Bei knapp 90 Sitzungen im Monat ist jede dieser Quoten allerdings noch Rauschen —
siehe nächster Abschnitt.

---

## 5. Entscheidungsregeln

**Nicht messbar heißt nicht beliebig.** Bei ~90 Sitzungen pro Monat ist kein A/B-Test
aussagekräftig; für einen belastbaren Vergleich bräuchte es etwa das Zehnfache. Daraus
folgt kein Stillstand, sondern eine andere Begründungspflicht:

1. **Beobachtete Reibung schlägt Vermutung.** Ein toter Klick, den man in der Aufzeichnung sieht, wird behoben. Eine Farbidee ohne Beleg nicht.
2. **Höchstens drei Änderungen pro Monat**, und jede mit Datum protokolliert. Mehr, und die Zuordnung im Folgemonat ist verloren.
3. **Struktur vor Formulierung.** Eine Seite ohne Conversion-Pfad ist ein Loch; eine suboptimale Button-Beschriftung ist eine Meinung.
4. **Nichts hinter Formulare sperren.** Belege werden derzeit fünfmal häufiger abgerufen als Termine gebucht — das ist der funktionierende Teil des Trichters.
5. **Marken- und Nicht-Marken-Verkehr immer getrennt bewerten.** Der Verkehr ist presse- und netzwerkgetrieben; ohne diese Trennung feiert man einen Zeitungsartikel als SEO-Erfolg.
6. **Ein Anstieg nach einem Presse- oder Messetermin ist keine Optimierungswirkung.** Erst der Sockel danach zählt.

---

## 6. Bekannte Fallstricke

> **localhost ist seit 02.09.2026 an der Quelle ausgeschlossen** — `consent.js` lädt Clarity
> nicht mehr auf `localhost`, `127.0.0.1`, `::1` oder `*.local`. **Für Daten ab diesem Tag
> entfällt das Herausrechnen.** In der Historie **davor** stecken lokale Sitzungen drin
> (belegt: `127.0.0.1:8123` und `:8140` unter den beliebtesten Seiten) — dort weiter abziehen,
> und Heatmaps und Aufzeichnungen aus dem August entsprechend vorsichtig lesen: die lassen sich
> nicht bereinigen. Befund und Beleg: [`_analytics/berichte/2026-09.md`](_analytics/berichte/2026-09.md) §2.1.

- **Der Sammler läuft fensterlos** (`pyw.exe`). Ein Fehlschlag ist deshalb **nur im Protokoll** `_analytics/_sammler.log` sichtbar. Vor jedem Monatslauf zuerst dort hineinsehen.
- **Der Task braucht einen angemeldeten Benutzer.** Er ist akkuunabhängig und holt verpasste Läufe nach (`StartWhenAvailable`) — wer den Laptop mindestens alle drei Tage benutzt, hat eine lückenlose Reihe.
- **Clarity-API: 429 bedeutet Kontingent aufgebraucht**, nicht Fehler. Kein Retry.
- **Mehr als zwei versäumte Tage sind endgültig weg.** Die Lückenerkennung reicht nur so weit wie die API — drei Tage.
- **In GSC bei 404-Gruppen nicht „Behebung validieren" klicken** — Begründung in `README.md`, Abschnitt *Search Console / Indexierung*.
- **`localhost`-Sitzungen aus den Clarity-Zahlen herausrechnen** — das sind eigene Tests, vom 10.–23.08. waren es 8 von 32. Sie sind fast alle Desktop und verzerren sonst den Geräte-Split ins Gegenteil.
- **Die Historie ist gitignored und existiert nur einmal.** `_analytics/` liegt in keinem Repo, und was älter als drei Tage ist, gibt die API nicht mehr her — ein Plattenverlust löscht sie endgültig. Seit 24.08.2026 nimmt sie der monatliche `backup_coding_config.py` als `_daten/homepage-clarity_history.jsonl` mit. **Nicht aus dem Backup-Umfang entfernen**, auch wenn sie dort als einziger Nicht-Config-Eintrag auffällt — die Begründung steht im Docstring des Skripts.

---

## 7. Auslöser: Outlook-Serientermin

Der Monatslauf hängt an einem **Outlook-Serientermin am ersten Werktag des Monats**, nicht
an einer geplanten Aufgabe. Grund: Es ist eine *erinnernde*, keine *handelnde* Aufgabe —
so hält es die Task-Registry im BD-Repo ausdrücklich fest
(`areas/compliance/working/scheduler-tasks.md`). Angelegt am 11.08.2026.

Bewusst der erste Werktag und nicht das Monatsende: Sonst fehlen die letzten Tage des
Monats in der Auswertung.

Der Termininhalt, zum Nachpflegen falls er verlorengeht:

```
HOMEPAGE-OPTIMIERUNG — Monatslauf (ca. 25 Min)

1) VORBEREITEN (10 Min) — das kann nur ich, nicht Claude

   Tote Klicks: zwei Aufzeichnungen ansehen.
   Notieren: auf WELCHES Element wurde geklickt?
   https://clarity.microsoft.com/projects/view/wql3vpgrxl/recordings

   Heatmaps für / und ueber-mich.html, je Klick + Scroll.
   WICHTIG: Mobil und Desktop getrennt umschalten (58 % kommen mobil).
   https://clarity.microsoft.com/projects/view/wql3vpgrxl/heatmaps

   NUR im Januar, Mai und September zusaetzlich (2 Min):
   Search Console -> Leistung -> letzte 28 Tage
   Filter setzen: Suchanfrage enthaelt nicht "galvano"
   Tabelle kopieren und Claude durchgeben.
   https://search.google.com/search-console/performance/search-analytics?resource_id=https%3A%2F%2Fsecure-galvano-ai.com%2F
   Warum nur dreimal im Jahr: der Verkehr ist presse- und netzwerkgetrieben,
   Suchdaten aendern sich zu langsam fuer einen Monatsrhythmus. Ein API-Zugang
   dafuer ist bewusst verworfen (Abschnitt 2).

2) DIE EINE ZAHL (2 Min)

   Terminanfragen im abgelaufenen Monat zählen — Bookings + Mail-Eingang.
   Auch wenn es 0 ist: 0 ist ein Ergebnis, kein fehlender Wert.

3) AUSWERTEN

   Claude Code im Ordner Coding öffnen, eingeben:

   /optimierung

   Danach die Notizen aus 1) und die Zahl aus 2) durchgeben.
   Ergebnis: Bericht unter homepage/_analytics/berichte/
   plus maximal 3 Änderungsvorschläge.

REGEL: Höchstens 3 Änderungen pro Monat. Mehr lässt sich im Folgemonat
nicht mehr auseinanderhalten — dann weiß niemand, was gewirkt hat.

WENN ETWAS KOMISCH AUSSIEHT: zuerst in homepage/_analytics/_sammler.log
schauen. Dort steht je Tag eine Zeile. Fehlen Tage, war der Laptop aus.
```
