from typing import Callable
from Event.UIEvent.Basic import Basic as Event
from Graphic import *
from Graphic.Effect.MarkBorder import TextType, EdgeType
from Graphic.UI import Label


class GraphicAPI:
    windows: MainWindows
    __debug_mode: bool
    debug: GraphicDebug | None
    def __init__(self, mainWindowsObject: MainWindows = None, size: tuple[int, ...] = (800, 600), ):
        ...

    def general_info(self) -> dict:
        ...

    def component_type(self, start_component: Root = None) -> set[str | ...]:
        ...

    def component_tree(self, start_component: Root = None) -> dict[set, ...]:
        ...

    def component_find(self, id: str, start_component: Root = None) -> Root | None:
        ...

    def components_find(self, id: tuple[str, ...], start_component: Root = None) -> tuple[Root | None, ...]:
        ...

    def components_find_type(self, component_type: str, start_component: Root = None) -> tuple[Root, ...]:
        ...

    def component_add(self, component: Root, father_component: Root = None) -> None:
        ...

    def components_add(self, component: tuple[Root, ...], father_component: Root =  None) -> None:
        ...

    def component_remove(self, target: str or Root) -> None:
        ...

    def components_remove(self, target: tuple[str or Root, ...]) -> None:
        ...

    def graphic_update(self) -> None:
        ...

    def event_get(self, pid: str, event_type: str, component: Root = None) -> Event | Root | str:
        ...

    def event_remove(self, pid: str) -> None:
        ...

    def event_add(self, event: Event, event_type: int = 0, father_component: Root = None) -> None:
        ...

    def event_tree(self, start_component: str | Root):
        ...

    def event_id_tree(self, start_component: str | Root):
        ...

    def event_type_tree(self, start_component: str | Root):
        ...

    def event_update(self):
        ...

    def set_debug(self, enable: bool = None):
        ...

    def update_component_event(self, component: Root, event_type: int, event: Event, *args, **kwargs) -> any:
        ...

    def update_component_graphic(self, component: Root, *args, **kwargs) -> any:
        ...


class GraphicDebug:
    __graphic_update_function: Callable
    __graphic_insert_function: list[Callable]
    __debug_component: GraphicAPI
    __debug_Label: Label
    one_layer: bool = True
    textType: TextType
    edgeType: EdgeType
    windows: MainWindows
    info_alpha: int

    def __init__(self, component: GraphicAPI, windows: MainWindows):
        ...

    def graphic_debug(self):
        ...

    def overwrite_add_graphic_function(self, function):
        ...

    def graphic_update(self):
        ...

    def graphic_debug_component(self, component: GraphicAPI):
        ...

    def graphic_debug_single(self, component: GraphicAPI):
        ...

    def overwrite_graphic_core(debug, enable: bool = True):
        ...


    def event_debug(self):
        ...

    def debug(self):
        ...
