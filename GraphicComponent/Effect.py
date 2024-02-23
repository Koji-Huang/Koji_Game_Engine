import pygame


def drawSquareBorder(surface: pygame.Surface, width: int = 1,
                     height: int = 1, color: tuple[int, ...] = (0, 0, 125, 125)):
    # Top
    surface.fill(color, (0, 0, surface.get_width(), height))
    # Left
    surface.fill(color, (0, 0, width, surface.get_height()))
    # Right
    surface.fill(color, (surface.get_width() -  width, 0, width, surface.get_height()))
    # Button
    surface.fill(color, (0, surface.get_height() - height, surface.get_width(), height))
    return
