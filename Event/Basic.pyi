import types


class BasicEvent:
    event_name: any
    track_function: any
    track_args: dict
    event_type: int or any
    event_type_name: str
    id: str

    def __init__(self, *args, **kwargs):...

    def track_check(self,  *args, **kwargs) -> any:...

    def track_run(self, *args, **kwargs) -> any:...

    def update_info(self, **kwargs) -> None: ...

    def update_kwargs(self, **kwargs) -> dict:...

    def delete(self):...

    def __copy__(self, copied: any = None):...


class Inspector:
    # target event object's class
    target_event_class = BasicEvent
    # target trigger event
    target_event: BasicEvent
    # if not active, it won't be updated, check, trigger in manager
    active: bool
    # id after manager initialize this object
    id: str
    # some kwargs
    __kwargs: dict[any, ...]

    def __init__(self, target: BasicEvent):
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

    def record_kwargs(self, kwargs_type, **kwargs):
        """
        Record kwargs for check and trigger use
        """

    def get_kwargs(self, kwargs_type, **kwargs):
        """
        Check recorded kwargs
        """
        pass

    def remove_kwargs(self,  kwargs_type, kwargs_key):
        """
        Remove a value form kwargs
        """

    def update_kwargs(self):
        """
        update kwargs to use
        """

    def is_active(self):
        """
        If self is active
        """
