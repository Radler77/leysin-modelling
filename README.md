Leysin Modelling
===

# Projektplan

## 1. Konkretisierte Fragestellung

Wie entwickeln sich Populationen im Wettkampf um verschiedene Ressourcen, abhängig von ihrem individuellen Verhalten? Wie breitet sich kooperatives vs. egoistisch-aggressives Verhalten unter Ressourcenknappheit aus?

## 2. Auswahl der Modellierungsklasse und -instrumente

Wir realisieren die Populationen als agentenbasiertes Modell mit verschiedenen Strategien.

## 3. Auswahl der Lösungsinstrumente

Das agentenbasierte Modell simulieren wir iterativ (und teilweise randomisiert), um eine "experimentelle" Approximation der zu erwartenden Dynamik zu erhalten.

## 4. AM Modell konkretisiertes Ziel

Wie entwickelt sich die Größe der Population, gegeben definierter Reproduktionsregeln?
Wie entwickelt sich die Umgebung, gegeben verschiedener Überlebensstrategien der Agenten? Kommt es beispielsweise zu einer Zerstörung/Degradierung frei nutzbarer Ressourcen? (Tragedy of Commons)
Welche Strategien setzen sich evolutionär in der Population durch, wenn verschiedene Agententypen durchmischt werden?

## 5. Abgleich mit Fähigkeitsprofil der Gruppe

Beide Informatiker, kein Vorwissen über Spieltheorie, Soziologie, Biologie, ... vorhanden.

## 6. Initiale Modellierung

### Umgebung
- feste Anzahl Äpfel spawnen pro Tag
- einen Apfel zu essen, gibt dem Agent 0.3 Sättigung
- Agenten bekommen täglich Information über alle verfügbaren Ressourcen und können bis zu 1 Ressource anfordern (-> Strategie)
### Agenten
- Sättigung 0 bis 1
- bei Sättigung 0 stirbt Agent über nächste Nacht
- ab Sättigung 0.7 reproduziert sich ein Agent am nächsten Tag
### Initiale Strategie
- ein Agent fordert genau dann einen zufälligen Apfel an, wenn seine Sättigung unter 1 liegt, andernfalls tut er nichts
- fordern mehrere Agenten dieselbe Ressource an, wird diese zunächst zufällig verteilt (in Zukunft: Kooperations-/Aggressionsstrategie)

## Brainstorm weitere Ideen zu Ökosystem mit Ressourcen

Ressourcennutzung / Verhalten von Agents
wie entwickeln sich Metriken mit verschiedenen Faktoren?

#### Ideen / Ansätze / ToDos
- Kopplung der Agenten?
  - zB sozialer Druck gegen Hoarder
  - 

#### Agenttypen
- Bedürfnispyramide: Threshold zum
    - Überleben
    - Zufriedenheit Stetig, aber gedeckelt

- Typen
  - normies: überleben, aber nicht mehr
  - selbstloser gutmensch: hilft anderen, tritt selbst zurück, gewinnt zufriedenheit
  - Horter (verkaufen für Geldmaximierung)
  - Psychopath:
    - nutzt andere aus


#### Ressourcentypen:
Eigenschaften:
- harvestTime
- 

Typen:
- permanent verfügbare Ressource
- Produktionsrate: Quellwasser
- "" Apfelbaum: produktionsquelle kann für gewinn vernichtetwerden
- CO2: global beschränkt (Budget insgesamt / pro Zeitraum? / Kosten bzw. Steuer?)
- Tragedy of the Commons: gratis, aber verteilungskampf

### Fragestellungen
- Welche Zusammensetzung 
