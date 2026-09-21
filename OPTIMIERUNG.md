# Monatlicher Optimierungs-Prozess

Ziel: **Terminanfragen erhöhen.** Alles andere (Klicks, Impressionen, Scrolltiefe) ist
Diagnose, kein Ziel. Rhythmus: **einmal im Monat, am zweiten Werktag**, für den abgelaufenen
Kalendermonat — als **Block 3 des Monatslaufs** (§7).

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
Befund seit 07.09.2026 auf SharePoint unter `01_LinkedIn/00_LIESMICH_Reichweite-und-Serie.md`
(das BD-Projekt `projects/linkedin-auftritt/` ist aufgeloest); hier steht nur, ob ein Beitrag
Verkehr auf die Seite gebracht hat.

> **Rhythmus entschieden am 15.09.2026: monatlich, in diesem Lauf — kein zweiter Termin.**
> Vorher stand im Beitragsprozess „bei Bedarf, etwa vierteljährlich". Das war richtig, solange
> Content Zweitverwertung war; seit dem 02.09.2026 ist er der Motor, und ein Kanal, der den
> Umsatz tragen soll, wird nicht dreimal im Jahr angesehen. **Monatlich ist zugleich die
> Obergrenze des Sinnvollen** — bei vier bis acht Beiträgen im Monat ist ein kürzerer Takt
> Rauschen (§5), und die 7-Tage-Werte des Dashboards zeigen genau das.
>
> **Was Stefan bleibt: der Export selbst** (2 Minuten, verlangt eine angemeldete Sitzung) und
> die vier Dashboard-Zahlen, die im Export fehlen. **Alles danach übernimmt ein Befehl:**
> ```
> py "Business Development/scripts/linkedin_abholen.py"
> ```
> Er holt die Datei aus dem Download-Ordner, benennt sie nach der Ablagekonvention, legt sie
> neben die alten Exporte auf SharePoint, fährt die Auswertung und räumt das Original weg.
> **Kein Task Scheduler** — an 29 von 30 Tagen gäbe es nichts abzuholen.
>
> **Zusätzlich, außer der Reihe:** nach **drei** ausgespielten Teilen einer neuen Serie
> (Beitragsprozess §7 Nr. 4). Das ist der Punkt, an dem sich Nachbessern noch lohnt.

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

### Wöchentlich *(neu 18.09.2026)*

Geplante Aufgabe `\SecureGalvano\Homepage Wochenbericht` (montags 09:20, fünf Minuten nach
dem Tages-Pull, damit der Sonntag schon in der Historie steht) rechnet die abgelaufene
Kalenderwoche aus der **bereits vorhandenen** Historie: `_scripts/wochenbericht.py`.
**Kein API-Aufruf** — der Bericht lässt sich beliebig oft und für jede vergangene Woche neu
rechnen (`py _scripts/wochenbericht.py --woche 2026-W37`). Die vorgeschaltete Aktion
`youtube_abrufe.py` holt die Video-Zählerstände, sonst stünde in der Video-Tabelle dauerhaft
„Erststand" statt eines Wochenzuwachses.

**Ablage:** `_analytics/wochen/<JJJJ>-W<NN>.md` (Langfassung) und `Desktop\HOMEPAGE-WOCHE.md`
(zwölf Zeilen, wird jede Woche überschrieben).

**Für die Frage „wird es mehr?“:** `py _scripts/wochenbericht.py --gesamt` schreibt
`_analytics/wochen/GESAMTVERLAUF.md` — alle gemessenen Wochen, die stärksten Einzeltage mit
ihrem Anteil am Gesamtverkehr, und jeder externe Verweis seit Beginn der Historie.
**Die Antwort auf die Verkehrsfrage steht damit trotzdem nur zur Hälfte da** (siehe Kasten).

> **Der Wochenbericht entscheidet nichts — er überwacht.** Bei rund 20 Sitzungen je Woche ist
> jede Differenz zur Vorwoche Rauschen; §5 sagt das schon für Monatswerte, und ein Wochenwert
> ist ein Viertel davon. Der Bericht schreibt diese Warnung selbst in seine erste Zeile,
> solange er unter 30 Sitzungen liegt. **Was er kann und der Monatslauf zu spät sieht:**
> Sammler-Lücken (über die API nach drei Tagen endgültig verloren), einen Ausreißertag, der
> noch eine Erklärung hat, und einen neu auftauchenden externen Verweis. **Trendgröße ist der
> rollierende Vierwochenwert**, nicht die einzelne Woche.

