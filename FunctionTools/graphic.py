import pygame


def cleaning_surface(surface: pygame.Surface):
    surface.fill((0, 0, 0, 0))
    surface.set_colorkey((0, 0, 0, 0))
