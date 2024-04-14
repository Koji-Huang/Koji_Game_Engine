import pygame

from Graphic.UI.Label import Label


class Image(Label):
    layout_mode: int
    image_antialiasing: bool
    image_surface: pygame.Surface
    def __init__(self, pos, size, image: str or pygame.Surface, alpha: int = 255, layout_mode=0,
                 antialiasing: bool = True, *args, **kwargs):...

    def change_image_object(self, image: str or pygame.Surface, layout_mode=0, antialiasing=True):
        ...

    def change_image_setting(self, alpha=255, layout_mode=0, antialiasing=True):
        ...

    def graph_draw(self):
        ...
