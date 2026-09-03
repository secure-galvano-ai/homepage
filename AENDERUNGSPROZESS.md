# Änderungsprozess Homepage

*Angelegt 31.08.2026 (Stefan). Abgeleitet aus dem Umbau desselben Tages — Leistungsseite,
Flyer, Beispiel-Befund und die Nachführung im Business-Development-Repo.*

> **Kein eigener Prozess, sondern eine Ergänzung.** Der Änderungsablauf steht in
> [`AGENTS.md` §5](../AGENTS.md) und gilt hier unverändert: Change-Klasse bestimmen,
> Anforderung klären, Assessment, Freigabe, Umsetzung, zyklische Verifikation. Die
> Querregeln gelten ebenso — fremde Arbeit in Ruhe lassen, Fehler zuordnen bevor man
> repariert, Nebenbefunde melden statt mitfixen, vermutete Ursachen erst nach der
> Messung dokumentieren.
>
> **Was hier steht, ist das, was eine Website zusätzlich braucht** und was Code nicht
> hat: Zahlen als Ausgangspunkt, Wirkung auf Leser statt auf Funktionen, Redundanz über
> Seiten hinweg, SEO, Konsistenz zu Dokumenten außerhalb des Repos, und ein Deploy, den
> man bestätigen muss.

**Abgrenzung zu [`OPTIMIERUNG.md`](OPTIMIERUNG.md):** Dort steht der **monatliche
Messlauf** — was gemessen wird, woher die Zahlen kommen, welche Entscheidungsregeln
gelten. Hier steht, **wie eine Änderung abläuft**, wenn sie beschlossen ist. Der Messlauf
liefert die Befunde, dieser Prozess setzt sie um. Merksatz: `OPTIMIERUNG.md` = was ist,
`AENDERUNGSPROZESS.md` = wie ändern.

---

## Der Zyklus

```
   ┌──────────────────────────────────────────────────────────────┐
   │                                                              │
   ▼                                                              │
 MESSEN ──► VERSTEHEN ──► ÄNDERN ──► PRÜFEN ──► VERÖFFENTLICHEN ──┘
 Clarity     Ursache vor   kleinster  vier      Deploy
 GSC         Maßnahme      Schnitt    Gates     bestätigen
 LinkedIn
```

**Eine Runde je Monat**, ausgelöst vom Serientermin am ersten Werktag. Dazwischen laufen
nur Änderungen, die aus einem belegten Befund kommen oder die ein Produkt nachziehen
(dann gilt §*Konsistenz nach außen* unten).

---

## Schritt 1 — Zahlen ansehen, bevor irgendetwas geändert wird

**Die häufigste Fehlerquelle ist nicht die Umsetzung, sondern die falsche Baustelle.**
Am 31.08.2026 lautete die Ausgangsvermutung, das Leistungsangebot komme auf der Website
nicht rüber, weil die Akquise wenig Rücklauf hatte. Die Zahlen zeigten: die Akquisemails
gehen bewusst link- und anhangfrei raus, die Empfänger waren nie auf der Seite. Die
Vermutung war plausibel und die Baustelle falsch.

Vor jeder Änderung deshalb:

| Frage | Quelle |
|---|---|
| Wie viele Leute sehen das überhaupt? | Clarity-Dashboard, 28 Tage |
| Wo brechen sie ab — mobil und Desktop getrennt? | Clarity Scroll-Heatmap |
| Was klicken sie, was nicht? | Clarity, Intelligente Ereignisse |
| Wie kommen sie an, mit welchen Begriffen? | Search Console |
| Ist der betroffene Bereich überhaupt im Weg der Nutzer? | Top-Seiten, Referrer |

**Wenn die Zahlen die Vermutung nicht stützen, wird die Vermutung geändert, nicht die
Seite.** Das kostet zehn Minuten und spart einen halben Tag.

---

## Schritt 2 — Klasse bestimmen

Wie in `AGENTS.md` §5, übersetzt auf die Website:

