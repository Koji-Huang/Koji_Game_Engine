from Graphic.Graph import Graph
from typing import Iterable
from time import time
from DataType.Generic.LinkedList import LinkedList
from pygame import Surface


class Animation(Graph):
    def __init__(self, pos, size, *args, **kwargs):
        self.animation_surface = LinkedList()
        self.animation_frame_size = 0
        self.animation_frame_rate = 0
        self.animation_last_update_frame = 0
        self.animation_last_update_time = time()
        super().__init__(pos, size, *args, **kwargs)

    def graph_draw(self, *args,
                   **kwargs):
        if self.animation_frame_size != 0:
            cost_time = time() - self.animation_last_update_time
            cost_frame = cost_time * self.animation_frame_rate
            now_frame = (self.animation_last_update_frame + cost_frame) / self.animation_frame_size
            self.draw_frame(now_frame)
        else:
            super().graph_draw(*args, **kwargs)

    def draw_frame(self, frame):
        self.graph_primer_surface.blit(self.animation_surface[frame], (0, 0))

    def animation_add_surface(self, surface):
        if isinstance(surface, Iterable) or isinstance(surface, Surface):
            self.animation_surface.append(surface)

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
