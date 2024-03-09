import Functions as F
from GlobalConstant import EventConstant
from GraphicComponent.UI.Label import Label
from GraphicComponent.Event import Event


class MouseButtonUp(Event):
    event_name = EventConstant.MouseButtonUp

    def __init__(self, function: any, button: int, Component: Label):
        super().__init__()
        self.track_function = function
        self.Label = Component

    def track_check(self, event, *args, **kwargs) -> any:
        """

        :param event:
        :param args:
        :return:
        """

        """
        event:
            rel_pos: [int, int]
            button: int
            touch: bool
            window: None
        """

        if F.Point_in_Rect(event.pos, self.Label.real_rect()):
            return True
        else:
            return False


class MouseButtonWheel(Event):
    event_name = EventConstant.MouseWheel

    def __init__(self, function: any, button: int, Component: Label):
        super().__init__()
        self.track_function = function
        self.Label = Component

    def track_check(self, event, *args, **kwargs) -> any:
        """

        :param event:
        :param args:
        :return:
        """
        """
        event:
            flipped: bool
            precise_x: float
            precise_y: float
            touch: bool
            windows: None
            x: int
            y: int
        """
        return True


class Button(Label):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)

    def bind_press_function(self, function, button, **kwargs):
        make_event = MouseButtonUp(function, button, self)
        self.event_add_event(EventConstant.MouseButtonUp, make_event, **kwargs)

    def unbind_press_function(self, button) -> None:
        if EventConstant.MouseButtonUp in self.event_track_type:
            for i in self.event[EventConstant.MouseButtonUp]:
                i: MouseButtonUp
                if i.event_name == button:
                    self.event_remove_event(button, i.id)

    def search_press_function(self, button) -> tuple[MouseButtonUp, ...]:
        ret = []
        if EventConstant.MouseButtonUp in self.event_track_type:
            for i in self.event[EventConstant.MouseButtonUp]:
                i: MouseButtonUp
                if i.event_name == button:
                    ret.append(i)
        return tuple(ret)
