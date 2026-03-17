import pygame

from game.settings import GAME_OVER_COLOR, TEXT_COLOR


def draw_text(
    screen: pygame.Surface,
    text: str,
    x: int,
    y: int,
    color: tuple[int, int, int] = TEXT_COLOR,
    size: int = 28,
) -> None:
    """Tekent tekst linksboven vanaf een vaste positie."""
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def draw_centered_text(
    screen: pygame.Surface,
    text: str,
    center_x: int,
    center_y: int,
    color: tuple[int, int, int] = TEXT_COLOR,
    size: int = 36,
) -> None:
    """Tekent tekst gecentreerd op het scherm."""
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rectangle = surface.get_rect(center=(center_x, center_y))
    screen.blit(surface, rectangle)


def draw_game_over_overlay(screen: pygame.Surface, width: int, height: int) -> None:
    """Tekent een donkere laag over het scherm bij game over."""
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 170))
    screen.blit(overlay, (0, 0))
    pygame.draw.rect(screen, GAME_OVER_COLOR, (140, 180, 520, 180), 3)
