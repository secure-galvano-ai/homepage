---
title: "Was in Anlagendaten steckt"
subtitle: "Fünf Auswertungen an einem exemplarischen Betrieb"
reference: "Rechenwege der Galvanotechnik, angewandt auf laufende Betriebsdaten"
footnote: "Sämtliche Zahlen sind exemplarisch gewählt. Es fließen keine Daten aus Kundenprojekten ein."
---

# Worum es geht

Eine Galvanikanlage schreibt jeden Tag Zehntausende Messwerte. Die wenigsten davon werden
ausgewertet. Dieses Dokument zeigt an einem **exemplarischen Betrieb**, was sich aus
diesen Daten rechnen lässt — und wo die Grenze zwischen einer belastbaren Aussage und
einer Vermutung verläuft.

**Sämtliche Zahlen sind exemplarisch gewählt.** Betrieb, Anlage, Messwerte und Mengen
stammen aus keinem realen Projekt. Die Rechenwege dagegen sind die üblichen der Galvanotechnik; die
Quellen stehen am Ende.

Der betrachtete Betrieb fährt eine **Zink-Nickel-Gestellanlage im alkalischen Elektrolyten**:
6 Warenträger je Stunde mit 1,8 m² Warenoberfläche, also 10,8 m² je Stunde, im
Zweischichtbetrieb an 220 Tagen — 3.520 Betriebsstunden im Jahr, bei 1.800 A mittlerem
Strom.

# 1 Strom und Spannung: der Widerstand als früherer Indikator

Gleichrichter zeichnen Spannung und Strom auf. Beide schwanken im Betrieb, und beide
schwanken normalerweise deutlich — Beschickung, Temperatur und Badalter wirken auf sie
ein. Eine einzelne Größe ist als Überwachungsgröße deshalb wenig geeignet.

Aus beiden zusammen lässt sich der Widerstand bilden, und dieser verhält sich anders:

| | Spannung | Strom | Widerstand |
|---|---|---|---|
| Normalzustand | 8,20 V | 1.800 A | 4,556 mΩ |
| beginnende Kontaktstörung | 8,45 V | 1.710 A | 4,942 mΩ |
| Änderung | **+3,0 %** | **−5,0 %** | **+8,5 %** |

Entscheidend ist die letzte Spalte. Eine Spannungsänderung von drei Prozent und eine
Stromänderung von fünf Prozent liegen bei den meisten Anlagen noch im normalen Rauschen —
jede für sich würde keinen Alarm auslösen. Der Widerstand steigt dagegen um 8,5 Prozent,
weil sich beide Effekte im Quotienten **addieren**, statt sich auszugleichen.

Deshalb ist die erste Frage an eine Anlage nicht, ob sie Werte aufzeichnet, sondern ob sie
**beide** aufzeichnet. Eine Anlage, die nur die Spannung festhält, lässt diesen Hebel
ungenutzt.

# 2 Amperestunden: was hätte abgeschieden werden müssen

Der Stromverlauf trägt mehr Information, als die Momentanwerte erkennen lassen. Über sein Zeitintegral — die Amperestunden —
liegt die abgeschiedene Metallmenge physikalisch fest. Das elektrochemische Äquivalent
folgt aus der molaren Masse, der Wertigkeit und der Faraday-Konstante:

    Ae = M / (z · F)

Für Zink mit M = 65,38 g/mol und z = 2 ergibt das 1,2197 g je Amperestunde. Davon kommt
allerdings nicht alles auf der Ware an: ein Teil des Stroms geht in die
Wasserstoffentwicklung. Der Anteil, der tatsächlich abscheidet — die Stromausbeute —
hängt stark am Elektrolyten:

| Elektrolyt | Stromausbeute | wirksam |
|---|---|---|
| saures Zink | 90 – 95 % | rund 1,10 g/Ah |
| alkalisches Zink, Zink-Nickel | 50 – 70 % | rund 0,73 g/Ah bei 60 % |

**Diese Zahl muss immer mit dem Elektrolyttyp genannt werden.** Eine Verwechslung verschiebt
das Ergebnis um den Faktor 1,5.

Für unser Beispiel:

    6.336.000 Ah  ×  0,7318 g/Ah  =  rund 4.637 kg Zink im Jahr

Das ist keine Schätzung und kein Erfahrungswert, sondern eine physikalische Untergrenze
dessen, was der Betrieb verbraucht haben muss. Sie entsteht ohne einen einzigen neuen
Sensor — der Strom wird ohnehin aufgezeichnet.

Dieser Weg umgeht zugleich eine bekannte Fehlerquelle: Rechnet man stattdessen von der
Sollschichtdicke aus, muss man einen Zuschlag für mechanischen Abrieb und für die
Streuung der Teile schätzen — in der Literatur rund 15 Prozent. Die gemessenen
Amperestunden enthalten diesen Effekt bereits.

