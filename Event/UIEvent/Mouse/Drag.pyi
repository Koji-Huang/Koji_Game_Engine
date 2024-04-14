from Event.UIEvent.Mouse.Basic import Basic, Inspector as father_inspector
from Graphic.Graphic import Graphic


class Drag(Basic):
    # the button to match
    button: int
    # start pos of dragging
    drag_start_pos: tuple[int, int]
    # end pos of dragging
    drag_end_pos: tuple[int, int]
    # relative pos
    relative_pos: tuple[int, int]
    # if it had pressed
    dragging: bool

    def __init__(self, component: any,  button: int = None, skip_track: bool = False,*args, **kwargs):
        """

        """

    def track_check(self, pos: tuple[int, int], *args, **kwargs):
        """

        """

    def track_run(self, *args, **kwargs):
        """

        """

    def is_dragging(self) -> bool:
        """

        """

class Inspector(father_inspector):
    def update_kwargs(self, component = None):
        ...

    def spread(self, **kwargs):
        ...
