import pygame
from Graphic import Graphic


class EdgeType:
    # 1: solid  2: hollow 3:
    dashed: bool = False
    solid: bool = True
    width: float = 3
    color: tuple = (255, 0, 0, 255)

    def __init__(self, width: float = 3, solid: bool = 1, dashed: bool = False, color: tuple = (255, 0, 0, 255)):
        ...

    def draw_border(self, surface: pygame.Surface, area: tuple[int, ...], alpha=255):
        ...

    def draw_single_edge(self, surface: pygame.Surface, start: tuple, end: tuple, alpha=255):
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


def mark_component(component: Graphic, edge_type=None, text_type=None,
                   area: tuple[int, ...] = None, text_inside: bool = True, alpha: int = 255):
    ...

