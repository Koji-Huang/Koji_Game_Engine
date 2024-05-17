from typing import overload
from pygame import Surface
from .Label import Label


class Image(Label):
    layout_mode: int
    image_antialiasing: bool
    image_surface: Surface
    @overload
    def __init__(self, pos, size, image: str, alpha: int = 255, layout_mode=0,
                 antialiasing: bool = True, *args, **kwargs):...
    @overload
    def __init__(self, pos, size, image: Surface, alpha: int = 255, layout_mode=0,
                 antialiasing: bool = True, *args, **kwargs):...

    def change_image_object(self, image: str or Surface, layout_mode=0, antialiasing=True):
        ...

    def change_image_setting(self, alpha=255, layout_mode=0, antialiasing=True):
        ...

    def graph_draw(self):
        ...
