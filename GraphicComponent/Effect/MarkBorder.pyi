import pygame
from GraphicComponent import Graphic


class EdgeType:
    # 1: solid  2: hollow 3:
    dashed: bool = False
    solid: bool = True
    width: float = 3
    color: tuple = (255, 0, 0, 255)

    def __init__(self, width: float = 3, solid: bool = 1, dashed: bool = False, color: tuple = (255, 0, 0, 255)):
        ...

    def draw_border(self, surface: pygame.Surface, area:  tuple[int, ...]):
        ...

    def draw_single_edge(self, surface: pygame.Surface, start: tuple, end: tuple):
        ...


class TextType:
    size: int
    text: str
    font: pygame.font.Font
    surface: pygame.Surface
    color: tuple = (255, 0, 0, 255)

    def __init__(self, size: int = 15, text: str = '', font: pygame.font.Font = None, color: tuple = (255, 0, 0, 255)):
        ...

    def draw(self, surface: pygame.Surface, pos: tuple[int, ...]):
        ...

    def change_text(self, text: str) -> None:
        ...


def mark_component(component: Graphic, edge_type: EdgeType, text_type: TextType, area: tuple[int, ...] = None):
    ...


