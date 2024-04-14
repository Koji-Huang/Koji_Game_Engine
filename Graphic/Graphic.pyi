from Graphic.Surface import Surface
import pygame

class Graphic(Surface):
    graph_active: bool
    graph_surface: pygame.Surface
    graph_primer_surface: pygame.Surface
    graph_kwargs: dict

    def __init__(self, pos, size, *args, **kwargs):...

    def graph_check(self):...

    def graph_update(self, *args, **kwargs):...

    def graph_draw(self, *args, **kwargs):...

    def scale(self, w: int, h: int, anti_aliasing: bool = False):...