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

    def delete(self):
        ...

    def __copy__(self, copied: any = None):
        ...


class Inspector:
    target_event_class = BasicEvent
    target_event: BasicEvent

    def __init__(self, target: BasicEvent):
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
