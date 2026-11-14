# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.com
**HTTPS:** Aktiv (GitHub Pages + Let's Encrypt)
**Hosting:** GitHub Pages (kostenlos)
**Stand:** 2026-11-08

---

## Stand der Website

Grundausstattung steht seit Mai 2026 (eigene Domain mit HTTPS, Impressum/Datenschutz, Bookings,
Open Graph, Sitemap, Search Console, JSON-LD, self-hosted Fonts, Clarity mit Opt-in-Consent);
Aufbau der Seiten: § *Projektstruktur*. Änderungsverlauf im `git log`, Wirkung jeder Änderung im
Monatsbericht ([`OPTIMIERUNG.md`](OPTIMIERUNG.md) §4, monatlich per `/optimierung`).

**Offen in der Wirkungsmessung (November-Lauf):**
- **`#belege` direkt unter dem Hero, vor dem Pitch-Video** *(Stefan, 28.09.2026)*. Anlass: Clarity
  August 111 Sitzungen, 0 CTA-Klicks, Startseite mobil nur zu 5 % bis zum Ende gelesen
  (`BD/archive/akquise-strategie-h2-2026-in-areas-2026-10/benchmark-werchota.md` §4 Nr. 4).
  Ablesen: CTA-Klicks, mobile Scrolltiefe.
- **`#bestand` „Ihre Anlage muss nicht neu sein"** *(Stefan, 02.10.2026)* samt Gegenstücken auf
  `leistungen.html` und `ausbildung.html` — Kennzahl in `OPTIMIERUNG.md` §4.
- **Für den Optimierungslauf nach dem Messpunkt 01.12.2026 vorgemerkt** *(Befund 21.10.2026; bis
  dahin zurückgestellt, damit der Versuch vom 03.11. zuordenbar bleibt)*: Startseite von zehn auf
  rund sechs Abschnitte (Kandidaten: Pitch-Video, „Aktuell" mit Rückblick vom 29.09., „So
  funktioniert's"; „Partner" bleibt wegen der gegenseitigen Verlinkung) und „Sicherheit" statt
  „Forschung" im Hauptmenü — nur mit Clarity-Beleg, höchstens drei Änderungen.
- **Versuch „Angebote und Hauptaufruf“ seit 03.11.2026** *(Clarity-Befund 28 Tage, Stefan: mehr Klicks
  und Ersttermine)*: zwei Startkarten mit sichtbarem Buchungsknopf, je Angebot nur der Beispiel-Befund,
  zwei Wege darunter; derselbe Hauptaufruf oben und unten auf Leistungen, Über mich, Demo; mobiler
  Sticky-CTA auf allen Inhaltsseiten außer `sicherheit.html` (lädt `site.js` nicht). Messpunkt
  01.12.2026, Bezugsgrößen in `OPTIMIERUNG.md` §4.

### Regeln, die dauerhaft gelten

- **Förderlogos erst mit dem Förderungsvertrag** *(Stefan, 25.09.2026)*. Ein Logo in der
  Trust-Bar liest sich als „gefördert durch", egal was daneben steht. Solange ein Ansuchen in
  Begutachtung ist, steht es nur als Text auf `forschung.html` mit ehrlichem Status — dort ist
  das FFG-Kleinprojekt „ML Galvanik" bewusst **ohne Verfahren** (was gemacht wird, nicht wie) und
  ohne Datengeber beschrieben. Offen: FFG-Logo, Wiedervorlage in
  `BD/projects/ffg-kleinprojekt-2026/README.md` § *Termine*.
- **Partner stehen im Streifen „Partner" am Fuß der Startseite — nicht im Thema und nicht in
  der Trust-Bar** *(Stefan, 21.10.2026)*. Anlass: Ein Block „In Zusammenarbeit mit" direkt hinter
  dem eigenen Lernwerkzeug auf `ausbildung.html` las sich für den Partner wie eine Mitarbeit an
  unserem Projekt. Der Streifen `#partner` (DE `index.html`, EN `en/index.html`, zwischen FAQ und
  Abschluss) trennt beides: **eigenes Wort „Partner" gegen „Gefördert durch", eigener Platz,
  eigene Optik** — flaches Logo im weißen Feld, ein Satz je Partner, alphabetisch, kein Beleg-Kontext.
  - **Jeder Satz sagt, dass der Partner eigenständig ist** („eigenständig betrieben", „run
    independently"). Keine Personennamen: Wer dort als Mensch steht, wirkt wie Personal.
  - **Logo nur vom Partner selbst oder von seinem eigenen Auftritt**, verkleinert und ohne
    Metadaten nach `assets/img/kooperation/`; Feld 160×60 px. `flex-shrink` gehört an den Link,
    nicht ans Bild — sonst quetscht der Textabsatz das Logo (21.10.2026: 58 statt 160 px).
  - **Das Feld ist für jeden Partner gleich groß, das Logo darin behält sein Seitenverhältnis**
    (`object-fit: contain`). Zwei Wortmarken haben selten dasselbe Format — eine feste Höhe am
    Bild zerrt die flachere in die Höhe (22.10.2026: 4:1 wäre auf 8:3 gezogen worden). Dateibreite
    dreifach (480 px), als Palettenbild gespeichert: ein Viertel des Gewichts bei gleicher
    Darstellung (28 → 6 KB).
  - Keine Partner-Begründung in Kommentaren oder Commits (Repo ist öffentlich).
- **Presse (`#aktuell`): maximal zwei Karten, veraltete ersetzen statt stapeln.** Eine sichtbar
  veraltete News-Sektion schadet mehr als keine. Eine Termin-Karte wird nach dem Termin getauscht
  (KI Days: seit 06.10.2026 Rückblick statt Ankündigung).
- **Keine Team-Sektion, keine Rollen-Kacheln, kein „wir".** Die Firmierung ist ein
  Einzelunternehmen — eine dargestellte Unternehmensstruktur wäre eine Irreführung über die
  Identität des Vertragspartners (Linie OLG München 6 U 1888/13 zur vorgetäuschten größeren
  Struktur). Fotos mit weiteren Personen sind trotzdem erlaubt, wenn sie einen **Anlass**
  dokumentieren statt eine Struktur: datierte Bildunterschrift, echter Termin, Freigabe der
  Abgebildeten. Vorbild ist das aws-Jurytermin-Foto auf `forschung.html` (17.08.2026).
  Die Kundensorge dahinter — „was, wenn der ausfällt?" — beantwortet kein Teamfoto, sondern ein
  benannter Mechanismus (Haftpflicht, Doku beim Kunden, Software läuft ohne ihn; § *Optional*).
- **„Lokale Datenverarbeitung", nicht „Ihre Daten bleiben bei Ihnen"** *(Stefan, 02.09.2026)* —
  der Wortlaut ist seitenübergreifend identisch: Startseiten-H2, Vertrauenszeile auf `demo.html`,
  Baustein *Laufende Überwachung* auf `leistungen.html`. Das Beleg-Foto in
  `#lokale-datenverarbeitung` (Entwicklungsrechner, Abgrenzung *Entwicklungsumgebung ≠ Hosting*)
  hat sein Gegenstück auf `leistungen.html` § *Was passiert mit unseren Daten?* — dort sichtbarer
  Text **und** FAQ-Schema gemeinsam ändern. Begriff nach außen: „Auswertung lokal, keine
  KI-Cloud, Übergabe verschlüsselt" (statt „kein Cloud-Upload", 03.09.2026).
- **Neue Seite? Den `preload`-Block für die Schriften mitkopieren.** Ohne ihn starten die
  Schriften erst, nachdem `fonts.css` geparst ist; der `font-display:swap`-Wechsel von Arial
  auf Montserrat/Open Sans verschiebt dann den Seitenkopf. Auf der Startseite waren das
  **CLS 0,153** bei einer Google-Grenze von 0,1 (gemessen 24.08.2026; mit Preload und
  WebP-Portrait: CLS 0, 997 → 467 KB). Das `crossorigin` am Preload-Link ist Pflicht, auch bei
  eigener Domain — fehlt es, lädt der Browser jede Schrift zweimal. Prüfen mit `check_site.py`
  und im Netzwerk-Protokoll: jede `woff2` genau einmal.
- **Urheberrecht:** nur Kurzzitate mit Quellenangabe. **Keine VN-Fotos, kein VOL.AT-Logo als Bild**,
  kein selbst gehosteter Volltext — Nachdruckrechte liegen bei Russmedia/VN. Der VOL.AT-Artikel
  steht hinter einer Bezahlschranke, deshalb verlinken wir die WISTO-Fassung. Kaeme eine
  Verlagsfreigabe, ersetzt sie diesen Link — nicht stapeln.
- **Angebote seit 03.11.2026: zwei Startangebote, zwei Wege** *(Stefan; kanonisch
  `BD/areas/kundenprozess.md` § Zwei Pfade)*: Erstgespräch (kostenlos) → Standortanalyse **oder**
  Erstanalyse (je 1.500 €, nur diese beiden prominent als Karte). Danach **Weg A · Fehlerbild**:
  **Fehlerursachenanalyse mit Demo-Werkzeug** (5.000 € je Fehlerbild, nach positiver Standort- oder
  Erstanalyse; Anker `#analyse-je-fehlerbild`, dort auch `#datenanalyse`, `#danach`) → **Einführung in den Betrieb**
  (nach Aufwand; `#einfuehrung`, `#ki-setup-check`, `#betreuung`), Betreuung je Anlage nur als
  Halbsatz. Oder **Weg B · KI-Anwendungsfall mit Ihrer eigenen KI** (nur nach der Standortanalyse):
  **KI-Fahrplan** (5.000 € für bis zu drei Anwendungsfälle: Machbarkeit, Kosten-Nutzen-Einschätzung,
  Fahrplan; `#ki-fahrplan`) → Arbeitsabläufe aufbauen und Mitarbeitende schulen (nach Aufwand).
  **Nicht mehr beworben:** die Begleitung der Fehlerbehebung (Absatz „Und danach?" und Abschnitt
  `#danach` entfallen), Training als eigenes Angebot. EN: *Path A – Defect pattern*, *Path B – AI
  use case with your own AI*, *AI Roadmap*, *Build workflows and train your team*. **Grundvoraussetzung** (gleicher Tag): Messwerte in einem
  Datenbanksystem, nicht in Excel-Tabellen; fehlt das, begleiten wir die Partnerwahl und den
  Aufbau der Aufzeichnung (nach Aufwand) — steht in beiden FAQ, bei Standort- und Erstanalyse und
  in `#bestand`. Abgelöst: das **KI-Basis-Setup** (9.900 €, 22.10.–03.11.2026) und die
  **Datenwerkstatt** als Angebot. `ausbildung.html` bleibt nur für alte direkte Links stehen:
  `noindex`, nicht in Nav, Fuß, Sitemap, `llms.txt`, kein Verweis von anderen Seiten; die PDFs
  `ki-setup-check-*`/`datenwerkstatt-*` liegen unverlinkt in `docs/`.
- **Tracking-Konvention:** je CTA-Position ein eigener Event-Name (`cta-nav`, `cta-hero`,
  `cta-ablauf`, `cta-abschluss`, `cta-sticky`, `cta-whatsapp-fab`, `mail-abschluss`), Downloads als
  `pdf-<dateiname>`. **Keine generischen Selektoren** — die haben die Zahlen einmal verdoppelt
  (erster Optimierungslauf 10.08.2026: jeder CTA war doppelt verdrahtet).
- **Bei Abweichungen zwischen Website und Angebotsvorlage gilt die Website** *(Stefan, 17.08.2026;
  Anlass: Laufzeit „innerhalb einer Woche" gegen acht Wochen in `BD/areas/business-model.md`)*.
  Preise kanonisch in `BD/areas/preise.yaml`, ausgegeben mit `py "Business Development/scripts/preise.py"`.
- **Anschrift, Buchungslink, Telefon, UID und Gruendungsdatum kommen aus `BD/areas/stammdaten.yaml`**
  *(seit 24.09.2026)*. Die Seiten sind statisches HTML und lesen die Datei nicht selbst —
  `py "Business Development/scripts/check_konsistenz.py"` meldet jede Seite, die eine abgeloeste
  Fassung traegt (alte Anschrift, Sammel-Buchungsseite, falsches Gruendungsdatum).
- **Beim Umbenennen oder Nachziehen einer Zahl `grep` über *alle* Seiten laufen lassen, nicht nur
  über die, die man gerade umbaut** — inklusive `<meta>`-Beschreibungen, `og:`-Tags und `en/`.
  Anlass: Nach der Umbenennung der Stufe „Diagnose" (31.08.2026, `BD/areas/business-model.md`
  §*Leiter*) stand das alte Wort bis 03.09.2026 noch viermal auf `sicherheit.html` und `ueber-mich.html`,
  wo niemand nachsieht. Dasselbe beim Einsparpotenzial **60.000–90.000 €**: die seit 15.09.2026
  abgelöste Oberkante 130.000 € (`BD/areas/preise.yaml` § `abgeloest`) stand bis 15.10.2026 auf vier Seiten.
- **Bewusst getragener Widerspruch, nicht erneut melden** *(Stefan, 11.08.2026)*:
  `docs/portrait_galvano_forum_2026.pdf` sagt „Trusted-AI-**Zertifizierung**" — weicht von der
  Linie ab (korrekt: *Modellpruefung*). Das Heft ist gedruckt; beim naechsten Nachdruck
  mitkorrigieren.
- **Kontaktblock im Portraet** trägt „Stefan Maier / AT-6960 Buch" *(25.09.2026, direkt im PDF
  getauscht)*; Original: `01_Außenauftritt/02_Veranstaltungen/20260618_Galvano Forum SWISSGALVANIK/01_Anbahnung/`.

## Optional (noch offen)

- [ ] Weitere Unterseiten (Trusted AI, Downloads)
- [ ] **Vier Zeilen „Ausfallsicherheit" bei `#ablauf`** (empfohlen statt Team-Sektion, § *Regeln, die dauerhaft gelten*).
- [ ] **UTM auf die eingehenden Links** setzen (Mailstufe 3, LinkedIn, Signatur) — die interne
      Verlinkung bleibt bewusst ohne UTM, sonst zerlegt sie die Sitzung. § *Demo-Seite*.
- [ ] **Demo-Video neu vertonen** *(entschieden 09.09.2026)* — vier Stellen im Ton von
      `RStpqzz3r5g`, Bildspur bleibt: (1) 1:24 der Trainingsweg ueber das Ishikawa-Ergebnis,
      (2) 0:53 „Backupdateien aus Anlagensteuerung/MES/X-Ray/Labor" als Integrationsweg,
      (3) 2:32 „fast keine dieser Fehler stimmen mit dem Anomaliescore ueberein" — klingt wie
      eine Einschraenkung, ist der Nutzen, (4) 4:22 der Preis „1.500 € netto" der Standortanalyse.
      Danach neu hochladen und **nur die ID im `<iframe>` tauschen** (§ *Demo-Seite*). Bis dahin
      bleibt das Video online — eine tote Landingpage kostet mehr.
- [ ] **Deckt der Inspektionsbericht „technisch ausgereift"?** So sagt es das Video bei 4:14.
      Die Modellpruefung ergab *Low Risk* — eine Risiko-, keine Reifegradaussage. Wenn der
      Wortlaut nicht belegt ist, faellt der Satz beim Neuvertonen mit weg.

---

## Architektur (Single-Source, seit 2026-07-03)

Gemeinsame Bausteine liegen **an genau einer Stelle** und werden nicht mehr pro
Seite dupliziert. Wer Farben, Nav oder Footer aendert, editiert **eine** Quelle:

| Baustein | Single Source | Wird genutzt von |
|----------|---------------|------------------|
| Design-Tokens (Farben) + Reset + Typo + Container + Nav + Buttons + section-header + Footer + WA-FAB + Sticky-CTA + fade-up | `assets/css/base.css` | jede Seite (erstes CSS im `<head>`) |
| Geteiltes Verhalten (Nav-Scroll, Mobile-Menue, fade-up, Sprachhinweis) | `assets/js/site.js` | jede Inhaltsseite (`defer`) ausser `sicherheit.html` und `en/security.html` (eigenes Menü-Skript, § *Englische Fassung*) |
| Nav + Footer + WA-FAB + Sticky (HTML), `hreflang`, CSS der englischen Seiten | `_generate_layout.py` -> Marker `<!-- BEGIN/END nav -->` usw. | alle Seiten in `PAGES` und `PAIRS` |

Die Markenfarben in `base.css :root` sind **kanonisch abgeleitet** aus
`Business Development/areas/brand/corporate_design.md`. Aendern sich Markenfarben, wird NUR
`base.css` editiert. Ad-hoc-Hex im Seiten-CSS vermeiden — stattdessen Token `var(--name)`.
Seiten-spezifisches CSS (Hero, einzelne Sektionen) bleibt im `<style>`-Block der Seite. Schriften:
Montserrat (Headlines), Open Sans (Body), **self-hosted** in `fonts/` (OFL) über `fonts/fonts.css`.

**Nicht migriert (bewusst):** `sicherheit.html` traegt weiter ihr eigenes CSS.
`ausbildung.html` bekommt Nav und Fuss generiert; ihr Seiten-CSS ist eine Kopie des Standes aus
`leistungen.html` plus eigener Abschnitte. Die Leistungsbausteine auf `leistungen.html` sind
handgeschrieben.

**Eine Seite (wieder) aufnehmen:** Nav-Eintrag in `NAV_LINKS`, Seite in `PAGES`
(`_generate_layout.py`), Marker in die Seite setzen, Sitemap-Eintrag, Meta-Block samt `preload`
der Schriften — dann `py _generate_layout.py`, `check_site.py` **und** `check_inhalt.py`. Der
zweite faengt zu lange Titel und Beschreibungen und fehlende Sitemap-Eintraege ab; beim Aufbau von
`ausbildung.html` am 02.09.2026 sind alle drei tatsaechlich aufgetreten.

**Nach einem groesseren Umbau: Klicktest gegen die Live-Seite** *(seit 21.10.2026)*:
`py -X utf8 _scripts/check_live.py` — jede Seite aus `sitemap.xml` am Bildschirm und am Handy,
jeder Link und Sprunganker, jede Kachel und Frage aufklappen, Videos, Konsolenfehler, seitliches
Verrutschen; dazu die Kennzahl „Angebote nach n Bildschirmen" am Handy. `check_site.py` sieht nur
die Dateien vor dem Push, dieser Test das, was live steht. Bookings (417) und LinkedIn (999)
sperren automatische Abrufe und gelten nicht als Befund — die Buchungsseite nach einer Aenderung
von Hand oeffnen.

## Englische Fassung (`en/`) — seit 12.10.2026

**Zweck:** US-Besucher (und alle ohne Deutsch) mit demselben Argument erreichen *(Stefan,
12.10.2026)*. Übersetzt sind die Seiten, die einen Erstkontakt tragen, dazu die Haltungsseite
`ethik` (gilt für jeden Markt gleich); die Liste der Paare steht **genau einmal**, in `PAIRS` in
`_generate_layout.py`. Demo, Datenwerkstatt und Forschung bleiben deutsch — Videos und Unterlagen
dort sind deutsch. Impressum und Datenschutz bleiben deutsch und sind aus dem englischen Fuß mit
„(German)“ verlinkt; deutsche PDFs und Videos tragen dort „(PDF, German)“ bzw. „Video in German.“

**Was automatisch passiert** (`py _generate_layout.py`): englische Nav und Fuß, der
DE/EN-Schalter (`lang-en`/`lang-de`), die `hreflang`-Paare im Kopf beider Seiten (x-default =
Deutsch) und das **CSS**: Der erste `<style>`-Block der deutschen Seite wird 1:1 in den
Marker `styles` der englischen kopiert. **Layout-Änderungen auf der deutschen Seite wandern
damit ohne Zutun mit** — den Generator laufen lassen genügt.

**Was nicht automatisch passiert, ist der Text — dafür gibt es die Prüfung.**
`_scripts/check_englisch.py` hält unter `en/_quelle/` fest, auf welchem deutschen Stand jede
Übersetzung beruht (Kopf-Metadaten, JSON-LD und Seiteninhalt ohne generierte Blöcke). Weicht
die deutsche Seite ab, meldet sie die geänderten Zeilen als Diff. Sie läuft an drei Stellen:

1. in `check_site.py` (Gate 1 vor jedem Deploy, Exit 1),
2. als **pre-commit** dieses Repos (`py _scripts/check_englisch.py --hook-installieren`; der
   Hook liegt nicht im Repo, nach einem neuen Klon einmal ausführen),
3. täglich im Code-Wächter (`Englisch  homepage`).

**Regel: Wer eine deutsche Seite mit englischem Gegenstück ändert, zieht die englische im selben
Commit nach** — die gemeldeten Zeilen übersetzen, dann
`py _scripts/check_englisch.py --bestaetigen <deutsche-seite>.html`. Bestätigen ohne
Nachziehen hebelt die Kontrolle aus. Zusätzlich vergleicht die Prüfung Abschnitte,
Überschriften und Funnel-Marker beider Seiten — ein beim Nachziehen verlorener Abschnitt fällt
auch ohne Diff auf. **Grenze:** Sie sieht, *dass* sich das Deutsche geändert hat, nicht, ob die
Übersetzung gut ist.

**Konventionen für englische Seiten:**
- Gleiche `id`s und Klassen wie die deutsche Seite (CSS und Anker hängen daran); Verweise auf
  gemeinsame Dateien mit `../`.
- **Jeder Funnel-Marker endet auf `-en`**, `data-video` ebenso — sonst mischt Clarity beide
  Sprachen (`OPTIMIERUNG.md` §4).
- Glossar: Modellprüfung = *model audit* (nie *certification/certified*), Standortanalyse =
  *Site Assessment*, Erstanalyse = *Initial Data Check*, Fehlerursachenanalyse mit Demo-Werkzeug =
  *Root Cause Analysis with Demo Tool*, Einführung in den Betrieb = *Rollout into Operations*,
  KI-Fahrplan = *AI Roadmap*, Weg A/B = *Path A/B*,
  nach Aufwand = *billed by effort*, Erstgespräch = *intro call*, Lohngalvanik = *job shop*,
  Ausschuss = *scrap*, Reklamation = *customer complaint*. Abgelöst (03.11.2026): *Defect Analysis*,
  *AI Base Setup*, *Data Workshop*.
  „Regelkarte“ ist auch als *control chart* gesperrt (die Prüfung schlägt an).
- Was nur für Österreich gilt (Förderprogramme), entfällt auf Englisch. Preise als
  „€1,500 net (excl. VAT)“.
- Englische FAQ-Knoten im JSON-LD tragen eigene `@id`s unter `/en/`.
- Die Unternehmenspräsentation gibt es auf Englisch als eigenes PDF (`company-presentation_…`),
  nicht das deutsche.

**Der Hinweis für Browser ohne Deutsch** (`site.js`): fest positioniert, einmal je Sitzung,
nur auf deutschen Seiten, die den Sprachschalter tragen. **Bewusst keine automatische
Umleitung** — Google rät davon ab, der Crawler käme sonst nicht mehr an die deutschen Seiten.
Auf `leistungen.html` und `sicherheit.html` (eigenes CSS) bringt das Skript seinen Stil selbst
mit; `sicherheit.html` lädt `site.js` nicht (eigenes Menü-Skript — beide zusammen schalten das
Menü doppelt und es öffnet nicht, gemessen 12.10.2026), dort erscheint der Hinweis also nicht.

## Demo-Seite (`demo.html`)

**Zweck:** die einzige Landingpage der Seite im engeren Sinn — ein Zweck, ein Handlungsaufruf,
keine Ablenkung. Sie traegt das Demo-Video der Anwendung und ist das Ziel, auf das Mail, Telefon
und LinkedIn zeigen. Begruendung der Platzierung im ganzen Trichter: SharePoint
`…/06_Praesentationsmaterialien/Videos & Podcasts/20260901_Demo Video Hompage/00_LIESMICH_Platzierung-und-Funnelbefund.md`.

**Was drauf ist:** YouTube-ID **`RStpqzz3r5g`** („Prozessdaten auswerten — die Anwendung im
Ueberblick"), **4:51**, nicht gelistet, eingebunden ueber `youtube-nocookie.com` — kein Cookie vor
Klick, die Datenschutzerklaerung setzt das voraus. Die Seite ist indexiert und steht in der
`sitemap.xml`; zwei Verweise zeigen darauf: Startseite unter dem Pitch-Video
(`link-demo-startseite`) und `leistungen.html` in der Sektion *Fehlerursachenanalyse mit Demo-Werkzeug*
(`cta-demo-vorprojekt` — Ereignisname bewusst alt, sonst bricht die Clarity-Reihe).
**Nicht** in die Belegspalte bei `#standortanalyse` — die sammelt Belege zur *Standortanalyse*,
das Video zeigt die *Anwendung*; ein dort am 02.09.2026 gesetzter dritter Verweis konkurrierte
mit den anderen, statt zu fuehren. Unter *Weitere Aufnahme* steht nur „Auswertungen und
Berichte" *(Stefan, 09.09.2026)*; weitere Videos (`lWJQq0x2_1c`) gehen gezielt im Gespräch raus.

**Die Seite erzaehlt DIE ANWENDUNG, nicht den Vor-Ort-Tag** *(Stefan, 02.09.2026; Anlass: kurzzeitig
stand hier die Standortanalyse-Fassung, das Video zeigt aber die Auswertung)*.
**Dauerregel daraus: Seite und Video muessen dasselbe versprechen.** Wird das Video getauscht,
wandern Ueberschrift, Vorspann, die drei Punkte *„Was Sie im Video sehen"*, `<title>`, die
`og:`-Tags und die Laengenangabe **im selben Zug** mit. Die Laenge steht an vier Stellen:
Hero-Label, Meta-Description und je einmal im Verweis auf Startseite und `leistungen.html`.

**Ein anderes Video einsetzen:** nur die ID im `<iframe>` tauschen, nie `youtube.com` statt
`youtube-nocookie.com`. **Kein zweites Video auf diese Seite** — eine Landingpage, ein Zweck.
Danach `py _scripts/check_site.py`, pushen und den Deploy bestaetigen (§ *Nach dem Push*).

**Das Startseiten-Video ist ein anderes** und bleibt, wo es ist: `index.html`, Sektion
*Intro-Video (Pitch)*, YouTube-ID `lLgcKqhHOrU`, „Warum Galvaniken auf Daten statt Bauchgefuehl
setzen" (2 Minuten). **Kein zweites Video auf die Startseite** — zwei Videos uebereinander teilen
die Aufmerksamkeit; die Startseite bekommt einen Verweis auf `demo.html`, nicht das Video selbst.

**Der Einseiter zum Weiterleiten** *(02.09.2026)*: `docs/anwendung-ueberblick.pdf`, verlinkt
**unter den drei Punkten**, bewusst **nicht** als Nebenweg unter dem CTA — dort konkurrierte er mit
dem Buchungs-Knopf. Zielgruppe sind Kollegen des Besuchers ohne fuenf Minuten fuer das Video: das
Blatt muss **allein stehen** (Video-Adresse, Kontakt, Ablauf). Erzeuger
`BD/templates/flyer-corporate/build_flyer_anwendung.py`, **nie im PDF nachbessern** (Pflichtstellen-
Pruefung: § *Projektstruktur*, `docs/`). **Aendert sich Video oder Seite, aendert sich das Blatt mit.**

**Messung:** Der CTA traegt `data-funnel="cta-demo-seite"`, derselbe Knopf oben im Hero seit
03.11.2026 `cta-demo-hero` (ein Zweck, ein CTA, zweimal gezeigt; darunter nur noch EIN Nebenweg,
`link-fehlerbild-demo`), der Videostart meldet sich als **`video-anwendung`** (aus
`data-video="anwendung"`; `consent.js` erfasst das erste YouTube-iframe der Seite, hier das einzige).
Eingehende Links aus Mail und LinkedIn bekommen UTM-Parameter (offen, § *Optional*).

## Datenwerkstatt-Seite (`ausbildung.html`) — Video und Zielgruppe *(11.09.2026)*

> **Seit 03.11.2026 nicht mehr auf der Website** (§ *Regeln, die dauerhaft gelten*, Angebote). Die
> Regeln unten gelten für die Seite selbst und beim Wiederaufnehmen, die Regelkarte-Sperre überall.

**Zielgruppe steht in der Kennzeile:** *„Weiterbildung fuer kleine Betriebe"* (Anlass: der Hero
setzte laufende Messtechnik voraus und nannte die Begleitung nicht). **Dauerregel:
Auf dieser Seite ist die manuelle Erfassung der gleichwertige Fall**, nicht der Sonderfall;
wer hier Text aendert, prueft beide Wege (Steuerung *und* Badbuch von Hand) und nennt das
Coaching als Teil des Angebots. Derselbe Satz steht im Flyer (`AENDERUNGSPROZESS.md` Gate 4).

**Was drauf ist:** YouTube-ID **`-btKYAPGAqw`**, eingebunden ueber `youtube-nocookie.com`,
**direkt unter dem Hero** — vor der Nutzenliste, weil ein Besucher aus einer Mail zuerst sehen
will, wovon die Rede ist. Inhalt: das Badbuch aus `lehrmittel/demos/badbuch/` (nachgestellter
Verlauf, keine Betriebsdaten, kein Lieferantenname). Der Videostart meldet sich als
**`video-badbuch`** (`data-video="badbuch"`).

**Titel wortgleich halten** (Dauerregel § *Demo-Seite*): YouTube-Titel und `title`-Attribut am
iframe lauten *„Digitale Badkarte mit KI aufbauen"* (geprueft 11.09.2026 ueber
`https://www.youtube.com/oembed?url=…`); wird er in YouTube Studio geaendert, wandert er hier mit.