**Zwei Dinge rechnet er bewusst anders als die Rohdaten:** `/` und `/index.html` werden als
eine Seite gezählt, und Verweise von der eigenen Domain stehen getrennt als *interne
Seitenwechsel* — ungetrennt sähe eine Woche ohne jeden externen Zulauf gut besucht aus.
Drei-Tage-Fenster aus Lückenläufen bleiben außen vor, weil sie sich überlappen.

### Monatlich

> **Wie eine Aenderung ablaeuft, steht in [`AENDERUNGSPROZESS.md`](AENDERUNGSPROZESS.md)** *(seit 31.08.2026)*. Dieses Dokument hier fuehrt den **Messlauf** — was gemessen wird und welche Entscheidungsregeln gelten. Merksatz: hier steht, **was ist**; dort steht, **wie geaendert wird**.

**Der Ablauf steht im Skill** [`.claude/skills/optimierung/SKILL.md`](../.claude/skills/optimierung/SKILL.md)
und wird mit `/optimierung` gestartet. Er ist bewusst nur dort beschrieben — stünde er
zusätzlich hier, würden die beiden Stände auseinanderdriften.

Die Arbeitsteilung in einem Satz: Claude liest die Historie, rechnet den Funnel durch und
schreibt den Bericht; 👤 Stefan liefert die drei Angaben, die in keiner Schnittstelle
stehen — **Terminanfragen**, das Element hinter den toten Klicks, und die
Heatmap-Auffälligkeiten mobil wie Desktop.

Auslöser ist der Monatslauf am zweiten Werktag des Monats (§7).

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
| **Demo-Seite: Zulauf und Weiterweg** *(neu 02.09.2026)* | Clarity `link-*` und `cta-demo-seite` | **12 Besuche vom 02.–17.09., davon 6 am Veröffentlichungstag** *(Stand 18.09.2026)* — danach an vier einzelnen Tagen je einer | **Veröffentlichungseffekt ohne Sockel** (Regel 6). Kein Grund, am Video zu arbeiten: Bei drei Website-Besuchern am Tag erzeugt kein Video Zulauf. Konsequenz ist die **Verwendung** — Link in Nachfass und Telefonat. Vollständiger Befund im Funnel-Dokument auf SharePoint §8a |
| **Demo-Einseiter: Weitergabe im Haus** *(neu 02.09.2026)* | Clarity `pdf-anwendung-demo` | **noch keine Historie** | erstmals im Oktober-Lauf ablesbar. Er misst etwas anderes als die übrigen `pdf-*`: nicht Interesse, sondern die Absicht, die Sache **intern weiterzureichen** — Abrufe ohne Terminanfrage sind hier kein Fehlschlag |
| **Datenwerkstatt-Seite: trägt das Angebot?** *(neu 02.09.2026)* | Clarity: Aufrufe `ausbildung.html`, `pdf-flyer-ausbildung`, `cta-ausbildung` | **noch keine Historie** — Seite seit 02.09. live | Erfolgsmaß ist **nicht** die Abrufzahl, sondern **Anfragen mit Ausbildungsbezug: drei binnen zwölf Wochen**. Bei null Anfragen und ≥ 150 Aufrufen ist die Annahme widerlegt — Kriterium und Konsequenz in `BD/projects/ausbildung-und-coaching-2026/zyklus-und-experiment.md` |
| **Trägt das Prozess-Argument?** *(neu 03.09.2026)* | Clarity `link-sicherheit-prozess` | **noch keine Historie** | Der Klick zeigt, ob der standardisierte Entwicklungsablauf als *Kaufgrund* gelesen wird — wer ihn anklickt, sucht den Beleg. **Wenig Klicks widerlegen das Argument nicht** (es steht vollständig auf der Seite); viele Klicks belegen es. Erstmals im Oktober-Lauf ablesbar |
| **Beleg-Foto: trägt die Datenort-Frage?** *(neu 03.09.2026)* | Clarity `link-sicherheit-startseite`, dazu `scroll-75` auf der Startseite | **noch keine Historie** — Foto und Verweis seit 03.09. live | Die Sektion liegt im unteren Drittel; bei Ø 44,6 % Scrolltiefe sieht sie heute nur ein Teil der Besucher. **Erst `scroll-75` lesen, dann die Klicks** — wenige Klicks bei wenig Scrolltiefe widerlegen das Foto nicht, sondern zeigen, dass die Sektion zu weit unten steht. Bei `scroll-75` über ~40 % und weiterhin null Klicks ist der Verweis der falsche Weg, nicht das Bild |
| **Video-Abrufe** *(neu 10.09.2026)* | `py _scripts/youtube_abrufe.py` → `_analytics/youtube_history.jsonl`; seit 18.09. wöchentlich über den Wochenbericht-Task | **16** Anwendung · **29** Pitch · **51** Prozessdatenauswertung *(Stand 18.09.2026)* — in acht Tagen **+1 / +5 / ±0** | **Die Zeitreihe wird hier nicht gepflegt**, jede Ablesung kommt datiert ins Funnel-Dokument auf SharePoint §8a. Das Demo-Video flacht nach dem Start ab, das ältere Pitch-Video wächst schneller |
| **Video: mittlere Wiedergabedauer** *(neu 02.09.2026)* | 👤 YouTube Studio, Video `RStpqzz3r5g` — **steht in keiner offenen Quelle**, nur mit Anmeldung | — | **< 2:00 heißt: Kurzfassung schneiden** (Länge ist 4:51, Zielmarke war 2–3 Min) |
| Core Web Vitals | Clarity | 93/100 · LCP 0,44 s · INP 140 ms · CLS 0 | ✅ halten |
| GSC Klicks | 👤 GSC, Export | **60** (+253 %) bei 317 Impressionen | steigend |
| **Nicht-Marken-Klicks** | 👤 GSC, Export | **~3 von 60** (29 davon Markensuche) | steigend |