# 3 Verschleppung: der zweite große Posten

Was die Ware aus dem Bad trägt, ist kein Nebeneffekt, sondern die zweite bestimmende
Größe für den Chemikalienverbrauch — und sie hängt an der **Fläche**, nicht an der
Stückzahl. Je Quadratmeter Warenoberfläche verlassen je nach Verfahren 100 bis 250
Milliliter das Becken, abhängig von Abtropfzeit, Geometrie und Viskosität. Die
Fachliteratur rechnet Beispiele mit 120 ml/m²; wir setzen hier 180 an.

    10,8 m²/h  ×  180 ml/m²  =  1,94 l/h  →  6.843 l im Jahr

Wie stark der Wert durchschlägt, zeigt die Gegenrechnung: mit 120 ml/m² wären es 4.562
Liter — ein Drittel weniger. Der Wert sollte deshalb bestimmt und nicht geschätzt werden.

## Woran die Verschleppung hängt

**Abtropfzeit.** Der wirksamste und zugleich kostengünstigste Hebel. Empfohlen werden 10 Sekunden bei
Gestellen, vor und hinter stark belasteten Bädern eher 15 bis 20. Bei Trommeln zwei halbe
Umdrehungen über dem Becken. Sehr lange Abtropfzeiten helfen nicht weiter — bei den
meisten Verfahren beginnt die Oberfläche dann zu reagieren.

**Gestellgeometrie.** Schöpfende Teile und Hohlräume tragen ein Vielfaches der glatten
Fläche aus. Dreh-, Kipp- und Schwenkgestelle entleeren sie über dem Becken; ein Rücklaufblech
mit Gefälle zum Bad führt das Abgetropfte zurück, statt es in die Spüle zu tragen.

**Trommel gegen Gestell.** Bei Schüttgut ist die Fläche je Charge nicht direkt bekannt und
muss über Teilegeometrie und Stückzahl abgeschätzt werden. Das ist der Grund, warum
Trommelanlagen in dieser Rechnung immer unsicherer sind als Gestellanlagen — nicht die
Physik unterscheidet sich, sondern die Kenntnis der Fläche.

## Die Gegenprobe über die Spüle

Der Tabellenwert lässt sich überprüfen. Als Maß für die Spülqualität
dient die dimensionslose **Kushnerzahl** — das Verhältnis der Konzentration im Prozessbad
zu der in der letzten Spüle:

    Ku = c₀ / cₙ

Für Verzinken nennt die Literatur Werte von 1.000 bis 3.000. Bei einer n-stufigen Kaskade
gilt näherungsweise:

    Q̇ = q̇ · ( ⁿ√Ku − 1 )

Mit Ku = 2.400 und drei Stufen ergibt das aus 1,94 l/h Verschleppung einen
Frischwasserbedarf von **24,1 l/h**. Dieselbe Spülqualität in einer Einfachspüle
verlangte **4.666 l/h** — das 194-Fache. Der Spülwasserbedarf wird damit
vorrangig von der Stufenzahl bestimmt.

Die Formel lässt sich umstellen. Aus dem gemessenen Frischwasserzulauf und dem Leitwert
der letzten Stufe, der sich proportional zur Konzentration verhält, folgt die
**tatsächliche** Verschleppung:

    q̇ = Q̇ / ( ⁿ√Ku − 1 )

Damit wird aus dem Tabellenwert eine Messung. Und wenn beide Wege auseinanderlaufen, ist
genau diese Differenz die Information: Sie zeigt, ob die Abtropfzeiten im Betrieb halten,
was die Auslegung annimmt.

Zwei Einschränkungen sind zu beachten. Die Näherung trägt nur oberhalb von etwa 20 l/h — unser
Beispiel liegt mit 24,1 l/h knapp darüber, ohne Reserve. Und die Rückführung aus der
Sparspüle ins Bad ist durch die **Verdunstung** begrenzt: Zurückführen lässt sich nur die Menge, die im
Arbeitsbehälter verdunstet.

# 4 Die Bilanz

Beide Rechnungen zusammen ergeben eine Bilanz. Was der Betrieb an einer Chemikalie
entnimmt, verteilt sich auf vier Posten:

    Entnahme  =  Abscheidung  +  Verschleppung  +  Zersetzung  +  Rest

Die ersten drei sind rechenbar. Für das Zink unseres Beispielbetriebs:

