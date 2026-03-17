# SE-GAME-ASSIGNMENT

Een groepsproject voor Software Engineering waarin we met Python en Pygame een eigen computerspel maken.

## Projectidee
We maken een Snake-achtige game waarin de speler over een grid beweegt en verschillende pickups kan verzamelen. Het project is bewust simpel en modulair opgezet, zodat eerstejaars studenten de code goed kunnen begrijpen en uitbreiden.

## Team
- Dion
- Member 2
- Member 3

## Opdrachtkoppeling
Deze game is gemaakt voor de week 6 / week 7 opdracht:
- werk in een groep van 3 of 4
- gebruik Git vanaf het begin
- lever de GitHub repository van de groep in
- maak een leuk en creatief spel
- gebruik polymorfisme
- zorg voor leesbare code, docstrings en een duidelijke README

## Benodigdheden
- Python 3.11 of nieuwer
- Pygame (staat in `requirements.txt`)

## Projectstructuur
```text
SE-GAME-ASSIGNMENT/
+-- README.md
+-- requirements.txt
+-- .gitignore
+-- main.py
+-- game/
|   +-- __init__.py
|   +-- settings.py
|   +-- game.py
|   +-- snake.py
|   +-- pickups.py
|   +-- ui.py
+-- assets/
```

## Installeren en starten
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Besturing
- Pijltjestoetsen: beweeg de slang
- `R`: start het spel opnieuw na game over
- `ESC`: stop het spel
- Venster sluiten: spel afsluiten

## Wat werkt nu?
- De game start op in een Pygame-venster
- De slang bestaat uit 3 delen
- De slang beweegt zichtbaar over het grid
- De speler kan sturen met de pijltjestoetsen
- Direct omkeren naar de tegenovergestelde richting is geblokkeerd
- De slang groeit wanneer hij een pickup raakt
- De score wordt bijgehouden
- De snelheid kan veranderen door pickups
- Er staan obstakels op het speelveld
- Als de slang zichzelf raakt, is het game over
- Als de slang een obstakel raakt, is het game over
- Het spel kan opnieuw gestart worden met `R`

## Polymorfisme in dit project
We gebruiken een basisklasse `Pickup` en meerdere subclasses:
- `FoodPickup`: gewone pickup, laat de slang groeien
- `BonusPickup`: geeft extra punten
- `SpeedPickup`: maakt het spel sneller
- `SlowPickup`: maakt het spel langzamer
- `HealPickup`: geeft een grotere groeiboost

Elke pickup heeft dezelfde interface via de methode `apply()`, maar elke subclass voert een ander effect uit. Dit is precies het polymorfisme dat in de opdracht wordt gevraagd.

## Verdeling van verantwoordelijkheden
- `main.py`: start het spel
- `game/game.py`: hoofdloop, events, score, game over en restart
- `game/snake.py`: beweging, richting en lichaam van de slang
- `game/pickups.py`: pickup-klassen en pickup-logica
- `game/ui.py`: tekst en overlays tekenen
- `game/team_features.py`: lege uitbreidpunten voor teamgenoten
- `game/settings.py`: alle vaste instellingen en kleuren

## Mogelijke volgende uitbreidingen
- startmenu
- highscore
- meer speciale effecten
- multiplayer of client-server bonus

## Handige uitbreidpunten voor het team
Er staat nu bewust een extra bestand klaar: `game/team_features.py`.
Daarin staan simpele placeholder-klassen waar teamgenoten verder aan kunnen werken:
- `StartMenuFeature`
- `HighScoreFeature`
- `ParticleFeature`

Zo kan iedereen aan een eigen feature werken zonder meteen de basis van de game-loop te veranderen.

## Testen
Start het spel met:

```bash
python main.py
```

Als alles goed staat, zie je een venster waarin de slang automatisch beweegt. Raak pickups aan om punten te verdienen en langer te worden. Probeer jezelf niet te raken.
Let ook op de obstakels op het speelveld.

## Git-werkwijze voor ons team
Voor deze opdracht is het slim om vaak kleine commits te maken in het Nederlands, bijvoorbeeld:
- `basis van snake movement toegevoegd`
- `food pickup en score toegevoegd`
- `game over en restart gemaakt`
- `meerdere pickup classes met polymorfisme toegevoegd`
- `readme verbeterd voor opdracht`

Iedereen moet regelmatig pullen, kleine stabiele stukken committen, en duidelijke commit-berichten gebruiken zodat de werkverdeling in Git goed zichtbaar blijft.