> ⛔ **Gesperrter Fachbegriff: „Regelkarte"** *(Stefan, 11.09.2026)*. Er liegt zu nah an einem
> Begriff eines Betriebs, fuer den Stefan gearbeitet hat, und darf **auf keinem oeffentlichen
> Kanal vorkommen** — auch nicht in `alt`, `title`, Meta-Angaben oder im HTML-Kommentar (der
> Quelltext ist oeffentlich; deshalb steht die Regel hier und nicht in der Seite). Statt
> dessen: *„die Kurve mit den Grenzen"*, *„der Verlauf"*, *„Verlaufskurve"*.
>
> **Die Sperre gilt dem Leser, nicht dieser Website** *(praezisiert 13.09.2026)* — **ueberall, wo
> Fremde mitlesen**: LinkedIn, Flyer, Vortragsfolie, Video, Bildunterschrift. Anlass: Fuer das
> LinkedIn-Beitragsbild vom 17.09.2026 musste das erst hergeleitet werden; dessen Bau-Skript
> maskiert den Begriff seither auf einer Kopie der Demo und bricht ab, wenn er stehen bleibt.
>
> **Nicht betroffen** sind die Demo `Badbuch.html` selbst und die Projektdoku im BD-Repo (nicht
> oeffentlich; ob die Demo verschickt wird, entscheidet Stefan). Gegenprobe:
> `grep -rn "Regelkarte" *.html` muss leer bleiben; auf `en/` schlaegt zusaetzlich `check_englisch.py` an.

