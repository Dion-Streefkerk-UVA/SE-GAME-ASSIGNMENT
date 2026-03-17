# kan hier wat je wil aan toevoegen of uitbreiden 

class TeamFeature:
    """Basisklasse voor uitbreidingen waar teamleden aan kunnen werken."""

    name = "onbekende feature"

    def update(self, game) -> None:
        """Werk speldata bij voor deze feature."""
        pass

    def draw(self, screen, game) -> None:
        """Teken extra onderdelen van deze feature."""
        pass


class StartMenuFeature(TeamFeature):
    """Placeholder voor een startmenu."""

    name = "startmenu"

    def update(self, game) -> None:
        # TODO: laat een teamlid hier een startscherm bouwen.
        pass

    def draw(self, screen, game) -> None:
        # TODO: teken hier later knoppen of instructies.
        pass


class HighScoreFeature(TeamFeature):
    """Placeholder voor highscores."""

    name = "highscore"

    def __init__(self) -> None:
        self.high_score = 0

    def update(self, game) -> None:
        # TODO: sla highscore op in bestand of geheugen.
        if game.score > self.high_score:
            self.high_score = game.score

    def draw(self, screen, game) -> None:
        # TODO: toon de highscore zichtbaar in de UI.
        pass


class ParticleFeature(TeamFeature):
    """Placeholder voor extra special effects."""

    name = "particles"

    def __init__(self) -> None:
        self.particles = []

    def update(self, game) -> None:
        # TODO: laat een teamlid hier particles animeren.
        pass

    def draw(self, screen, game) -> None:
        # TODO: teken hier bijvoorbeeld explosies of trails.
        pass
