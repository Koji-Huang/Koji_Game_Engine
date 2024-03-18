from GraphicComponent import *


class GraphicComponentManager:
    def __init__(self, mainWindowsObject: MainWindows = None, size: tuple[int, ...] = None, ):
        ...

    def general_info(self):
        ...

    def component_type(self, start_component: Root = None) -> tuple[str, ...]:
        ...

    def components_tree(self, start_component: Root = None) -> dict:
        ...

    def find_component(self, id: str) -> Root:
        ...

    def find_components(self, ids: tuple[str, ...]) -> tuple[Root, ...]:
        ...

    def find_components_type(self, type: str) -> tuple[Root, ...]:
        ...

    def add_component(self, component: Root, father_component: Root) -> None:
        ...

    def add_components(self, component: tuple[Root, ...], father_component: Root) -> None:
        ...

    def remove_component(self, target: str or Root) -> None:
        ...

    def remove_components(self, target: tuple[str or Root, ...]) -> None:
        ...

