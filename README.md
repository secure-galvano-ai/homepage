# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.com
**HTTPS:** Aktiv (GitHub Pages + Let's Encrypt)
**Hosting:** GitHub Pages (kostenlos)
**Stand:** 2026-04-29

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
- [x] Nachweise-Page mit 22 Zertifikaten (Hall-of-Fame Gallery + Lightbox-Modal)

## Optional (noch offen)

- [ ] Google Fonts lokal hosten (DSGVO-optimiert)
- [ ] Weitere Unterseiten (Trusted AI, Downloads)

---

## Projektstruktur

```
homepage/
  index.html               Landing Page (mit WhatsApp-FAB)
  nachweise.html           Hall-of-Fame Gallery — 22 Zertifikate, Lightbox-Modal
  impressum.html           Impressum (ECG/UGB)
  datenschutz.html         Datenschutzerklärung (DSGVO)
  credentials/
    _generate_credentials.py  Renderer: PDF -> JPG-Thumbs + Full
    thumbs/                Grid-Thumbnails (~600w, ~1.5 MB total)
    full/                  Lightbox-Originale (~1800w, ~9.5 MB total)
  logo.png                 Logo (aus brand/)
  portrait.jpg             Gründer-Porträt
  favicon.ico              Browser-Tab Icon
  apple-touch-icon.png     iOS Home Screen Icon
  og-image.jpg             Social Media Vorschaubild
  CNAME                    Custom Domain Config
  robots.txt               Crawler-Erlaubnis
  sitemap.xml              Google Sitemap
  _generate_assets.py      Generator für Favicon/OG-Image
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

- **Headlines:** Montserrat (Bold/SemiBold) — Google Fonts
- **Body:** Open Sans (Regular/Light) — Google Fonts
- **Fallback:** Arial

## Externe Services

| Service | Zweck | Link |
|---------|-------|------|
| Microsoft Bookings | Erstberatung buchen | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/` |
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
Quelle: `TrustedAIZertifizierung/kompetenznachweise/20251030_Lebenslauf & Nachweise_Stefan Maier.pdf`.
Metadaten (Titel, Untertitel, Kategorie pro Seite) sind in `credentials/_generate_credentials.py` definiert — Reihenfolge dort ändern, Seiten 6-27 des PDFs werden zu 22 JPG-Paaren.

## WhatsApp-Kontakt

Floating-Button unten rechts auf jeder Page, verlinkt auf `wa.me/4368181483538` mit voreingestelltem Greeting. Funktioniert mit normaler WhatsApp-App **und** WhatsApp Business — keine separate Konfiguration nötig.
