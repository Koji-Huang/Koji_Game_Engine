from Graphic.Basel.Surface import Surface
import pygame


class Graph(Surface):
    def __init__(self, pos, size, surface=None, *args, **kwargs):
        self.graph_surface = pygame.Surface(size).convert_alpha()
        self.graph_primer_surface = pygame.Surface(size).convert_alpha()
        if surface:
            self.graph_primer_surface.blit(surface, (0, 0))
        self.graph_kwargs = dict()
        self.graph_active = True
        super().__init__(pos, size, *args, **kwargs)
        self.graph_update()

    def graph_check(self):
        result = bool(True in [son.graph_check() for son in self.son if isinstance(son, Graph)])
        self.graph_active = result if not self.graph_active else True
        return self.graph_active

    def graph_update(self, *args, **kwargs):

        if kwargs:
            self.graph_kwargs.update(kwargs)
            self.graph_active = True

        # graph_son = [son for son in self.son if isinstance(son, Graph)]
        active_son = list()

        for i in self.son:
            if isinstance(i, Graph):
                i.graph_update()
                if i.graph_active:
                    active_son.append(i)

        self.graph_active = True in active_son if not self.graph_active else True

        if self.graph_active:
            self.graph_draw()

            # F.Surface.cleaning_surface(self.graph_surface)
            # self.graph_surface.blit(self.graph_primer_surface, (0, 0))

            self.graph_surface = self.graph_primer_surface.copy()

            for son in self.son:
                if isinstance(son, Graph):
                    self.graph_surface.blit(son.graph_surface, son.pos())
                    son.graph_active = False

    def graph_draw(self, *args,
                   **kwargs):
        ...

    def set_size(self, size):
        super().set_size(size)
        if isinstance(self, Graph):
            if self.graph_primer_surface:
                self.graph_primer_surface = pygame.transform.scale(self.graph_primer_surface, size)
            if self.graph_surface:
                self.graph_surface = pygame.transform.scale(self.graph_surface, size)
            self.graph_active = True

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Graph(self.pos(), self.size())
        else:
            copied: Graph
            copied.graph_active = self.graph_active
            copied.graph_surface = self.graph_surface.copy()
            copied.graph_primer_surface = self.graph_primer_surface.copy()
            copied.graph_kwargs = self.graph_kwargs.copy()
        super().__copy__(copied)
        return copied

    def scale(self, w: int, h: int, anti_aliasing: bool = False):
        self.graph_active = True
        self.w = w
        self.h = h
        if anti_aliasing:
            self.graph_primer_surface = pygame.transform.smoothscale(self.graph_primer_surface, (w, h))
            self.graph_surface = pygame.transform.smoothscale(self.graph_surface, (w, h))
        else:
            self.graph_primer_surface = pygame.transform.scale(self.graph_primer_surface, (w, h))
            self.graph_surface = pygame.transform.scale(self.graph_surface, (w, h))
        return None

