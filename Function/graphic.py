import pygame
from Graphic import Graphic
from Function.coordinate import point_in_rect


def cleaning_surface(surface: pygame.Surface):
    surface.fill((0, 0, 0, 0))
    surface.set_colorkey((0, 0, 0, 0))
