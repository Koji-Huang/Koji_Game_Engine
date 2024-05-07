import pygame.mouse

from ..UIEvent import Basic as BasicUIEvent, Inspector as FatherInspector
from Function.coordinate import point_in_rect


class Basic(BasicUIEvent):
    def __init__(self, component, skip_track: bool = False, *args, **kwargs):
        super().__init__(component, skip_track, *args, **kwargs)
        self.event_type_name = "UI Mouse Event"
        self.pos = (0, 0)
        self.tangent_length = component.w ** 2 + component.h ** 2

    def track_check(self, pos, distance, *args, **kwargs):
        return False if super().track_check(*args, **kwargs) or distance > self.tangent_length is False\
            else point_in_rect(pos, self.graphic_object.rect())

    def update_info(self, pos=None, **kwargs):
        if pos is not None:
            self.pos = pos
        super().update_info(**kwargs)
        return kwargs

    def update_kwargs(self, component: any = None, **kwargs):
        super().update_kwargs()
        if component is None:
            component = self.graphic_object
        if kwargs.get('pos') is None:
            click_pos = pygame.mouse.get_pos()
            cost_size = component.real_pos()
        else:
            click_pos: tuple[int, int] = kwargs['pos']
            cost_size = component.pos()
        kwargs['pos'] = (click_pos[0] - cost_size[0], click_pos[1] - cost_size[1])
        kwargs['distance'] = cost_size[0] ** 2 + cost_size[1] ** 2
        return kwargs

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Basic(self.pos)
        else:
            copied.pos = self.pos
        super().__copy__(copied)
        return copied


class Inspector(FatherInspector):
    target_event_class = Basic

    def update_kwargs(self, component: any = None, **kwargs: dict):
        super().update_kwargs()
        pos = self.get_mouse_pos()
        self.__kwargs["generic"]["pos"] = pos

    def get_mouse_pos(self):
        click_pos = pygame.mouse.get_pos()
        cost_size = self.target_event.graphic_object.real_pos()
        return tuple((click_pos[0] - cost_size[0], click_pos[1] - cost_size[1]))


