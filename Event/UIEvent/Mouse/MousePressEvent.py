import pygame.mouse
from .MouseBasicEvent import Basic, Inspector as father_inspector


class Press(Basic):
    def __init__(self, component, bind_button: int = None, skip_track: bool = False, *args, **kwargs):
        super().__init__(component, skip_track, *args, **kwargs)
        self.event_type_name = "UI Mouse Click Event"
        self.button = bind_button
        self.pressing = False
        self.press_outside = False

    def track_check(self, pos, button, *args, **kwargs) -> any:
        # print(self.press_outside)
        if self.button is not None:
            if super().track_check(pos, *args, **kwargs) is False:
                if button[self.button] is False:
                    self.press_outside = False
                    if self.pressing:
                        self.pressing = False
                else:
                    if self.pressing is False:
                        self.press_outside = True
                return False
            else:
                if button[self.button]:
                    self.pressing = True
                else:
                    if self.pressing and self.press_outside is False:
                        self.pressing = False
                        return True
                    if self.press_outside is True:
                        self.press_outside = False
                    self.pressing = False
            return self.pressing
        else:
            return True


class Inspector(father_inspector):
    target_event_class = Press

    def update_kwargs(self, component: any = None):
        super().update_kwargs()
        self.__kwargs['generic']['button'] = pygame.mouse.get_pressed()
