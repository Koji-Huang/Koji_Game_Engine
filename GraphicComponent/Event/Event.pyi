
from GraphicComponent.UI import Label


class Event:
    event_name: any
    track_function: any
    track_args: dict
    event_id: int or any
    graphic_object: any
    id: str

    def __init__(self, graphic_object: Label):...

    def track_check(self,  *args, **kwargs) -> any:...

    def track_run(self, *args, **kwargs) -> any:...

    def update_info(self, **kwargs) -> None: ...

    def delete(self):
        ...

    def __copy__(self, copied: any = None):
        ...
