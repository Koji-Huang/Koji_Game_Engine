from Graphic.Graphic import Graphic
import pygame


class MainWindows(Graphic):
    windows_surface: pygame.Surface

    def __init__(self, size: tuple[int, int], pygame_parament: tuple or list = (), *args, **kwargs):...

    def graph_draw(self, *args, **kwargs):
        ...

    def update(self, *args) -> None:
        ...

    def graph_update(self, *args, **kwargs):
        ...

    def event_update(self):
        ...