import pygame.font
from Functions import Surface
from GraphicComponent.UI.Label import Label


class Text(Label):
    def __init__(self, pos, size, text: str, font: pygame.font.Font, antialiasing: bool = True,
                 color: tuple[int, ...] or list[int, ...] = (255, 255, 255), *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)
        self.text = text
        self.font = font
        self.text_antialiasing = antialiasing
        self.color = color
        self.graph_draw()

    def change_text_text(self, text: str):
        self.graph_active = True
        self.text = text

    def change_text_font(self, font: pygame.font.Font):
        self.graph_active = True
        self.font = font

    def change_text_color(self, color: tuple[int, ...] or list[int, ...] = (255, 255, 255)):
        self.graph_active = True
        self.color = color

    def change_text_antialiasing(self, antialiasing: bool):
        self.graph_active = True
        self.text_antialiasing = antialiasing

    def graph_draw(self) -> None:
        super().graph_draw()
        if self.graph_active:
            Surface.cleaning_surface(self.graph_primer_surface)
            self.graph_primer_surface.blit(self.font.render(self.text, self.text_antialiasing, self.color), (0, 0))
