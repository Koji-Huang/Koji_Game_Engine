from Graphic import Graphic


class Label(Graphic):
    def __init__(self, pos, size, *args, **kwargs):

        super().__init__(pos, size, *args, *kwargs)

        self.graph_primer_surface.fill((0, 0, 0))
        self.graph_primer_surface.set_colorkey((0, 0, 0))
        self.graph_surface = self.graph_primer_surface.copy()

    def set_color(self, color: tuple[int, ...] or list[int, ...]):
        self.graph_primer_surface.fill(color)

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Label(self.pos(), self.size())
        else:
            copied.graph_primer_surface = self.graph_primer_surface.copy()
            copied.graph_surface = self.graph_primer_surface.copy()
        super().__copy__(copied)
        return copied

