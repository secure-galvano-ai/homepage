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

**Die entscheidende Einschränkung:** Die Clarity-API liefert nur die letzten drei Tage.
Wer einmal im Monat abfragt, hat 27 Tage unwiederbringlich verloren — die Daten sind über
die API danach nicht mehr erreichbar. Deshalb läuft ein **täglicher Sammler**
(`_scripts/clarity_daily.py`), der die Historie lokal aufbaut. Das ist keine Bequemlichkeit,
sondern die einzige Möglichkeit, überhaupt an einen Monatsverlauf zu kommen.

**Was dauerhaft manuell bleibt:** Heatmaps und Sitzungsaufzeichnungen. Die API kennt die
*Anzahl* toter Klicks, nicht das *Element*. Das sind 👤 ~10 Minuten pro Monat und der Teil
mit dem höchsten Erkenntniswert — nicht wegrationalisieren.

---

## 2. Zugänge und Geheimnisse

| Was | Wo | Erneuern |
|---|---|---|
| Clarity-API-Token | `.env` im Repo-Wurzelverzeichnis, Schlüssel `CLARITY_API_TOKEN` — **gitignored** | Clarity → Einstellungen → Datenexport → *Neues API-Token generieren* (nur Projektadmin) |
| — (kein GSC-Zugang eingerichtet) | Entscheidung 11.08.2026: der API-Zugang lohnt den Aufwand nicht | — |
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

| Kennzahl | Woher | Aktuell (Juli/Aug 2026) | Richtung |
|---|---|---|---|
| **Terminanfragen** | 👤 Bookings + Mail | ~0–1 | steigend |
| CTA-Klicks je Position | Clarity `data-funnel` | 1 gesamt | steigend |
| Beleg-Abrufe (PDF/Video) | Clarity `pdf-*`, `video-*` | ~10 | steigend |
| Sitzungen | Clarity | 95 (88 ohne localhost) | steigend |
| Scroll ≥ 25 % | Clarity `scroll-25` | 55 % | > 70 % |
| Tote Klicks | Clarity Einblicke | 15,8 % | < 5 % |
| Nicht-Marken-Klicks | GSC, manuell | ~25 von 47 (Aug 2026) | steigend |

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

- **Der Sammler läuft fensterlos** (`pyw.exe`). Ein Fehlschlag ist deshalb **nur im Protokoll** `_analytics/_sammler.log` sichtbar. Vor jedem Monatslauf zuerst dort hineinsehen.
- **Der Task braucht einen angemeldeten Benutzer.** Er ist akkuunabhängig und holt verpasste Läufe nach (`StartWhenAvailable`) — wer den Laptop mindestens alle drei Tage benutzt, hat eine lückenlose Reihe.
- **Clarity-API: 429 bedeutet Kontingent aufgebraucht**, nicht Fehler. Kein Retry.
- **Mehr als zwei versäumte Tage sind endgültig weg.** Die Lückenerkennung reicht nur so weit wie die API — drei Tage.
- **In GSC bei 404-Gruppen nicht „Behebung validieren" klicken** — Begründung in `README.md`, Abschnitt *Search Console / Indexierung*.
- **`localhost`-Sitzungen aus den Clarity-Zahlen herausrechnen** — das sind eigene Tests, im August waren es 7 von 95.

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
