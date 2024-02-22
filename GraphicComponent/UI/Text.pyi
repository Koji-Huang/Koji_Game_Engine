import pygame.font

from GraphicComponent.UI.Label import Label

class Text(Label):
    text: str
    font: pygame.font.Font
    antialias: bool
    color: tuple[int, ...] or list[int, ...]

    def __init__(self, pos, size, text: str, font: pygame.font.Font, antialias: bool = True,
                 color: tuple[int, ...] or list[int, ...] = (255, 255, 255), *args, **kwargs):...

    def change_text(self, text: str):...

    def change_font(self, font: pygame.font.Font):...

    def change_color(self, color: tuple[int, ...] or list[int, ...] = (255, 255, 255)):...

    def change_antialias(self, antialias: bool):...

    def render(self) -> None:...