from typing import Callable
from Event.UIEvent.UIEvent import Basic as Event
from . import *
from .EffectFunction.MarkBorder import TextType, EdgeType
from .UI import Label
from .Basic import *


class GraphicDebug:
    __graphic_update_function: Callable
    __graphic_insert_function: list[Callable]
    __debug_component: Graph
    __debug_Label: Label
    one_layer: bool = True
    textType: TextType
    edgeType: EdgeType
    windows: MainWindows
    info_alpha: int

    def __init__(self, component: Graph, windows: MainWindows):
        ...

    def graphic_debug(self):
        ...

    def add_graphic_function(self, function):
        ...

    def graphic_update(self):
        ...

    def graphic_debug_component(self, component: Surface):
        ...

    def graphic_debug_single(self, component: Surface):
        ...

    def overwrite_graphic_core(debug, enable: bool = True):
        ...

    def event_debug(self):
        ...

    def debug(self):
        ...
