from ..Basic import BasicEvent as BasicEventObject


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

    def component_spread_args(self, args: dict, component=None):
        return args.copy()
