from ..Basic import BasicEvent as BasicEventObject, Inspector as FatherInspector


class Basic(BasicEventObject):
    def __init__(self, graphic_object: any, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_type_name = "Event_UI_Basic"
        self.graphic_object = graphic_object

    def track_check(self, *args, **kwargs):
        if super().track_check(*args, **kwargs):
            return True

    def track_run(self, *args, **kwargs):
        return super().track_run(graphic_object=self.graphic_object, *args, *self.track_args, **kwargs)

    def update_info(self, graphic_object=None, **kwargs):
        if graphic_object is not None:
            self.graphic_object = graphic_object
        super().update_info(**kwargs)

    def delete(self):
        if self.graphic_object is not None:
            self.graphic_object.event_remove(self.event_type, self)
        return super().delete()

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Basic(self.graphic_object)
        else:
            copied.graphic_object = self.graphic_object
        super().__copy__(copied)
        return copied


class Inspector(FatherInspector):
    def __init__(self, target: Basic):
        super().__init__(target)

    def check(self, **kwargs):
        return super().check(**kwargs)

    def trigger(self, **kwargs):
        self.target_event.track_run(**kwargs)
        self.spread(**kwargs)

    def spread(self, **kwargs):
        if kwargs:
            kwargs = self.component_spread_args(kwargs)
        self.target_event.graphic_object.event_spread(self.target_event.event_type, **kwargs)

    def component_spread_args(self, args: dict = None, component=None):
        if args is None:
            return dict()
        return args
