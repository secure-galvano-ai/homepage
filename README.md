# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.com
**HTTPS:** Aktiv (GitHub Pages + Let's Encrypt)
**Hosting:** GitHub Pages (kostenlos)
**Stand:** 2026-05-24

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

## Optional (noch offen)

- [ ] Weitere Unterseiten (Trusted AI, Downloads)

---

## Projektstruktur

```
homepage/
  index.html               Landing Page mit Funnel (Hero, Services, Ablauf, Pakete, Demos, Vorteile, Founder, Forschung, FAQ, CTA)
  ueber-mich.html          Vollständiges Profil + Bio + Nachweise-Galerie
  nachweise.html           Redirect-Stub auf ueber-mich.html#nachweise
  impressum.html           Impressum (ECG/UGB) + Marken-Hinweis
  datenschutz.html         Datenschutzerklärung (DSGVO)
  assets/
    img/                   Bild-Assets: logo, portrait, aws, trustifai, og-image,
                           techniker-monitoring, stefan-entmetallisierung-2006
    js/
      consent.js           Opt-in-Consent-Gate für Microsoft Clarity + CTA-Funnel-Events
  credentials/
    _generate_credentials.py  Renderer: PDF -> JPG-Thumbs + Full
    thumbs/                Grid-Thumbnails (16 Zertifikate)
    full/                  Lightbox-Originale
  docs/
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

Assets neu generieren (Favicon, OG-Image):
```bash
cd homepage
py _generate_assets.py
```

Nachweise neu rendern (wenn das Quell-PDF aktualisiert wird):
```bash
cd homepage
py credentials/_generate_credentials.py
```
Quelle: `Business Development/resources/credentials/20260512_Lebenslauf & Nachweise_Stefan Maier.pdf`.
Metadaten (Titel, Untertitel, Kategorie pro Seite) sind in `credentials/_generate_credentials.py` definiert — Reihenfolge dort ändern, Seiten 6-28 des PDFs werden zu 23 JPG-Paaren (Seite 28: WKO-Workshop NISG 2026, ergänzt 05/2026).

## WhatsApp-Kontakt

Floating-Button unten rechts auf jeder Page, verlinkt auf `wa.me/4368181483538` mit voreingestelltem Greeting. Funktioniert mit normaler WhatsApp-App **und** WhatsApp Business — keine separate Konfiguration nötig.
