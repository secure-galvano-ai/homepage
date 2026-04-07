# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.github.io/homepage/
**Ziel:** Migration von IONOS (16€/Monat) auf GitHub Pages (0€)

---

## Naechste Schritte

### 1. Custom Domain verbinden (GitHub)

1. https://github.com/secure-galvano-ai/homepage/settings/pages
2. "Custom domain" = `secure-galvano-ai.com` eintragen
3. Save
4. Nach DNS-Propagation (~30 Min): "Enforce HTTPS" ankreuzen

### 2. DNS-Eintraege bei IONOS setzen

Login: https://my.ionos.de → Domains → secure-galvano-ai.com → DNS

**Bestehende A-Records und CNAME loeschen**, dann neu anlegen:

| Typ | Name | Ziel |
|-----|------|------|
| **A** | `@` | `185.199.108.153` |
| **A** | `@` | `185.199.109.153` |
| **A** | `@` | `185.199.110.153` |
| **A** | `@` | `185.199.111.153` |
| **CNAME** | `www` | `secure-galvano-ai.github.io` |

### 3. IONOS Hosting kuendigen

1. https://my.ionos.de → Vertraege
2. **Webhosting-Paket kuendigen** (das teure)
3. **Domain-Vertrag BEHALTEN** (nur Registrierung, ~1€/Monat)
4. Achtung: Erst kuendigen wenn DNS umgestellt und neue Seite unter eigener Domain laeuft

### 4. Seite erweitern (optional)

- [ ] Impressum-Seite (`impressum.html`)
- [ ] Datenschutz-Seite (`datenschutz.html`)
- [ ] Video-Embed (YouTube iframe)
- [ ] Kontaktformular (Formspree oder Netlify Forms, kostenlos)
- [ ] Weitere Unterseiten (Trusted AI, Team, Downloads)
- [ ] Favicon

---

## Projektstruktur

```
homepage/
  index.html          Landing Page (Single File, kein Framework)
  logo.png            Kopie aus brand/
  README.md           Diese Datei
```

## Corporate Design Assets

| Asset | Pfad |
|-------|------|
| **Logo (gross)** | `brand/logo.png` |
| **Logo (Header)** | `brand/logo_header.png` |
| **Corporate Design Doku** | `brand/corporate_design.md` |
| **Canva Workflow** | `brand/canva_workflow.md` |

### Farben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Schild-Blau | `#2B5EA7` | Primaer — Headlines, Buttons |
| Dunkelblau | `#1B2A4A` | Hintergruende, Text |
| Logo-Gruen | `#3D8C3E` | Akzent — Checkmarks, Erfolg |
| Silber | `#D4D8DC` | Trennlinien, dezente Flaechen |
| Hellgrau | `#F5F7FA` | Sektions-Hintergrund |
| Cyan | `#00D4FF` | Tech-Akzent (sparsam) |

### Fonts

- **Headlines:** Montserrat (Bold/SemiBold)
- **Body:** Open Sans (Regular/Light)
- **Fallback:** Arial

---

## Deployment

Push auf `main` → GitHub Pages deployed automatisch (~1 Min).

```bash
cd homepage
git add -A
git commit -m "Beschreibung"
git push
```
