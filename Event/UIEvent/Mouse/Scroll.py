

class Scrolling(Event):
    event_name = EventConstant.MouseWheel

    def __init__(self, function: any, Component: any):
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
            flipped: bool
            precise_x: float
            precise_y: float
            touch: bool
            windows: None
            x: int
            y: int
        """
        return True

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Press(self.track_function, 0, self.graphic_object)
        super().__copy__(copied)
        return copied
