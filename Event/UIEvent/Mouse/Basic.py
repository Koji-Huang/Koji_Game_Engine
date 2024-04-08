from ..Basic import Basic as BasicUIEvent, Inspector as FatherInspector
from Functions import Point_in_Rect


class Basic(BasicUIEvent):
    def __init__(self, component, *args, **kwargs):
        super().__init__(component, *args, **kwargs)
        self.event_type_name = "Event_UI_Mouse_Basic"
        self.pos = (0, 0)

    def track_check(self, *args, **kwargs):
        return False if super().track_check(*args, **kwargs) \
            else Point_in_Rect(self.pos, self.graphic_object.rect())

    def update_info(self, pos=None, **kwargs):
        if pos is not None:
            self.pos = pos
        super().update_info(**kwargs)

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Basic(self.pos)
        else:
            copied.pos = self.pos
        super().__copy__(copied)
        return copied

    def component_spread_args(self, args: dict, component: any = None):
        args = super().component_spread_args(args, component)
        if component is None:
            click_pos: tuple[int, int] = args['pos']
            cost_size = self.graphic_object.size()
            args['pos'] = (click_pos[0] - cost_size[0], click_pos[1] - cost_size[1])
        return args


class Inspector(FatherInspector):
    def __init__(self, target: Basic):
        """
        Inspector is used to trigger event object with args. (args won't come from space)
        :param target: the target event to trigger
        """
        pass

    def check(self):
        """
        check if event can be trigger
        """
        pass

    def trigger(self):
        """
        trigger event.
        """
        pass