**Es bleibt EIN Video auf dieser Seite.** `consent.js` greift das erste YouTube-iframe; ein
zweites waere in der Messung unsichtbar und teilte die Aufmerksamkeit. Der Verweis auf
`demo.html` bleibt bewusst ein **Nebensatz** in der Nutzen-Sektion (`link-demo-ausbildung`):
das Video hier zeigt ein **selbstgebautes** Werkzeug, `demo.html` die **fertige** Software.

**Im Style-Block nur Klassen, die auf DIESER Seite vorkommen** — Gemeinsames gehoert nach
`assets/css/base.css`. Anlass: Der Block war aus `sicherheit.html`/`leistungen.html` kopiert und
trug rund 10 kB fremde Regeln (11.09.2026 ausgebaut, jede Klasse gegen Rumpf, Generator, JS und
`base.css` geprueft). *Bewusst gelassen: `.wa-fab`/`.wa-label` (§ WhatsApp-Kontakt).*

**Die Hero-Laenge ist eine Messgroesse.** Waechst der Hero, rutscht der Hauptknopf mobil hinter
das Einwilligungsbanner (Klasse: `AENDERUNGSPROZESS.md` Gate 3; hier am 11.09.2026 erneut, der
erste Entwurf lag **60 px** darunter). Nach jeder Hero-Textaenderung auf **390 × 844** nachmessen.
Stand: Hauptknopf endet bei y 577, Banner ab 731 — **154 px Luft**, englisch ebenso *(gemessen
03.11.2026, Playwright-Chromium ohne gespeicherte Einwilligung)*.

