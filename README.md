# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.com
**HTTPS:** Aktiv (GitHub Pages + Let's Encrypt)
**Hosting:** GitHub Pages (kostenlos)
**Stand:** 2026-07-02

---

## Setup (erledigt)

- [x] GitHub Pages Repo + Deployment
- [x] Custom Domain `secure-galvano-ai.com` verbunden
- [x] DNS bei IONOS umgestellt (4x A-Record + CNAME)
- [x] HTTPS erzwungen
- [x] IONOS Zusatzartikel gekündigt (Domain Guard, Mail Business, SSL)
- [x] IONOS WordPress-Vertrag läuft am **02.06.2026** aus, Domain bleibt
- [x] Impressum + Datenschutz (ECG/DSGVO-konform)
- [x] Gründer-Section mit Porträt + Bio
- [x] Microsoft Bookings Kalender-Link
- [x] LinkedIn-Profil verlinkt
- [x] AWS Deep Tech Badge
- [x] Favicon + Apple Touch Icon
- [x] Open Graph Tags (Social Media Sharing)
- [x] robots.txt + sitemap.xml
- [x] Google Search Console verifiziert + Sitemap eingereicht
- [x] WhatsApp-Floating-Button auf allen Pages (private Nummer aus CV)
- [x] Nachweise als Sektion auf `ueber-mich.html` (16 Zertifikate, Lightbox); `nachweise.html` ist Redirect-Stub
- [x] `ueber-mich.html` als vollständiges Profil + Bio + Nachweise (2026-05-02)
- [x] 8-Wochen-Diagnose mit Festpreis 9.500 € netto (Briefing 2026-05-12)
- [x] FAQ-Section, Pakete-Section, Ablauf-Section
- [x] JSON-LD Structured Data (LocalBusiness, Person, Service, FAQPage)
- [x] Galvano-Forum-2026-Portrait + Forschungsvorhaben-Präsentation als PDF-Downloads (`docs/`)
- [x] **Microsoft Clarity, Opt-in-Consent** — `consent.js` laedt Clarity nur nach Zustimmung, Funnel-Events auf den CTAs, Widerruf via Footer-Link (2026-05-14)
- [x] Trust-Bar mit echten Logos (aws Deep Tech + TRUSTIFAI by TÜV AUSTRIA) (2026-05-13)
- [x] Cost-of-Inaction-Streifen, Datenfluss-Grafik, Fachpresse-Platzhalter (2026-05-13)
- [x] **Self-Hosted Fonts** (Montserrat + Open Sans lokal, kein Google-Fonts-Request) (2026-05-13)
- [x] `ausbildung.html`: Entscheider-/Geschäftsführungs-Zielgruppe + Förderhinweis ergänzt — Ausrichtung auf DGO-FA "Digitale Transformation und Innovation" (digitale Optimierung + Fördermöglichkeiten) (2026-05-24)
- [x] `ausbildung.html`: als **Basis-Kurs** positioniert (Entwicklungsumgebung als Fundament, Aufbaustufen folgen) + Durchführung **ab 4 Teilnehmern** (Gruppe-Eckdaten + Pilot-Badge) (2026-05-24)
- [x] `index.html`: schlanke "Zweiter Weg"-Brücke nach der Trust-Bar — holt proaktive "Digitalisierung-vorantreiben"-Betriebe ab (ohne akuten Schmerz) und leitet zu Praxiskurs + Folgewege, Hero bleibt schmerz-first (2026-05-24)
- [x] `index.html`: "Zweiter Weg"-Streifen zur Sektion **Datendienstleistungen** (`#datendienste`) ausgebaut — "Data Scientist auf Zeit"-On-Ramp für Betriebe ohne strukturierte Datenbasis, mit "Auf Anfrage"-Badge + Mailto-Anfrage (kein neues Backend, reuse Bookings + mailto-Pattern) (2026-05-29)
- [x] **Customer-Journey-Reorder (evidenzbasiert, B2B-CRO-Recherche)** (2026-05-29):
  - Neue **3-Kachel-Leistungsübersicht** (`#leistungen`) direkt nach Trust-Bar — Self-Select-Onramp (Diagnose dominant, Daten/Praxiskurs dezent); Hero bleibt schmerz-first
  - Hero-Sekundär-Button → "Leistungen ansehen ↓" (`#leistungen`, kein Duplikat zu Diagnose-Kachel, Scroll-Cue)
  - **PAS-Reihenfolge:** 3 Symptome (Agitate) jetzt VOR Cost-of-Inaction
  - **Datendienste-Vollblock** von oben nach unten (hinter Angebot) — konkurriert nicht mehr früh mit Haupt-Conversion
  - **Mid-Scroll-CTA** ("Verfügbarkeit anfragen") an der Pull-Quote
  - Versteckter **Kundenstimmen-/Referenz-Slot** in der Pull-Quote-Sektion (auskommentiert, aktivieren nach Pilotkunden-Freigabe)
  - **Sticky-Mobil-CTA** (`#stickyCta`, erscheint ab 700px Scroll, nur ≤760px; WhatsApp-FAB weicht aus)
  - **Funnel-Tracking** in `consent.js`: Kachel-Klicks (`data-funnel`) + Mid-Scroll-CTA + Scroll-Tiefe (25/50/75/100 %) als Clarity-Events (nur nach Consent)
- [x] **Fokussierung (2026-07-02):** Seite auf den Kern-Funnel verschlankt.
  - `ausbildung.html` + `sicherheit.html` **zurückgestellt** — `noindex`, raus aus Nav/Footer/Sitemap; Dateien bleiben erhalten und sind jederzeit reaktivierbar (Nav-`<li>` wieder einsetzen + Sitemap-Eintrag + `noindex` entfernen).
  - Leistungen von 6 auf **3 Kern-Bausteine** reduziert (KI-Diagnose, Live-Monitoring, KPI-Dashboard) — Datenquelle `LEISTUNGEN` in `_generate_leistungen.py`, danach `py _generate_leistungen.py`.
  - Sicherheits-Inhalt als **Corporate-PDF** `docs/sicherheit-methoden-standards.pdf` (Statement „Methoden & Standards"), verlinkt in der Trust-Bar (Startseite) und im Footer. Quelle/Build: `Desktop/sga_pdf_build/` (Pandoc + XeLaTeX via `templates/pdf-corporate/build_pdf.py`, kundentaugliches `_statement_template.tex`).

- [x] **Fokussierung auf EINE Botschaft (2026-07-30)** — ausgeloest durch 60 Tage Clarity-Daten
  (104 Sitzungen, **0 Klicks** auf den Buchungs-CTA, 15 % erreichten den Abschluss-Bereich).
  - **Neue Sektion `#ablauf` „So arbeiten wir zusammen"** — die sechsstufige Vertriebsleiter aus
    `BD/areas/business-model.md` (Stand 29.07.), **ohne Preise**. Schliesst die Luecke, dass die
    Website die **Standortanalyse** (Pflicht-Gate vor jedem Festpreis) gar nicht kannte und direkt
    die 8-Wochen-Diagnose versprach. Ersetzt die Sektionen „Die Diagnose auf Ihren eigenen Daten"
    und „Noch nicht so weit für einen Termin?" — beide gingen darin auf.
  - **Faehigkeiten-Treppe verdichtet** — aus drei Karten wird eine Aussage plus kompakte
    3-Schritt-Leiste. Zwei nummerierte Treppen auf einer Seite waren die groesste Redundanz.
  - **Datenflut + Datenhoheit zusammengelegt** (waren zwei Sektionen, eine Botschaft).
  - **Ergebnis: 9 Sektionen → 8, Seitenlaenge 9,8 → 7,2 Bildschirme (−27 %)**, Haupt-CTA von
    85 % auf 75 % Scrolltiefe. Kein horizontaler Ueberlauf, keine Tap-Ziele < 44 px (mobil geprueft).
  - **Ton durchgaengig auf Kundennutzen** (Vorgabe Stefan): im Ablauf-Block keine einzige Ich-Form
    mehr. Aus „Ohne diesen Schritt nenne ich keinen Festpreis" wird „Ihren Festpreis bekommen Sie
    danach auf belastbarer Grundlage statt auf Verdacht".
  - **Erstgespraech 30 → 60 Minuten**, seitenweit angeglichen (auch `ueber-mich.html` + Bookings).
  - **Diagnose: 8 Wochen → innerhalb einer Woche.** Der Ablauf-Block auf `leistungen.html` heisst
    jetzt „Ablauf in zwei Schritten"; die alten Phasen bildeten die neue Leiter bereits ab
    (Phase 1 „Verstehen" = Standortanalyse, Phase 2 „Auswerten" = Diagnose). **Der Produktname
    bleibt „Diagnose"** — `business-model.md` legt das ausdruecklich fest; „Proof of Concept" ist
    die Funktion, nicht der Kundenname (und Beraterjargon auf einer deutschen Seite).
    ⚠ **`BD/areas/business-model.md` fuehrt Stufe 3 weiter mit 8 Wochen / 9.500 € — muss nachgezogen
    werden**, sonst widersprechen sich Website und Angebotsvorlage.
  - **Je Phase ein Beleg zum Selbstbedienen** statt nur „Termin buchen": Beispiel-Auswertung
    (Stufe 2), Unternehmenspraesentation (Stufe 3), Sicherheits-PDF (Stufe 5). Grundlage:
    Gartner via Vereigen Media — *75 % der B2B-Einkaeufer bevorzugen einen rep-free Kaufprozess*;
    HubSpot — oben im Trichter gehoert Aufklaerung hin, das Beratungsgespraech ans Ende.
  - **WhatsApp-FAB eingeklappt** (`base.css`) — der dauerhaft sichtbare ganze Satz konkurrierte mit
    dem primaeren CTA; 358 px → 72 px, Beschriftung klappt bei Hover/Fokus auf. Kanal bleibt.
  - **Vor-Ort-Tag entfernt** (Startseite + Leistungen) — als Produkt am 28.07. gestrichen, stand aber
    noch direkt neben dem Haupt-CTA. Auf der Leistungsseite ersetzt durch den Hinweis auf die Standortanalyse.
  - **Tracking differenziert** — bisher feuerten alle vier Buchungs-CTAs denselben Event-Namen, die
    Position war nicht ablesbar. Jetzt je Position ein eigener: `cta-nav`, `cta-hero`, `cta-ablauf`,
    `cta-abschluss`, `cta-sticky`, `cta-whatsapp-fab`, `mail-abschluss`. Dazu neu: `pdf-<dateiname>`
    je Download und `video-gestartet`. Ausserdem gefixt: nach „Cookie-Einstellungen → erneut
    akzeptieren" wurden die Funnel-Listener nie gesetzt.

- [x] **Presse-/Aktuell-Sektion (2026-08-10)** — VN-/VOL.AT-Bericht vom 06.08.2026
  („Alberschwender Ingenieur entwickelt Prüf-Software, die mit KI immer besser wird",
  Andreas Scalet) eingebunden.
  - **Neue Sektion `#aktuell` auf `index.html`**, direkt **nach der Trust-Bar** — bewusst hoch:
    laut Clarity erreichen nur ~15 % den unteren Seitenbereich, eine News-Sektion im Fuss waere tot.
    Zwei Karten: **Pressestimme** (Headline + Kurzzitat + Quelle) und **Termin** (KI Days Vorarlberg,
    28.–30.09.2026, Forum Vorarlberg / Campus V Dornbirn) als Dringlichkeits-Anker mit
    eigenem Funnel-Event `cta-aktuell-termin`; darunter das Knappheits-Zitat aus dem Artikel
    („in der Tiefe statt in der Breite") — **fremdbelegt statt selbst behauptet**.
  - **`ueber-mich.html`:** Sektion `#fachpresse` heisst jetzt „Presse & Veröffentlichungen",
    Medienbericht als erste, volle Breite einnehmende Karte ueber den beiden Leuze-Fachartikeln.
  - **Bewusst OHNE Link/PDF.** Der VOL.AT-Artikel liegt hinter der Bezahlschranke — ein Button
    dorthin fuehrt Besucher gegen eine Paywall, das ist schlechter als kein Button. Der Volltext
    (auch als Scan oder nachgebautes PDF) darf **nicht** selbst gehostet werden: Nachdruck-/
    Online-Rechte liegen bei Russmedia/VN, Zitatrecht deckt nur Kurzzitate. Stattdessen
    „Pressestimme"-Karte: Kurzzitat + Blattname + Autor + Datum. **Button-Slot liegt
    auskommentiert im Code** (`index.html`, `ueber-mich.html`, Marker `VOLAT_ARTIKEL_URL`) —
    einkommentieren, sobald eine frei zugaengliche URL oder eine schriftliche Verlagsfreigabe
    vorliegt.
  - **Urheberrecht generell:** nur Kurzzitate + Quellenangabe. **Keine VN-Fotos** (©Fa/Demako, ©FA)
    und **kein VOL.AT-Logo als Bild** — Quellen-Nennung als Text. Beim Nachpflegen beibehalten.
  - **Pflegeregel:** max. 2 Karten in `#aktuell`, veraltete ersetzen statt stapeln. Ist kein
    Termin offen, Karte 2 durch die naechste Neuigkeit tauschen — eine sichtbar veraltete
    News-Sektion schadet mehr als keine. **Nach dem 30.09.2026 ist die Termin-Karte abgelaufen.**

- [ ] **Bewusst offen: `docs/portrait_galvano_forum_2026.pdf`** (Entscheidung Stefan, 11.08.2026)
  Der Referenten-Beitrag im Galvano Forum 2026 sagt im Text „Trusted-AI-**Zertifizierung** des
  TUeV Austria“ und firmiert als „Stefan Maier **e.U.**“. Beides weicht von der sonst
  durchgehaltenen Linie ab — korrekt sind **Modellpruefung** und die Firmierung ohne e.U.
  Das Heft ist gedruckt, die gehostete Fassung bleibt vorerst verlinkt; der Widerspruch wird
  bewusst getragen. **Nicht erneut als Befund melden.** Beim naechsten Nachdruck oder einer
  Neuauflage des Beitrags mitkorrigieren.

- [x] **Erster Optimierungslauf (2026-08-10)** — Grundlage: 28 Tage Clarity (95 Sitzungen) + GSC
  (47 Klicks, +422 % durch den VN-Bericht). Ablauf und Regeln ab jetzt in [`OPTIMIERUNG.md`](OPTIMIERUNG.md),
  monatlich per `/optimierung`.
  - **Messung repariert.** `consent.js` verdrahtete jeden Buchungs-/Mail-/WhatsApp-Link doppelt:
    einmal generisch (`cta-erstgespraech`), einmal positionsgenau ueber `data-funnel`. Ein einzelner
    Klick sah dadurch aus wie zwei, die Zahlen waren weder summierbar noch vergleichbar. Generische
    Selektoren entfernt; Voraussetzung dafuer waren **7 bisher ungetrackte CTAs** (u. a. der
    Abschluss-Button auf `ueber-mich.html`, die Forschungs-Mail, vier Links auf `sicherheit.html`).
    Ebenso raus: das Inline-`onclick` `pdf_download_beispiel` auf `forschung.html` und die
    PDF-Doppelbenennung (`a[href$=".pdf"]:not([data-funnel])`).
  - **Zweiter Hero-Button ist jetzt ein Angebot statt eines Sprungankers** — Musterbefund-PDF
    (`pdf-musterbefund-hero`). Der Verkehr kommt presse-/namensgetrieben, also in der
    Orientierungsphase; 45 % der Sitzungen erreichen nicht einmal 25 % Scrolltiefe, der Beleg lag
    vorher erst bei ~60 %. Belege wurden im Messzeitraum ~10-mal abgerufen, ein Termin einmal geklickt.
  - **`forschung.html` hat einen Kunden-Pfad bekommen** — drittstaerkste Seite (17 Aufrufe), vorher
    ohne jeden Ausgang fuer Betriebe; der vorhandene Mailto richtet sich an Forschungspartner.
  - **Klickfalle in der Presse-Karte beseitigt** — fett gesetzte Artikel-Ueberschrift ohne Ziel neben
    einer optisch gleichen Karte *mit* Button (15,8 % tote Klicks). Karte hat jetzt ein echtes Ziel
    (`ueber-mich.html#fachpresse`). Der VOL.AT-Button bleibt auskommentiert, bis eine frei
    zugaengliche URL vorliegt.
  - **Gruendungsdatum 01.05.2025** ergaenzt (Impressum + Werdegang) — wurde extern angefragt.
  - **Sitemap-`lastmod`** auf den tatsaechlichen Stand gezogen.
  - ⚠ **`check_site.py` meldet zwei tote Verweise auf `VOLAT_ARTIKEL_URL`** — beide stehen in
    HTML-Kommentaren, der Pruefer entfernt Kommentare nicht. Falscher Alarm, kein Defekt.

- [x] **Konsolidierung auf EINE Seite (2026-07-30, Entscheidung Stefan):** `leistungen.html`
  aufgeloest, alles auf der Startseite. Nach dem Fokus-Umbau war der Grossteil ohnehin redundant —
  die sechs Schritte deckten Ablauf und Folgewege ab, die Einwand-Kacheln vier der neun FAQ.
  **Uebernommen wurde nur das Nicht-Redundante:** drei FAQ (Datenlage, uneindeutige Ursache,
  mehrere Standorte) als eingeklapptes Accordion + Datenhoheit als fuenfte Kachel. Die drei
  Demo-Videos haengen jetzt an den Schritten 3, 4 und 6. FAQPage-Schema von `leistungen.html`
  nach `index.html` uebernommen (Rich-Result-Faehigkeit bleibt). Nav und Footer zeigen auf
  `index.html#ablauf`, Sitemap 6 -> 5 URLs, `_generate_leistungen.py` stillgelegt.
  **Kosten: 7,4 -> 7,8 Bildschirme** (+0,4 fuer eine ganze aufgenommene Seite, weil die FAQ
  eingeklappt ist). Haupt-CTA bei 71 %.

## Optional (noch offen)

- [ ] Weitere Unterseiten (Trusted AI, Downloads)

---

## Architektur (Single-Source, seit 2026-07-03)

Gemeinsame Bausteine liegen **an genau einer Stelle** und werden nicht mehr pro
Seite dupliziert. Wer Farben, Nav oder Footer aendert, editiert **eine** Quelle:

| Baustein | Single Source | Wird genutzt von |
|----------|---------------|------------------|
| Design-Tokens (Farben) + Reset + Typo + Container + Nav + Buttons + section-header + Footer + WA-FAB + Sticky-CTA + fade-up | `assets/css/base.css` | jede Seite (erstes CSS im `<head>`) |
| Geteiltes Verhalten (Nav-Scroll, Mobile-Menue, fade-up) | `assets/js/site.js` | jede Seite (`defer`) |
| Nav + Footer + WA-FAB + Sticky (HTML) | `_generate_layout.py` -> Marker `<!-- BEGIN/END nav -->` usw. | index, leistungen, ueber-mich, forschung, impressum, datenschutz |
| Leistungs-Karten | `_generate_leistungen.py` -> Marker | leistungen.html |

Die Markenfarben in `base.css :root` sind **kanonisch abgeleitet** aus
`Business Development/areas/brand/corporate_design.md`. Aendern sich Markenfarben,
wird NUR `base.css` editiert. Seiten-spezifisches CSS (Hero, einzelne Sektionen)
bleibt im `<style>`-Block der jeweiligen Seite.

**Nicht migriert (bewusst):** `ausbildung.html` + `sicherheit.html` sind
zurueckgestellt (noindex, nicht in Nav/Sitemap) und tragen weiter ihr eigenes
CSS. Zum Reaktivieren: in `_generate_layout.py` PAGES + NAV_LINKS ergaenzen,
Marker in die Seite setzen, `py _generate_layout.py` laufen lassen.

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
Sichttext. Exit 1 bei Fehlern -> nicht deployen.

Optionaler zweiter/dritter Validator (Node, kein Java noetig), als unabhaengiger
Gegencheck bei groesseren Umbauten:

```bash
npx --yes htmlhint *.html
npx --yes html-validate index.html leistungen.html ueber-mich.html forschung.html impressum.html datenschutz.html
```

## Projektstruktur

```
homepage/
  index.html               Predictive-Quality-Landing (ein roter Faden, KEINE Preise): Hero, Gruender-Stimme, Proof (TUeV/8-von-10), Schmerz, 3-Stufen-Treppe Fehlersuche->Live->Frueherkennung (#so-funktionierts), Diagnose-Angebot ohne Preis (#angebot), Kontakt (#kontakt). Traegt KEINE Leistungs-Teaser-Karten mehr.
  leistungen.html          Redirect-Stub auf index.html#ablauf (aufgeloest 2026-07-30, alles auf EINE Seite).
                           Vollstaendige Seite: git show 78ce8c3:leistungen.html
  ausbildung.html          Redirect-Stub auf die Startseite (Praxiskurs = Saeule 2, bis 2027 eingefroren).
                           Kursinhalt reaktivieren: git show feed14a:ausbildung.html
  sicherheit.html          Zurueckgestellt (noindex, nicht in Nav/Sitemap) — ersetzt durch docs/sicherheit-methoden-standards.pdf
  ueber-mich.html          Vollständiges Profil + Bio + Nachweise-Galerie
  nachweise.html           Redirect-Stub auf ueber-mich.html#nachweise (Instant-Meta-Refresh + Canonical, KEIN noindex)
  impressum/ stefan-maier/ kontakt/ trusted-ai/ data-analytics/
                           Redirect-Stubs auf die WordPress-Alt-URLs — generiert aus _generate_redirects.py,
                           nicht von Hand editieren. Nur Pfade mit echtem Nachfolger; tote PDFs bleiben 404.
  impressum.html           Impressum (ECG/UGB) + Marken-Hinweis
  datenschutz.html         Datenschutzerklärung (DSGVO)
  404.html                 GitHub-Pages-Fehlerseite (noindex, nicht in Nav/Sitemap) — faengt Alt-URLs
                           der WordPress-Zeit ab. NUR absolute Pfade (/assets/...), weil Pages die Datei
                           auch fuer tiefe Pfade wie /wp-content/uploads/... ausliefert. Ohne Layout-Marker
                           (Generator erzeugt relative hrefs) und ohne JS.
  assets/
    img/                   Bild-Assets: logo, portrait, aws, trustifai, og-image,
                           techniker-monitoring, stefan-entmetallisierung-2006
    css/
      base.css             SINGLE SOURCE: Tokens + Reset + Typo + Container + Nav + Buttons + section-header + Footer + WA-FAB + Sticky + fade-up (jede Seite bindet es als erstes CSS ein)
      leistungen.css       Geteilte Komponenten-CSS für die Leistungsbausteine (Karten + Mail-Button); genutzt von leistungen.html
    js/
      consent.js           Opt-in-Consent-Gate für Microsoft Clarity + CTA-Funnel-Events
      site.js              Geteiltes Verhalten: Nav-Scroll-Schatten, Mobile-Menue-Toggle, fade-up-Scroll-Animation
  _scripts/
    check_site.py          Self-Check (HTML/CSS/Tokens/Marker-Sync/Links/Transliteration) — vor jedem Deploy laufen lassen
  _generate_layout.py      Generator: Nav + Footer + WA-FAB + Sticky aus einer Quelle in die Marker-Bloecke aller Seiten
  _generate_redirects.py   Generator: Redirect-Stubs fuer WordPress-Alt-URLs (REDIRECTS-Dict = einzige Quelle)
  credentials/
    _generate_credentials.py  Renderer: PDF -> JPG-Thumbs + Full
    thumbs/                Grid-Thumbnails (16 Zertifikate)
    full/                  Lightbox-Originale
  docs/
    sicherheit-methoden-standards.pdf    Corporate-PDF Statement „Datensicherheit & Compliance" (ersetzt sicherheit.html)
    portrait_galvano_forum_2026.pdf      Galvano-Forum-Referenten-Portrait
    praesentation_forschungsvorhaben_2025-07.pdf  Forschungsvorhaben-Präsentation (Stand Juli 2025)
  fonts/
    fonts.css                Self-Hosted @font-face Definitionen (Montserrat + Open Sans, OFL)
    Montserrat-{400,600,700}-{latin,latin-ext}.woff2   6 WOFF2-Files
    OpenSans-{300,400,600}-{latin,latin-ext}.woff2     6 WOFF2-Files
  favicon.ico              Browser-Tab Icon (Root — Browser-Konvention)
  apple-touch-icon.png     iOS Home Screen Icon (Root — Konvention)
  CNAME                    Custom Domain Config
  robots.txt               Crawler-Erlaubnis
  sitemap.xml              Google Sitemap (5 URLs)
  _generate_assets.py      Generator für Favicon/OG-Image (liest/schreibt assets/img/)
  _generate_leistungen.py  STILLGELEGT (Ziel ist nur noch ein Redirect-Stub) — bricht bewusst beim Aufruf ab
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
| **Durch „noindex"-Tag ausgeschlossen** | `ausbildung.html`, `sicherheit.html` — bewusst zurueckgestellt (Fokussierung 2026-07-02). | Nichts. Reaktivierung siehe Setup-Abschnitt oben. |
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
`noindex` gehoert nur auf zurueckgestellte **Inhalts**seiten mit Self-Canonical
(`ausbildung.html`, `sicherheit.html`).

**Sitemap:** `lastmod` beim Deploy auf das tatsaechliche Aenderungsdatum ziehen
(`git log -1 --format=%ad --date=short -- <datei>`) — veraltete Werte kosten Crawl-Prioritaet.

## DNS-Konfiguration (IONOS)

| Typ | Name | Ziel |
|-----|------|------|
| **A** | `@` | `185.199.108.153` |
| **A** | `@` | `185.199.109.153` |
| **A** | `@` | `185.199.110.153` |
| **A** | `@` | `185.199.111.153` |
| **CNAME** | `www` | `secure-galvano-ai.github.io` |

## IONOS Vertragsstatus

- **Vertrag 100185485** (WordPress Hosting Grow): Läuft am 02.06.2026 aus
- **Zusatzartikel** (Domain Guard, Mail Business, SSL): Gekündigt
- **Domain `secure-galvano-ai.com`**: Automatische Verlängerung aktiv (15.05.2026)
- **Domain `rvh.at`**: Bleibt (Microsoft 365 Mail läuft darüber)

## Corporate Design Assets

| Asset | Pfad |
|-------|------|
| **Logo (groß)** | `brand/logo.png` |
| **Logo (Header)** | `brand/logo_header.png` |
| **Porträt** | Quelle: `Stefan Maier - Dokumente/02_Unterlagen/04_Fotos/MICHAELKREYER/` |
| **Corporate Design Doku** | `brand/corporate_design.md` |
| **Canva Workflow** | `brand/canva_workflow.md` |

### Farben

**Single Source: `assets/css/base.css :root`** (kanonisch aus `corporate_design.md`).
Farbe ändern = nur dort editieren, gilt sofort site-weit. Ad-hoc-Hex im Seiten-CSS
vermeiden — stattdessen Token `var(--name)` nutzen.

| Farbe | Token / Hex | Verwendung |
|-------|-----|------------|
| Schild-Blau | `--schild-blau` `#2B5EA7` | Primär — Headlines, Buttons |
| Dunkelblau | `--dunkelblau` `#1B2A4A` | Hintergründe, Text |
| Logo-Grün | `--logo-gruen` `#3D8C3E` | Akzent — Checkmarks, Erfolg |
| Silber | `--silber` `#D4D8DC` | Trennlinien, dezente Flächen |
| Hellgrau | `--hellgrau` `#F5F7FA` | Sektions-Hintergrund |
| Cyan | `--cyan-akzent` `#00D4FF` | Tech-Akzent (sparsam) |
| (abgeleitet) | `--schild-blau-hover` `--dunkelblau-mid` `--dunkelblau-deep` `--blau-tint` `--text-body` `--text-light` | Hover, Verläufe, Footer-BG, Fließtext |

### Fonts

- **Headlines:** Montserrat (Bold/SemiBold) — **lokal self-hosted** in `fonts/` (OFL-lizenziert)
- **Body:** Open Sans (Regular/Light) — **lokal self-hosted** in `fonts/` (OFL-lizenziert)
- **Fallback:** Arial
- Einbindung in jeder Page über `<link href="fonts/fonts.css" rel="stylesheet">` — kein Google-Fonts-Request, DSGVO-freundlich

## Externe Services

| Service | Zweck | Link |
|---------|-------|------|
| Microsoft Bookings | Erstgespräch buchen | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/` |
| Microsoft Clarity | Web-Analyse (Opt-in, Projekt `wql3vpgrxl`) | `clarity.microsoft.com` |
| Google Search Console | SEO / Indexierung | `search.google.com/search-console` |
| GitHub Pages | Hosting | `github.com/secure-galvano-ai/homepage/settings/pages` |
| IONOS | Domain-Registrar | `my.ionos.de` |

## Deployment

Push auf `main` → GitHub Pages deployed automatisch (~1 Min).

```bash
cd homepage
git add -A
git commit -m "Beschreibung"
git push
```

**KEIN GPG-Signing in diesem Repo.** Die Homepage ist ein reines Content-Repo
(HTML/CSS/Assets) — Commit-Signing ist nur für Code-Repos vorgesehen. Lokal per
`git config commit.gpgsign false` deaktiviert; Commits laufen ohne Yubikey-PIN-Dialog.

### GitHub Pages — bekannte Fallstricke (Anti-Patterns)

*Aus der Deploy-Panne 2026-07-02 gelernt. Symptom war: Pages meldet `Page build failed`/`errored`, die Live-Seite bleibt aber (korrekt) auf dem letzten guten Stand. In ~2 h Debugging stellte sich heraus: **der `build`-Job gelingt praktisch immer — es scheitert nur der `deploy`-Job, und zwar GitHub-seitig.***

1. **Zuerst herausfinden, WAS failt — Build oder Deploy.** Der Legacy-Endpoint `pages/builds/latest` ist laggy/irreführend. Autoritativ ist der Actions-Run:
   ```bash
   RID=$(gh api "repos/secure-galvano-ai/homepage/actions/runs?per_page=1" --jq '.workflow_runs[0].id')
   gh api "repos/secure-galvano-ai/homepage/actions/runs/$RID/jobs" --jq '.jobs[] | "\(.name): \(.conclusion)"'
   gh run view "$RID" --log-failed | tail -30
   ```
   - `deploy` + `Deployment cancelled` → **Concurrency** (Punkt 2).
   - `deploy` + `Timeout reached, aborting!` → **Pages-Backend-Timeout** (GitHub-seitig, transient) → abwarten + EINMAL neu deployen.
2. **NIEMALS mehrere Pages-Deploys schnell hintereinander triggern.** Die Concurrency-Gruppe `pages` hat **Queue-Tiefe 1** — jeder neue Deploy **cancelt den vorher wartenden**. Rapides `git push` + wiederholtes `gh api --method POST .../pages/builds` erzeugt eine Kaskade aus `Deployment cancelled`/`failure`. → **EINMAL pushen, dann 2–10 Min ungestört warten. Nicht nachtreten.**
3. **Bei Fehler zuerst die LIVE-Seite prüfen, nicht blind retrien** (letzter guter Build bleibt live, meist schon korrekt): `curl -s https://secure-galvano-ai.com/ | grep -o '<h1>[^<]*'`
4. **`.nojekyll` NICHT reflexartig hinzufügen.** Der Jekyll-`build` gelingt hier (getestet); `.nojekyll` löst das Deploy-Problem NICHT und liefert zusätzlich `_generate_*.py` **öffentlich** aus (Jekyll schließt `_`-Dateien sonst aus). → **ohne `.nojekyll` bleiben.**
5. **Kein `{{ … }}` / `{% … %}` im HTML** — Jekyll/Liquid parst das und failt den *Build* (war hier NICHT die Ursache, ist aber die klassische echte Build-Bremse).

Assets neu generieren (Favicon, OG-Image):
```bash
cd homepage
py _generate_assets.py
```

Leistungsbausteine ändern/ergänzen (Karten auf `leistungen.html` + Teaser auf `index.html`):
```bash
cd homepage
# 1. Baustein in der LEISTUNGEN-Liste in _generate_leistungen.py bearbeiten
# 2. Neu rendern:
py _generate_leistungen.py
```
**Eine Datenquelle:** die `LEISTUNGEN`-Liste in `_generate_leistungen.py`. Der
Generator schreibt statisches HTML zwischen die `<!-- BEGIN/END leistungen:* -->`
-Marker (crawlbar, kein JS nötig). Das HTML zwischen den Markern **nicht von Hand
bearbeiten** — es wird beim nächsten Lauf überschrieben. Kategorie-Chips (`data-cat`)
sind gesetzt, ein Filter lässt sich später ohne Datenänderung ergänzen.

Nachweise neu rendern (wenn das Quell-PDF aktualisiert wird):
```bash
cd homepage
py credentials/_generate_credentials.py
```
Quelle: `Business Development/resources/credentials/20260512_Lebenslauf & Nachweise_Stefan Maier.pdf`.
Metadaten (Titel, Untertitel, Kategorie pro Seite) sind in `credentials/_generate_credentials.py` definiert — Reihenfolge dort ändern, Seiten 6-28 des PDFs werden zu 23 JPG-Paaren (Seite 28: WKO-Workshop NISG 2026, ergänzt 05/2026).

## WhatsApp-Kontakt

Floating-Button unten rechts auf jeder Page, verlinkt auf `wa.me/4368181483538` mit voreingestelltem Greeting. Funktioniert mit normaler WhatsApp-App **und** WhatsApp Business — keine separate Konfiguration nötig.
