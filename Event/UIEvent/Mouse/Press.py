from GlobalConstant import EventConstant


class Press(Event):
    event_name = EventConstant.MouseButtonUp

    def __init__(self, function: any, button: int, component: any):
        super().__init__(component)
        self.track_function = function

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

        if F.Point_in_Rect(event.graphic_object, self.graphic_object.real_rect()):
            return True
        else:
            return False

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Press(self.track_function, 0, self.graphic_object)
        super().__copy__(copied)
        return copied