| Klasse | Beispiele | Ablauf |
|---|---|---|
| **Standard** | Tippfehler, Datum, ein Link, ein PDF austauschen | Schritt 4–6, ohne Assessment |
| **Normal** | Text mit Aussagewirkung, neue Sektion, Navigation, Meta-Angaben, Preisaussagen | alle Schritte |
| **Emergency** | falsche Rechtsaussage, kaputter CTA, Ausfall | Umsetzung + Verifikation sofort, Rest danach nachziehen |

**Preis-, Leistungs- und Rechtsaussagen sind nie Standard** — auch wenn es nur ein Wort ist.

---

## Schritt 3 — Umsetzen, aber höchstens drei Änderungen im Monat

Die Regel steht in [`OPTIMIERUNG.md`](OPTIMIERUNG.md) §5 und ist keine Bequemlichkeit: bei
rund hundert Sitzungen im Monat lässt sich die Wirkung von mehr als drei Änderungen im
Folgemonat nicht mehr zuordnen. **Ausgenommen ist das Nachziehen eines geänderten
Produkts** — wenn sich das Angebot ändert, muss die Kommunikation folgen, sonst
verspricht die Seite etwas anderes als geliefert wird.

**Beobachtete Reibung schlägt Vermutung.** Ein toter Klick aus einer Aufzeichnung wird
behoben; eine Farbidee ohne Beleg nicht.

---

## Schritt 4 — Die vier Gates vor dem Commit

### Gate 1 · Automatisch

```
py _scripts/check_site.py       # Dateien, Links, Assets
py _scripts/check_inhalt.py     # Metadaten, Überschriften, Marker, Dubletten, Sitemap
```

`check_inhalt.py` bricht ab bei: doppelten Titeln oder Descriptions, fehlendem canonical,
mehr als einer H1, doppelt vergebenen Funnel-Markern, einem CTA ohne Marker, toten
Ankern, Seiten außerhalb der Sitemap. Als Hinweis meldet es Längen außerhalb der
Zielbereiche, Überschriften-Sprünge und Textdubletten — die brauchen ein Urteil.

### Gate 2 · Wording

Jeder neue Satz durchläuft den **Carnegie-Durchlauf** aus `CLAUDE.md` §1: Was hat der
Leser davon? Ich-Satzanfänge minimieren, Qualifikation an den Nutzen anhängen, kein Satz,
der ein Defizit beim Leser feststellt. Prüfen lässt sich das mechanisch:

```
grep -oE '\b(Ich|ich|mich|mir|mein\w*)\b' leistungen.html | wc -l
```

