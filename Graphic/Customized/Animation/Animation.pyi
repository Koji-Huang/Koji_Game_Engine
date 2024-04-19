from typing import overload
from typing import Iterable
from Graphic.Basel.Graph import Graph
from DataType.Generic.LinkedList import LinkedList
from pygame import Surface

class Animation(Graph):
    # loaded_surface
    animation_surface: LinkedList[Surface | None]
    # the number of frame
    animation_frame_size: float
    # how many frame a tick play
    animation_frame_rate: float
    # last rate
    animation_last_update_frame: float
    # last_update_time
    animation_last_update_time: float

    def __init__(self, pos, size, *args, **kwargs):...

    def graph_draw(self, *args, **kwargs):...

    def draw_frame(self, frame):
        """

        """
        pass

    @overload
    def animation_add_surface(self, surface: Surface):
        pass

    @overload
    def animation_add_surface(self, surfaces: Iterable[Surface]):
        pass

