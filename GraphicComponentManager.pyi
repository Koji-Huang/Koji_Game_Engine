from GraphicComponent import *
from GraphicComponent.Effect.MarkBorder import TextType, EdgeType
from GraphicComponent.UI import Label


class GraphicComponentManager:
    windows: MainWindows
    __debug_mode: bool
    debug: GraphicComponentDebug | None
    def __init__(self, mainWindowsObject: MainWindows = None, size: tuple[int, ...] = (800, 600), ):
        ...

    def general_info(self) -> dict:
        ...

    def component_type(self, start_component: Root = None) -> set[str | ...]:
        ...

    def components_tree(self, start_component: Root = None) -> dict[set, ...]:
        ...

    def find_component(self, ID: str, start_component: Root = None) -> Root | None:
        ...

    def find_components(self, ID: tuple[str, ...], start_component: Root = None) -> tuple[Root | None, ...]:
        ...

    def find_components_type(self, component_type: str, start_component: Root = None) -> tuple[Root, ...]:
        ...

    def add_component(self, component: Root, father_component: Root = None) -> None:
        ...

    def add_components(self, component: tuple[Root, ...], father_component: Root =  None) -> None:
        ...

    def remove_component(self, target: str or Root) -> None:
        ...

    def remove_components(self, target: tuple[str or Root, ...]) -> None:
        ...

    def graphic_update(self) -> None:
        ...

    def event_update(self) -> None:
        ...

    def set_debug(self, enable: bool = None):
        ...

    def update_component_event(self, component: Root, event_type: int, event: Event, *args, **kwargs) -> any:
        ...

    def update_component_graphic(self, component: Root, *args, **kwargs) -> any:
        ...


class GraphicComponentDebug:
    __graphic_update_function: any
    __graphic_insert_function: list
    __debug_component: Graphic
    __debug_Label: Label
    one_layer: bool = True
    textType: TextType
    edgeType: EdgeType
    windows: MainWindows
    info_alpha: int

    def __init__(self, component: Graphic, windows: MainWindows):
        ...

    def graphic_debug(self):
        ...

    def overwrite_add_graphic_function(self, function):
        ...

    def graphic_update(self):
        ...

    def graphic_debug_component(self, component: Graphic):
        ...

    def graphic_debug_single(self, component: Graphic):
        ...

    def overwrite_graphic_core(debug, enable: bool = True):
        ...

    def event_debug(self):
        ...

    def debug(self):
        ...
