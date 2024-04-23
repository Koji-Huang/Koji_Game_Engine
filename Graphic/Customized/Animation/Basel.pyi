from abc import ABCMeta
from typing import overload
from typing import Iterable
from Graphic.Basel.Graph import Graph
from DataType.Generic.LinkedList import LinkedList
from pygame import Surface

class Animation(Graph, metaclass=ABCMeta):
    # loaded_surface
    animation_frame: LinkedList[int, [any or None]]
    # the number of frame
    animation_frame_size: float
    # how many frames a tick play
    animation_frame_rate: float
    # last rate
    animation_last_update_frame: float
    # last_update_time
    animation_last_update_time: float

    def __init__(self, pos, size, *args, **kwargs):...

    def graph_draw(self, *args, **kwargs):...

    def draw_frame(self, frame):
        pass

    def next_frame(self, cost_time: float):
        pass

    @overload
    def animation_add_frame(self, surface: Surface | Iterable[Surface]):
        pass

    @overload
    def animation_add_surface(self, surfaces: Iterable[Surface]):
        pass

