# kan hier wat je wil aan toevoegen of uitbreiden 

import pygame

from game.settings import TEXT_COLOR
from game.ui import draw_centered_text

class TeamFeature:
    """Basisklasse voor uitbreidingen waar teamleden aan kunnen werken."""

    name = "onbekende feature"

    def update(self, game) -> None:
        """Werk speldata bij voor deze feature."""
        pass

    def draw(self, screen, game) -> None:
        """Teken extra onderdelen van deze feature."""
        pass

    def handle_event(self, event, game) -> None:
        """Handel events af voor deze feature."""
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
        self.selected_option = 0  # 0=Start, 1=High Score, 2=Quit
        self.options = ["Start Game", "High Score", "Quit"]

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

        # (nog niets) - event handling gebeurt via handle_event()
        pass

    def handle_event(self, event, game) -> None:
        if self.state != self.STATE_MENU:
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.options)
        elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            if self.selected_option == 0:
                self.set_game_started()
            elif self.selected_option == 1:
                game.running = False
        elif event.key == pygame.K_ESCAPE:
            game.running = False

    def draw(self, screen, game) -> None:
        """Tekent het menu op het scherm."""
        if self.state != self.STATE_MENU:
            return

        center_x = game.screen.get_width() // 2
        center_y = game.screen.get_height() // 2
        draw_centered_text(
            screen,               
            "Snake",
            center_x,
            center_y - 140,
            size=64,
        )

        # Menu opties
        for idx, option in enumerate(self.options):
            text = option
            color = TEXT_COLOR
            if idx == self.selected_option:
                text = f"> {option}"
                color = (255, 220, 50)

            draw_centered_text(
                screen,
                text,
                center_x,
                center_y - 40 + idx * 50,
                color=color,
                size=36,
            )

        draw_centered_text(
            screen,
            "Gebruik ⬆️/⬇️ en Enter",
            center_x,
            center_y + 120,
            color=(180, 180, 180),
            size=24,
        )


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
