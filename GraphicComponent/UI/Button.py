import pygame.event
import Functions as F
from GlobalConstant import EventConstant
from GraphicComponent.UI.Label import Label
from GraphicComponent.Event import Event


class MousePressEvent(Event):
    event_name = EventConstant.MousePressEvent

    def __init__(self, function: any, button: int, Component: Label):
        super().__init__()
        self.track_function = function
        self.Label = Component

    def track_check(self, event, *args) -> any:
        if F.Point_in_Rect(event.pos, self.Label.real_rect()):
            return True
        else:
            return False


class Button(Label):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)

    def bind_press_function(self, function, button, **kwargs):
        make_event = MousePressEvent(function, button, self)
        self.event_add_event(EventConstant.MousePressEvent, make_event, **kwargs)

    def unbind_press_function(self, button) -> None:
        if EventConstant.MousePressEvent in self.event_track_type:
            for i in self.event[EventConstant.MousePressEvent]:
                i: MousePressEvent
                if i.event_name == button:
                    self.event_remove_event(button, i.id)

    def search_press_function(self, button) -> tuple[MousePressEvent, ...]:
        ret = []
        if EventConstant.MousePressEvent in self.event_track_type:
            for i in self.event[EventConstant.MousePressEvent]:
                i: MousePressEvent
                if i.event_name == button:
                    ret.append(i)
        return tuple(ret)
