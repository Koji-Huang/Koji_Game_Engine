from GraphicComponent.Event import Event
from GraphicComponent.UI import Label


class Press(Event):
    def __init__(self, function: any, button: int, Component: Label):
        """

        :param function:
        :param button:
        :param Component:
        """

    def track_check(self, event, *args) -> any:
        """

        :param event:
        :param args:
        :return:
        """

class Scrolling(Event):
    def __init__(self, function: any, button: int, Component: Label):
        """

        :param function:
        :param button:
        :param Component:
        """

    def track_check(self, event, *args) -> any:
        """

        :param event:
        :param args:
        :return:
        """

class Hold(Event):
    ...

class Click(Event):
    ...
