from ..Basic import Basic as BasicUIEvent, Inspector as FatherInspector


class Basic(BasicUIEvent):
    pos: tuple[int, int]

    def __init__(self, component, *args, **kwargs):
        """
        Basic Mouse Event.
        MouseEvent is always on Relative coordinates.
        pos is mean that the pos of mouse but relative to the component
        """
        pass

    def update_info(self, pos=None, **kwargs):
        """
        New info add
        pos: self.pos
        """
        pass

    def __copy__(self, copied: any = None):
        """
        New arg add
        pos: self.pos
        """
        pass


class Inspector(FatherInspector):
    target_event_class: Basic

    def __init__(self, target: Basic):
        """
        Inspector is used to trigger event object with args. (args won't come from space)
        :param target: the target event to trigger
        """
        pass

    def check(self, **kwargs):
        """
        check if event can be trigger
        """
        pass

    def trigger(self, **kwargs):
        """
        trigger event.
        """
        pass

    def get_click_pos(self):
        ...