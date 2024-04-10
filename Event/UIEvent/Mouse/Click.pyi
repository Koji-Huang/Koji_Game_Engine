import pygame.mouse

from Basic import Basic, Inspector as father_inspector


class Click(Basic):
    button: tuple[bool, ...] = None

    def __init__(self, component, *args, **kwargs):
        ...

    def track_check(self,  *args, **kwargs) -> any:...

    def track_run(self, *args, **kwargs) -> any:...

    def update_info(self, **kwargs) -> None: ...

    def delete(self):
        ...

    def __copy__(self, copied: any = None):
        ...


class Inspector(father_inspector):
    def update_kwargs(self, component: any = None):
        ...

