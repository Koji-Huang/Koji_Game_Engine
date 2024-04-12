import pygame.font
from FunctionTools.graphic import cleaning_surface
from GraphicComponent.UI.Label import Label


class Text(Label):
    def __init__(self, pos, size, text: str, font: pygame.font.Font, antialiasing: bool = True,
                 color: tuple[int, ...] or list[int, ...] = (255, 255, 255), *args, **kwargs):
        self.text = text
        self.font = font
        self.text_antialiasing = antialiasing
        self.color = color
        super().__init__(pos, size, *args, **kwargs)

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
            cleaning_surface(self.graph_primer_surface)
            self.graph_primer_surface.blit(self.font.render(self.text, self.text_antialiasing, self.color), (0, 0))
