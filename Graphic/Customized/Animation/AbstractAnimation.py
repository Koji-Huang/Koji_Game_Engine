from Graphic.Basic.Graph import Graph
from time import time
from DataType.Generic.LinkedList import LinkedList
from abc import ABCMeta, abstractmethod


class Animation(Graph, metaclass=ABCMeta):
    def __init__(self, pos, size, *args, **kwargs):
        self.primer_frame = LinkedList()
        self.animation_frame = LinkedList()
        self.animation_frame_size = 0
        self.animation_frame_rate = 30
        self.animation_last_update_frame = 0
        self.animation_last_update_time = time()
        super().__init__(pos, size, *args, **kwargs)

    def graph_draw(self, *args,
                   **kwargs):
        if self.animation_frame_size != 0:
            cost_time = time() - self.animation_last_update_time
            now_frame = self.next_frame(cost_time)
            self.draw_frame(now_frame)
            self.animation_last_update_frame = now_frame
            self.animation_last_update_time += cost_time
        else:
            super().graph_draw(*args, **kwargs)

    @abstractmethod
    def draw_frame(self, frame):
        pass

    def next_frame(self, cost_time):
        cost_frame = cost_time * self.animation_frame_rate
        return int((self.animation_last_update_frame + cost_frame) % self.animation_frame_size)

    def animation_add_frame(self, surface):
        self.animation_frame.append(surface)

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Animation(self.pos(), self.size())
        copied.animation_frame = self.animation_frame.__copy__()
        copied.animation_frame_size = self.animation_frame_size
        copied.animation_frame_rate = self.animation_frame_rate
        copied.animation_last_update_frame = self.animation_last_update_frame
        copied.animation_last_update_time = self.animation_last_update_time
        super().__copy__(copied)
        return copied
