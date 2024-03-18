import math

import pygame

import GlobalConstant
from GraphicComponent.UI.Label import Label
from GraphicComponent.UI.Button import MouseButtonWheel


def scale(**kwargs):
    camera = kwargs['camera']
    event = kwargs['event']

    if event.y > 0:
        scale_num = 1.1
    elif event.y < 0:
        scale_num = 0.9
    else:
        return

    print(event)
    pos = pygame.mouse.get_pos()
    object_click_surface = tuple((pos[i] - camera.pos()[i] for i in [0, 1]))
    object_click_inside_map = tuple(object_click_surface[i] / camera.allScaleRatio + camera.originPoint[i] for i in [0, 1])
    inside_map_origin_point = camera.originPoint
    click_origin_cost_x = inside_map_origin_point[0] + object_click_inside_map[0]
    click_origin_cost_y = inside_map_origin_point[1] + object_click_inside_map[1]
    reserve_x = click_origin_cost_x - click_origin_cost_x * scale_num
    reserve_y = click_origin_cost_y - click_origin_cost_y * scale_num

    camera.scale(scale_num, (reserve_x, reserve_y))


class Camera(Label):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)
        self.originPoint = (0, 0)
        self.allScaleRatio: float = 1
        rollEvent = MouseButtonWheel(scale, pygame.MOUSEWHEEL, self)
        self.event_add(pygame.MOUSEWHEEL, rollEvent)

    def scale(self, rel_ratio=None, rel_pos=None):
        if rel_ratio and rel_pos:
            for i in self.son:
                self.scale_son(i, rel_ratio, rel_pos)
        elif rel_ratio:
            for i in self.son:
                self.scale_son(i, rel_ratio, (0, 0))
        elif rel_pos:
            for i in self.son:
                self.scale_son(i, 1, rel_pos)
        self.allScaleRatio *= rel_ratio
        self.originPoint = tuple((self.originPoint[0] + rel_pos[0], self.originPoint[1] + rel_pos[1]))

    def scale_son(self, son: Label, rel_ratio: float, rel_pos: tuple):
        # set default value
        if self.allScaleRatio == 1:
            son.origin_pos = son.pos()
            son.origin_size = son.size()
        # Reset Surface
        self.graph_primer_surface.fill((0, 0, 0, 255))
        # operate
        son.set_pos(tuple(rel_pos[i] + son.pos()[i] * rel_ratio for i in [0, 1]))
        son.set_size(tuple(i * rel_ratio for i in son.size()))
        son.graph_active = True
        # Spread
        for grandson in son.son:
            self.scale_son(grandson, rel_ratio, rel_pos)

    def event_receive(self, evnet_name, **kwargs):
        super().event_receive(evnet_name, camera=self, **kwargs)