> **Wortwahl im Hero ist seit 13.09.2026 gebunden** *(Stefan)*: **gebaut werden Werkzeuge,
> nicht Auswertungen.** Die Auswertung ist das Ergebnis, das Werkzeug der Gegenstand. Wo
> „Auswertung" die Taetigkeit meint („bevor die erste Auswertung laeuft"), ist es **richtig und
> bleibt**. Dieselbe Unterscheidung gilt fuer LinkedIn und den Flyer.

## Aenderungsprozess

Wie eine Aenderung an dieser Website ablaeuft — von den Zahlen ueber die vier Gates bis zur Deploy-Bestaetigung — steht in [`AENDERUNGSPROZESS.md`](AENDERUNGSPROZESS.md). Er setzt auf `AGENTS.md` §5 auf und ergaenzt nur, was eine Website zusaetzlich braucht. Der monatliche Messlauf steht in [`OPTIMIERUNG.md`](OPTIMIERUNG.md).

## Qualitaetssicherung / Self-Check

**Bei groesseren Aenderungen an HTML/CSS/Layout IMMER vor dem Commit/Deploy:**

```bash
cd homepage
py _generate_layout.py          # Nav/Footer/FAB/Sticky aus Single-Source neu rendern
py _scripts/check_site.py        # Self-Check (0 Fehler = grün)
```

