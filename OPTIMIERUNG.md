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
| **Search Console API** (MCP) | 16 Monate, Suchanfrage/Seite/Gerät/Land, URL-Inspektion | ✅ vollständig | Wie Leute ankommen |
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
| Google-OAuth (GSC) | `~/.gsc-mcp/` außerhalb des Repos | Bei „invalid_grant" neu autorisieren |
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
Geplante Aufgabe `\SecureGalvano\Clarity Daily Pull` ruft jeden Morgen
`py homepage/_scripts/clarity_daily.py` auf und hängt den Tagesstand an
`homepage/_analytics/clarity_history.jsonl` an (gitignored, Duplikate werden über
`date`+`metric`+`dimensions` verworfen). Bei HTTP 429 bricht das Skript sauber ab —
kein Retry, sonst ist das Tageskontingent weg.

### Monatlich — Claude allein
1. `clarity_history.jsonl` einlesen, Vormonat gegen Vormonat davor stellen
2. Über den GSC-MCP ziehen: Suchanfragen, Seiten, Geräte, jeweils Klicks/Impressionen/CTR/Position
3. Markenanfragen (`secure galvano`, `galvano ai`, `stefan maier`) getrennt von Nicht-Marke auswerten — sonst überdeckt der Namensverkehr alles
4. Funnel gegenrechnen: Sitzungen → Scroll 25/50/75 → PDF/Video → CTA-Klick, je Position
5. Seiten ohne Conversion-Pfad prüfen (grep auf `data-funnel` je HTML-Datei)
6. Abweichungen und Hypothesen in `_analytics/berichte/JJJJ-MM.md` schreiben

### Monatlich — 👤 Stefan (~15 Minuten)
7. [Heatmaps](https://clarity.microsoft.com/projects/view/wql3vpgrxl/heatmaps) für `/` und `ueber-mich.html`, je Klick + Scroll, **Mobil und Desktop getrennt** (Mobilanteil liegt bei ~58 %)
8. Unter *Einblicke → Tote Klicks* zwei Aufzeichnungen ansehen und notieren, **auf welches Element** geklickt wurde
9. Terminanfragen aus Bookings + Mail-Eingang zählen — das ist die einzige Zahl, die zählt, und sie steht in keinem Analysewerkzeug

### Monatlich — gemeinsam
10. Claude schlägt maximal **drei** Änderungen vor, mit Begründung und erwarteter Wirkung
11. 👤 Stefan gibt frei, Claude setzt um, Commit über `/commit`
12. Änderung im Monatsbericht mit Datum vermerken — sonst ist im Folgemonat nicht zuordenbar, was gewirkt hat

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
| Nicht-Marken-Klicks | GSC | ~25 von 47 | steigend |

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

- **MCP lädt nur beim Sitzungsstart.** Nach jeder Änderung an `.mcp.json` eine neue Claude-Sitzung starten, sonst fehlt der Server kommentarlos.
- **Unter Windows `node <cli.js>` statt `npx`** — der `npx.cmd`-Shim bricht die stdio-Pipes (`-32000`).
- **`claude mcp list` „✓ Connected" trügt** — die CLI ist nicht die VSCode-Erweiterung.
- **Clarity-API: 429 bedeutet Kontingent aufgebraucht**, nicht Fehler. Kein Retry.
- **Verpasste Tage sind endgültig weg.** Läuft der Sammler länger als drei Tage nicht, klafft eine Lücke in der Historie, die niemand mehr füllen kann.
- **In GSC bei 404-Gruppen nicht „Behebung validieren" klicken** — Begründung in `README.md`, Abschnitt *Search Console / Indexierung*.
- **`localhost`-Sitzungen aus den Clarity-Zahlen herausrechnen** — das sind eigene Tests, im August waren es 7 von 95.
