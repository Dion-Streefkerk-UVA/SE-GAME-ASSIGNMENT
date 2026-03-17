import pygame

from game.settings import (
    CELL_SIZE,
    GRID_HEIGHT,
    GRID_WIDTH,
    SNAKE_COLOR,
    SNAKE_HEAD_COLOR,
)


class Snake:
    """Stelt de slang van de speler voor."""

    def __init__(self) -> None:
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2

        self.body = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y),
        ]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.should_grow = False

    def change_direction(self, new_direction: tuple[int, int]) -> None:
        """Verandert de richting, behalve als dat direct achteruit is."""
        if new_direction == (0, 0):
            return

        if new_direction == (-self.direction[0], -self.direction[1]):
            return

        self.next_direction = new_direction

    def move(self) -> None:
        """Beweegt de slang een vakje over het grid."""
        self.direction = self.next_direction

        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

        self.body.insert(0, new_head)

        if self.should_grow:
            self.should_grow = False
        else:
            self.body.pop()

    def grow(self) -> None:
        """Zorgt dat de slang bij de volgende beweging langer wordt."""
        self.should_grow = True

    def get_head_position(self) -> tuple[int, int]:
        """Geeft de positie van het hoofd van de slang terug."""
        return self.body[0]

    def hits_itself(self) -> bool:
        """Controleert of het hoofd een ander deel van het lichaam raakt."""
        return self.body[0] in self.body[1:]

    def draw(self, screen: pygame.Surface) -> None:
        """Tekent elk deel van de slang als een rechthoek."""
        for index, (x, y) in enumerate(self.body):
            rectangle = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR
            pygame.draw.rect(screen, color, rectangle)
            pygame.draw.rect(screen, (10, 10, 10), rectangle, 1)