`_scripts/check_site.py` ist das "pyright der Homepage" (nur tinycss2; Pruefliste im Skript, u. a.
Layout-Marker **in Sync mit dem Generator** und englische Fassung auf deutschem Stand). Exit 1 bei
Fehlern -> nicht deployen. `check_inhalt.py` (Metadaten, Marker, Sitemap): `AENDERUNGSPROZESS.md` Gate 1.

Optionaler Gegencheck bei groesseren Umbauten (Node, kein Java):
`npx --yes htmlhint *.html` und `npx --yes html-validate *.html en/*.html`.

## Projektstruktur

```
homepage/
  index.html               Startseite (Predictive Quality, ein roter Faden); Sektionen: grep 'id="' index.html.
                           #ablauf = Startkarten und Wege (§ Stand der Website). KEINE Leistungs-Teaser-Karten.
  leistungen.html          Leistungsseite, handgeschrieben, seit 03.11.2026 auf die Haelfte gekuerzt (Stefan;
                           4,6 statt 9,2 Bildschirme). Anker: § Regeln, Angebote; #standortanalyse/#erstanalyse
                           = Landeabschnitt der LinkedIn-Links; #fragen mit FAQPage-Schema; #potenzialfelder,
                           #anwendungen, #bausteine stehen leer. Je Angebot nur der Beispiel-Befund als PDF;
                           Produktblaetter, Blanko-Angebote unverlinkt in docs/ (gehen im Gespraech raus). Seit
                           31.08.2026 wieder eigene Seite (87 GSC-Impressionen auf Weiterleitung, 0 Klicks).
  demo.html                Landingpage fuer das Demo-Video (ein Zweck, ein CTA) — § Demo-Seite.
  ausbildung.html          Datenwerkstatt, seit 03.11.2026 noindex und unverlinkt — § Datenwerkstatt-Seite.
                           Reihenfolge Nutzen -> Ablauf -> Beispiel, Knoepfe fuehren zu leistungen.html.
  forschung.html           Forschungsprojekte (FFG-Kleinprojekt, aws), aws-Jurytermin-Foto.
  ethik.html               Ethik & Werte (seit 27.10.2026, Nav nach "Über mich"): Haltung zu KI und
                           Beschaeftigung. Jede Zahl mit nummerierter Referenz am Seitenende; Herkunft:
                           Change-Management-Recherche 26.10.2026 (SharePoint, Akquise-Ordner) und BD
                           archive/ffg-kleinprojekt-eingereicht-2026-09/stand-der-technik.md (Ausbildungs-
                           bestand = Bestand, nicht Neuabschluesse). Kein Betrieb genannt, auch nicht
                           umschrieben. Abbildungen Inline-SVG/HTML.
  sicherheit.html          Compliance-Seite (indexiert, in Sitemap und Footer, bewusst NICHT in der Haupt-
                           navigation: PAGES-Eintrag mit None); eigenes Seiten-CSS (§ Architektur).
  ueber-mich.html          Vollständiges Profil + Bio + Nachweise-Galerie
  nachweise.html           Redirect-Stub auf ueber-mich.html#nachweise (Instant-Meta-Refresh + Canonical, KEIN noindex)
  en/                      Englische Fassung — § Englische Fassung. en/_quelle/ = deutscher Stand je
                           Uebersetzung fuer check_englisch.py (wegen des Unterstrichs nicht ausgeliefert).
  impressum/ stefan-maier/ kontakt/ trusted-ai/ data-analytics/
                           Redirect-Stubs auf die WordPress-Alt-URLs — generiert aus _generate_redirects.py,
                           nicht von Hand editieren. Nur Pfade mit echtem Nachfolger; tote PDFs bleiben 404.
  termin/                  Kurzlink secure-galvano-ai.com/termin -> Bookings-Erstgespraech (fuer LinkedIn und
                           Mails; noindex, kein canonical) — aus SHORTLINKS in _generate_redirects.py
  impressum.html           Impressum (ECG/UGB) + Marken-Hinweis
  datenschutz.html         Datenschutzerklärung (DSGVO)
  404.html                 GitHub-Pages-Fehlerseite (noindex, nicht in Nav/Sitemap), faengt Alt-URLs der
                           WordPress-Zeit ab. NUR absolute Pfade (/assets/...), weil Pages sie auch fuer tiefe
                           Pfade wie /wp-content/uploads/... ausliefert; ohne Layout-Marker (Generator
                           erzeugt relative hrefs) und ohne JS.
  assets/                  img/ (Partnerlogos in kooperation/) · css/base.css = SINGLE SOURCE (§ Architektur),
                           jede Seite bindet es als erstes CSS ein · js/consent.js = Opt-in-Consent-Gate für
                           Microsoft Clarity + CTA-Funnel-Events · js/site.js = geteiltes Verhalten
  _scripts/                check_site.py (vor jedem Deploy), check_inhalt.py, check_englisch.py, sitemap_pflegen.py;
                           Messung (clarity_daily.py, youtube_abrufe.py, wochenbericht.py) -> OPTIMIERUNG.md
  _doku/                   Betriebsdoku, die nicht ausgeliefert wird (Unterstrich) — infrastruktur.md
  _generate_layout.py      Generator: Nav + Footer + WA-FAB + Sticky aus einer Quelle in die Marker-Bloecke aller Seiten
  _generate_redirects.py   Generator: Redirect-Stubs fuer WordPress-Alt-URLs (REDIRECTS-Dict = einzige Quelle) und Kurzlinks (SHORTLINKS)
  _generate_assets.py      Generator für Favicon/OG-Image (liest/schreibt assets/img/)
  credentials/             _generate_credentials.py (PDF -> JPG, § Deployment); thumbs/ Grid, full/ Lightbox
  docs/                    Belege zum Verlinken und Mitschicken; bewusst KEINE Einzelliste (driftet bei jedem
                           neuen Beleg). Wo welcher verlinkt ist: grep -o "docs/[a-z0-9_-]*\.pdf" *.html
                           Wird von Jekyll ausgeliefert -- hier nur, was oeffentlich sein darf. Die PDFs
                           kommen aus BD-Build-Skripten, NIE von Hand bearbeiten -- im Skript aendern, neu
                           bauen. Erzeuger: grep -rl "<dateiname>.pdf" in BD templates/ (Flyer, Befunde),
                           areas/coaching-und-ausbildung/ (Datenwerkstatt), scripts/ (angebot_muster.py
                           = die drei Angebots-Muster ohne Empfaenger, Nummer, Datum, IBAN, Unterschrift,
                           Pruefung dort UMGEKEHRT, Docstring angebot_bauen.py). Das NDA-Muster ist seit
                           09.11.2026 nicht mehr veroeffentlicht (Entscheidung Stefan: Vertraulichkeit wird je
                           Kunde in der Anbahnung einzeln vereinbart). Ausnahme:
                           unternehmenspraesentation_/company-presentation_secure-galvano-ai.pdf aus dem
                           Pitch-Deck-Master (SharePoint 01_Aussenauftritt/06_Praesentationsmaterialien/
                           Pitch Deck/03_Decks/_Werkzeuge/download_bauen.py, 00_LIESMICH.md "Zwei abgeleitete
                           Fassungen"). Dateinamen NICHT aendern -- consent.js bildet das Clarity-Ereignis
                           daraus. Jedes Skript prueft Seitenzahl und Pflichtstellen (overflow:hidden
                           schnitt einmal die Fusszeile lautlos ab).
  fonts/                   fonts.css + Montserrat/Open Sans als WOFF2 (latin, latin-ext), OFL
  favicon.ico, apple-touch-icon.png  Browser-Tab- und iOS-Icon (im Root — Konvention)
  CNAME                    Custom Domain Config — nicht löschen (_doku/infrastruktur.md)
  _config.yml              Nur exclude: haelt README/OPTIMIERUNG/AENDERUNGSPROZESS aus der Auslieferung — nie docs/ eintragen
  robots.txt               Crawler-Erlaubnis
  sitemap.xml              Google Sitemap. Welche URL hineingehoert, ist Handarbeit; die lastmod-Daten nicht
                           (_scripts/sitemap_pflegen.py), und check_site.py Check 8 haelt die Liste gegen
                           noindex und fehlende Dateien.
```

