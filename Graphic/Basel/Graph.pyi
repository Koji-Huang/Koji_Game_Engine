from Graphic.Basel.Surface import Surface
from pygame import Surface as PygameSurface

class Graph(Surface):
    graph_active: bool
    graph_surface: PygameSurface
    graph_primer_surface: PygameSurface
    graph_kwargs: dict

    def __init__(self, pos, size, surface: PygameSurface = None, *args, **kwargs):
        """
        :param surface: the surface as primer_surface
        """

    def graph_check(self):...

    def graph_update(self, *args, **kwargs):...

    def graph_draw(self, *args, **kwargs):...

    def scale(self, w: int, h: int, anti_aliasing: bool = False):...

