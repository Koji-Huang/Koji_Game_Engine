import pygame.font

from Graphic.UI.Label import Label

class Text(Label):
    text: str
    font: pygame.font.Font
    text_anti_aliasing: bool
    color: tuple[int, ...] or list[int, ...]

    def __init__(self, pos, size, text: str, font: pygame.font.Font, anti_alias: bool = True,
                 color: tuple[int, ...] or list[int, ...] = (255, 255, 255), *args, **kwargs):...

    def change_text_text(self, text: str):...

    def change_text_font(self, font: pygame.font.Font):...

    def change_text_color(self, color: tuple[int, ...] or list[int, ...] = (255, 255, 255)):...

    def change_text_antialiasing(self, antialiasing: bool):...

    def graph_draw(self) -> None:...