## Search Console / Indexierung

> Der **monatliche Optimierungslauf** (Clarity + Search Console, Kennzahlen, Entscheidungsregeln,
> Zugaenge) steht in [`OPTIMIERUNG.md`](OPTIMIERUNG.md). Dieser Abschnitt hier deckt nur die
> Indexierungs-Sonderfaelle ab.

Der Bericht **Seitenindexierung** meldet regelmaessig „nicht indexierte Seiten". Die
meisten Eintraege sind **Soll-Zustand**, kein Defekt. Einordnung vor jeder Reaktion:

| Meldung | Ursache | Zu tun |
|---|---|---|
| **Nicht gefunden (404)** | **Zwei** Quellen. (a) Alt-URLs der WordPress-Installation bei IONOS, mit dem Vertragsende **02.06.2026** weg. (b) Eigene, einmal ausgelieferte Dateien, die inzwischen entfernt wurden — die Liste holt `git log --diff-filter=D --name-only -- "*.html" "*.pdf" "*.jpg"` und die Gegenprobe, ob die Datei heute noch existiert. Kein **Link im Repo** zeigt je darauf, das prueft `check_site.py`. | Zweiteilen: URL **mit** heutigem Pendant -> Redirect-Stub in `_generate_redirects.py`. URL **ohne** Pendant (tote PDFs und Bilder, `/wp-*.php`-Bot-Scans, vom Auftritt genommene Werkzeugseiten) -> nichts tun, 404 ist der korrekte Endzustand. Eine Weiterleitung auf eine bewusst verborgene Nachfolgeadresse ist **keine** Option. |
| **Durch „noindex"-Tag ausgeschlossen** | Keine Seite in der Sitemap traegt `noindex` — `check_site.py` Check 8 prueft das in beide Richtungen, auch die Umkehrung (die vier verborgenen Seiten `termin/`, `li/`, `en/li/`, `werkzeug/aufgaben/` duerfen dort nicht auftauchen). Was im **Sitemap**-Bericht trotzdem hier landet, sind Adressen, die Google aus einer Sitemap kennt und die heute 404 liefern: GitHub Pages serviert dafuer `404.html`, und die traegt `noindex`. Gleiche Wurzel wie die Zeile darueber. | Nichts. Steht eine URL betroffen da, die **wirklich in `sitemap.xml`** liegt, ist es ein Defekt — dann schlaegt Check 8 an. |
| **Alternative Seite mit richtigem kanonischen Tag** | `/index.html` vs. `/` — Canonical zeigt korrekt auf `/`. | Nichts. |
| **Gecrawlt / Gefunden – zurzeit nicht indexiert** | Googles Qualitaets-/Budget-Entscheidung, kein technischer Fehler. Einziger echter SEO-Hebel im Bericht. | Betroffene URL in der URL-Pruefung ansehen, Inhalt schaerfen (eigenstaendiger Text, interne Verlinkung), dann **„Indexierung beantragen"**. Nicht wiederholt beantragen. |

