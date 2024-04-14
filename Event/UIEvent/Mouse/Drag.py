import pygame

from Event.UIEvent.Mouse.Basic import Basic, Inspector as father_inspector


class Drag(Basic):
    def __init__(self, component: any,  button: int = None, skip_track: bool = False,*args, **kwargs):
        super().__init__(component, skip_track, *args, **kwargs)
        self.button = button
        self.drag_start_pos = (0, 0)
        self.drag_end_pos = (0, 0)
        self.relative_pos = (0, 0)
        self.dragging = False

    def track_check(self, pos: tuple[int, int], button: tuple[int, ...], *args, **kwargs):
        # No Button Match, only spread
        if self.button is None:
            return True
        # No Button Pressing
        if button[self.button] is False and self.dragging is False:
            return False
        # Mouse pos out of component and self is not dragging
        if super().track_check(pos, *args, **kwargs) and self.dragging is False:
            return False
        # Button Click Down
        if self.dragging is False and button[self.button] is True:
            self.drag_start_pos = pos
            self.drag_end_pos = (0, 0)
            self.dragging = True
            return True
        # Button Pressing
        if self.dragging:
            self.relative_pos = (pos[0] - self.drag_start_pos[0],
                                 pos[1] - self.drag_start_pos[1])
        # Button Up
        if button[self.button] is False and self.dragging:
            self.drag_end_pos = pos
            self.dragging = False

        # In no case
        return True

    def track_run(self, *args, **kwargs):
        return super().track_run(start_pos=self.drag_start_pos, end_pos=self.drag_end_pos,
                                 relative_pos=self.relative_pos, *args, **kwargs)

    def is_dragging(self) -> bool:
        return self.dragging


class Inspector(father_inspector):
    target_event_class = Drag

    def update_kwargs(self, component=None):
        super().update_kwargs()
        self.__kwargs['generic']['button'] = pygame.mouse.get_pressed()
