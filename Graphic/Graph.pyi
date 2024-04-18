from Graphic.Surface import Surface as _Surface
from pygame import Surface

class Graph(_Surface):
    graph_active: bool
    graph_surface: Surface
    graph_primer_surface: Surface
    graph_kwargs: dict

    def __init__(self, pos, size, surface: Surface = None, *args, **kwargs):
        """
        :param surface: the surface as primer_surface
        """

    def graph_check(self):...

    def graph_update(self, *args, **kwargs):...

    def graph_draw(self, *args, **kwargs):...

    def scale(self, w: int, h: int, anti_aliasing: bool = False):...