**„Behebung validieren" bei 404 nicht klicken.** GSC validiert nur gegen 200/Redirect. Solange
auch nur eine legitim tote URL in der Gruppe steckt, schlaegt der Lauf zwangslaeufig fehl — das
erklaert den Status „Fehlgeschlagen" vom 25.07.2026, nicht ein Defekt auf der Seite. Google dropt
solche URLs nach ~4–8 Wochen selbst; schneller: `Entfernungen → Neuer Antrag → Praefix` fuer `…/wp-content/`.

**Redirects auf GitHub Pages.** Server-seitige 301 gibt es nicht. Google behandelt den
**Instant-Meta-Refresh** (`content="0; url=…"`) laut Doku als permanenten Redirect und nennt ihn
ausdruecklich als Ersatz, wenn server-seitige Redirects nicht implementierbar sind. Genau das
erzeugt `_generate_redirects.py` — plus `rel=canonical` und einen sichtbaren Link als No-JS-Fallback.

**Kein `noindex` auf Redirect-Stubs.** `noindex` blockt die URL komplett aus der Suche und
verhindert damit, dass Google den Refresh ueberhaupt als Redirect verarbeitet; zusammen mit
`rel=canonical` sind es widerspruechliche Signale. `noindex` gehoert nur auf zurueckgestellte
**Inhalts**seiten mit Self-Canonical.

**Sitemap:** `lastmod` zieht `py _scripts/sitemap_pflegen.py` aus dem letzten Commit je Datei
(`--pruefen` schreibt nicht), `check_site.py` warnt bei veralteten Werten — die kosten
Crawl-Prioritaet, ein pauschales „heute" verbrennt sie. Anlass fuer Skript statt Textvorgabe: am
22.10.2026 waren alle 13 Daten veraltet, das aelteste um 3,5 Monate.

## DNS-Konfiguration, IONOS und Systemabhängigkeiten

Ausgelagert nach [`_doku/infrastruktur.md`](_doku/infrastruktur.md) *(15.10.2026)*: Soll-Stand
beider Zonen (`secure-galvano-ai.com`, `rvh.at`), Endstand der Absenderauthentifizierung
(`p=quarantine`, warum kein `p=reject`), IONOS-Vertrag, Login-Wiederherstellung, der Vorfall vom
17.08.2026, „Was bricht was" (§ *Systeme und Abhängigkeiten*) und der Routine-Check nach jeder IONOS-Aktion.

## Corporate Design Assets

Logos (`logo.png` groß, `logo_header.png`) und `corporate_design.md` liegen in `BD/areas/brand/`, Farben
und Schriften der Website § *Architektur*; Porträt-Quelle: `Stefan Maier - Dokumente/02_Unterlagen/04_Fotos/MICHAELKREYER/`.

## Externe Services

| Service | Zweck | Link |
|---------|-------|------|
| Microsoft 365 | Mail `smaier@rvh.at`, Tenant **PhonixData** | `admin.microsoft.com` · DKIM: `security.microsoft.com` |
| Microsoft Bookings — **der Link der Website** *(umgestellt 14.09.2026)* | Erstgespräch buchen, **30 Min.**, buchbar Mo–Do 9–19, Fr und Sa 9–14 *(eigene Zeiten im Dienst, Stefan 14.11.2026; löst Mo 13–17 / Do 9–14 vom 01.10. ab)*; Frage „Wie sind Sie auf uns aufmerksam geworden?" seit 01.10.2026, Pflicht und Antwort „Fachartikel oder Presse" seit 14.11.2026 (Herkunftsmessung, Antwort steht im Outlook-Termin) — läuft auf dem rvh.at-Tenant. Dienst `secure galvano ai - unverbindliches Erstgespräch`. Gepflegt wird in `_generate_layout.py` die Konstante `BOOKING_URL` | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/DdIPgTj7-0ymr6eHc38SQg2` |
| Microsoft Bookings — **der Link der `/en/`-Seiten** *(15.10.2026)* | Dasselbe Erstgespräch auf Englisch: Dienst `secure galvano ai - free intro call`, **Sprache English (United States)**, sonst eine Kopie des deutschen Dienstes (Zeiten, Teams, Erinnerungen) mit eigenen englischen Fragen. **Warum ein eigener Dienst:** Bookings richtet Oberfläche, Fragen und Bestätigungsmail nach der Sprache des **Dienstes**, nicht nach dem Browser. Die Fragen sind in Bookings dienstübergreifend — eine deutsche Frage umzuformulieren ändert sie im deutschen Dienst mit. Konstante `BOOKING_URL_EN`, maßgeblich `stammdaten.buchung_en`. **Die Kopie zieht nicht mit:** Wer Zeiten, Dauer, Beschreibung oder Fragen am deutschen Dienst ändert, ändert den englischen im selben Zug | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/ZivH8iyBokGAiByKXkWuqA2` |
| Microsoft Bookings — **Arbeitstermin** *(30.09.2026, seit 02.10.2026 `secure galvano ai - Arbeitstermin`)* | Arbeitstermine im laufenden Projekt — Coaching wie IT eines Kunden, **1 Std.**, Teams, ohne Preis. **Nie auf der Website verlinken** — der Link steht nur im Angebot (`stammdaten.buchung_coaching`, Begründung in `BD/areas/coaching-und-ausbildung/README.md` § Angebot und Ablauf) | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/WguGbyr1pUWQxZrPA0ISQA2` |
| Microsoft Bookings — Sammel-Buchungsseite | Zeigt **alle sichtbaren Dienste zur Auswahl** — Erstgespräch, Arbeitstermin und seit 15.10.2026 der englische Intro call. Der Arbeitstermin muss sichtbar bleiben: **Bookings sperrt einen ausgeblendeten Dienst auch über seinen Direktlink** („Wir bieten im Moment keine Dienste … an", geprüft 30.09.2026). **Die Website verlinkt deshalb nur den Dienst-Direktlink des Erstgesprächs** — der zeigt nur diesen einen Dienst (geprüft ohne Anmeldung, 30.09.2026). Neuer Dienst: Typ 1:1/1:N wird beim Anlegen festgelegt und ist danach nicht änderbar (`BD/areas/vertrieb/mailsequenz/buchungsdienst.md`) | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/` |
| Microsoft Clarity | Web-Analyse (Opt-in, Projekt `wql3vpgrxl`) | `clarity.microsoft.com` |
| Google Search Console | SEO / Indexierung | `search.google.com/search-console` |
| GitHub Pages | Hosting + TLS-Zertifikat | `github.com/secure-galvano-ai/homepage/settings/pages` |
| IONOS | **Domain-Registrar und DNS-Betreiber** — Login über Kundennummer, nicht über die Mailadresse | `my.ionos.de` · Service `0721 170 555` |

