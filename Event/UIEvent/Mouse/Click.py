import pygame.mouse
from FunctionTools.coordinate import point_in_rect
from Event.UIEvent.Mouse.Basic import Basic, Inspector as father_inspector


class Click(Basic):
    def __init__(self, component, bind_button: int = None, *args, **kwargs):
        super().__init__(component, *args, **kwargs)
        self.event_type_name = "UI Mouse Click Event"
        self.button = bind_button
        self.pressed = False
        self.press_outside = False

    def track_run(self, *args, **kwargs):
        if self.button is None:
            pass
        else:
            return super().track_run(*args, **kwargs)

    def track_check(self, pos, button, *args, **kwargs) -> any:
        # print(self.press_outside)
        if self.button is not None:
            if super().track_check(pos, *args, **kwargs) is False:
                if button[self.button] is False:
                    self.press_outside = False
                    if self.pressed:
                        self.pressed = False
                else:
                    if self.pressed is False:
                        self.press_outside = True
                return False
            else:
                if button[self.button]:
                    self.pressed = True
                else:
                    if self.pressed and self.press_outside is False:
                        self.pressed = False
                        return True
                    if self.press_outside is True:
                        self.press_outside = False
                    self.pressed = False
        else:
            return True


class Inspector(father_inspector):
    target_event_class = Click

    def update_kwargs(self, component: any = None):
        super().update_kwargs()
        self.__kwargs['generic']['button'] = pygame.mouse.get_pressed()
