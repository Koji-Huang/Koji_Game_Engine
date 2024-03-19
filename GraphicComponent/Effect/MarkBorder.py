import pygame


class EdgeType:
    # 1: solid  2: hollow 3:
    dashed: bool = False
    solid: bool = True
    width: float = 3
    color: tuple = (255, 0, 0, 255)

    def __init__(self, width: float = 3, solid: bool = 1, dashed: bool = False, color: tuple = (255, 0, 0, 255)):
        self.width = width
        self.solid = solid
        self.dashed = dashed
        self.color = color

    def draw_border(self, surface: pygame.Surface, area: tuple[int, ...]):
        # top
        self.draw_single_edge(surface, (area[0] + self.width, area[1]), (area[0] + area[2], area[1]))
        # left
        self.draw_single_edge(surface, (area[0], area[1]), (area[0], area[1] + area[3]))
        # right
        self.draw_single_edge(surface, (area[0] + area[2], area[1]), (area[0] + area[2], area[1] + area[3]))
        # button
        self.draw_single_edge(surface, (area[0], area[1] + area[3]), (area[0] + area[2] + self.width, area[1] + area[3]))

    def draw_single_edge(self, surface: pygame.Surface, start: tuple, end: tuple):
        inverse_color = list(255 - i for i in self.color)
        inverse_color[3] = 255

        if start[0] - end[0] == 0:
            tmp_surface = pygame.Surface((abs(start[0] - end[0]) + self.width, abs(start[1] - end[1]))).convert_alpha()

        else:
            tmp_surface = pygame.Surface((abs(start[0] - end[0]), abs(start[1] - end[1]) + self.width)).convert_alpha()

        tmp_surface.fill(self.color)

        # if self.dashed:
        #     segments_number = int((abs(start[0] - end[0]) + abs(start[1] - end[1])) / self.width / 2)
        #     for percent in [i / segments_number for i in range(segments_number)]:
        #         x = int(start[0] * (1 - percent) + end[0] * percent)
        #         y = int(start[1] * (1 - percent) + end[1] * percent)
        #         pygame.draw.rect(tmp_surface, inverse_color, (x, y, self.width, self.width))
        #
        # if not self.solid:
        #     pygame.draw.line(tmp_surface, inverse_color, start, end,
        #                      int(self.width * 0.6) if self.width * 0.6 < 4 else 4)
        #
        # if not self.dashed or not self.solid:
        #     tmp_surface.set_colorkey(inverse_color)

        draw_pos = (min(start[0], end[0]), min(start[1], end[1]))

        surface.blit(tmp_surface, draw_pos, special_flags=0)


class TextType:
    size: int
    text: str
    font: pygame.font.Font
    surface: pygame.Surface
    color: tuple = (255, 0, 0, 255)

    def __init__(self, size: int = 15, text: str = '', font: pygame.font.Font = None, color: tuple = (255, 0, 0, 255)):
        self.size = size
        self.text = text
        self.color = color
        if font is None:
            self.font = pygame.font.SysFont('arial', size)
        self.change_text(self.text)

    def draw(self, surface: pygame.Surface, pos: tuple[int, ...]):
        surface.blit(self.surface, pos)

    def change_text(self, text: str) -> None:
        self.text = text
        self.surface = self.font.render(self.text, False, self.color, (0, 0, 0, 0))


def mark_component(component, edge_type=None, text_type=None, area: tuple[int, ...] = None):
    if text_type is not None:
        text_type.draw(component.graph_primer_surface, (area[0], area[1] - text_type.size))
    if area is None:
        area = (0, 0, component.graph_primer_surface.get_width(), component.graph_primer_surface.get_height())
    if (edge_type is None and text_type is None) or edge_type is not None:
        if edge_type is None:
            edge_type = EdgeType()
        edge_type.draw_border(component.graph_primer_surface, area)
