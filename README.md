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

## Optional (noch offen)

- [ ] Weitere Unterseiten (Trusted AI, Downloads)

---

## Projektstruktur

```
homepage/
  index.html               Predictive-Quality-Landing (ein roter Faden, KEINE Preise): Hero, Gruender-Stimme, Proof (TUeV/8-von-10), Schmerz, 3-Stufen-Treppe Fehlersuche->Live->Frueherkennung (#so-funktionierts), Diagnose-Angebot ohne Preis (#angebot), Kontakt (#kontakt). Traegt KEINE Leistungs-Teaser-Karten mehr.
  leistungen.html          Detailseite (Diagnose-Faden, KEINE Preise): 3 Bausteine (aus _generate_leistungen.py) + Einstieg/Diagnose (#preise, preisfrei) + Ablauf-Detail (#standort-audit) + Folgewege/Videos (#folgewege/#videos) + FAQ (#faq)
  ausbildung.html          Zurueckgestellt (noindex, nicht in Nav/Sitemap) — Datei erhalten
  sicherheit.html          Zurueckgestellt (noindex, nicht in Nav/Sitemap) — ersetzt durch docs/sicherheit-methoden-standards.pdf
  ueber-mich.html          Vollständiges Profil + Bio + Nachweise-Galerie
  nachweise.html           Redirect-Stub auf ueber-mich.html#nachweise
  impressum.html           Impressum (ECG/UGB) + Marken-Hinweis
  datenschutz.html         Datenschutzerklärung (DSGVO)
  assets/
    img/                   Bild-Assets: logo, portrait, aws, trustifai, og-image,
                           techniker-monitoring, stefan-entmetallisierung-2006
    css/
      leistungen.css       Geteilte Komponenten-CSS für die Leistungsbausteine (Karten + Mail-Button); genutzt von leistungen.html + index.html
    js/
      consent.js           Opt-in-Consent-Gate für Microsoft Clarity + CTA-Funnel-Events
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
  sitemap.xml              Google Sitemap (6 URLs)
  _generate_assets.py      Generator für Favicon/OG-Image (liest/schreibt assets/img/)
  _generate_leistungen.py  Generator für die Leistungsbausteine (eine Datenquelle -> Karten in leistungen.html + index.html)
  README.md                Diese Datei
```

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

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Schild-Blau | `#2B5EA7` | Primär — Headlines, Buttons |
| Dunkelblau | `#1B2A4A` | Hintergründe, Text |
| Logo-Grün | `#3D8C3E` | Akzent — Checkmarks, Erfolg |
| Silber | `#D4D8DC` | Trennlinien, dezente Flächen |
| Hellgrau | `#F5F7FA` | Sektions-Hintergrund |
| Cyan | `#00D4FF` | Tech-Akzent (sparsam) |

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
