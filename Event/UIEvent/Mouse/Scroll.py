import time

import pygame.mouse
from Event.UIEvent.Mouse.Basic import Basic, Inspector as father_inspector


class Scroll(Basic):
    def __init__(self, component, assess_time_interval: int = 0.2, skip_track: bool = False, *args, **kwargs):
        super().__init__(component, skip_track, *args, **kwargs)
        self.event_type_name = "UI Mouse Scroll Event"
        self.record_scroll_x = 0
        self.record_scroll_y = 0
        self.last_time = time.time()
        self.update_time = time.time()
        self.assess_time_interval = assess_time_interval

    def track_run(self, _time: int, precise_x: float, precise_y: int, touch: bool, *args, **kwargs):
        is_new_scroll: bool = self.update_time + self.assess_time_interval < _time
        if is_new_scroll:
            self.record_scroll_x = 0
            self.record_scroll_y = 0
        self.last_time = self.update_time
        self.update_time = _time
        self.record_scroll_x += precise_x
        self.record_scroll_y += precise_y
        return super().track_run(
            is_new_scroll=is_new_scroll,
            record_x=self.record_scroll_x,
            record_y=self.record_scroll_y,
            update_time=self.update_time,
            last_time=self.last_time,
            *args, **kwargs)

    def is_scrolling(self):
        return self.update_time - time.time() <= self.assess_time_interval


class Inspector(father_inspector):
    target_event_class = Scroll

    def check(self, **kwargs):
        return self.__kwargs['generic']['track']

    def update_kwargs(self, component: any = None):
        super().update_kwargs()
        pygame_event = pygame.event.get(pygame.MOUSEWHEEL)
        self.__kwargs['generic']['_time'] = time.time()
        if pygame_event != []:
            pygame_event = pygame_event[0]
            self.__kwargs['generic']['track'] = True
            self.__kwargs['generic']['precise_x'] = pygame_event.precise_x
            self.__kwargs['generic']['precise_y'] = pygame_event.precise_y
            self.__kwargs['generic']['touch'] = pygame_event.touch
        else:
            self.__kwargs['generic']['track'] = False