| Posten | Menge | Anteil | Woher |
|---|---|---|---|
| Abscheidung | 4.637 kg | 98,8 % | Amperestunden × Äquivalent × Stromausbeute |
| Verschleppung | 55 kg | 1,2 % | Fläche × Ausschleppung × Konzentration |
| Zersetzung | 0 kg | — | Metall zersetzt sich nicht |
| **erwartet** | **4.692 kg** | | |
| Ist-Entnahme laut Lager | 5.008 kg | | |
| **Rest** | **316 kg** | **6,7 %** | nicht erklärt |

Der Zersetzungsterm ist beim Metall null, bei Additiven dagegen der bestimmende Posten —
Glanzbildner und Komplexbildner werden an der Anode oxidiert, und zwar
**überproportional** zur anodischen Stromdichte. Bei cyanidischen Elektrolyten ist dieser
Zusammenhang seit Langem als Gleichung beschrieben und wird auch dort auf die
Ladungseinheit bezogen gerechnet. Praktisch heißt das: Eine schrumpfende Anodenfläche
treibt den Verbrauch je Amperestunde stärker als linear.

Aufschlussreich ist die Verteilung. Das über die Verschleppung verlorene
Metall macht nur gut ein Prozent aus — der wirtschaftliche Schaden der Verschleppung liegt
nicht beim Metall, sondern bei Additiven, Komplexbildnern und der Abwasserbehandlung.
Wer die Verschleppung über den Metallwert rechnet, unterschätzt sie erheblich.

# 5 Der Rest ist die eigentliche Information

Die 316 Kilogramm sind das Ergebnis dieser Auswertung — nicht die 4.637.

Die ersten drei Posten sind vorhersagbar. Sie lassen sich auch überschlagen; ein
Erkenntnisgewinn entsteht daraus nicht. Aussagekräftig wird die Bilanz dort, wo sie **nicht**
aufgeht.
Ein Rest von wenigen Prozent ist normal: Wägetoleranzen, Buchungsungenauigkeit im Lager,
Schwankungen der Stromausbeute über das Badalter. Ein Rest, der darüber hinauswächst oder
über die Monate systematisch zunimmt, begründet eine Ursachensuche.

Der eigentliche Wert liegt darin, dass das System **überbestimmt** ist. Die Amperestunden
kommen aus dem Strom, die Verschleppung unabhängig davon aus Leitwert und Durchsatz. Zwei
Wege auf dieselbe Größe. Stimmen sie überein, ist eine Aussage belegt statt geschätzt.
Weichen sie voneinander ab, ist der Anlass zur Ursachensuche eindeutig. Das unterscheidet
das Vorgehen von einer Grenzwertüberwachung, die lediglich meldet, dass ein Wert
überschritten wurde.

Welche Ursache hinter welchem Rest steckt und wie er sich zuordnen lässt, ist der Teil,
der in einem Projekt erarbeitet wird. Er hängt an der einzelnen Anlage und lässt sich
nicht aus einem Dokument ableiten.

# Was hier bewusst nicht steht

**Keine Zusagen.** Die Rechenwege sind allgemein, die Zahlen exemplarisch. Was Ihre Anlage
tatsächlich zeigt, ergibt sich erst aus der Auswertung Ihrer Daten.

**Keine Betriebsdaten.** Es sind keine Werte aus Kundenprojekten eingeflossen — weder
gerundet noch verfremdet.

**Kein Verfahren.** Wie aus einem unerklärten Rest eine Diagnose wird, welche
Verbrauchskoeffizienten je Chemikalie gelten und wo die Grenze zwischen Rauschen und
Befund liegt, steht hier nicht. Das ist die Arbeit, nicht ihre Beschreibung.

**Zum Aufwand.** Die Amperestunden-Rechnung braucht keinen neuen
Sensor, aber Verbrauchsmengen, die je Anlage gebucht sind. Wird im Lager nur nach Gebinde
gebucht, ohne Anlagenzuordnung, fehlt die zweite Hälfte der Bilanz.

# Quellen

Die Rechenwege sind Fachwissen der Galvanotechnik und in der Literatur beschrieben:
J. N. M. Unruh, *Lehrbuch der Galvanotechnik* (Leuze Verlag) — Kushnerzahl,
Kaskadenformel, Stoffbilanz einer Spülstufe, elektrochemisches Äquivalent, Verbrauch je
Ladungseinheit. Hauser, *Spülen ist berechenbar und beherrschbar* (WOMag 2013) —
Spülkriterium und Maßnahmen zur Verschleppungsminderung. TU Dresden, *Spritzspülen*
(Galvanotechnik 1/2004) — messtechnische Bestimmung des Verschleppungsvolumens. Dazu die
Ressourceneffizienz-Praxisbeispiele der öffentlichen Beratungsstellen zu Abtropfzeiten und
Gestelltechnik.