## Deployment

Push auf `main` → GitHub Pages deployed automatisch (~1 Min).

```bash
cd homepage
git commit -m "Beschreibung" -- <nur die eigenen Dateien>   # nie -A, fremde Arbeit bleibt draussen (AGENTS.md §5)
git push
```

**KEIN GPG-Signing in diesem Repo** (reines Content-Repo, lokal `commit.gpgsign false`) — kein Yubikey-PIN-Dialog.

### Nach dem Push: Deploy bestätigen *(Regel seit 26.08.2026, Stefan)*

`check_site.py` prüft die **Dateien vor** dem Push, nicht, was live steht. Anlass 02.07.2026:
Build gelang, der **Deploy**-Job scheiterte GitHub-seitig, die Seite blieb still auf dem alten
Stand — zwei Stunden Suche, weil lokal alles grün war. **Pflicht — ein Befehl, fünf Sekunden:**

```bash
cd homepage && gh run list --limit 1
# erwartet: completed  success  pages build and deployment
```

Steht dort `failure` oder hängt der Lauf: **nicht neu pushen**, sondern die Anti-Patterns
unten lesen. Ein zweiter Push auf denselben Fehler kostet nur Zeit.

**Zusätzlich in den Browser — nur, wenn sich sichtbar etwas geändert hat** (Layout, CSS, Assets,
Textbausteine, generierte Seiten): nach rund einer Minute die Seite **live** öffnen — Änderung da,
Navigation und Footer unverändert, keine neuen Konsolenfehler; bei Layout und Design **ein
Bildschirmfoto ansehen** (der Strukturbaum zeigt keine verrutschten Abstände oder falschen Farben).

**Bei reinen Text- oder Doku-Änderungen entfällt die Browser-Runde** — dort findet sie
nichts, was der Deploy-Status nicht schon sagt. **Das Ergebnis wird gemeldet**, auch wenn
alles passt; eine stille Prüfung ist keine.

### GitHub Pages — bekannte Fallstricke (Anti-Patterns)

*Aus der Deploy-Panne 2026-07-02 gelernt. Symptom war: Pages meldet `Page build failed`/`errored`, die Live-Seite bleibt aber (korrekt) auf dem letzten guten Stand. In ~2 h Debugging stellte sich heraus: **der `build`-Job gelingt praktisch immer — es scheitert nur der `deploy`-Job, und zwar GitHub-seitig.***

1. **Zuerst herausfinden, WAS failt — Build oder Deploy.** Der Legacy-Endpoint `pages/builds/latest` ist laggy/irreführend. Autoritativ ist der Actions-Run:
   ```bash
   RID=$(gh api "repos/secure-galvano-ai/homepage/actions/runs?per_page=1" --jq '.workflow_runs[0].id')
   gh api "repos/secure-galvano-ai/homepage/actions/runs/$RID/jobs" --jq '.jobs[] | "\(.name): \(.conclusion)"'
   gh run view "$RID" --log-failed | tail -30
   ```
   - `deploy` + `Deployment cancelled` → **Concurrency** (Punkt 3).
   - `deploy` + `Timeout reached, aborting!` → **Pages-Backend-Timeout** (GitHub-seitig, transient) → abwarten + EINMAL neu deployen.
   - `deploy` + `HttpError: No server is currently available` (503) → **Zombie-Queue** (Punkt 2).
2. **Zombie-Queue: Run steht ewig auf `queued` und lässt sich nicht canceln → `POST /pages/builds`.**
   *Belegt 17.08.2026.* Nach einem 503 im `deploy`-Job blieben **zwei** Runs (der eigene **und** ein
   älterer, schon vor dem Push hängender) dauerhaft auf `queued`; `gh run cancel` antwortete
   widersprüchlich mit *„Cannot cancel a workflow run that is completed"*. Weder Warten (1,5 h) noch
   der eine erlaubte `gh run rerun --failed` half — die Actions-Runs waren nicht mehr aufzuwecken.
   Gelöst hat es ein frisch angestoßener Legacy-Build, der in gut zwei Minuten durchlief:
   ```bash
   gh api --method POST repos/secure-galvano-ai/homepage/pages/builds
   sleep 150 && gh api repos/secure-galvano-ai/homepage/pages/builds/latest --jq '.status'
   ```
   **Abgrenzung zu Punkt 3:** Läuft ein Deploy noch oder wartet er regulär → Finger weg, jeder
   Trigger cancelt ihn. Hängt er als Zombie (`queued`, nicht cancelbar, > 30 Min) → dieser POST.
   `githubstatus.com` meldete durchgehend „operational" — keine Entscheidungsgrundlage.
3. **NIEMALS mehrere Pages-Deploys schnell hintereinander triggern.** Die Concurrency-Gruppe `pages` hat **Queue-Tiefe 1** — jeder neue Deploy **cancelt den vorher wartenden**. Rapides `git push` + wiederholtes `gh api --method POST .../pages/builds` erzeugt eine Kaskade aus `Deployment cancelled`/`failure`. → **EINMAL pushen, dann 2–10 Min ungestört warten. Nicht nachtreten.**
4. **Bei Fehler zuerst die LIVE-Seite prüfen, nicht blind retrien** (letzter guter Build bleibt live, meist schon korrekt): `curl -s https://secure-galvano-ai.com/ | grep -o '<h1>[^<]*'`
5. **`.nojekyll` NICHT reflexartig hinzufügen.** Der Jekyll-`build` gelingt hier (getestet); `.nojekyll` löst das Deploy-Problem NICHT und liefert zusätzlich `_generate_*.py` **öffentlich** aus (Jekyll schließt `_`-Dateien sonst aus). → **ohne `.nojekyll` bleiben.**
6. **Kein `{{ … }}` / `{% … %}` im HTML** — Jekyll/Liquid parst das und failt den *Build* (war hier NICHT die Ursache, ist aber die klassische echte Build-Bremse).

Favicon/OG-Image neu generieren: `py _generate_assets.py`. Nachweise neu rendern (Quell-PDF
`Business Development/resources/credentials/20260512_Lebenslauf & Nachweise_Stefan Maier.pdf`
geändert): `py credentials/_generate_credentials.py` — dort auch Seitenauswahl, Metadaten und
Reihenfolge. Schwärzungen (Liste `REDAKTIONEN`) gehören in den Erzeuger, nicht ins fertige Bild
(`CLAUDE.md` §1 *Dokumentation*).

## WhatsApp-Kontakt — abgeschaltet seit 07.09.2026

Der Floating-Button ist **entfernt** (Stefan) — die private Mobilnummer im Klartext brachte laufend
Phishing-Anfragen. Auch `telephone` ist aus dem Schema.org-Block; **keine Telefonnummer mehr auf der
Website** (§ 5 ECG erfüllt die E-Mail im Impressum), Kontakt über Buchung + mailto. Mechanik:
`_generate_layout.py` rendert den `wa-fab`-Block leer, Marker, `.wa-fab`-CSS und `consent.js`-Logik
bleiben ungenutzt liegen; zurück über `render_wa_fab()` (die Nummer liegt bewusst nicht im Repo).
