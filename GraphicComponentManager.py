import pygame.display
from GraphicComponent import *
from GraphicComponent.Effect.MarkBorder import TextType, EdgeType, mark_component
from GraphicComponent.UI import Label


class GraphicComponentDebug:
    def __init__(self, component, windows: MainWindows):
        self.__graphic_update_function = None
        self.__graphic_insert_function = list()
        self.__debug_component = component
        self.__debug_Label = Label((0, 0), component.size())
        self.one_layer: bool = True
        self.info_alpha = 125
        self.textType = TextType()
        self.edgeType = EdgeType()
        self.windows = windows

    def graphic_debug(self):
        self.__debug_Label.graph_surface.fill((0, 0, 0, 0))
        if self.one_layer:
            self.graphic_debug_component(self.__debug_component)
        self.graphic_update()

    def graphic_update(self):
        if self.one_layer:
            self.__debug_Label.graph_surface.set_alpha(self.info_alpha)
            self.windows.windows_surface.blit(self.__debug_Label.graph_surface, (0, 0))
            pygame.display.flip()
        else:
            if self.__graphic_update_function is None:
                self.overwrite_graphic_core()

                def draw_board(component, *args, **kwargs):
                    self.textType.change_text(f'{type(component).__name__}:{component.ID}')
                    mark_component(component, self.edgeType, self.textType,
                                   (0, 0, component.w - self.edgeType.width, component.h - self.edgeType.width),
                                   alpha=self.info_alpha)

                self.overwrite_add_graphic_function(draw_board)
            else:
                self.windows.graph_update()

    def graphic_debug_component(self, component):
        self.graphic_debug_single(component)
        for son in component.son:
            if isinstance(son, Label):
                self.graphic_debug_component(son)

    def graphic_debug_single(self, component):
        self.textType.change_text(f'{type(component).__name__}:{component.ID}')
        mark_component(self.__debug_Label, self.edgeType, self.textType, component.real_rect())

    def overwrite_graphic_core(debug, enable: bool = True):
        if enable:
            debug.__graphic_update_function = Graphic.graph_update

            def overwrite_graph_update(self, *args, **kwargs):
                debug.__graphic_update_function(self, *args, **kwargs)
                for insert in debug.__graphic_insert_function:
                    insert(self, *args, **kwargs)
            Graphic.graph_update = overwrite_graph_update
        else:
            Graphic.graph_update = debug.__graphic_update_function
            debug.__graphic_update_function = None

    def overwrite_add_graphic_function(self, function):
        self.__graphic_insert_function.append(function)

    def event_debug(self):
        pass

    def debug(self):
        self.graphic_debug()
        self.event_debug()


class GraphicComponentManager:
    def __init__(self, mainWindowsObject: MainWindows = None, size: tuple[int, int] = (800, 600), ):
        self.__debug_mode = False
        self.debug = None
        if mainWindowsObject:
            self.windows = mainWindowsObject
        else:
            self.windows = MainWindows(size)

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

    def components_tree(self, start_component: Root = None) -> dict[Root: set, ...]:
        if start_component is None:
            start_component = self.windows
        ret = dict()
        son_ret = set()
        for son in start_component.son:
            son_ret.update(self.components_tree(son))
        ret[start_component] = son_ret
        return ret

    def find_component(self, ID: str, start_component: Root = None) -> Root | None:
        if start_component is None:
            start_component = self.windows
        if start_component.ID == ID:
            return start_component
        else:
            for son in start_component.son:
                ret = self.find_component(ID, son)
                if ret is not None:
                    return ret
        return None

    def find_components(self, ID: tuple[str, ...], start_component: Root = None) -> tuple[Root | None, ...]:
        ret = list()
        for each_ID in ID:
            ret.append(self.find_component(each_ID, start_component))
        return tuple(ret)

    def find_components_type(self, component_type: str, start_component: Root = None) -> tuple[Root, ...]:
        ret = list()
        if start_component is None:
            start_component = self.windows
        if start_component.__str__() == component_type:
            ret.append(start_component)
        for son in start_component.son:
            ret += self.find_components_type(component_type, son)
        return tuple(ret)

    def add_component(self, component: Root, father_component: Root = None) -> None:
        if father_component is None:
            father_component = self.windows
        father_component.tree_add_son(component)

    def add_components(self, component: tuple[Root, ...], father_component: Root = None) -> None:
        if father_component is None:
            father_component = self.windows
        for each in component:
            self.add_component(each, father_component)

    def remove_component(self, target: str | Root) -> None:
        if isinstance(target, str):
            target = self.find_component(target, self.windows)
        if isinstance(target, Root):
            target.delete_with_son()

    def remove_components(self, target: tuple[str or Root, ...]) -> None:
        for i in target:
            self.remove_component(i)

    def graphic_update(self):
        if self.__debug_mode:
            Graphic.graph_update(self.windows)
            self.windows.windows_surface.blit(self.windows.graph_surface, (0, 0))
            self.debug.graphic_debug()
        else:
            self.windows.graph_update()

    def event_update(self):
        self.windows.event_update()
        if self.__debug_mode:
            self.debug.event_debug()

    def set_debug(self, enable: bool = None):
        if enable:
            self.__debug_mode = True
            if self.debug is None:
                self.debug = GraphicComponentDebug(self.windows, self.windows)
        else:
            self.__debug_mode = False

    def update_component_event(self, component: Root, event_type: int, event: Event, **kwargs):
        if component is None:
            component = self.windows
        component.event_spread(event_type, event=event, **kwargs)

    def update_component_graphic(self, component: Root, *args, **kwargs):
        if component is not None:
            component = self.windows
        component.graph_update()
