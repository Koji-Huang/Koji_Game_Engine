from GraphicComponent.Surface import Surface
import pygame

class Graphic(Surface):
    graph_active: bool
    graph_surface: pygame.Surface
    graph_primer_surface: pygame.Surface
    graph_kwargs: dict

    def __init__(self, pos, size, *args, **kwargs):...

    def graph_update_check(self):...

    def graph_update(self, *args, **kwargs):...

    def __graph_update(self, *args, **kwargs):...
