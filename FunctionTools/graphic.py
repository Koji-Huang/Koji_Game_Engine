import pygame
from GraphicComponent import Graphic
from FunctionTools.coordinate import point_in_rect


def cleaning_surface(surface: pygame.Surface):
    surface.fill((0, 0, 0, 0))
    surface.set_colorkey((0, 0, 0, 0))
