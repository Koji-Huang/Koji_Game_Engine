from typing import overload
from Event.UIEvent.UIEvent import Basic as Event
from . import *
from .Basic import *
from .Debug import GraphicDebug


windows: MainWindows
__debug_mode: bool
debug: GraphicDebug | None


@overload
def init(mainWindowsObject: MainWindows = None): ...
@overload
def init(size: tuple[int], flags = None, *args, **kwargs): ...
def init(mainWindowsObject: MainWindows = None, flags = None, *args, **kwargs): ...


def create_windows(size, flags, *args, **kwargs):
    ...


def general_info() -> dict:
    ...


def component_type(start_component: Root = None) -> set[str | ...]:
    ...


def component_tree(start_component: Root = None) -> dict[set, ...]:
    ...


def component_find(id: str, start_component: Root = None) -> Root | None:
    ...


def components_find(id: tuple[str, ...], start_component: Root = None) -> tuple[Root | None, ...]:
    ...


def components_find_type(component_type: str, start_component: Root = None) -> tuple[Root, ...]:
    ...


def component_add(component: Root, father_component: Root = None) -> None:
    ...


def components_add(component: tuple[Root, ...], father_component: Root =  None) -> None:
    ...


def component_remove(target: str or Root) -> None:
    ...


def components_remove(target: tuple[str or Root, ...]) -> None:
    ...


def graphic_update() -> None:
    ...


def event_get(pid: str, event_type: str, component: Root = None) -> Event | Root | str:
    ...


def event_remove(pid: str) -> None:
    ...


def event_add(event: Event, event_type: int = 0, father_component: Root = None) -> None:
    ...


def event_tree(start_component: str | Root):
    ...


def event_id_tree(start_component: str | Root):
    ...


def event_type_tree(start_component: str | Root):
    ...


def event_update():
    ...


def set_debug(enable: bool = None):
    ...


def update_component_event(component: Root, event_type: int, event: Event, *args, **kwargs) -> any:
    ...


def update_component_graphic(component: Root, *args, **kwargs) -> any:
    ...

