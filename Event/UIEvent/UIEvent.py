from Event.BasicEvent import BasicEvent as BasicEventObject, Inspector as FatherInspector


class Basic(BasicEventObject):
    def __init__(self, graphic_object: any, skip_track: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_type_name = "Event_UI_Basic"
        self.graphic_object = graphic_object
        self.skip_track = skip_track

    def track_check(self, *args, **kwargs):
        if super().track_check(*args, **kwargs):
            return True

    def track_run(self, *args, **kwargs):
        if self.skip_track:
            pass
        else:
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
    target_event_class = Basic

    def __init__(self, target: Basic):
        super().__init__(target)
        self.event_type_name = "UI Event"
        self.__kwargs["spread"] = dict()
        self.__kwargs['spread']['Inspector'] = self

    def trigger(self, **kwargs):
        args = {}
        args.update(self.__kwargs['generic'])
        args.update(self.__kwargs['trigger'])
        args.update(kwargs) if kwargs is not None else None

        self.spread(**args)
        super().trigger(**args)

    def spread(self, **kwargs):
        args = {}
        args.update(self.__kwargs['generic'])
        args.update(self.__kwargs['spread'])
        args.update(kwargs) if kwargs is not None else None
        self.target_event.graphic_object.event_spread(self.target_event.event_type, **kwargs)

    def update_kwargs(self, component=None):
        pass
