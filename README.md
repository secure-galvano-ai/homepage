# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.com
**HTTPS:** Aktiv (GitHub Pages + Let's Encrypt)
**Hosting:** GitHub Pages (kostenlos)
**Stand:** 2026-09-03

---

## Meilensteine

Grundausstattung steht seit Mai 2026: GitHub Pages mit eigener Domain und erzwungenem HTTPS,
Impressum/Datenschutz, Bookings-Termin, Open Graph, `robots.txt`/Sitemap, Search Console,
JSON-LD, self-hosted Fonts, Clarity mit Opt-in-Consent.

| Datum | Umbau | Ergebnis |
|---|---|---|
| 29.05.2026 | Customer-Journey neu geordnet (PAS, 3-Kachel-Onramp, Sticky-Mobil-CTA, Funnel-Tracking) | — |
| 02.07.2026 | **Fokussierung** — `ausbildung.html` + `sicherheit.html` zurueckgestellt, Leistungen 6 → 3 | — |
| 30.07.2026 | **EINE Botschaft** — Sektion `#ablauf` mit der sechsstufigen Vertriebsleiter (ohne Preise), Redundanzen zusammengelegt | 9 → 8 Sektionen, Seitenlaenge −27 % |
| 30.07.2026 | `leistungen.html` aufgeloest, alles auf die Startseite | Sitemap 6 → 5 URLs |
| 10.08.2026 | Presse-/Aktuell-Sektion `#aktuell` nach der Trust-Bar | — |
| 10.08.2026 | **Erster Optimierungslauf** — Messung repariert (jeder CTA war doppelt verdrahtet), zweiter Hero-Button ist jetzt ein Beleg statt eines Sprungankers | Ablauf ab jetzt in [`OPTIMIERUNG.md`](OPTIMIERUNG.md), monatlich per `/optimierung` |
| 17.08.2026 | Presse-Karte verlinkt die frei lesbare WISTO-Fassung | tote Platzhalter weg |
| 31.08.2026 | **`leistungen.html` zurueckgeholt** — echte Seite mit der Standortanalyse als Schwerpunkt, neun Bausteinen und Abgrenzung; Hero mobil entzerrt, Consent-Banner kompakt | Sitemap 5 → 6 URLs; Anlass: 87 GSC-Impressionen auf eine Weiterleitung, 0 Klicks auf kommerzielle Suchanfragen |
| 31.08.2026 | **`demo.html` angelegt** — Landingpage fuer das Demo-Video, ein Zweck und ein CTA, bis zur Aufnahme `noindex` und unverlinkt | § *Demo-Seite*; Platzierungsentscheidung in `BD/projects/demo-video-akquise/` |
| 17.08.2026 | Foto vom aws-Jurytermin (April 2025) auf `forschung.html`, unter dem Förderprojekt | Anlassfoto statt Team-Sektion — siehe Regel unten |
| 24.08.2026 | **Core Web Vitals** — Schriften per `preload` vorgezogen, Hero-Portrait als WebP | CLS 0,153 → **0**, Seitengewicht 997 → 467 KB, LCP 1404 → 1268 ms (live nachgemessen) |
| 03.09.2026 | **Schnellanalyse als Einstieg** (500 € netto), sechs Anwendungen und fünf Fragen auf `leistungen.html`; Leistung umbenannt in *Standortanalyse Daten- und KI-Potenziale*; neuer Einseiter *Leistungen im Überblick*; „kein Cloud-Upload“ ersetzt durch „Auswertung lokal, keine KI-Cloud, Übergabe verschlüsselt“ | Marktfragen des Kanalpartners eingearbeitet |
| 03.09.2026 | **Sensorik-Block nachgezogen** *(zweite Runde desselben Tages)* — siebte Anwendung *Die Sonde, die falsch misst*, drei weitere Fragen (Sondendrift, „ersetzt das unsere Fachkräfte", Prüfnachweis an der Anlage), drei zusätzliche Grenzen in der Abgrenzung, zwei neue Portfolio-Bausteine | Quelle: `BD/conversations/2026/2026-09-03_waldemar-daubert-marktfragen-und-antworten.md` §7 |
| 02.09.2026 | **`demo.html` scharfgeschaltet** — Video `RStpqzz3r5g` eingebunden, Texte auf die Anwendung statt auf den Vor-Ort-Tag umgestellt, zwei Verweise gesetzt | § *Demo-Seite* |
| 02.09.2026 | **„Ihre Daten bleiben bei Ihnen" → „Lokale Datenverarbeitung"** *(Stefan)* — Startseiten-H2, Vertrauenszeile auf `demo.html`, Baustein *Laufende Überwachung* auf `leistungen.html` | Wortlaut bleibt seitenübergreifend identisch |
| 03.09.2026 | **Beleg-Foto in `#lokale-datenverarbeitung`** *(dritte Runde desselben Tages)* — der Entwicklungsrechner mit Gesicht daneben, dazu die Abgrenzung *Entwicklungsumgebung ≠ Hosting* und der erste Verweis von der Startseite auf `sicherheit.html` (`link-sicherheit-startseite`). Bild: `assets/img/entwicklungsrechner.webp`, 57 KB, `loading="lazy"` | Quelle: LinkedIn-Beitrag 05.08.2026 *Mehr KI-Leistung oder Daten im Haus?* (SharePoint `01_LinkedIn/2026/2026-08-05_…`). Gegenstück auf `leistungen.html` § *Was passiert mit unseren Daten?* mitgezogen, sichtbarer Text **und** FAQ-Schema |

### Regeln, die daraus dauerhaft gelten

- **Presse (`#aktuell`): maximal zwei Karten, veraltete ersetzen statt stapeln.** Eine sichtbar
  veraltete News-Sektion schadet mehr als keine. ⚠ **Die Termin-Karte (KI Days) ist nach dem
  30.09.2026 abgelaufen** und muss dann getauscht werden.
- **Keine Team-Sektion, keine Rollen-Kacheln, kein „wir".** Die Firmierung ist ein
  Einzelunternehmen — eine dargestellte Unternehmensstruktur wäre eine Irreführung über die
  Identität des Vertragspartners (Linie OLG München 6 U 1888/13 zur vorgetäuschten größeren
  Struktur). Fotos mit weiteren Personen sind trotzdem erlaubt, wenn sie einen **Anlass**
  dokumentieren statt eine Struktur: datierte Bildunterschrift, echter Termin, Freigabe der
  Abgebildeten. Vorbild ist das aws-Jurytermin-Foto auf `forschung.html` (17.08.2026).
  Die eigentliche Kundensorge dahinter — „was, wenn der ausfällt?" — beantwortet ohnehin kein
  Teamfoto, sondern ein benannter Mechanismus (Haftpflicht, Doku beim Kunden, Software läuft
  ohne ihn). **Noch offen, empfohlen:** vier Zeilen „Ausfallsicherheit" bei `#angebot`.
- **Neue Seite? Den `preload`-Block für die Schriften mitkopieren.** Ohne ihn starten die
  Schriften erst, nachdem `fonts.css` geparst ist; der `font-display:swap`-Wechsel von Arial
  auf Montserrat/Open Sans verschiebt dann den Seitenkopf. Auf der Startseite waren das
  **CLS 0,153** bei einer Google-Grenze von 0,1 (gemessen 24.08.2026). Das `crossorigin` am
  Preload-Link ist Pflicht, auch bei eigener Domain — fehlt es, lädt der Browser jede Schrift
  ein zweites Mal. Prüfen mit `_scripts/check_site.py` und einem Blick ins Netzwerk-Protokoll:
  jede `woff2` darf genau einmal auftauchen.
- **Urheberrecht:** nur Kurzzitate mit Quellenangabe. **Keine VN-Fotos, kein VOL.AT-Logo als Bild**,
  kein selbst gehosteter Volltext — Nachdruckrechte liegen bei Russmedia/VN. Der VOL.AT-Artikel
  steht hinter einer Bezahlschranke, deshalb verlinken wir die WISTO-Fassung. Kaeme eine
  Verlagsfreigabe, ersetzt sie diesen Link — nicht stapeln.
- **Aus- und Weiterbildung ist seit 02.09.2026 wieder auf der Website** — `ausbildung.html`
  als eigene Seite, Nav-Eintrag „Datenwerkstatt" (der naheliegende Name „KI-Werkstatt" ist in
  Vorarlberg von der WKO belegt). Grund ist die **Neuausrichtung des
  Angebotsschwerpunkts** (Strategiegespraech 02.09.2026, `BD/projects/ausbildung-und-coaching-2026/`):
  verkauft wird die Befaehigung, nicht mehr nur die fertige Software. Damit ist der Beschluss
  vom 25.08. ueberholt — **die Messerkenntnis dahinter gilt aber weiter und hat den Aufbau
  bestimmt:** 104 Sitzungen mit **0 Klicks** auf den Buchungs-CTA heisst, dass ein reiner
  Termin-Aufruf auf dieser Seite nicht traegt. Deshalb steht jetzt ein **niederschwelliger
  zweiter Weg** daneben (Ueberblick als PDF, ohne E-Mail-Gate), und die Seite hat eine
  **Erfolgsdefinition mit Abbruchkriterium** statt einer Daumenprobe
  (`BD/projects/ausbildung-und-coaching-2026/zyklus-und-experiment.md`). Der Absatz darunter
  steht als Begruendung der damaligen Entscheidung — er ist Historie, nicht mehr die Regel.
- ~~**Kein Coaching-Baustein auf der Website**~~ *(Stefan, 25.08.2026 — am 02.09.2026 abgeloest)*.
  Anlass war ein privates 1:1-KI-Coaching, das Spass gemacht hat. Es kommt trotzdem **nicht**
  zurueck auf die Seite, aus drei Gruenden: (1) Der fruehere Baustein war **In-House-Coaching fuer
  Galvanikbetriebe** (Fachkraefte und Lehrlinge schulen) — ein anderes Produkt als 1:1-Begleitung
  einer Privatperson; ihn zu reaktivieren wuerde das Falsche bewerben. (2) Die Abschaltung war eine
  **Messentscheidung**: 11 Einstiege in 60 Tagen auf `ausbildung.html`, gleichzeitig 104 Sitzungen
  mit **0 Klicks** auf den Buchungs-CTA. Die Antwort darauf war *eine* Botschaft und drei statt
  sechs Bausteine — ein vierter Weg verschlechtert genau diese Kennzahl. (3) Saeule 2 bleibt bis
  2027 eingefroren (`BD/areas/business-model.md`). Der Kanal fuer die Energie aus solchen Sessions
  ist die bezahlte Lehre (Digital Campus Vorarlberg, WIFI), nicht die Startseite. Projekt-Ablage
  des Falls seit 26.08.2026 auf SharePoint:
  `01_Business Development\02_Vertrieb\06_KI-Coaching Einzelpersonen\` (nicht mehr im BD-Repo).
  **Neu bewerten,** wenn unaufgefordert
  mehrere Anfragen von Privatpersonen kommen — dann eine eigene schlanke Seite, nicht der alte
  Baustein im Galvanik-Funnel.
- **Zurueckgestellte Seiten — Stand 02.09.2026: es gibt keine mehr.** `sicherheit.html` ist seit
  11.08. wieder live (Footer, Sitemap, bewusst nicht in der Hauptnavigation), `ausbildung.html`
  seit 02.09. neu aufgebaut und in Nav und Sitemap. Der Weg fuer die naechste Wiederbelebung
  bleibt derselbe: Nav-Eintrag in `_generate_layout.py`, Seite in `PAGES`, Sitemap-Eintrag,
  Meta-Block samt `preload` der Schriften — danach `check_site.py` **und** `check_inhalt.py`.
  Der zweite faengt zu lange Titel, zu lange Beschreibungen und fehlende Sitemap-Eintraege ab;
  beim Aufbau am 02.09. sind alle drei tatsaechlich aufgetreten.
- **Tracking-Konvention:** je CTA-Position ein eigener Event-Name (`cta-nav`, `cta-hero`,
  `cta-ablauf`, `cta-abschluss`, `cta-sticky`, `cta-whatsapp-fab`, `mail-abschluss`), Downloads als
  `pdf-<dateiname>`. **Keine generischen Selektoren** — die haben die Zahlen einmal verdoppelt.
- **Bei Abweichungen zwischen Website und Angebotsvorlage gilt die Website** *(Stefan, 17.08.2026)*.
  Konkret angewandt: Die Diagnose dauert **„innerhalb einer Woche"**, nicht acht Wochen —
  `BD/areas/business-model.md` wurde am 17.08. an vier Stellen nachgezogen. Der Vor-Ort-Teil steckt
  seit 30.07. in der vorgelagerten **Standortanalyse** (Stufe 2). Preis unveraendert 9.500 €.
- **Produktname bleibt „Diagnose"**, nicht „Proof of Concept" — so in `BD/areas/business-model.md`
  festgelegt.
- **Bewusst getragener Widerspruch, nicht erneut melden** *(Stefan, 11.08.2026)*:
  `docs/portrait_galvano_forum_2026.pdf` sagt „Trusted-AI-**Zertifizierung**" und „Stefan Maier
  **e.U.**" — beides weicht von der Linie ab (korrekt: *Modellpruefung*, Firmierung ohne e.U.).
  Das Heft ist gedruckt; beim naechsten Nachdruck mitkorrigieren.

## Optional (noch offen)

- [ ] Weitere Unterseiten (Trusted AI, Downloads)
- [ ] **UTM auf die eingehenden Links** setzen (Mailstufe 3, LinkedIn, Signatur) — die interne
      Verlinkung bleibt bewusst ohne UTM, sonst zerlegt sie die Sitzung. § *Demo-Seite*.
- [ ] **Konkurrieren die „Weiteren Aufnahmen" mit dem Hauptvideo?** Der erste der drei Links
      auf `demo.html` heisst „Auffaelligkeiten an Prozessdaten erkennen" und verspricht damit
      dasselbe wie das Hauptvideo darueber. Im naechsten Monatslauf gegen die Klickzahlen
      pruefen und im Zweifel den Link streichen — eine Landingpage hat einen Zweck.

---

## Architektur (Single-Source, seit 2026-07-03)

Gemeinsame Bausteine liegen **an genau einer Stelle** und werden nicht mehr pro
Seite dupliziert. Wer Farben, Nav oder Footer aendert, editiert **eine** Quelle:

| Baustein | Single Source | Wird genutzt von |
|----------|---------------|------------------|
| Design-Tokens (Farben) + Reset + Typo + Container + Nav + Buttons + section-header + Footer + WA-FAB + Sticky-CTA + fade-up | `assets/css/base.css` | jede Seite (erstes CSS im `<head>`) |
| Geteiltes Verhalten (Nav-Scroll, Mobile-Menue, fade-up) | `assets/js/site.js` | jede Seite (`defer`) |
| Nav + Footer + WA-FAB + Sticky (HTML) | `_generate_layout.py` -> Marker `<!-- BEGIN/END nav -->` usw. | index, leistungen, ueber-mich, forschung, impressum, datenschutz |
| ~~Leistungs-Karten~~ | `_generate_leistungen.py` **abgeloest 31.08.2026** — die Bausteine stehen handgeschrieben in `leistungen.html` (neun statt drei). Skript nicht ausfuehren | — |

Die Markenfarben in `base.css :root` sind **kanonisch abgeleitet** aus
`Business Development/areas/brand/corporate_design.md`. Aendern sich Markenfarben,
wird NUR `base.css` editiert. Seiten-spezifisches CSS (Hero, einzelne Sektionen)
bleibt im `<style>`-Block der jeweiligen Seite.

**Nicht migriert (bewusst):** `sicherheit.html` traegt weiter ihr eigenes CSS.
`ausbildung.html` ist seit 02.09.2026 in `PAGES` und `NAV_LINKS` und bekommt Nav und Fuss
generiert; ihr Seiten-CSS ist eine Kopie des Standes aus `leistungen.html` plus eigener
Abschnitte. Zum Reaktivieren weiterer Seiten: in `_generate_layout.py` PAGES + NAV_LINKS ergaenzen,
Marker in die Seite setzen, `py _generate_layout.py` laufen lassen.

## Demo-Seite (`demo.html`) — scharf seit 02.09.2026

**Zweck:** die einzige Landingpage der Seite im engeren Sinn — ein Zweck, ein Handlungsaufruf,
keine Ablenkung. Sie traegt das Demo-Video der Anwendung und ist das Ziel, auf das Mail, Telefon
und LinkedIn zeigen. Begruendung der Platzierung im ganzen Trichter:
`Business Development/projects/demo-video-akquise/README.md`.

**Was drauf ist:** YouTube-ID **`RStpqzz3r5g`** („Prozessdaten auswerten — die Anwendung im
Ueberblick"), **4:51**, nicht gelistet, eingebunden ueber `youtube-nocookie.com` — kein Cookie vor
Klick, die Datenschutzerklaerung setzt das voraus. `noindex` ist raus, die Seite steht in der
`sitemap.xml`, und zwei Verweise zeigen darauf: Startseite unter dem Pitch-Video
(`link-demo-startseite`) und `leistungen.html` in der Karte *Vorprojekt*
(`cta-demo-vorprojekt`, stand dort schon seit 31.08.). **Nicht** in die Belegspalte bei
`#standortanalyse` — die sammelt Belege zur *Standortanalyse*, das Video zeigt die *Anwendung*.
Ein am 02.09. dort versuchsweise gesetzter dritter Verweis ist aus genau diesem Grund wieder
raus: zwei Links auf dieselbe Seite konkurrieren miteinander, statt zu fuehren.

**Die Seite erzaehlt DIE ANWENDUNG, nicht den Vor-Ort-Tag** *(Stefan, 02.09.2026)*. Zwischen
31.08. und 01.09. stand hier kurzzeitig die Standortanalyse-Fassung („So laeuft ein Tag
Standortanalyse ab", Kartenwand, Rundgang) — das aufgenommene Video zeigt aber die Auswertung.
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
**unter den drei Punkten** und bewusst **nicht** als dritter Nebenweg unter dem CTA — wer
weiterreichen will, tut das direkt nach dem Inhalt, und dort konkurriert der Link nicht mit dem
Buchungs-Knopf. Zielgruppe sind die Kollegen des Besuchers, die keine fuenf Minuten Video schauen:
das Blatt muss deshalb **allein stehen** und traegt Video-Adresse, Kontakt und Ablauf selbst.
Gebaut wird es von `BD/projects/demo-video-akquise/build_flyer_anwendung.py` (Inhalt und Layout
stehen dort, **nie im PDF nachbessern**); der Build prueft Seitenzahl **und** Pflichtstellen, weil
`overflow:hidden` Inhalt sonst lautlos abschneidet — genau das passierte beim ersten Lauf mit der
Fusszeile. **Aendert sich das Video oder die Seite, aendert sich das Blatt mit** (dieselbe Regel
wie oben: Seite und Video muessen dasselbe versprechen — das Blatt gehoert dazu).

**Messung:** Der CTA traegt `data-funnel="cta-demo-seite"`, der Videostart meldet sich als
`video-gestartet` (die Erkennung in `consent.js` nimmt das erste YouTube-iframe der Seite — auf
`demo.html` gibt es genau eines, es ist nichts anzupassen). Eingehende Links aus Mail und LinkedIn
bekommen UTM-Parameter, damit der Verkehr im Monatslauf trennbar bleibt.

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
  leistungen.html          Leistungsseite (seit 31.08.2026 wieder echt, handgeschrieben): Standortanalyse als
                           Schwerpunkt (#standortanalyse), Anwendungen, Portfolio, Abgrenzung, Sticky-CTA.
                           Seit 03.09.2026: Sektion #schnellanalyse als kleiner Einstieg (500 EUR netto,
                           eine Frage, ein Datenauszug, remote) VOR dem Schwerpunkt, sieben Anwendungen
                           (#anwendungen) und acht Fragen (#fragen) mit FAQPage-Schema. Leistungsname
                           seither "Standortanalyse Daten- und KI-Potenziale".
                           Nav/Footer/WA-FAB/Sticky kommen aus _generate_layout.py. Kachel-Fassung bis 07/2026:
                           git show 78ce8c3:leistungen.html
  demo.html                Landingpage fuer das Demo-Video (ein Zweck, ein CTA). Seit 31.08.2026 angelegt,
                           bis zur Aufnahme noindex + nicht in der Sitemap + unverlinkt — § Demo-Seite.
  ausbildung.html          Datenwerkstatt — Aus- und Weiterbildung (seit 02.09.2026 neu aufgebaut, in Nav
                           und Sitemap). Am 02.09. abends von 13 auf 8 Sektionen gekuerzt, Reihenfolge
                           Nutzen -> Ablauf -> Beispiel -> Angebot. Flyer dazu:
                           docs/datenwerkstatt-ueberblick.pdf, gebaut aus
                           BD/projects/ausbildung-und-coaching-2026/build_flyer_datenwerkstatt.py.
                           Vorgaengerfassungen: git show feed14a:ausbildung.html (Kurs 2026-07),
                           git show 417588d:ausbildung.html (Langfassung vom 02.09.)
  sicherheit.html          Compliance-Seite (seit 11.08.2026 wieder indexiert, in Sitemap und Footer, bewusst NICHT
                           in der Hauptnavigation). Nav/Footer dort handgepflegt, nicht ueber _generate_layout.py.
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
  docs/                    Belege zum Verlinken und Mitschicken (Musterbefund, Flyer, Beispielauswertungen,
                           Methoden-und-Standards, Meisterbrief, Fachartikel, Praesentationen). Bewusst KEINE
                           Einzelliste hier -- sie driftet bei jedem neuen Beleg. Wo welcher verlinkt ist:
                           grep -o "docs/[a-z0-9_-]*\.pdf" *.html
                           Die fuenf erzeugten Einseiter kommen aus BD-Build-Skripten und werden NIE von
                           Hand bearbeitet -- Aenderung immer im Skript, dann neu bauen:
                             standortanalyse-flyer.pdf        BD/templates/flyer-corporate/build_flyer.py
                             standortanalyse-musterbefund.pdf BD/templates/befund-corporate/build_befund.py
                             leistungen-ueberblick.pdf        BD/templates/uebersicht-corporate/build_uebersicht.py
                             datenwerkstatt-ueberblick.pdf    BD/projects/ausbildung-und-coaching-2026/build_flyer_datenwerkstatt.py
                             anwendung-ueberblick.pdf         BD/projects/demo-video-akquise/build_flyer_anwendung.py
                           Jedes Skript prueft Seitenzahl und Pflichtstellen selbst und bricht ab, wenn
                           Inhalt verschluckt wird. leistungen-ueberblick.pdf ist das Blatt zum
                           Weiterreichen: alle vier Wege nebeneinander, mit Aufwand und Preis.
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
| **Durch „noindex"-Tag ausgeschlossen** | Derzeit keine Inhaltsseite. `sicherheit.html` ist seit 11.08.2026, `ausbildung.html` seit 02.09.2026 wieder indexiert — beide koennen im Bericht noch eine Weile hier auftauchen, bis Google neu crawlt. | Nichts. Bei `ausbildung.html` nach zwei Wochen pruefen und noetigenfalls einmalig „Indexierung beantragen". |
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
Aktuell traegt es keine Seite ausser `demo.html` bis zur Videoaufnahme.

**Sitemap:** `lastmod` beim Deploy auf das tatsaechliche Aenderungsdatum ziehen
(`git log -1 --format=%ad --date=short -- <datei>`) — veraltete Werte kosten Crawl-Prioritaet.

## DNS-Konfiguration (IONOS) — Soll-Stand beider Zonen

**Verifiziert am 17.08.2026 gegen die autoritativen Nameserver.** Diese Tabellen sind die
Wiederherstellungsvorlage: Weicht eine Zone davon ab, ist etwas passiert.

### `secure-galvano-ai.com` (Website, GitHub Pages)

| Typ | Name | Ziel |
|-----|------|------|
| **A** | `@` | `185.199.108.153` |
| **A** | `@` | `185.199.109.153` |
| **A** | `@` | `185.199.110.153` |
| **A** | `@` | `185.199.111.153` |
| **A** | `www` | `185.199.111.153` *(seit 17.08.; vorher CNAME auf `secure-galvano-ai.github.io` — IONOS liess beides nicht gleichzeitig zu, funktional gleichwertig, 301 auf die Hauptdomain)* |
| — | **AAAA** | **keiner.** Ein AAAA auf IONOS bricht HTTPS, siehe Vorfall unten |
| **TXT** | `@` | `v=spf1 -all` |
| **TXT** | `_dmarc` | `v=DMARC1; p=reject;` |

**Spoofing-Schutz seit 17.08.2026:** Von dieser Domain wird **nichts** versendet — alle Kontaktwege
auf der Website sind `mailto:`-Links auf `@rvh.at`, das Hosting ist statisch, es gibt keinen
serverseitigen Mailversand. Deshalb sagen SPF und DMARC hier kompromisslos „niemand darf in meinem
Namen senden", und empfangende Server weisen Fälschungen ab. Der frühere `_dmarc`-CNAME auf
`dmarc.ionos.de` (`p=none`) wurde dafür gelöscht — ein CNAME und ein TXT können nicht auf demselben
Hostnamen stehen. **Muss zurückgedreht werden, falls jemals von `@secure-galvano-ai.com` gesendet
werden soll.** Die MX-Einträge bleiben bewusst stehen; SPF regelt nur den Versand, nicht den Empfang.

### `rvh.at` (Mail, Microsoft 365)

| Typ | Name | Ziel | Prio |
|-----|------|------|------|
| **MX** | `@` | `rvh-at.mail.protection.outlook.com` | **0** |
| **TXT** | `@` | `v=spf1 include:_spf-eu.ionos.com include:spf.protection.outlook.com ~all` | — |
| **TXT** | `_dmarc` | `v=DMARC1; p=none; rua=mailto:dmarc@rvh.at; fo=1` | — |
| **CNAME** | `autodiscover` | `autodiscover.outlook.com` | — |
| **CNAME** | `selector1._domainkey` | `selector1-rvh-at._domainkey.phonixdata.a-v1.dkim.mail.microsoft` | — |
| **CNAME** | `selector2._domainkey` | `selector2-rvh-at._domainkey.phonixdata.a-v1.dkim.mail.microsoft` | — |

DKIM ist seit 17.08.2026 aktiv (`Get-DkimSigningConfig -Identity rvh.at` → `Enabled True`,
`Status Valid`). Versandtest über mail-tester.com am 17.08.2026: **9,5/10**.

**Warum `rvh.at` anders behandelt wird als die Markendomain:** Hier laeuft produktiver Mailverkehr.
Ein hartes `-all` / `p=reject` ohne Belege koennte legitime Mails abweisen — etwa von einem System,
an das gerade niemand denkt. Deshalb steht DMARC bewusst auf `p=none` **mit `rua`**, die Berichte
gehen an das freigegebene Postfach `dmarc@rvh.at` (angelegt 17.08.2026). Eskalationsplan:

| Wann | Schritt |
|---|---|
| erledigt 17.08.2026 | `p=none` + `rua` — sammelt Belege, aendert nichts an der Zustellung |
| nach 2–4 Wochen | Berichte auswerten. Sendet nur Microsoft 365, kann `include:_spf-eu.ionos.com` raus |
| dann | `~all` → `-all` und `p=none` → `p=quarantine` |
| nochmals 2–4 Wochen spaeter | `p=quarantine` → `p=reject` |

Das Schaerfen ist seit dem 17.08. deutlich sicherer, weil DKIM aktiv ist: DMARC gilt schon als
bestanden, wenn **entweder** SPF **oder** DKIM passt. Bei Weiterleitungen bricht SPF regelmaessig,
die DKIM-Signatur ueberlebt sie.

#### Wiedervorlage — Outlook-Serientermin *(angelegt 17.08.2026)*

Erinnernde Aufgabe mit Urteilsbedarf, deshalb Kalendertermin und **kein** Task-Scheduler-Eintrag.
Serie: monatlich am zweiten Montag, **erster Termin 14.09.2026**, endet nach 3 Terminen
(14.09. · 12.10. · 09.11.), Erinnerung 1 Tag vorher. Termintext hier hinterlegt, damit er einen
Kalenderwechsel ueberlebt:

```
Betreff: DMARC rvh.at — Berichte pruefen und naechste Stufe setzen

Berichte liegen im freigegebenen Postfach dmarc@rvh.at (XML-Anhaenge).

SCHRITT 1 — Auswerten
Welche Systeme senden unter rvh.at? Erwartet wird ausschliesslich
Microsoft 365 (spf.protection.outlook.com).
Taucht etwas Unbekanntes auf: NICHT verschaerfen, erst klaeren.

SCHRITT 2 — Nur wenn Schritt 1 sauber ist, im IONOS-DNS setzen:
  TXT @       v=spf1 include:spf.protection.outlook.com -all
              (der IONOS-Include kann raus, wenn nichts darueber sendet)
  TXT _dmarc  v=DMARC1; p=quarantine; rua=mailto:dmarc@rvh.at; fo=1

SCHRITT 3 — Beim uebernaechsten Termin, wenn weiterhin nichts auffaellt:
  TXT _dmarc  v=DMARC1; p=reject; rua=mailto:dmarc@rvh.at; fo=1

PRUEFEN nach jeder Aenderung:
  nslookup -type=TXT rvh.at ns1027.ui-dns.de
  nslookup -type=TXT _dmarc.rvh.at ns1027.ui-dns.de
  Danach eine Testmail ueber mail-tester.com, Ziel weiterhin >= 9/10.

ABBRUCHKRITERIUM: Wenn nach einer Verschaerfung eine legitime Mail
nicht ankommt, sofort eine Stufe zurueck.

Hintergrund und Soll-Konfiguration beider Zonen:
homepage/README.md, Abschnitt DNS-Konfiguration.
```

## IONOS — Vertrag, Zugang, Vorfall *(Stand 17.08.2026)*

**Vertrag:** `100185485` (WordPress Hosting Grow) gekuendigt, am 08.06.2026 per Tarifwechsel in
einen **reinen Domain-Vertrag** ueberfuehrt — keine Grundgebuehr, nur die jaehrliche Domaingebuehr.
Zusatzartikel (Domain Guard, Mail Business, SSL) gekuendigt. `secure-galvano-ai.com` laeuft bis
**15.05.2027** mit **automatischer Verlaengerung**; beide Domains bei IONOS registriert, Nameserver
`ns*.ui-dns.*`. **Zahlungsmethode im Blick behalten** — fehlt sie, scheitert die Verlaengerung lautlos.

### Wenn der Login nicht mehr geht

Am 06.07.2026 wurde die Kontakt-Adresse auf `smaier@rvh.at` umgestellt. Seither meldet ein Login mit
der alten Kennung *„Ihr IONOS Login wurde geloescht"* — **irrefuehrend, sagt nichts ueber den Bestand
der Domains aus.** Weder die Kundennummer aus den ICANN-Mails noch der Domainname `secure-galvano-ai.com`
werden akzeptiert; ueber `rvh.at` kommt man bis zur Identifikation.

**Der Weg, der funktioniert:** telefonisch (**0721 170 555**) eine **„Kontozugangs-Wiederherstellung"**
verlangen — **nicht** die „Umschreibung der Kundennummer", das ist der Prozess fuer einen
Inhaberwechsel und hier falsch. Kein Formular unterschreiben, das nach Inhaberwechsel aussieht.
Identifikationsmerkmale: Vertrag 100185485, Tarifwechsel 08.06.2026, beide Domainnamen,
Kontaktadresse `smaier@rvh.at`. *(Kundennummer steht bewusst nicht im Repo, nur im Postfach.)*

### Der Vorfall — und was daraus folgt

Bei der Wiederherstellung des Zugangs fuehrte IONOS am 17.08. um 15:39–15:45 einen **„Domain-Umzug
innerhalb Ihrer Kundennummer"** durch und setzte dabei **beide Zonen auf Standardwerte zurueck**:
A/AAAA auf die IONOS-Standardseite, MX auf `mx00/mx01.ionos.de`, SPF ohne Outlook-Include,
`autodiscover` auf IONOS, `www`-CNAME ersatzlos weg.

Die Website meldete `ERR_SSL_PROTOCOL_ERROR`, spaeter 404. **Beim Mailverkehr gab es keine sichtbaren
Symptome** — eingehende Post waere still zu IONOS gelaufen, sobald die gecachten MX-Werte ablaufen
(TTL 3600 s). Das ist der gefaehrlichere Teil: Ein kaputtes Zertifikat sieht man, verlorene Antworten
nicht.

**Diagnose, in dieser Reihenfolge:**
1. `nslookup -type=A/AAAA/MX <domain> <autoritativer NS>` — **nicht** ueber den lokalen Resolver
   oder 8.8.8.8; deren Caches verschleiern den Zustand.
2. `curl --resolve <domain>:443:<GitHub-IP> https://<domain>` — trennt DNS- von TLS-Problem.
3. `gh api repos/secure-galvano-ai/homepage/pages` — zeigt, ob GitHub das Zertifikat noch fuehrt.
   Es war durchgehend `approved`; der Fehler lag ausschliesslich im DNS.

**Zwei Fallstricke der IONOS-Maske:** Eintraege tragen eine Spalte `Service` (`Default Site`, `Mail`).
Einzelne Zeilen lassen sich dann nicht aendern — man deaktiviert den **ganzen Dienst**, wodurch alle
zugehoerigen Zeilen verschwinden. Das Entfernen *eines* MX loescht also auch SPF, DMARC, DKIM und
autodiscover; danach alles neu anlegen. Und ein neuer A-Eintrag auf `@` kann einen bestehenden
`www`-CNAME verdraengen — IONOS meldet das im Bestaetigungsdialog, den man lesen muss.

**Nach jeder IONOS-Vertrags- oder Kontoaktion beide Zonen pruefen** (Routine-Check unten). Die
Verlagerung des DNS zu einem eigenen Anbieter wurde **geprueft und verworfen** *(Stefan, 17.08.2026)*:
nicht guenstiger, nicht spuerbar schneller, nicht pflegeleichter (zwei Systeme statt einem). Der
einzige Gewinn waere der Schutz vor genau diesem Reset — und dessen teurer Teil, die zweistuendige
Diagnose, ist mit den Soll-Tabellen oben erledigt. **Neu bewerten, wenn IONOS erneut in die Zone
eingreift**, dann mit einem EU-Anbieter (Hetzner DNS, deSEC) statt Cloudflare.

## Systeme und Abhängigkeiten

Wer hängt woran. Diese Übersicht existiert, weil am 17.08.2026 ein einziger DNS-Vorgang bei IONOS
gleichzeitig Website und Mailempfang lahmgelegt hat — der Zusammenhang war nicht offensichtlich.

| Baustein | Anbieter / Ort | Wichtige Fakten |
|---|---|---|
| **Domain-Registrierung** | IONOS SE | `secure-galvano-ai.com` läuft bis **15.05.2027**, **automatische Verlängerung aktiv**. `rvh.at` ebenfalls bei IONOS. Beide im selben Domain-Vertrag |
| **DNS-Zonen** | IONOS (`ns*.ui-dns.*`) | Beide Zonen. **Einziger Single Point of Failure** — siehe Vorfall oben |
| **Website-Hosting** | GitHub Pages | Repo `secure-galvano-ai/homepage`, Branch `main`, Root. Datei **`CNAME`** im Repo-Root enthält `secure-galvano-ai.com` — **nicht löschen**, sonst verliert Pages die Custom Domain |
| **TLS-Zertifikat** | GitHub Pages (Let's Encrypt) | Automatisch, deckt apex **und** `www`, gültig bis **04.11.2026**, erneuert sich selbst. Status: `gh api repos/secure-galvano-ai/homepage/pages` |
| **Mail** | Microsoft 365, Tenant **PhonixData** | Postfach `smaier@rvh.at`. Absenderadresse aller Geschäfts- und Akquisemails — **bleibt bewusst `@rvh.at`**, obwohl die Marke `secure-galvano-ai.com` lautet *(Entscheidung Stefan, 17.08.2026)* |
| **Terminbuchung** | Microsoft Bookings | Läuft auf dem **rvh.at-Tenant**. Hängt damit am selben Microsoft-365-Konto wie die Mail |
| **Analyse** | Microsoft Clarity | Projekt `wql3vpgrxl`, Opt-in |
| **Indexierung** | Google Search Console | Property auf `secure-galvano-ai.com` — bei DNS-Ausfall meldet sie Crawl-Fehler |

### Was bricht was

| Ursache | Folge | Sichtbar? |
|---|---|---|
| A-Records auf `@` fehlen oder falsch | Website komplett unerreichbar | ja, sofort |
| **AAAA-Eintrag vorhanden** (auf etwas anderes als GitHub) | HTTPS bricht für alle IPv6-Clients, `ERR_SSL_PROTOCOL_ERROR` | ja, aber nur für einen Teil der Besucher — leicht zu übersehen |
| `CNAME`-Datei im Repo gelöscht | Pages verliert Custom Domain, Zertifikat wird ungültig | verzögert |
| **MX von `rvh.at` falsch** | eingehende Mail geht verloren oder landet woanders | **nein** — sieht aus wie „keine Antwort" |
| SPF/DKIM fehlen | ausgehende Mails landen im Spam, DMARC schlägt fehl | nein |
| `autodiscover` falsch | Outlook-Neueinrichtung schlägt fehl, bestehende Clients laufen weiter | verzögert |
| Microsoft-365-Konto gesperrt | Mail **und** Terminbuchung auf der Website gleichzeitig tot | ja |

### Routine-Check

Nach **jeder** Vertrags- oder Kontoänderung bei IONOS beide Zonen gegen die Soll-Tabellen oben
prüfen — und zwar gegen den **autoritativen** Nameserver, nicht über den lokalen Resolver:

```bash
nslookup -type=A   secure-galvano-ai.com ns1093.ui-dns.com
nslookup -type=AAAA secure-galvano-ai.com ns1093.ui-dns.com
nslookup -type=MX  rvh.at ns1027.ui-dns.de
nslookup -type=TXT rvh.at ns1027.ui-dns.de
```

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
| Microsoft 365 | Mail `smaier@rvh.at`, Tenant **PhonixData** | `admin.microsoft.com` · DKIM: `security.microsoft.com` |
| Microsoft Bookings | Erstgespräch buchen (60 Min.) — **läuft auf dem rvh.at-Tenant** | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/` |
| Microsoft Bookings — **Kurzgespräch 30 Min.** *(neu 03.09.2026)* | Dienst-Direktlink für die Akquise, seit 03.09. auch auf der Buchungsseite sichtbar. Verwendungsregel: [`mailsequenz/README.md`](../Business%20Development/projects/akquise-strategie-h2-2026/mailsequenz/README.md) § *Buchungslinks* | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/s/j9sT4U4iQ0WwxD0oCfcdeg2` |
| Microsoft Clarity | Web-Analyse (Opt-in, Projekt `wql3vpgrxl`) | `clarity.microsoft.com` |
| Google Search Console | SEO / Indexierung | `search.google.com/search-console` |
| GitHub Pages | Hosting + TLS-Zertifikat | `github.com/secure-galvano-ai/homepage/settings/pages` |
| IONOS | **Domain-Registrar und DNS-Betreiber** — Login über Kundennummer, nicht über die Mailadresse | `my.ionos.de` · Service `0721 170 555` |

> Alle Abhängigkeiten zwischen diesen Diensten stehen im Abschnitt
> [Systeme und Abhängigkeiten](#systeme-und-abh%C3%A4ngigkeiten).

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

### Nach dem Push: Deploy bestätigen *(Regel seit 26.08.2026, Stefan)*

`check_site.py` prüft die **Dateien vor** dem Push. Es kann prinzipiell nicht sehen, was
danach live steht — und genau dort lag die Panne vom 02.07.2026: Der Build gelang, der
**Deploy**-Job scheiterte GitHub-seitig, und die Seite blieb still auf dem alten Stand.
Zwei Stunden Suche, weil lokal alles grün war.

**Pflicht — ein Befehl, fünf Sekunden:**

```bash
cd homepage && gh run list --limit 1
# erwartet: completed  success  pages build and deployment
```

Steht dort `failure` oder hängt der Lauf: **nicht neu pushen**, sondern die Anti-Patterns
unten lesen. Ein zweiter Push auf denselben Fehler kostet nur Zeit.

**Zusätzlich in den Browser — aber nur, wenn sich sichtbar etwas geändert hat**
(Layout, CSS, Assets, Textbausteine, generierte Seiten). Dann rund eine Minute warten und
die geänderte Seite **live** öffnen, nicht lokal:

- `browser_navigate` auf `https://secure-galvano-ai.com/...` + `browser_snapshot` — ist die
  Änderung da, stehen Navigation und Footer unverändert?
- `browser_console_messages` — neue Fehler?
- Bei Layout- und Designänderungen **ein Bildschirmfoto ansehen**. Der Strukturbaum zeigt
  keine verrutschten Abstände, überlappenden Elemente oder falschen Farben.

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
   - `deploy` + `Deployment cancelled` → **Concurrency** (Punkt 2).
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
   **Abgrenzung zu Punkt 2:** Läuft ein Deploy noch oder wartet er regulär → Finger weg, jeder
   Trigger cancelt ihn. Hängt er als Zombie (`queued`, nicht cancelbar, > 30 Min) → genau dieser
   POST ist der Ausweg. `githubstatus.com` meldete dabei durchgehend „operational", taugt also
   nicht als Entscheidungsgrundlage.
3. **NIEMALS mehrere Pages-Deploys schnell hintereinander triggern.** Die Concurrency-Gruppe `pages` hat **Queue-Tiefe 1** — jeder neue Deploy **cancelt den vorher wartenden**. Rapides `git push` + wiederholtes `gh api --method POST .../pages/builds` erzeugt eine Kaskade aus `Deployment cancelled`/`failure`. → **EINMAL pushen, dann 2–10 Min ungestört warten. Nicht nachtreten.**
4. **Bei Fehler zuerst die LIVE-Seite prüfen, nicht blind retrien** (letzter guter Build bleibt live, meist schon korrekt): `curl -s https://secure-galvano-ai.com/ | grep -o '<h1>[^<]*'`
5. **`.nojekyll` NICHT reflexartig hinzufügen.** Der Jekyll-`build` gelingt hier (getestet); `.nojekyll` löst das Deploy-Problem NICHT und liefert zusätzlich `_generate_*.py` **öffentlich** aus (Jekyll schließt `_`-Dateien sonst aus). → **ohne `.nojekyll` bleiben.**
6. **Kein `{{ … }}` / `{% … %}` im HTML** — Jekyll/Liquid parst das und failt den *Build* (war hier NICHT die Ursache, ist aber die klassische echte Build-Bremse).

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
