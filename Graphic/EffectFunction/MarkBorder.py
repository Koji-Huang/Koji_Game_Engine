import pygame
from DataType.Generic.LinkedList import LinkedList


class EdgeType:
    def __init__(self, width: float = 1, dashed: bool = False, color: tuple = (0, 255, 230, 255)):
        self.width = width
        self.dashed = dashed
        self.color = color
        self.edges = LinkedList()
        self.save = dict()
        for vertical in [True, False]:
            self.save[vertical] = dict()
            for dashed in [True, False]:
                self.save[vertical][dashed] = dict()

    def draw_border(self, surface: pygame.Surface, area: tuple[int, ...], alpha=255):
        # top
        self.draw_single_edge(surface, (area[0] + self.width, area[1]),
                              (area[0] + area[2], area[1]), alpha)
        # left
        self.draw_single_edge(surface, (area[0], area[1]),
                              (area[0], area[1] + area[3]), alpha)
        # right
        self.draw_single_edge(surface, (area[0] + area[2], area[1]),
                              (area[0] + area[2], area[1] + area[3]), alpha)
        # button
        self.draw_single_edge(surface, (area[0], area[1] + area[3]),
                              (area[0] + area[2] + self.width, area[1] + area[3]), alpha)

    def draw_single_edge(self, surface: pygame.Surface, start: tuple, end: tuple, alpha=255, vertical_direction: bool = True):

        cost = (end[0] - start[0], end[1] - start[1])
        length = abs(cost[0]) + abs(cost[1])
        if self.save[vertical_direction][self.dashed].get(length):
            surface.blit(self.save[vertical_direction][self.dashed].get(length), start)
            return
        tmp_surface = pygame.Surface((cost[0] + 1, cost[1] + 1))

        if self.dashed:
            segments_number = int((abs(start[0] - end[0]) + abs(start[1] - end[1])) / self.width / 2)
            piece = 1 / segments_number
            for percent in [i / segments_number for i in range(int(segments_number))][::3]:
                x = int(start[0] * (1 - percent) + end[0] * percent)
                y = int(start[1] * (1 - percent) + end[1] * percent)
                xx = int(start[0] * (1 - percent - piece) + end[0] * (percent + piece))
                yy = int(start[1] * (1 - percent - piece) + end[1] * (percent + piece))
                pygame.draw.line(surface, self.color, (x, y), (xx, yy), int(self.width))
                pygame.draw.line(tmp_surface, self.color, (x - start[0], y - start[1]), (xx - start[0], yy - start[1]), int(self.width))
        else:
            pygame.draw.line(surface, self.color, start, end, int(self.width))
            pygame.draw.line(tmp_surface, self.color, (0, 0), cost, int(self.width))

        self.save[vertical_direction][self.dashed][length] = tmp_surface

    def add_edge(self, start, end, direction: bool = True):
        self.edges.append((start, end, direction))



class TextType:
    def __init__(self, size: int = 10, text: str = '', font: pygame.font.Font = None,
                 color: tuple = (0, 255, 230, 255)):
        self.size = size
        self.text = text
        self.color = color
        if font is None:
            self.font = pygame.font.SysFont('arial', size)
        self.saved = dict()
        self.change_text(self.text)

    def change_text(self, text: str) -> None:
        self.text = text
        if text in self.saved.keys():
            self.surface = self.saved[text]
        else:
            self.surface = self.font.render(self.text, False, self.color).convert_alpha()
            self.saved[text] = self.surface


def mark_component(component, edge_type=None, text_type=None,
                   area: tuple[int, ...] = None, text_inside: bool = True, alpha: int = 255):

    if area is None:
        area = (1, 1, component.graph_surface.get_width() - 2, component.graph_surface.get_height() - 2)
    if text_type is not None:
        text_type.surface.set_alpha(alpha)
        if text_inside:
            component.graph_surface.blit(text_type.surface, (area[0], area[1]))
        else:
            component.graph_surface.blit(text_type.surface, (area[0], area[1] - text_type.size))
    if (edge_type is None and text_type is None) or edge_type is not None:
        if edge_type is None:
            edge_type = EdgeType()
        edge_type.draw_border(component.graph_surface, area, alpha)
