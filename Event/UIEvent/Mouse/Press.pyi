import pygame.mouse

from Basic import Basic, Inspector as father_inspector


class Press(Basic):
    button: int = None
    pressing: bool = False
    press_outside: bool = False

    def __init__(self, component, bind_button: int = None, skip_track: bool = False, *args, **kwargs):
        ...

    def track_check(self, pos, button, *args, **kwargs) -> any:...

    def track_run(self, *args, **kwargs) -> any:...

    def update_info(self, **kwargs) -> None: ...

    def delete(self):
        ...

    def __copy__(self, copied: any = None):
        ...


class Inspector(father_inspector):
    def update_kwargs(self, component: any = None):
        ...

