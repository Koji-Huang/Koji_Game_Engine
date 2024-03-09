from GraphicComponent.UI.Label import Label
from GraphicComponent.Event import Event



class MouseButtonUp(Event):
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

class MouseButtonWheel(Event):
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

class Button(Label):
    def __init__(self, pos, size, *args, **kwargs):...

    def bind_press_function(self, function, button, **kwargs) -> None:...

    def unbind_press_function(self, button) -> None:...

    def search_press_function(self) -> tuple[Event, ...]:...