### LinkedIn *(neu 15.09.2026 — §1 führt den Kanal seit 31.08., Kennzahlen fehlten)*

Quelle für alle Zeilen: XLSX-Export → `Business Development/scripts/analyse_linkedin.py`,
Befund unter `01_LinkedIn/Analytics-Exporte/` auf SharePoint. **Zwei Werte stehen nur im
Dashboard** und sind mit 👤 markiert — sie sind nicht im Export enthalten.

| Kennzahl | Stand 18.06.–15.09.2026 (90 Tage) | Richtung |
|---|---|---|
| **Profilbesuche / 90 Tage** 👤 | **299 (+219 %)** | **die Leitzahl** — wer das Profil öffnet, prüft die Person. Der Schritt unmittelbar vor dem Anruf |
| **Impressionen je Beitrag, Anlassbeitrag** | **511** (Median, stabil seit 12 Monaten) | ≥ 500 halten |
| **Impressionen je Beitrag, Serienbeitrag** | **199** (166 und 232) | **→ 400.** Darunter trägt die Serie den Kanal nicht, sie verdünnt ihn |
| Beiträge je Monat | **5** (Aug und Sept) | 4–8; unter 4 drosselt die Verteilung, über 8 fällt die Wirkung je Beitrag |
| Neue Follower je Monat | **65–84** | ≥ 60 |
| Engagement-Rate | **2,4 %** (Jahreswert 2,6 %) | ≥ 2,5 % |
| **Zielkonten im Publikum** | **Collini 5 % · SurTec 5 %** | halten — das ist der eigentliche Zweck des Kanals |
| **Kommentare unter fremden Beiträgen** 👤 | **2 / Woche** | **≥ 1 / Woche** — LinkedIn selbst nennt bis zu **3× mehr Profilaufrufe** für wöchentliches Kommentieren; im Export nicht enthalten, nur im Wochenfortschritt sichtbar |
| In Suchen erschienen 👤 | 51 (±0 %) | steigend |
| Impressionen / 7 Tage 👤 | 780 (**−27 %**) | **Diagnose, kein Ziel** — der Wochenwert misst, was gepostet wurde, nicht was daraus wurde. Nie danach steuern |
| Verkehr von LinkedIn auf die Seite | erstmals im Oktober-Lauf trennbar (UTM seit 15.09.) | — |

> **Nur diese Tabelle wird monatlich nachgezogen — sonst keine Stelle** *(15.09.2026)*. Dieselben
> Zahlen stehen mit Absicht auch in `brand/messaging.md` § 5b, `marketing.md` und der
> `verwertungskalkulation.md` — dort aber **als datierter Befund**, nicht als laufender Wert.
> Ein Befund mit Stand-Datum bleibt dauerhaft richtig und braucht keine Pflege; er beschreibt,
> was damals gemessen wurde. **Wer ihn trotzdem nachzieht, erzeugt genau die Drift, die er
> verhindern will.** Aktualisiert wird hier — und nur, wenn sich die Aussage ändert, wandert eine
> neue datierte Zeile in die anderen Dokumente.

