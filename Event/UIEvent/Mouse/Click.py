import pygame.mouse
from FunctionTools.coordinate import point_in_rect
from FunctionTools.parameter import mix_series
from Basic import Basic, Inspector as father_inspector


class Click(Basic):
    def __init__(self, component, *args, **kwargs):
        super().__init__(component, *args, **kwargs)
        self.event_type_name = "UI Mouse Click Event"
        self.button = (False, False, False, False, False, False, False)

    def track_check(self, pos, *args, **kwargs) -> any:
        if super().track_check(*args, **kwargs) is False:
            return False
        if point_in_rect(pos, self.graphic_object.rect()):
            return True

    def update_info(self, button: tuple[bool, ...] = None, **kwargs) -> None:
        super().update_info(**kwargs)
        if button is not None:
            self.button = mix_series(self.button, button)


class Inspector(father_inspector):
    target_event_class = Click

    def update_kwargs(self, component: any = None):
        super().update_kwargs()
        self.__kwargs['generic']['button'] = pygame.mouse.get_pressed()