Bleibt eine Ich-Form stehen, muss sie begründet sein — in der Navigation („Über mich")
ist sie richtig, in einer Leistungsbeschreibung selten.

### Gate 3 · Sichtprüfung im Browser, mobil **und** Desktop

**Nicht ansehen, sondern messen.** Am 31.08.2026 lag der Haupt-CTA auf dem Handy hinter
dem Cookie-Banner — im Screenshot nicht auffällig, in der Messung eindeutig:

```js
// Element gegen Banner, bei scrollY = 0
const r = document.querySelector('[data-funnel="cta-hero"]').getBoundingClientRect();
const b = document.querySelector('.consent-banner').getBoundingClientRect();
// Seitliche Lage mitprüfen — sonst meldet der Test eine Überdeckung, die es nicht gibt
r.bottom > b.top && r.top < b.bottom && r.left < b.right && r.right > b.left
```

Pflicht bei jeder sichtbaren Änderung: **390 × 844 (mobil), 1366 × 768 (Notebook) und
1280 × 900 (Desktop)**, Seitenhöhe prüfen, jeden neuen Link einmal klicken, Anker anspringen
lassen.

**1366 × 768 ist seit 02.09.2026 Pflichtmaß** und hat sofort einen Treffer geliefert: Auf der
Startseite lag der Haupt-CTA (y 655–707) vollständig hinter dem Einwilligungsbanner
(y 613–752) — derselbe Fehler wie am 31.08. auf dem Handy, nur auf dem verbreitetsten
Notebook-Format. **Das Banner klebt an `bottom`, der CTA an der Hero-Höhe: Je flacher das
Fenster, desto sicherer treffen sie sich.** Ein hoher Desktop-Viewport zeigt das Problem nie.

**Bannerkonflikte flächig prüfen, nicht je Seite** *(03.09.2026)*. Zwei Einzelfälle in drei
Tagen (31.08. mobil, 02.09. auf 1366 × 768) waren dieselbe Ursache: Das Banner klebt unten
links, die Hero-Knöpfe stehen links — sie treffen sich, sobald der Hero hoch genug ist. Eine
Messung über **alle Seiten × alle Pflichtmaße** in einem Durchgang (Iframe je Größe, jedes
`data-funnel`-Element gegen das Bannerrechteck) fand am 03.09. sofort **zwei weitere**, die
niemand vermutet hatte: `cta-leistungen-hero` auf **1280 × 900 und 1440 × 900**. Beide lagen
oberhalb der damaligen `max-height:860px`-Schranke. **Wer einen Bannerkonflikt findet, sucht
die Klasse, nicht den nächsten Einzelfall** — die Lösung war eine Zeile statt einer dritten
Sonderregel. **Den WhatsApp-Knopf mitmessen**, er ist das Ausweichziel.

**Beim Prüfen den Browser-Cache bedenken:** `consent.js` wird gecacht, eine geänderte Regel
wirkt im lokalen Test erst nach hartem Neuladen. Wer nur misst und nicht gegenprüft, hält eine
wirksame Änderung für unwirksam — Gegenprobe ist `document.querySelectorAll('style')` auf die
neue Regel oder ein `fetch` der Datei.

### Gate 3b · Die Seite als Station einer Reise lesen *(neu 02.09.2026)*

Eine Seite kann für sich stimmen und trotzdem an der falschen Stelle stehen. Vier Fragen, je
Änderung in zwei Minuten beantwortbar:

| Frage | Woran man scheitert |
|---|---|
| **Woher kommt der Besucher — Mail, Suche, Vortrag, Empfehlung?** | Aus einer Mail kommt jemand mit einer konkreten Frage. Findet er oben keinen Einstieg, scrollt er nicht bis zum CTA am Seitenende (Befund `ausbildung.html`, 02.09.2026) |
| **Welche Frage hat er in dieser Phase — und beantwortet die Seite genau die?** | Orientierung braucht einen Beleg zum Mitnehmen (PDF), nicht sofort einen Termin. Deshalb steht auf der Datenwerkstatt-Seite **PDF vor Termin** |
| **Gibt es mehr als eine sinnvolle Fortsetzung? Dann steht sie als Weiche da, nicht als Nachsatz** | Standortanalyse und Datenwerkstatt sind gleichwertige Antworten auf „wer macht es". Als Halbsatz angehängt verliert die zweite immer |
| **Welche stille Frage bleibt offen?** | „Was passiert mit meinen Daten" ist bei Galvanikbetrieben die häufigste. Sie braucht einen Verweis dort, wo Daten zur Sprache kommen — nicht nur im Fußbereich |

**Ein Weg pro Seite und Phase.** Zwei gleichrangige Links nebeneinander halbieren die
Entscheidung; eine Weiche mit zwei benannten Wegen ist etwas anderes als zwei konkurrierende
Knöpfe.

### Gate 4 · Konsistenz nach außen

Die Website ist nicht die einzige Stelle, an der dieselbe Aussage steht. **Bei jeder
Änderung an Leistung, Ablauf, Preis oder Benennung mitprüfen:**

| Wo | Was dort steht |
|---|---|
| `templates/flyer-corporate/build_flyer.py` | Flyer — Ablauf, Aufwand, Preis |
| `templates/befund-corporate/build_befund.py` | Beispiel-Befund — Ablauf, Ergebnisumfang |
| `areas/standortanalyse-durchfuehrung.md` | Prozess, Kriterien, offene Punkte |
| `areas/business-model.md` | die Leiter, die Preise, die Benennung |
| `areas/brand/messaging.md`, `competition.md`, `marketing.md` | Einwandantworten, Preis-Einstieg |
| `areas/sales-pipeline.md` + Leadliste `Listen` | Statuswerte, Stufenbenennung |
| JSON-LD in `index.html` | das, was Google ausspielt |

**Das ist der teuerste Fehlerherd.** Am 31.08.2026 stand nach dem Website-Umbau in
`business-model.md` noch die alte Leiter mit einem Festpreis, den es nicht mehr gab.
Prüfen mit `grep` auf den alten Begriff, nicht aus dem Kopf.

---

## Schritt 5 — Veröffentlichen und bestätigen

```
git add <nur die eigenen Dateien>     # nie -A, fremde Arbeit bleibt draußen
git commit
git push
gh run list --limit 1                 # erwartet: completed success
curl.exe -s <URL> | grep <neuer Text> # der Beweis, dass es live ist
```

**Der Deploy-Check ist Pflicht**, nicht Kür: `check_site.py` prüft die Dateien **vor** dem
Push und kann prinzipiell nicht sehen, was live steht. Am 02.07.2026 gelang der Build und
scheiterte der Deploy — zwei Stunden Suche, weil lokal alles grün war.

---

## Schritt 6 — Zurück in die Messung

Jede Änderung, deren Wirkung man sehen will, braucht **einen eigenen Funnel-Marker**.
Ohne ihn ist sie im nächsten Monatslauf unsichtbar. Neue Marker in
[`OPTIMIERUNG.md`](OPTIMIERUNG.md) §4 nachtragen, damit sie beim nächsten Lauf abgefragt
werden.

Im Bericht des Folgemonats steht dann unter *Wirkung der Änderungen* mit Datum, was die
Änderung gebracht hat — oder dass sie nichts gebracht hat. Beides ist ein Ergebnis.

---

## Fallstricke, die schon Zeit gekostet haben

- **`overflow:hidden` verschluckt Inhalt lautlos.** Bei den PDF-Generatoren bricht die
  Seitenzahl-Prüfung nicht, wenn ein Abschnitt abgeschnitten wird. Deshalb prüfen beide
  Generatoren zusätzlich, ob definierte Pflichtstellen im fertigen PDF stehen. Marker
  dafür **schreibungsunabhängig** vergleichen (Überschriften stehen per CSS in Versalien)
  und nur Zeichenketten nehmen, **die im Layout nicht umbrechen**.
- **Einen CSS-Selektor umbenennen trifft mehr als die eine Stelle.** `.project-card h3`
  auf `h2` umzustellen nahm der zweiten Karte die Formatierung, weil sie weiter eine `h3`
  führt. Nach jeder Selektor-Änderung die berechneten Stile im Browser gegenprüfen.
- **Handgepflegte Seiten driften.** `sicherheit.html` war die einzige Seite mit eigener
  Navigation und hat einen neuen Menüpunkt nicht mitbekommen. Alle Seiten gehören in
  `_generate_layout.py`.
- **Bei exakt 297 mm Seitenhöhe wirft Chrome eine leere zweite Seite aus.** Die Generatoren
  stehen deshalb auf 296,6 mm. Wer das nicht weiß, kürzt Inhalt, der nicht zu lang ist.
- **Videos in neue Tabs zu verlinken zieht vom Angebot weg.** Bewegtbild gehört auf die
  Seite oder auf `demo.html`, nicht mitten in eine Leistungsbeschreibung.

---

## Was hier bewusst nicht steht

**Keine Rollen, keine Freigabestufen, kein Redaktionsplan.** Hier arbeiten ein Mensch und
Agenten; die Freigabe ist ein Satz im Chat. Und **keine Wiederholung von `AGENTS.md` §5** —
wenn dort etwas geändert wird, soll es hier nicht zweimal falsch stehen.
