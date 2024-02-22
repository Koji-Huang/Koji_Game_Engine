import pygame.font
from Functions import Surface
from GraphicComponent.UI.Label import Label


class Text(Label):
    def __init__(self, pos, size, text: str, font: pygame.font.Font, antialias: bool = True,
                 color: tuple[int, ...] or list[int, ...] = (255, 255, 255), *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)
        self.text = text
        self.font = font
        self.antialias = antialias
        self.color = color
        self.render()

    def change_text(self, text: str):
        self.graph_active = True
        self.text = text
        self.render()

    def change_font(self, font: pygame.font.Font):
        self.graph_active = True
        self.font = font
        self.render()

    def change_color(self, color: tuple[int, ...] or list[int, ...] = (255, 255, 255)):
        self.graph_active = True
        self.color = color
        self.render()

    def change_antialias(self, antialias: bool):
        self.graph_active = True
        self.antialias = antialias
        self.render()

    def render(self) -> None:
        Surface.cleaning_surface(self.graph_primer_surface)
        self.graph_primer_surface.blit(self.font.render(self.text, self.antialias, self.color), (0, 0))
