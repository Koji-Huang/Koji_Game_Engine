from GraphicComponent import Graphic


class Label(Graphic):
    def __init__(self, pos, size, *args, **kwargs):

        super().__init__(pos, size, *args, *kwargs)

        self.graph_primer_surface.fill((0, 0, 0))
        self.graph_primer_surface.set_colorkey((0, 0, 0))

        self.graph_surface = self.graph_primer_surface.copy()

    def set_color(self, color: tuple[int, ...] or list[int, ...]):
        self.graph_primer_surface.fill(color)
