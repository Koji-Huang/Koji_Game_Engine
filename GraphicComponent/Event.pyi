
class Event:
    event_name: any
    track_function: any
    track_index: int
    track_args: dict
    event_id: int or any
    id: str

    def __init__(self) -> None:...

    def track_check(self, *args, **kwargs) -> any:...

    def track_run(self, *args, **kwargs) -> any:...

    def __track_run(self, *args, **kwargs) -> any:...

    def update_info(self, **kwargs) -> None: ...