> **Die Dashboard-Prozente vergleichen uneinheitliche Zeiträume.** „299 Profilbesuche in 90 Tagen,
> +219 % gegenüber den 7 vorausgegangenen Tagen" ist so, wie LinkedIn es anzeigt — Bezugsgröße und
> Fenster passen nicht zusammen. **Als Richtungsangabe brauchbar, nicht als Messwert**; belastbar
> ist nur der Vergleich zweier Exporte.

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
7. **Auf LinkedIn Anlass- und Serienbeiträge nie gemeinsam mitteln** *(neu 15.09.2026)*. Dasselbe Muster wie Regel 5: Die beiden Sorten liegen um den Faktor 2,5 auseinander (511 gegen 199), und ihr Mischungsverhältnis schwankt von Monat zu Monat. Ein gemeinsamer Median zeigt deshalb Bewegungen an, die es nicht gibt — im September sah es nach einem Reichweiteneinbruch von 555 auf 386 aus, während die Anlassbeiträge punktgenau ihr Niveau hielten. **Wer beide Werte nicht getrennt hat, hat keine Aussage.**

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

## 7. Auslöser: Block 3 des Monatslaufs

Der Lauf hat seit **21.09.2026 keinen eigenen Serientermin mehr**. Er ist **Block 3** des
Outlook-Serientermins *„Monatslauf — Buchhaltung, Liquidität, Homepage, Sicherheit"*,
**2. Werktag des Monats, 09:00–12:00**; dort sind sechs monatliche Erinnerungen auf zwei
zusammengelegt worden *(Stefan, 21.09.2026)*. Reihenfolge und Übergänge stehen im Skill
`.claude/skills/monatslauf/SKILL.md`, der Termintext kanonisch in
`business-development/areas/buchhaltung/ARBEITSANWEISUNG.md` (Anhang *Termintexte*).

Unverändert: Es ist eine *erinnernde*, keine *handelnde* Aufgabe — deshalb Kalendertermin und
**kein** Eintrag in der Task-Registry (`areas/compliance/working/scheduler-tasks.md`).

**Zweiter Werktag, nicht Monatsende** — sonst fehlen die letzten Tage des Monats in der
Auswertung. *(Diese Datei nannte bis 21.09.2026 den **ersten** Werktag; der Kalendereintrag
stand tatsächlich schon immer auf dem zweiten — Serienmuster „2. Wochentag Mo–Fr". Am Zeitraum
ändert das nichts, der Vormonat ist an beiden Tagen vollständig.)*

**Ein Prompt startet alles:** `/monatslauf` fährt die vier Blöcke der Reihe nach. Wird nur
dieser Teil nachgeholt, tut es `/optimierung` allein.

Der Teil des Termintextes, der diesen Block betrifft — zum Nachpflegen, falls er verlorengeht
(vollständig steht er in der SOP im BD-Repo):

```
HOMEPAGE-OPTIMIERUNG — Block 3 des Monatslaufs (ca. 25 Min)

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

   LINKEDIN — Export ziehen (2 Min, seit 15.09.2026 fester Bestandteil):
   https://www.linkedin.com/analytics/creator/content/
   Zeitraum auf 365 Tage, oben rechts "Exportieren". Datei im Download-Ordner liegen lassen.
   Danach auf der Uebersichtsseite vier Zahlen abschreiben, die im Export FEHLEN:
   Profilbesucher 90 Tage, Impressionen 7 Tage, "in Suchen erschienen",
   Kommentare aus dem Woechentlichen Fortschritt.
   Ablegen und auswerten macht Claude in Schritt 3 mit einem Befehl.

2) DIE EINE ZAHL (2 Min)

   Terminanfragen im abgelaufenen Monat zählen — Bookings + Mail-Eingang.
   Auch wenn es 0 ist: 0 ist ein Ergebnis, kein fehlender Wert.

3) AUSWERTEN — im Monatslauf läuft dieser Block automatisch mit

   Claude Code im Ordner Coding öffnen, eingeben:

   /monatslauf     (alle vier Blöcke des Vormittags)
   /optimierung    (nur diesen Block, wenn er nachgeholt wird)

   Danach die Notizen aus 1) und die Zahl aus 2) durchgeben.
   Ergebnis: Bericht unter homepage/_analytics/berichte/
   plus maximal 3 Änderungsvorschläge.

REGEL: Höchstens 3 Änderungen pro Monat. Mehr lässt sich im Folgemonat
nicht mehr auseinanderhalten — dann weiß niemand, was gewirkt hat.

WENN ETWAS KOMISCH AUSSIEHT: zuerst in homepage/_analytics/_sammler.log
schauen. Dort steht je Tag eine Zeile. Fehlen Tage, war der Laptop aus.
```
