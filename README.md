# SE-GAME-ASSIGNMENT

Een groepsproject voor Software Engineering waarin we met Python en Pygame een eigen computerspel maken.

## Projectidee
We maken een Snake-achtige game waarin de speler over een grid beweegt en verschillende pickups kan verzamelen. Het project is bewust simpel en modulair opgezet, zodat eerstejaars studenten de code goed kunnen begrijpen en uitbreiden.

## Team
- Bob Engel
- Dion Streefkerk
- Dirrik Maitland
- Samnang van Steen

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
|   +-- team_features.py
+-- assets/
```

## Repo Architecture Guide
Deze repository is bewust simpel opgezet zodat iedereen in het team snel kan zien waar code hoort.

### Root van de repository
- `README.md`
  De hoofdhandleiding van het project. Hierin staan de speluitleg, installatie, besturing en afspraken voor het team.
- `requirements.txt`
  Bevat de Python-packages die nodig zijn om het project te draaien.
- `.gitignore`
  Zorgt dat tijdelijke bestanden zoals `.venv` en `__pycache__` niet in Git terechtkomen.
- `main.py`
  Het startpunt van het spel. Dit bestand maakt een `Game` object en start de game-loop.

### De map `game/`
In deze map staat alle logica van het spel. Elk bestand heeft een duidelijke verantwoordelijkheid.

- `game/__init__.py`
  Maakt van `game/` een Python package.
- `game/settings.py`
  Bevat alle vaste instellingen, zoals schermgrootte, kleuren, grid-grootte en snelheid.
- `game/game.py`
  De centrale controller van het spel.
  Dit bestand regelt:
  - de hoofdloop
  - keyboard input
  - reset en game over
  - score en snelheid
  - obstakels
  - het aanroepen van andere onderdelen
- `game/snake.py`
  Bevat de `Snake` class.
  Dit bestand regelt:
  - de positie van de slang
  - richting veranderen
  - bewegen over het grid
  - groeien
  - botsing met zichzelf
  - het tekenen van de slang
- `game/pickups.py`
  Bevat de pickup-hiërarchie.
  Dit bestand laat polymorfisme zien via:
  - `Pickup` als basisklasse
  - `FoodPickup`
  - `BonusPickup`
  - `SpeedPickup`
  - `SlowPickup`
  - `HealPickup`
- `game/ui.py`
  Bevat losse functies voor het tekenen van tekst en overlays.
  Daardoor blijft `game.py` overzichtelijker.
- `game/team_features.py`
  Bevat lege uitbreidpunten voor teamleden.
  Hier kunnen teamgenoten nieuwe features bouwen zonder direct de hele basisstructuur te hoeven aanpassen.

### De map `assets/`
- `assets/`
  Bedoeld voor afbeeldingen, geluiden, achtergronden of andere bestanden die later aan het spel worden toegevoegd.

### Hoe de onderdelen samenwerken
1. `main.py` start de game.
2. `game/game.py` maakt alle belangrijke objecten aan.
3. `game/snake.py` regelt de slang.
4. `game/pickups.py` regelt pickups en hun effecten.
5. `game/ui.py` helpt bij het tekenen van tekst en schermlagen.
6. `game/team_features.py` geeft ruimte voor toekomstige uitbreidingen door teamleden.

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

## Exact Branch-Werkproces Voor Ons Team
We gebruiken drie niveaus van branches:
- `main`
  Alleen voor stabiele versies van het project.
  Deze branch is protected en hier wordt niet direct op gecommit of naartoe gepusht.
  Wij werken alleen via een Pull Request van `dev` naar `main`.
- `dev`
  De gezamenlijke ontwikkelbranch.
  Hier komen goed werkende features eerst samen.
- `feature/...`
  Een eigen branch per taak of per teamlid.
  Voorbeelden:
  - `feature/startmenu`
  - `feature/highscore`
  - `feature/particles`
  - `feature/extra-pickups`

### Regel 1
Niemand commit direct op `main`.

### Regel 1b
Niemand pusht direct naar `main`.
`main` mag alleen aangepast worden via een Pull Request, en alleen na toestemming van Dion.

### Regel 2
Niemand werkt direct op `dev` voor grote veranderingen.
Iedereen maakt eerst een eigen feature branch vanaf `dev`.

### Stap voor stap per teamlid
1. Haal eerst de nieuwste versie op:
```bash
git checkout dev
git pull origin dev
```

2. Maak daarna je eigen feature branch:
```bash
git checkout -b feature/jouw-feature
```

3. Werk aan je code in kleine stappen en commit vaak:
```bash
git add .
git commit -m "highscore basis toegevoegd"
```

4. Push je branch naar GitHub:
```bash
git push -u origin feature/jouw-feature
```

5. Maak op GitHub een Pull Request:
- van `feature/jouw-feature`
- naar `dev`

6. Pas na controle of als de code goed werkt, wordt die branch gemerged in `dev`.

### Wat gebeurt er met `dev`?
- `dev` bevat alle nieuwste werkende features
- als iets nog kapot of half af is, hoort het nog niet naar `dev`
- alleen stabiele feature branches worden gemerged naar `dev`

### Hoe mergen naar `dev` werkt in GitHub
- je pusht eerst je eigen `feature/...` branch naar GitHub
- daarna maak je een Pull Request van `feature/...` naar `dev`
- er wordt niet direct naar `dev` gepusht
- `dev` is bedoeld als merge-only branch via GitHub Pull Requests
- een feature wordt pas naar `dev` gemerged na toestemming van de afgesproken reviewers
- werk dus altijd via:
  `feature/... -> Pull Request -> dev`

### Wanneer mergen we `dev` naar `main`?
Dat doen we alleen wanneer `dev` op dat moment stabiel is.
Bijvoorbeeld:
- na een werkende demo
- na een groepstest
- voor een inlevermoment

Dan gaat het proces zo:
1. Controleer of `dev` goed werkt
2. Maak een Pull Request van `dev` naar `main`
3. Dion controleert en merge pas daarna naar `main`

### Hoe mergen naar `main` werkt in GitHub
- er wordt niet direct naar `main` gepusht
- `main` is een protected branch
- alleen via een Pull Request van `dev` naar `main` mag `main` aangepast worden
- Dion beslist wanneer die Pull Request wordt gemerged
- werk dus altijd via:
  `dev -> Pull Request -> main`


### Handige branch-namen
- `feature/startmenu`
- `feature/highscore`
- `feature/particles`
- `feature/sounds`
- `feature/obstacles`
- `feature/multiplayer`

### Belangrijke afspraken
- pull altijd eerst de nieuwste `dev`
- commit kleine werkende stukjes
- gebruik duidelijke commit messages in het Nederlands
- maak een Pull Request naar `dev`
- merge nooit zomaar direct naar `main`
- als je vastloopt: vraag eerst in de groep voordat je grote bestanden herschrijft
