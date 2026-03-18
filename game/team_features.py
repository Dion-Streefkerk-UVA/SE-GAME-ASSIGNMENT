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
    """Startmenu voor het spel."""

    name = "startmenu"

    # Menu states
    STATE_MENU = "menu"
    STATE_PLAYING = "playing"
    STATE_PAUSED = "paused"

    def __init__(self) -> None:
        self.state = self.STATE_MENU
        self.selected_option = 0  # 0=Start, 1=Quit
        self.options = ["Start Game", "Quit"]
        self.key_pressed_last_frame = set()

    def is_in_menu(self) -> bool:
        """Controleert of we in het menu scherm zijn."""
        return self.state == self.STATE_MENU

    def set_game_started(self) -> None:
        """Zet de state naar 'spel aan het spelen'."""
        self.state = self.STATE_PLAYING

    def toggle_pause(self) -> None:
        """Schakelt tussen pauzeren en spelen."""
        if self.state == self.STATE_PLAYING:
            self.state = self.STATE_PAUSED
        elif self.state == self.STATE_PAUSED:
            self.state = self.STATE_PLAYING

    def update(self, game) -> None:
        """Update menu input en state."""
        if self.state != self.STATE_MENU:
            return

        # Voeg hier input handling toe
        pass

    def draw(self, screen, game) -> None:
        """Tekent het menu op het scherm."""
        if self.state != self.STATE_MENU:
            return

        # Voeg hier menu tekenen toe
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
