import pygame.mouse
from Event.UIEvent.Mouse.MouseBasicEvent import Basic, Inspector as father_inspector


class Click(Basic):
    def __init__(self, component, bind_button: int = None, skip_track: bool = False, *args, **kwargs):
        super().__init__(component, skip_track, *args, **kwargs)
        self.event_type_name = "UI Mouse Click Event"
        self.button = bind_button
        self.pressed = False
        self.press_outside = False

    def track_check(self, pos, button, *args, **kwargs):
        if self.button is None:
            return True
        is_pressing = button[self.button]
        is_outside = super().track_check(pos, *args, **kwargs)
        is_changed = is_pressing != self.pressed

        if is_outside and is_changed:
            if is_pressing:
                self.press_outside = True
            else:
                self.pressed = False
                self.press_outside = False
        if not is_outside and is_changed:
            if is_pressing:
                self.press_outside = False
                self.pressed = True
            else:
                if not self.press_outside:
                    self.pressed = False
                    return True
                else:
                    self.press_outside = False
                    self.pressed = False
                    return True
        return False

        # if not is_outside:
        #     if is_pressing is True:
        #         self.press_outside = False
        #         if self.pressed:
        #             self.pressed = False
        #     else:
        #         if self.pressed is False:
        #             self.press_outside = True
        #     return False
        # else:
        #     if is_pressing:
        #         self.pressed = True
        #     else:
        #         if self.pressed and self.press_outside is False:
        #             self.pressed = False
        #             return True
        #         if self.press_outside is True:
        #             self.press_outside = False
        #         self.pressed = False


class Inspector(father_inspector):
    target_event_class = Click

    def update_kwargs(self, component: any = None):
        super().update_kwargs()
        self.__kwargs['generic']['button'] = pygame.mouse.get_pressed()
