from GraphicComponent.Surface import Surface
import Functions as F
import pygame


class Graphic(Surface):
    graph_is_updated = False
    graph_surface = None
    graph_primer_surface = None
    graph_kwargs = dict()

    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)
        self.graph_surface = pygame.Surface(size).convert_alpha()
        self.graph_primer_surface = pygame.Surface(size).convert_alpha()
        self.graph_kwargs = dict()
        self.graph_active = True
        self.graph_update()

    def graph_update_check(self):
        result = bool(True in [son.graph_update_check() for son in self.son if isinstance(son, Graphic)])
        self.graph_active = result if not self.graph_active else True
        return self.graph_active

    def graph_update(self, *args, **kwargs):

        if kwargs:
            self.graph_kwargs = F.Mix_Kwargs(self.graph_kwargs, kwargs)
            self.graph_active = True

        graph_son = [son for son in self.son if isinstance(son, Graphic)]

        for i in graph_son:
            i.graph_update()

        active_son = [son for son in graph_son if son.graph_active]

        self.graph_active = bool(active_son) if not self.graph_active else True

        if self.graph_active:
            self.__graph_update()

            # F.Surface.cleaning_surface(self.graph_surface)
            # self.graph_surface.blit(self.graph_primer_surface, (0, 0))

            self.graph_surface = self.graph_primer_surface.copy()

            for son in graph_son:
                self.graph_surface.blit(son.graph_surface, son.pos())
                son.graph_active = False

    def __graph_update(self, *args,
                       **kwargs):
        ...
