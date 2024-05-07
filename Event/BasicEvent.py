from typing import Callable

ID_Index = 0
ID_Receive = set()


_event_id_get: Callable[[], str]
_event_id_recycle: Callable[[str], None]
_inspector_id_get: Callable[[], str]
_inspector_id_recycle: Callable[[str], None]


class BasicEvent:
    def __init__(self, *args, **kwargs):
        self.event_type_name = "Event_Basic"
        self.event_name = 'undefined'
        self.track_args = dict()
        self.id = _event_id_get()

    def track_check(self, *args, **kwargs):
        return True

    def track_run(self, *args, **kwargs):
        return self.track_function(*args, *self.track_args, **kwargs)

    def update_info(self, **kwargs):
        for update_name, update_value in kwargs.items():
            self.track_args.update({update_name: update_value})

    def update_kwargs(self, **kwargs):
        return kwargs

    def delete(self):
        tmp = self.id
        _event_id_recycle(self.id)
        del self
        return tmp

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = BasicEvent()
        copied.event_name = self.event_name
        copied.track_function = self.track_function
        copied.track_args = self.track_args
        copied.event_type_name = self.event_type_name

        return copied


class Inspector:
    target_event_class = BasicEvent

    def __init__(self, target: BasicEvent):
        self.__kwargs = dict()
        self.__kwargs['check'] = dict()
        self.__kwargs['trigger'] = dict()
        self.__kwargs['generic'] = dict()
        self.__kwargs['generic']['inspector'] = self
        self.active = True
        self.id = _inspector_id_get()
        if isinstance(target, self.target_event_class):
            self.target_event = target
        else:
            raise f"Error Event Type for inspect\nTarget Event: {self.target_event_class}\nInput Event: {target}\n"

    def check(self, **kwargs):
        args = {}
        args.update(self.__kwargs['generic'])
        args.update(self.__kwargs['check'])
        args.update(kwargs) if kwargs is not None else None
        return self.target_event.track_check(**args)

    def trigger(self, **kwargs):
        args = {}
        args.update(self.__kwargs['generic'])
        args.update(self.__kwargs['trigger'])
        args.update(kwargs) if kwargs is not None else None
        return self.target_event.track_run(**args)

    def record_kwargs(self, kwargs_type, **kwargs):
        if self.__kwargs.get(kwargs_type) is not None:
            self.__kwargs[kwargs]: dict
            for key in kwargs.keys():
                self.__kwargs[kwargs_type][key] = kwargs[key]

    def get_kwargs(self, kwargs_type):
        return self.__kwargs.get(kwargs_type)

    def remove_kwargs(self, kwargs_type, kwargs_key):
        if self.__kwargs.get(kwargs_type):
            if self.__kwargs[kwargs_type].get(kwargs_key):
                self.__kwargs[kwargs_type][kwargs_key].remove(kwargs_key)

    def update_kwargs(self):
        pass

    def is_active(self):
        return self.active
