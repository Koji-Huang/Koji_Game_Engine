import pygame.mouse

from Basic import Basic, Inspector as father_inspector


class Scroll(Basic):
    record_scroll_x: float
    record_scroll_y: float
    last_time: float
    update_time: float
    assess_time_interval: float

    def __init__(self, component, assess_time_interval: int = 0.2, skip_track: bool = False, *args, **kwargs):
        ...

    def track_check(self, *args, **kwargs) -> any:...

    def track_run(self, *args, **kwargs) -> any:...

    def update_info(self, **kwargs) -> None: ...

    def delete(self):
        ...

    def __copy__(self, copied: any = None):
        ...


class Inspector(father_inspector):
    target_event_class = Scroll
    target_event: Scroll

    def update_kwargs(self, pygame_event: any = None, component: any = None):
        ...

