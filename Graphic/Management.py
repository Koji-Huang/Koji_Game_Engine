import pygame.display
from .Basic import *


class GraphicManagement:
    def __init__(self, mainWindowsObject: MainWindows = None, size: tuple[int, int] = (800, 600), ):
        self.__debug_mode = False
        self.debug = None
        if mainWindowsObject:
            self.windows = mainWindowsObject
        else:
            self.windows = MainWindows(size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def general_info(self):
        ...

    def component_type(self, start_component: Root = None):
        if start_component is None:
            start_component = self.windows
        ret = set()
        ret.add(start_component.__str__())
        for son in start_component.son:
            ret.update(self.component_type(son))
        return ret

    def component_tree(self, start_component: Root = None) -> dict[Root: set, ...]:
        if start_component is None:
            start_component = self.windows
        ret = dict()
        son_ret = set()
        for son in start_component.son:
            son_ret.update(self.component_tree(son))
        ret[start_component] = son_ret
        return ret

    def component_find(self, ID: str, start_component: Root = None) -> Root | None:
        if start_component is None:
            start_component = self.windows
        if start_component.id == ID:
            return start_component
        else:
            for son in start_component.son:
                ret = self.component_find(ID, son)
                if ret is not None:
                    return ret
        return None

    def components_find(self, ID: tuple[str, ...], start_component: Root = None) -> tuple[Root | None, ...]:
        ret = list()
        for each_ID in ID:
            ret.append(self.component_find(each_ID, start_component))
        return tuple(ret)

    def components_find_type(self, component_type: str, start_component: Root = None) -> tuple[Root, ...]:
        ret = list()
        if start_component is None:
            start_component = self.windows
        if start_component.__str__() == component_type:
            ret.append(start_component)
        for son in start_component.son:
            ret += self.components_find_type(component_type, son)
        return tuple(ret)

    def component_add(self, component: Root, father_component: Root = None) -> None:
        if father_component is None:
            father_component = self.windows
        father_component.tree_add_son(component)

    def components_add(self, component: tuple[Root, ...], father_component: Root = None) -> None:
        if father_component is None:
            father_component = self.windows
        for each in component:
            self.component_add(each, father_component)

    def component_remove(self, target: str | Root) -> None:
        if isinstance(target, str):
            target = self.component_find(target, self.windows)
        if isinstance(target, Root):
            target.delete_with_son()

    def components_remove(self, target: tuple[str or Root, ...]) -> None:
        for i in target:
            self.component_remove(i)

    def graphic_update(self):
        if self.__debug_mode:
            Graph.graph_update(self.windows)
            self.windows.windows_surface.blit(self.windows.graph_surface, (0, 0))
            self.debug.graphic_debug()
        else:
            self.windows.graph_update()

    def event_get(self, pid: str, event_type: str = None, component: Root = None):
        if component is None:
            component = self.windows
        if event_type is not None:
            if event_type in component.event_type:
                for event in component.event[event_type]:
                    if event.id == pid:
                        return event, component, event_type
            else:
                return None
        else:
            for event_type in component.event_type:
                for event in component.event[event_type]:
                    if event.id == pid:
                        return event, component, event_type
        for son in component.son:
            son_result = self.event_get(pid, event_type, son)
            if son_result is not None:
                return son_result, component, event_type
        return None

    def event_remove(self, pid: str, event_type: str = None, component: Root = None) -> None:
        event, component, event_type = self.event_get(pid, event_type, component)
        component.event_remove(event_type, pid)

    def event_add(self, event, event_type: int = 0, father_component: Root = None) -> None:
        if father_component is None:
            father_component = self.windows
        father_component.event_add(event_type, event)

    def event_tree(self, start_component: str | Root = None, event_type: str = None):
        if start_component is None:
            start_component = self.windows
        ret = dict()
        if event_type is None:
            copied = start_component.event.copy()
            collections = list()
            for son in start_component.son:
                collections.append(self.event_tree(son))
        else:
            copied = start_component.event[event_type].copy()
            collections = list()
            for son in start_component.son:
                collections.append(self.event_tree(son))
        ret[start_component.id] = {copied: collections}
        return ret

    def event_id_tree(self, start_component: str | Root, event_type: str = None):
        if start_component is None:
            start_component = self.windows
        ret = dict()
        if event_type is None:
            copied = {event_type: event.id for event_type in start_component.event_type
                      for event in start_component.event[event_type]}
            collections = list()
            for son in start_component.son:
                collections.append(self.event_id_tree(son))
        else:
            copied = [event.id for event in start_component.event[event_type]]
            collections = list()
            for son in start_component.son:
                collections.append(self.event_id_tree(son))
        ret[start_component.id] = {copied: collections}
        return ret

    def event_type_tree(self, start_component: str | Root, event_type: str = None):
        if start_component is None:
            start_component = self.windows
        ret = dict()
        if event_type is None:
            copied = start_component.event_type.copy()
            collections = list()
            for son in start_component.son:
                collections.append(self.event_type_tree(son))
        else:
            copied = [event_type]
            collections = list()
            for son in start_component.son:
                collections.append(self.event_type_tree(son))
        ret[start_component.id] = {copied: collections}
        return ret

    def event_update(self):
        self.windows.event_update()
        if self.__debug_mode:
            self.debug.event_debug()

    def set_debug(self, enable: bool = None):
        if enable:
            self.__debug_mode = True
            if self.debug is None:
                from .Debug import GraphicDebug
                self.debug = GraphicDebug(self.windows, self.windows)
        else:
            self.__debug_mode = False

    def update_component_event(self, component: Root, event_type: int, event, **kwargs):
        if component is None:
            component = self.windows
        component.event_spread(event_type, event=event, **kwargs)

    def update_component_graphic(self, component: Root, *args, **kwargs):
        if component is not None:
            component = self.windows
        component.graph_update()
