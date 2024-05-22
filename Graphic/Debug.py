
from .EffectFunction.MarkBorder import TextType, EdgeType, mark_component
from .UI import Label
from .Basic import *
from .Management import GraphicManagement
import pygame


class GraphicDebug:
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
        self.__debug_Label.graph_surface.fill((0, 0, 0, self.info_alpha))
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
                    self.textType.change_text(f'{type(component).__name__}:{component.id}')
                    mark_component(component, self.edgeType, self.textType,
                                   (0, 0, component.w - self.edgeType.width, component.h - self.edgeType.width),
                                   alpha=self.info_alpha)

                self.add_graphic_function(draw_board)
            else:
                self.windows.graph_update()

    def graphic_debug_component(self, component):
        self.graphic_debug_single(component)
        for son in component.son:
            if isinstance(son, Surface):
                self.graphic_debug_component(son)

    def graphic_debug_single(self, component):
        self.textType.change_text(f'{type(component).__name__}:{component.id}')
        mark_component(self.__debug_Label, self.edgeType, self.textType, component.real_rect())

    def overwrite_graphic_core(debug, enable: bool = True):
        if enable:
            debug.__graphic_update_function = Graph.graph_update

            def overwrite_graph_update(self, *args, **kwargs):
                debug.__graphic_update_function(self, *args, **kwargs)
                for insert in debug.__graphic_insert_function:
                    insert(self, *args, **kwargs)

            GraphicManagement.graph_update = overwrite_graph_update
        else:
            GraphicManagement.graph_update = debug.__graphic_update_function
            debug.__graphic_update_function = None

    def add_graphic_function(self, function):
        self.__graphic_insert_function.append(function)

    def event_debug(self):
        pass

    def debug(self):
        self.graphic_debug()
        self.event_debug()