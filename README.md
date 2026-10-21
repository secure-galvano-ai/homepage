# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.com
**HTTPS:** Aktiv (GitHub Pages + Let's Encrypt)
**Hosting:** GitHub Pages (kostenlos)
**Stand:** 2026-10-21

---

## Stand der Website

Grundausstattung steht seit Mai 2026: GitHub Pages mit eigener Domain und erzwungenem HTTPS,
Impressum/Datenschutz, Bookings-Termin, Open Graph, `robots.txt`/Sitemap, Search Console,
JSON-LD, self-hosted Fonts, Clarity mit Opt-in-Consent. Aufbau der einzelnen Seiten:
§ *Projektstruktur*. Der Änderungsverlauf steht im `git log`, die Wirkung jeder Änderung im
Monatsbericht ([`OPTIMIERUNG.md`](OPTIMIERUNG.md) §4, monatlich per `/optimierung`).

**Offen in der Wirkungsmessung (November-Lauf):**
- **`#belege` direkt unter dem Hero, vor dem Pitch-Video** *(Stefan, 28.09.2026)*. Anlass: Clarity
  August 111 Sitzungen, 0 CTA-Klicks, Startseite mobil nur zu 5 % bis zum Ende gelesen
  (`BD/archive/akquise-strategie-h2-2026-in-areas-2026-10/benchmark-werchota.md` §4 Nr. 4).
  Ablesen: CTA-Klicks, mobile Scrolltiefe.
- **`#bestand` „Ihre Anlage muss nicht neu sein"** *(Stefan, 02.10.2026)* samt Gegenstücken auf
  `leistungen.html` und in der Weiche *Selbst können* — Kennzahl in `OPTIMIERUNG.md` §4.

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
  eigene Optik** — flaches Logo im weißen Feld, ein Satz daneben, kein Beleg-Kontext. **Ein Logo
  reicht**, weitere Partner alphabetisch darunter, ein Satz je Partner.
  - **Jeder Satz sagt, dass der Partner eigenständig ist** („eigenständig betrieben", „run
    independently"). Keine Personennamen: Wer dort als Mensch steht, wirkt wie Personal.
  - **Logo nur vom Partner selbst**, verkleinert und ohne Metadaten nach
    `assets/img/kooperation/`; Darstellung 160×60 px. `flex-shrink` gehört an den Link, nicht
    ans Bild — sonst quetscht der Textabsatz das Logo (21.10.2026: 58 statt 160 px).
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
- **Aus- und Weiterbildung: `ausbildung.html`, Nav „Datenwerkstatt"** *(seit 02.09.2026;
  „KI-Werkstatt" ist in Vorarlberg von der WKO belegt)*. Grund: verkauft wird die Befähigung,
  nicht nur die fertige Software (`BD/areas/coaching-und-ausbildung/`). 104 Sitzungen mit
  **0 Klicks** auf den Buchungs-CTA zeigten, dass ein reiner Termin-Aufruf dort nicht trägt —
  deshalb ein **niederschwelliger zweiter Weg** (Überblick als PDF, ohne E-Mail-Gate) und eine
  **Erfolgsdefinition mit Abbruchkriterium** (`BD/areas/coaching-und-ausbildung/README.md` § Experiment).
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
  Anlass: Die Stufe hieß ab 31.08.2026 **„Vorprojekt"** statt „Diagnose" (seit 21.10.2026 „Analyse je Fehlerbild")
  (`BD/areas/business-model.md` §*Leiter*); bis 03.09.2026 stand „Diagnose" noch viermal auf
  `sicherheit.html` und `ueber-mich.html`, wo niemand nachsieht. Dasselbe beim Einsparpotenzial:
  **60.000–90.000 €**, die Oberkante 130.000 € ist seit 15.09.2026 abgelöst
  (`BD/areas/preise.yaml` § `abgeloest`) und stand bis 15.10.2026 noch auf vier Seiten.
- **Bewusst getragener Widerspruch, nicht erneut melden** *(Stefan, 11.08.2026)*:
  `docs/portrait_galvano_forum_2026.pdf` sagt „Trusted-AI-**Zertifizierung**" — weicht von der
  Linie ab (korrekt: *Modellpruefung*). Das Heft ist gedruckt; beim naechsten Nachdruck
  mitkorrigieren.
- **Kontaktblock im Portraet nachgesetzt** *(Stefan, 25.09.2026)*: statt „Stefan Maier e.U." und
  Alberschwender PLZ steht „Stefan Maier / AT-6960 Buch". Ohne Quelldatei (InDesign beim Verlag)
  direkt im PDF getauscht, in der eingebetteten Univers LT Std Light Condensed (keine 9 im
  Teilsatz — sie ist die um 180° gedrehte 6, fontTools). Original unverändert unter
  `01_Außenauftritt/02_Veranstaltungen/20260618_Galvano Forum SWISSGALVANIK/01_Anbahnung/`.

## Optional (noch offen)

- [ ] Weitere Unterseiten (Trusted AI, Downloads)
- [ ] **Vier Zeilen „Ausfallsicherheit" bei `#ablauf`** (empfohlen statt Team-Sektion, § *Regeln, die dauerhaft gelten*).
- [ ] **UTM auf die eingehenden Links** setzen (Mailstufe 3, LinkedIn, Signatur) — die interne
      Verlinkung bleibt bewusst ohne UTM, sonst zerlegt sie die Sitzung. § *Demo-Seite*.
- [ ] **Demo-Video neu vertonen** *(entschieden 09.09.2026)* — vier Stellen im Ton von
      `RStpqzz3r5g`, Bildspur bleibt: (1) 1:24 der Trainingsweg ueber das Ishikawa-Ergebnis,
      (2) 0:53 „Backupdateien aus Anlagensteuerung/MES/X-Ray/Labor" als Integrationsweg,
      (3) 2:32 „fast keine dieser Fehler stimmen mit dem Anomaliescore ueberein" — klingt wie
      eine Einschraenkung, ist der Nutzen, (4) 4:22 der Preis „1.500 € netto" fuer die
      Standortanalyse (steht inzwischen auch auf der Startseite, kein Widerspruch mehr). Danach
      neu hochladen und **nur die ID im `<iframe>` tauschen** (§ *Demo-Seite*). Bis dahin bleibt
      das Video online — eine tote Landingpage kostet mehr.
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
`Business Development/areas/brand/corporate_design.md`. Aendern sich Markenfarben,
wird NUR `base.css` editiert. Ad-hoc-Hex im Seiten-CSS vermeiden — stattdessen Token
`var(--name)` nutzen. Seiten-spezifisches CSS (Hero, einzelne Sektionen) bleibt im
`<style>`-Block der jeweiligen Seite. Schriften: Montserrat (Headlines) und Open Sans (Body),
**self-hosted** in `fonts/` (OFL), eingebunden über `fonts/fonts.css` — kein Google-Fonts-Request.

**Nicht migriert (bewusst):** `sicherheit.html` traegt weiter ihr eigenes CSS.
`ausbildung.html` bekommt Nav und Fuss generiert; ihr Seiten-CSS ist eine Kopie des Standes aus
`leistungen.html` plus eigener Abschnitte. Die Leistungsbausteine auf `leistungen.html` sind
handgeschrieben.

**Eine Seite (wieder) aufnehmen:** Nav-Eintrag in `NAV_LINKS`, Seite in `PAGES`
(`_generate_layout.py`), Marker in die Seite setzen, Sitemap-Eintrag, Meta-Block samt
`preload` der Schriften — dann `py _generate_layout.py`, `check_site.py` **und**
`check_inhalt.py`. Der zweite faengt zu lange Titel, zu lange Beschreibungen und fehlende
Sitemap-Eintraege ab; beim Aufbau von `ausbildung.html` am 02.09.2026 sind alle drei
tatsaechlich aufgetreten.

**Nach einem groesseren Umbau: Klicktest gegen die Live-Seite** *(seit 21.10.2026)*:
`py -X utf8 _scripts/check_live.py` — jede Seite aus `sitemap.xml` am Bildschirm und am Handy,
jeder Link und Sprunganker, jede Kachel und Frage aufklappen, Videos, Konsolenfehler, seitliches
Verrutschen; dazu die Kennzahl „Angebote nach n Bildschirmen" am Handy. `check_site.py` sieht nur
die Dateien vor dem Push, dieser Test das, was live steht. Bookings (417) und LinkedIn (999)
sperren automatische Abrufe und gelten nicht als Befund — die Buchungsseite nach einer Aenderung
von Hand oeffnen.

## Englische Fassung (`en/`) — seit 12.10.2026

**Zweck:** US-Besucher (und alle ohne Deutsch) mit demselben Argument erreichen *(Stefan,
12.10.2026)*. Übersetzt sind die vier Seiten, die einen Erstkontakt tragen:

| Deutsch | Englisch |
|---|---|
| `index.html` | `en/index.html` |
| `leistungen.html` | `en/services.html` |
| `ueber-mich.html` | `en/about.html` |
| `sicherheit.html` | `en/security.html` |

Die Liste steht **genau einmal**, in `PAIRS` in `_generate_layout.py`. Demo, Datenwerkstatt
und Forschung bleiben deutsch — Videos und Unterlagen dort sind deutsch. Impressum und
Datenschutz bleiben deutsch und sind aus dem englischen Fuß mit „(German)“ verlinkt;
deutsche PDFs und Videos tragen auf den englischen Seiten „(PDF, German)“ bzw. „Video in German.“

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
  *Site Assessment*, Analyse je Fehlerbild = *Defect Analysis* (bis 20.10.2026 Vorprojekt = *Feasibility Project*), Erstgespräch = *intro call*,
  Lohngalvanik = *job shop*, Ausschuss = *scrap*, Reklamation = *customer complaint*.
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
(`link-demo-startseite`) und `leistungen.html` in der Karte *Vorprojekt* (`cta-demo-vorprojekt`).
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

**Messung:** Der CTA traegt `data-funnel="cta-demo-seite"`, der Videostart meldet sich als
**`video-anwendung`** (aus `data-video="anwendung"` am iframe; die Erkennung in `consent.js` nimmt
das erste YouTube-iframe der Seite — auf `demo.html` gibt es genau eines, es ist nichts
anzupassen). Eingehende Links aus Mail und LinkedIn bekommen UTM-Parameter, damit der Verkehr im
Monatslauf trennbar bleibt.

## Datenwerkstatt-Seite (`ausbildung.html`) — Video und Zielgruppe *(11.09.2026)*

**Zielgruppe steht in der Kennzeile:** *„Weiterbildung fuer kleine Betriebe"*. Der Hero setzte
bis 11.09.2026 laufende Messtechnik voraus („In Ihren Anlagen laeuft die Messtechnik laengst
mit") und nannte die Begleitung nicht — beides ging an der Zielgruppe vorbei. **Dauerregel:
Auf dieser Seite ist die manuelle Erfassung der gleichwertige Fall**, nicht der Sonderfall;
wer hier Text aendert, prueft beide Wege (Steuerung *und* Badbuch von Hand) und nennt das
Coaching als Teil des Angebots. Derselbe Satz steht im Flyer (`AENDERUNGSPROZESS.md` Gate 4).

**Was drauf ist:** YouTube-ID **`-btKYAPGAqw`**, eingebunden ueber `youtube-nocookie.com`,
**direkt unter dem Hero** — vor der Nutzenliste, weil ein Besucher aus einer Mail zuerst sehen
will, wovon die Rede ist. Inhalt: das Badbuch aus `lehrmittel/demos/badbuch/` (nachgestellter
Verlauf, keine Betriebsdaten, kein Lieferantenname). Der Videostart meldet sich als
**`video-badbuch`** (`data-video="badbuch"`).

**Titel wortgleich halten:** Der YouTube-Titel lautet *„Digitale Badkarte mit KI aufbauen"*
(geprueft 11.09.2026 ueber `https://www.youtube.com/oembed?url=…`), das `title`-Attribut am
iframe ebenso. Wird er in YouTube Studio geaendert, wandert er hier mit — Seite und Video
muessen dasselbe versprechen.

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
Stand: Hauptknopf endet bei y 643, Banner ab 714 — **71 px Luft** *(gemessen 13.09.2026)*.

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

`_scripts/check_site.py` ist das "pyright der Homepage" (zero-dependency ausser
tinycss2) und prueft je Seite: HTML wohlgeformt, CSS parst sauber, alle
`var(--token)` aufloesbar, Layout-Marker vorhanden **und in Sync mit dem
Generator**, interne Links/Assets existieren, keine Transliterations-Reste im
Sichttext, englische Fassung auf deutschem Stand. Exit 1 bei Fehlern -> nicht deployen.
`check_inhalt.py` (Metadaten, Marker, Sitemap) steht in `AENDERUNGSPROZESS.md` Gate 1.

Optionaler Gegencheck bei groesseren Umbauten (Node, kein Java):
`npx --yes htmlhint *.html` und `npx --yes html-validate *.html en/*.html`.

## Projektstruktur

```
homepage/
  index.html               Predictive-Quality-Landing (ein roter Faden), Sektionen per grep 'id="' index.html.
                           Preise im #ablauf nur fuer die Einstiegsstufen (Standortanalyse, Analyse je
                           Fehlerbild; Umsetzung und Betreuung ohne Preis). KEINE Leistungs-Teaser-Karten.
  leistungen.html          Leistungsseite, handgeschrieben: Standortanalyse als Schwerpunkt, #datenanalyse
                           (Stufe 3 „Analyse je Fehlerbild“), #anwendungen, #fragen mit FAQPage-Schema,
                           Blanko-Angebote als PDF. Seit 31.08.2026 wieder eigene Seite -- Anlass: 87
                           GSC-Impressionen auf eine Weiterleitung, 0 Klicks auf kommerzielle Suchanfragen.
  demo.html                Landingpage fuer das Demo-Video (ein Zweck, ein CTA) — § Demo-Seite.
  ausbildung.html          Datenwerkstatt — Aus- und Weiterbildung, Reihenfolge Nutzen -> Ablauf ->
                           Beispiel -> Angebot (Partner stehen seit 21.10.2026 nur noch im
                           Streifen #partner der Startseite). Flyer dazu:
                           docs/datenwerkstatt-ueberblick.pdf — § Datenwerkstatt-Seite.
  forschung.html           Forschungsprojekte (FFG-Kleinprojekt, aws), aws-Jurytermin-Foto.
  sicherheit.html          Compliance-Seite (indexiert, in Sitemap und Footer, bewusst NICHT in der
                           Hauptnavigation). Nav/Footer aus _generate_layout.py (PAGES-Eintrag mit
                           None = kein eigener Nav-Punkt); nur das Seiten-CSS ist noch eigen.
  ueber-mich.html          Vollständiges Profil + Bio + Nachweise-Galerie
  nachweise.html           Redirect-Stub auf ueber-mich.html#nachweise (Instant-Meta-Refresh + Canonical, KEIN noindex)
  en/                      Englische Fassung: index, services, about, security. Nav/Fuss/hreflang/CSS
                           aus _generate_layout.py, der Text ist Handarbeit. en/_quelle/ = deutscher
                           Stand je Uebersetzung fuer check_englisch.py (Jekyll liefert es wegen des
                           Unterstrichs nicht aus). § Englische Fassung.
  impressum/ stefan-maier/ kontakt/ trusted-ai/ data-analytics/
                           Redirect-Stubs auf die WordPress-Alt-URLs — generiert aus _generate_redirects.py,
                           nicht von Hand editieren. Nur Pfade mit echtem Nachfolger; tote PDFs bleiben 404.
  termin/                  Kurzlink secure-galvano-ai.com/termin -> Bookings-Erstgespraech (fuer LinkedIn und
                           Mails; noindex, kein canonical) — aus SHORTLINKS in _generate_redirects.py
  impressum.html           Impressum (ECG/UGB) + Marken-Hinweis
  datenschutz.html         Datenschutzerklärung (DSGVO)
  404.html                 GitHub-Pages-Fehlerseite (noindex, nicht in Nav/Sitemap) — faengt Alt-URLs
                           der WordPress-Zeit ab. NUR absolute Pfade (/assets/...), weil Pages die Datei
                           auch fuer tiefe Pfade wie /wp-content/uploads/... ausliefert. Ohne Layout-Marker
                           (Generator erzeugt relative hrefs) und ohne JS.
  assets/
    img/                   Bild-Assets (Bestand: ls assets/img); Partnerlogos in kooperation/
    css/
      base.css             SINGLE SOURCE (§ Architektur) — jede Seite bindet es als erstes CSS ein
    js/
      consent.js           Opt-in-Consent-Gate für Microsoft Clarity + CTA-Funnel-Events
      site.js              Geteiltes Verhalten (§ Architektur)
  _scripts/                check_site.py (vor jedem Deploy), check_inhalt.py, check_englisch.py;
                           Messung (clarity_daily.py, youtube_abrufe.py, wochenbericht.py) -> OPTIMIERUNG.md
  _doku/                   Betriebsdoku, die nicht ausgeliefert wird (Unterstrich) — infrastruktur.md
  _generate_layout.py      Generator: Nav + Footer + WA-FAB + Sticky aus einer Quelle in die Marker-Bloecke aller Seiten
  _generate_redirects.py   Generator: Redirect-Stubs fuer WordPress-Alt-URLs (REDIRECTS-Dict = einzige Quelle) und Kurzlinks (SHORTLINKS)
  _generate_assets.py      Generator für Favicon/OG-Image (liest/schreibt assets/img/)
  credentials/
    _generate_credentials.py  Renderer: PDF -> JPG-Thumbs + Full (§ Deployment)
    thumbs/ full/          Grid-Thumbnails und Lightbox-Originale
  docs/                    Belege zum Verlinken und Mitschicken (Musterbefund, Flyer, Beispielauswertungen,
                           Methoden-und-Standards, Meisterbrief, Fachartikel, Praesentationen). Bewusst KEINE
                           Einzelliste hier -- sie driftet bei jedem neuen Beleg. Wo welcher verlinkt ist:
                           grep -o "docs/[a-z0-9_-]*\.pdf" *.html
                           Wird von Jekyll ausgeliefert -- hier nur, was oeffentlich sein darf.
                           Die erzeugten PDFs kommen aus BD-Build-Skripten und werden NIE von
                           Hand bearbeitet -- Aenderung im Skript, dann neu bauen. Erzeuger finden:
                             grep -rl "<dateiname>.pdf" "../Business Development/templates" \
                               "../Business Development/scripts" "../Business Development/areas"
                           (Flyer/Befunde unter templates/*-corporate/, Datenwerkstatt unter
                           areas/coaching-und-ausbildung/, NDA und die vier Angebots-Muster unter
                           scripts/ -- angebot_muster.py baut alle vier in einem Lauf).
                           Ausnahme: unternehmenspraesentation_secure-galvano-ai.pdf (DE) und
                           company-presentation_secure-galvano-ai.pdf (EN) kommen aus dem Pitch-Deck-
                           Master auf SharePoint: 01_Aussenauftritt/06_Praesentationsmaterialien/
                           Pitch Deck/03_Decks/_Werkzeuge/download_bauen.py, Ablauf im 00_LIESMICH.md
                           dort ("Zwei abgeleitete Fassungen"). Dateinamen NICHT aendern -- consent.js
                           bildet das Clarity-Ereignis aus dem Dateinamen.
                           Angebots-Muster = das verbindliche Kundendokument im Muster-Modus (ohne
                           Empfaenger, Nummer, Datum, IBAN, Unterschrift); die Pruefung laeuft dort
                           UMGEKEHRT und schlaegt an, wenn eine dieser Angaben doch drinsteht
                           (Docstring BD/scripts/angebot_bauen.py). Jedes Skript prueft Seitenzahl
                           und Pflichtstellen und bricht ab, wenn Inhalt verschluckt wird
                           (overflow:hidden schnitt beim ersten Lauf die Fusszeile lautlos ab).
  fonts/                   fonts.css + Montserrat/Open Sans als WOFF2 (latin, latin-ext), OFL
  favicon.ico              Browser-Tab Icon (Root — Browser-Konvention)
  apple-touch-icon.png     iOS Home Screen Icon (Root — Konvention)
  CNAME                    Custom Domain Config — nicht löschen (_doku/infrastruktur.md)
  _config.yml              Nur exclude: haelt README/OPTIMIERUNG/AENDERUNGSPROZESS aus der Auslieferung — nie docs/ eintragen
  robots.txt               Crawler-Erlaubnis
  sitemap.xml              Google Sitemap (13 URLs, davon 4 englisch -- Stand 12.10.2026)
  README.md                Diese Datei
```

## Search Console / Indexierung

> Der **monatliche Optimierungslauf** (Clarity + Search Console, Kennzahlen, Entscheidungsregeln,
> Zugaenge) steht in [`OPTIMIERUNG.md`](OPTIMIERUNG.md). Dieser Abschnitt hier deckt nur die
> Indexierungs-Sonderfaelle ab.

Der Bericht **Seitenindexierung** meldet regelmaessig „nicht indexierte Seiten". Die
meisten Eintraege sind **Soll-Zustand**, kein Defekt. Einordnung vor jeder Reaktion:

| Meldung | Ursache | Zu tun |
|---|---|---|
| **Nicht gefunden (404)** | Alt-URLs der WordPress-Installation bei IONOS. Instanz ist mit dem Vertragsende **02.06.2026** weg. Kein Link im Repo zeigt darauf (`check_site.py` prueft das). | Zweiteilen: Alt-URL **mit** heutigem Pendant -> Redirect-Stub in `_generate_redirects.py` eintragen. Alt-URL **ohne** Pendant (tote PDFs, `/wp-*.php`-Bot-Scans) -> nichts tun, 404 ist der korrekte Endzustand. |
| **Durch „noindex"-Tag ausgeschlossen** | Keine Inhaltsseite der Website traegt `noindex`. Frueher zurueckgestellte Seiten koennen noch eine Weile hier auftauchen, bis Google neu crawlt. | Nichts. Haengt eine Seite nach Wochen noch hier, einmalig „Indexierung beantragen". |
| **Alternative Seite mit richtigem kanonischen Tag** | `/index.html` vs. `/` — Canonical zeigt korrekt auf `/`. | Nichts. |
| **Gecrawlt / Gefunden – zurzeit nicht indexiert** | Googles Qualitaets-/Budget-Entscheidung, kein technischer Fehler. Einziger echter SEO-Hebel im Bericht. | Betroffene URL in der URL-Pruefung ansehen, Inhalt schaerfen (eigenstaendiger Text, interne Verlinkung), dann **„Indexierung beantragen"**. Nicht wiederholt beantragen. |

**„Behebung validieren" bei 404 nicht klicken.** GSC validiert nur gegen 200/Redirect.
Solange auch nur eine legitim tote URL in der Gruppe steckt, schlaegt der Lauf
zwangslaeufig fehl — das erklaert den Status „Fehlgeschlagen" vom 25.07.2026, nicht ein
Defekt auf der Seite. Google dropt solche URLs nach ~4–8 Wochen selbst; wer es
beschleunigen will, nimmt `Entfernungen → Neuer Antrag → Praefix` fuer `…/wp-content/`.

**Redirects auf GitHub Pages.** Server-seitige 301 gibt es nicht. Google behandelt den
**Instant-Meta-Refresh** (`content="0; url=…"`) laut Doku als permanenten Redirect und
nennt ihn ausdruecklich als Ersatz, wenn server-seitige Redirects nicht implementierbar
sind. Genau das erzeugt `_generate_redirects.py` — plus `rel=canonical` und einen
sichtbaren Link als No-JS-Fallback.

**Kein `noindex` auf Redirect-Stubs.** `noindex` blockt die URL komplett aus der Suche
und verhindert damit, dass Google den Refresh ueberhaupt als Redirect verarbeitet;
zusammen mit `rel=canonical` sind es widerspruechliche Signale auf derselben URL.
`noindex` gehoert nur auf zurueckgestellte **Inhalts**seiten mit Self-Canonical.

**Sitemap:** `lastmod` beim Deploy auf das tatsaechliche Aenderungsdatum ziehen
(`git log -1 --format=%ad --date=short -- <datei>`) — veraltete Werte kosten Crawl-Prioritaet.

## DNS-Konfiguration, IONOS und Systemabhängigkeiten

Ausgelagert nach [`_doku/infrastruktur.md`](_doku/infrastruktur.md) *(15.10.2026)*: Soll-Stand
beider Zonen (`secure-galvano-ai.com`, `rvh.at`), Endstand der Absenderauthentifizierung
(`p=quarantine`, warum kein `p=reject`), IONOS-Vertrag, Login-Wiederherstellung, der Vorfall vom
17.08.2026, „Was bricht was" und der Routine-Check nach jeder IONOS-Aktion.

## Corporate Design Assets

| Asset | Pfad |
|-------|------|
| **Logo (groß)** | `BD/areas/brand/logo.png` |
| **Logo (Header)** | `BD/areas/brand/logo_header.png` |
| **Porträt** | Quelle: `Stefan Maier - Dokumente/02_Unterlagen/04_Fotos/MICHAELKREYER/` |
| **Corporate Design Doku** | `BD/areas/brand/corporate_design.md` |

Farben und Schriften der Website: § *Architektur* (Tokens in `assets/css/base.css :root`).

## Externe Services

| Service | Zweck | Link |
|---------|-------|------|
| Microsoft 365 | Mail `smaier@rvh.at`, Tenant **PhonixData** | `admin.microsoft.com` · DKIM: `security.microsoft.com` |
| Microsoft Bookings — **der Link der Website** *(umgestellt 14.09.2026)* | Erstgespräch buchen, **30 Min.**, buchbar Mo 13–17, Di/Mi 9–19, Do 9–14 *(eigene Zeiten im Dienst, Stefan 01.10.2026)*; optionale Frage „Wie sind Sie auf uns aufmerksam geworden?" seit 01.10.2026 (Herkunftsmessung, Antwort steht im Outlook-Termin) — läuft auf dem rvh.at-Tenant. Dienst `secure galvano ai - unverbindliches Erstgespräch`. Gepflegt wird in `_generate_layout.py` die Konstante `BOOKING_URL` | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/DdIPgTj7-0ymr6eHc38SQg2` |
| Microsoft Bookings — **der Link der `/en/`-Seiten** *(15.10.2026)* | Dasselbe Erstgespräch auf Englisch: Dienst `secure galvano ai - free intro call`, **Sprache English (United States)**, sonst eine Kopie des deutschen Dienstes (Zeiten, Teams, Erinnerungen) mit eigenen englischen Fragen. **Warum ein eigener Dienst:** Bookings richtet Oberfläche, Fragen und Bestätigungsmail nach der Sprache des **Dienstes**, nicht nach dem Browser. Die Fragen sind in Bookings dienstübergreifend — eine deutsche Frage umzuformulieren ändert sie im deutschen Dienst mit. Konstante `BOOKING_URL_EN`, maßgeblich `stammdaten.buchung_en`. **Die Kopie zieht nicht mit:** Wer Zeiten, Dauer, Beschreibung oder Fragen am deutschen Dienst ändert, ändert den englischen im selben Zug | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/ZivH8iyBokGAiByKXkWuqA2` |
| Microsoft Bookings — **Arbeitstermin** *(30.09.2026, seit 02.10.2026 `secure galvano ai - Arbeitstermin`)* | Arbeitstermine im laufenden Projekt — Coaching wie IT eines Kunden, **1 Std.**, Teams, ohne Preis. **Nie auf der Website verlinken** — der Link steht nur im Angebot (`stammdaten.buchung_coaching`, Begründung in `BD/areas/coaching-und-ausbildung/README.md` § Angebot und Ablauf) | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/WguGbyr1pUWQxZrPA0ISQA2` |
| Microsoft Bookings — Sammel-Buchungsseite | Zeigt **alle sichtbaren Dienste zur Auswahl** — Erstgespräch, Arbeitstermin und seit 15.10.2026 der englische Intro call. Der Arbeitstermin muss sichtbar bleiben: **Bookings sperrt einen ausgeblendeten Dienst auch über seinen Direktlink** („Wir bieten im Moment keine Dienste … an", geprüft 30.09.2026). **Die Website verlinkt deshalb nur den Dienst-Direktlink des Erstgesprächs** — der zeigt nur diesen einen Dienst (geprüft ohne Anmeldung, 30.09.2026) | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/` |
| Microsoft Bookings — Kurzgespräch 30 Min. *(03.09.2026, abgelöst · seit 21.09.2026 ausgeblendet)* | Erster Akquise-Dienst, **1:N-Gruppendienst** — deshalb fehlten Name und Mailadresse des Buchenden im Outlook-Termin und Fremde konnten in denselben Slot buchen. **Ausgeblendet, nicht gelöscht**, weil der Termin vom 14.09. daran hängt; der Direktlink führt seitdem ins Leere. Der Typ 1:1/1:N wird beim Anlegen festgelegt und ist danach **nicht änderbar** | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/j9sT4U4iQ0WwxD0oCfcdeg2` |
| Microsoft Clarity | Web-Analyse (Opt-in, Projekt `wql3vpgrxl`) | `clarity.microsoft.com` |
| Google Search Console | SEO / Indexierung | `search.google.com/search-console` |
| GitHub Pages | Hosting + TLS-Zertifikat | `github.com/secure-galvano-ai/homepage/settings/pages` |
| IONOS | **Domain-Registrar und DNS-Betreiber** — Login über Kundennummer, nicht über die Mailadresse | `my.ionos.de` · Service `0721 170 555` |

> Alle Abhängigkeiten zwischen diesen Diensten stehen in
> [`_doku/infrastruktur.md`](_doku/infrastruktur.md) § *Systeme und Abhängigkeiten*.

## Deployment

Push auf `main` → GitHub Pages deployed automatisch (~1 Min).

```bash
cd homepage
git commit -m "Beschreibung" -- <nur die eigenen Dateien>   # nie -A, fremde Arbeit bleibt draussen (AGENTS.md §5)
git push
```

**KEIN GPG-Signing in diesem Repo** (reines Content-Repo, lokal `commit.gpgsign false`) —
Commits laufen ohne Yubikey-PIN-Dialog.

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
   Trigger cancelt ihn. Hängt er als Zombie (`queued`, nicht cancelbar, > 30 Min) → genau dieser
   POST ist der Ausweg. `githubstatus.com` meldete dabei durchgehend „operational", taugt also
   nicht als Entscheidungsgrundlage.
3. **NIEMALS mehrere Pages-Deploys schnell hintereinander triggern.** Die Concurrency-Gruppe `pages` hat **Queue-Tiefe 1** — jeder neue Deploy **cancelt den vorher wartenden**. Rapides `git push` + wiederholtes `gh api --method POST .../pages/builds` erzeugt eine Kaskade aus `Deployment cancelled`/`failure`. → **EINMAL pushen, dann 2–10 Min ungestört warten. Nicht nachtreten.**
4. **Bei Fehler zuerst die LIVE-Seite prüfen, nicht blind retrien** (letzter guter Build bleibt live, meist schon korrekt): `curl -s https://secure-galvano-ai.com/ | grep -o '<h1>[^<]*'`
5. **`.nojekyll` NICHT reflexartig hinzufügen.** Der Jekyll-`build` gelingt hier (getestet); `.nojekyll` löst das Deploy-Problem NICHT und liefert zusätzlich `_generate_*.py` **öffentlich** aus (Jekyll schließt `_`-Dateien sonst aus). → **ohne `.nojekyll` bleiben.**
6. **Kein `{{ … }}` / `{% … %}` im HTML** — Jekyll/Liquid parst das und failt den *Build* (war hier NICHT die Ursache, ist aber die klassische echte Build-Bremse).

Favicon/OG-Image neu generieren: `py _generate_assets.py`. Nachweise neu rendern (wenn das
Quell-PDF aktualisiert wird): `py credentials/_generate_credentials.py`. Quelle: `Business Development/resources/credentials/20260512_Lebenslauf & Nachweise_Stefan Maier.pdf`.
Seitenauswahl und Metadaten (Titel, Untertitel, Kategorie pro Seite) stehen in
`credentials/_generate_credentials.py` — Reihenfolge dort ändern. Schwärzungen (Liste
`REDAKTIONEN`) gehören in den Erzeuger, nicht ins fertige Bild (`CLAUDE.md` §1 *Was öffentlich
gestellt wird*).

## WhatsApp-Kontakt — abgeschaltet seit 07.09.2026

Der Floating-Button ist **entfernt** (Stefan): Er trug die private Mobilnummer im Klartext auf
jeder Seite — Folge waren laufende Phishing-Anfragen. Auch `telephone` ist aus dem Schema.org-Block
raus; **eine Telefonnummer steht nirgends mehr auf der Website** (§ 5 ECG erfüllt die E-Mail im
Impressum). Kontaktweg: Erstgespräch-Buchung + mailto.

Mechanik: `_generate_layout.py` rendert den `wa-fab`-Block leer, die Marker bleiben. Zurückholen =
`render_wa_fab()` wieder auf die Link-Fassung (die Nummer liegt bewusst nicht mehr im Repo);
`.wa-fab`-CSS in `base.css` und die Logik in `consent.js` bleiben ungenutzt liegen.
