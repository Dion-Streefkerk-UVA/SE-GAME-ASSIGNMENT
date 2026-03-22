import random

import pygame

from game.pickups import Pickup
from game.settings import (
    BACKGROUND_COLOR,
    CELL_SIZE,
    FLASH_GAME_OVER_COLOR,
    FLASH_PICKUP_COLOR,
    GAME_OVER_COLOR,
    GRID_COLOR,
    MAX_FPS,
    MIN_FPS,
    OBSTACLE_COLOR,
    RENDER_FPS,
    START_FPS,
    TEXT_COLOR,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from game.snake import Snake
from game.team_features import HighScoreFeature, ParticleFeature, StartMenuFeature
from game.ui import draw_centered_text, draw_game_over_overlay, draw_text


class Game:
    """Regelt de hoofdloop van het spel."""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Arena")
        self.clock = pygame.time.Clock()
        self.running = True
        self.reset()

    def reset(self) -> None:
        """Zet alle speldata terug naar de beginstand."""
        self.snake = Snake()
        self.score = 0
        self.current_fps = START_FPS
        self.game_over = False
        self.tick_count = 0
        self.move_timer = 0.0
        self.game_over_delay = 0.0
        self.flash_timer = 0
        self.flash_color = FLASH_PICKUP_COLOR
        self.last_pickup_text = "Eet pickups voor punten"
        self.obstacles = []
        self.events = []  
        self.start_menu = StartMenuFeature()
        self.team_features = [
            self.start_menu,
            HighScoreFeature(),
            ParticleFeature(),
        ]
        self.create_obstacles()
        self.spawn_pickup()

    def create_obstacles(self) -> None:
        """Maakt een aantal obstakels op vrije plekken."""
        blocked_positions = set(self.snake.body)

        while len(self.obstacles) < 6:
            position = (
                random.randint(2, 37),
                random.randint(4, 27),
            )

            if position in blocked_positions:
                continue

            self.obstacles.append(position)
            blocked_positions.add(position)

    def spawn_pickup(self) -> None:
        """Maakt een nieuwe pickup op een vrije plek."""
        blocked_positions = self.snake.body + self.obstacles
        self.pickup = Pickup.create_random(blocked_positions)

    def change_speed(self, amount: int) -> None:
        """Verhoogt of verlaagt de snelheid binnen veilige grenzen."""
        new_fps = self.current_fps + amount
        self.current_fps = max(MIN_FPS, min(MAX_FPS, new_fps))

    def start_flash(self, color: tuple[int, int, int]) -> None:
        """Start een korte kleurflits als feedback voor de speler."""
        self.flash_timer = 6
        self.flash_color = color

    def handle_events(self) -> None:
        self.events = pygame.event.get()  
        
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
                continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset()
                continue
            if hasattr(self, "start_menu") and self.start_menu.is_in_menu():
                continue
            if self.game_over:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((1, 0))

    def get_move_delay(self) -> float:
        """Berekent hoeveel seconden tussen twee slang-bewegingen zitten."""
        return 1 / self.current_fps

    def update(self, delta_time: float) -> None:
        
        if hasattr(self, "start_menu") and self.start_menu.is_in_menu():
            for feature in self.team_features:
                feature.update(self)
            return

        if self.game_over_delay > 0:
            self.game_over_delay -= delta_time

            
        if self.game_over:
            for feature in self.team_features:
                feature.update(self)
            return

        self.move_timer += delta_time

        if self.flash_timer > 0:
            self.flash_timer -= 1

        while self.move_timer >= self.get_move_delay():
            self.move_timer -= self.get_move_delay()
            self.snake.move()
            self.tick_count += 1

            if self.snake.get_head_position() == self.pickup.position:
                self.pickup.apply(self.snake, self)
                self.start_flash(FLASH_PICKUP_COLOR)

            if self.snake.hits_itself():
                self.game_over = True
                self.last_pickup_text = "Je raakte jezelf"
                self.start_flash(FLASH_GAME_OVER_COLOR)
                break

            if self.snake.get_head_position() in self.obstacles:
                sound = pygame.mixer.Sound("assets/slang_botst.mp3")
                sound.play()
                self.game_over = True  # ← Game stopt NU
                self.game_over_delay = sound.get_length()  # ← Maar overlay pas later
                self.last_pickup_text = "Je botste tegen een obstakel"
                self.start_flash(FLASH_GAME_OVER_COLOR)
                break
        
        
                
        for feature in self.team_features:
            feature.update(self)

    def draw_grid(self) -> None:
        """Tekent een subtiele achtergrond met rasterlijnen."""
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))

        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

    def draw_obstacles(self) -> None:
        """Tekent obstakels als blokken op het speelveld."""
        border_width = 1 if self.tick_count % 16 < 8 else 2

        for x, y in self.obstacles:
            rectangle = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, OBSTACLE_COLOR, rectangle)
            pygame.draw.rect(self.screen, (30, 30, 30), rectangle, border_width)

    def draw_flash(self) -> None:
        """Tekent een korte transparante flash over het scherm."""
        if self.flash_timer <= 0:
            return

        alpha = 20 + self.flash_timer * 10
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((*self.flash_color, alpha))
        self.screen.blit(overlay, (0, 0))

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grid()

        if hasattr(self, "start_menu") and self.start_menu.is_in_menu():
            for feature in self.team_features:
                feature.draw(self.screen, self)
            pygame.display.flip()
            return

        self.draw_obstacles()
        self.pickup.draw(self.screen, self.tick_count)
        self.snake.draw(self.screen)
        draw_text(self.screen, f"Score: {self.score}", 10, 10, TEXT_COLOR, 30)
        draw_text(self.screen, f"Snelheid: {self.current_fps}", 10, 42, TEXT_COLOR, 26)
        draw_text(self.screen, self.last_pickup_text, 10, 72, TEXT_COLOR, 24)
        draw_text(self.screen, f"Obstakels: {len(self.obstacles)}", 10, 100, TEXT_COLOR, 24)
        for feature in self.team_features:
            feature.draw(self.screen, self)
        self.draw_flash()

        if self.game_over and self.game_over_delay <= 0:
            draw_game_over_overlay(self.screen, WINDOW_WIDTH, WINDOW_HEIGHT)
            draw_centered_text(
                self.screen,
                "Game Over",
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2 - 35,
                GAME_OVER_COLOR,
                56,
            )
            draw_centered_text(
                self.screen,
                "Druk op R om opnieuw te starten",
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2 + 15,
                TEXT_COLOR,
                30,
            )
            draw_centered_text(
                self.screen,
                "ESC of venster sluiten = stoppen",
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2 + 55,
                TEXT_COLOR,
                24,
            )

        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            delta_time = self.clock.tick(RENDER_FPS) / 1000
            self.handle_events()
            self.update(delta_time)
            self.draw()

        pygame.quit()
