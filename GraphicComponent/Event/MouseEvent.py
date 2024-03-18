from GraphicComponent.Event import Event
from GlobalConstant import EventConstant
import Functions as F


class Press(Event):
    event_name = EventConstant.MouseButtonUp

    def __init__(self, function: any, button: int, Component: any):
        super().__init__(Component)
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


class Scrolling(Event):
    event_name = EventConstant.MouseWheel

    def __init__(self, function: any, button: int, Component: any):
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