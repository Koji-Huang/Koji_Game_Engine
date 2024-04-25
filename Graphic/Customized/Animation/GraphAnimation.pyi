from typing import Iterable
from pygame import Surface
from Graphic.Customized.Animation.Basel import Animation as Basel
from Graphic.Basel.Graph import Graph
from DataType.Generic.LinkedList import LinkedList


class Animation(Basel):

    def __init__(self, pos, size, *args, **kwargs):
        pass

    def draw_frame(self, frame):
        pass

    def __copy__(self, copied: any = None):
        pass

    def animation_add_frame(self, surface: Graph | Iterable[Graph]):
        pass

    def set_size(self, size):
        pass