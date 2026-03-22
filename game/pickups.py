import random

import pygame

from game.settings import (
    BONUS_COLOR,
    CELL_SIZE,
    FOOD_COLOR,
    GRID_HEIGHT,
    GRID_WIDTH,
    SNAKE_COLOR,
    SLOW_COLOR,
    SPEED_BOOST_AMOUNT,
    SPEED_BOOST_COLOR,
    SPEED_COLOR,
)

class Pickup:
    """Basisklasse voor alle pickups in het spel."""

    color = FOOD_COLOR
    score_value = 0
    fps_change = 0

    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position

    def apply(self, snake, game) -> None:
        """Past het effect van de pickup toe."""
        raise NotImplementedError

    def draw(self, screen: pygame.Surface, tick_count: int) -> None:
        """Tekent de pickup op het scherm."""
        x, y = self.position
        rectangle = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        inset = 2 if tick_count % 10 < 5 else 4
        inner_rectangle = rectangle.inflate(-inset, -inset)
        pygame.draw.rect(screen, self.color, inner_rectangle)
        pygame.draw.rect(screen, (245, 245, 245), inner_rectangle, 1)

    @classmethod
    def create_random(cls, blocked_positions: list[tuple[int, int]]) -> "Pickup":
        """Maakt een willekeurige pickup-subklasse aan op een vrije plek."""
        pickup_classes = [
            FoodPickup,
            FoodPickup,
            BonusPickup,
            SpeedPickup,
            SlowPickup,
            HealPickup,
            SpeedBoostPickup,
            ShrinkPickup,
        ]
        pickup_class = random.choice(pickup_classes)
        position = _get_random_free_position(blocked_positions)
        return pickup_class(position)


class FoodPickup(Pickup):
    """Een simpele pickup die de slang laat groeien."""

    color = FOOD_COLOR
    score_value = 1

    def apply(self, snake, game) -> None:
        snake.grow()
        game.score += self.score_value
        game.spawn_pickup()
        game.last_pickup_text = "+1 lengte"
        
        sound = pygame.mixer.Sound("assets/Sound_crunch.wav")
        sound.play()


class BonusPickup(Pickup):
    """Geeft extra punten."""

    color = BONUS_COLOR
    score_value = 3

    def apply(self, snake, game) -> None:
        snake.grow()
        game.score += self.score_value
        game.spawn_pickup()
        game.last_pickup_text = "+3 bonuspunten"


class SpeedPickup(Pickup):
    """Maakt het spel iets sneller."""

    color = SPEED_COLOR
    score_value = 2
    fps_change = 2

    def apply(self, snake, game) -> None:
        snake.grow()
        game.score += self.score_value
        game.change_speed(self.fps_change)
        game.spawn_pickup()
        game.last_pickup_text = "Sneller!"


class SlowPickup(Pickup):
    """Maakt het spel iets langzamer."""

    color = SLOW_COLOR
    score_value = 2
    fps_change = -2

    def apply(self, snake, game) -> None:
        snake.grow()
        game.score += self.score_value
        game.change_speed(self.fps_change)
        game.spawn_pickup()
        game.last_pickup_text = "Langzamer!"


class HealPickup(Pickup):
    """Geeft extra groei en punten als veilige bonuspickup."""

    color = SNAKE_COLOR
    score_value = 4

    def apply(self, snake, game) -> None:
        snake.grow()
        snake.grow()
        game.score += self.score_value
        game.spawn_pickup()
        game.last_pickup_text = "+4 groeiboost"

class SpeedBoostPickup(Pickup):
    """Maakt de slang tijdelijk sneller voor een paar seconden."""

    color = SPEED_BOOST_COLOR
    score_value = 2

    def apply(self, snake, game) -> None:
        """Activeert een tijdelijke snelheidsboost."""
        snake.grow()
        game.score += self.score_value
        game.activate_speed_boost(SPEED_BOOST_AMOUNT)
        game.spawn_pickup()
        game.last_pickup_text = "Tijdelijke speed boost!"

class ShrinkPickup(Pickup):
    """Maakt de slang korter, maar niet kleiner dan lengte 3."""

    color = (180, 80, 220)
    score_value = 2

    def apply(self, snake, game) -> None:
        snake.shrink(2)
        game.score += self.score_value
        game.spawn_pickup()
        game.last_pickup_text = "Krimpen!"


def _get_random_free_position(
    blocked_positions: list[tuple[int, int]],
) -> tuple[int, int]:
    """Zoekt een vrije plek op het grid die niet bezet is."""
    free_positions = []

    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if (x, y) not in blocked_positions:
                free_positions.append((x, y))

    return random.choice(free_positions)
