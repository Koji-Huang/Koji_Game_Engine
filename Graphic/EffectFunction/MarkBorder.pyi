import pygame
from Graphic.Basel import Graph


class EdgeType:
    #  2: hollow 3:
    dashed: bool = False
    width: float = 3
    color: tuple = (255, 0, 0, 255)
    save: dict[bool, [dict[bool, [dict[int, [pygame.Surface]]]]]]
    # vertical - dashed - edge length - edge

    def __init__(self, width: float = 3, solid: bool = 1, dashed: bool = False, color: tuple = (255, 0, 0, 255)):
        ...

    def draw_border(self, surface: pygame.Surface, area: tuple[int, ...], alpha=255):
        ...

    def draw_single_edge(self, surface: pygame.Surface, start: tuple, end: tuple, alpha=255, vertical_direction: bool = True):
        ...


class TextType:
    size: int
    text: str
    saved: dict[str, [pygame.Surface]]
    font: pygame.font.Font
    surface: pygame.Surface
    color: tuple = (255, 0, 0, 255)

    def __init__(self, size: int = 15, text: str = '', font: pygame.font.Font = None, color: tuple = (255, 0, 0, 255)):
        ...

    def draw(self, surface: pygame.Surface, pos: tuple[int, ...]):
        ...

    def change_text(self, text: str) -> None:
        ...


def mark_component(component: Graph, edge_type=None, text_type=None,
                   area: tuple[int, ...] = None, text_inside: bool = True, alpha: int = 255):
    ...


