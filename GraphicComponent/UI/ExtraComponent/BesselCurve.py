import pygame

from GraphicComponent.UI.Label import Label
import Functions as F


class BesselCurve(Label):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)
        # the width of line
        self.line_size = 2
        # the color of line
        self.line_color = (255, 255, 255, 255)
        # the start line ( x, y )
        self.line_start_line = tuple()
        # the end line ( x, y )
        self.line_end_line = tuple()
        # how much times draw once
        self.line_drawing_accuracy = 8

    def set_point(self, start_line: tuple[tuple[int, ...], ...], end_line: tuple[tuple[int, ...], ...]):
        self.line_start_line = start_line
        self.line_end_line = end_line

    def set_line_size(self, size: int):
        self.line_size = size

    def set_line_color(self, color: tuple[int, int, int, int]):
        self.line_color = color

    def draw_line(self, show_control_points: bool = True, show_points: bool = False):
        if self.line_start_line and self.line_end_line:
            self.graph_primer_surface.fill((0, 0, 0, 0))
            self.graph_primer_surface.set_colorkey((0, 0, 0, 0))
            if show_control_points:
                pygame.draw.circle(self.graph_primer_surface, (255, 0, 0, 255), self.line_start_line[0], 10)
                pygame.draw.circle(self.graph_primer_surface, (255, 125, 125, 255), self.line_start_line[1], 10)
                pygame.draw.circle(self.graph_primer_surface, (0, 255, 0, 255), self.line_end_line[0], 10)
                pygame.draw.circle(self.graph_primer_surface, (125, 255, 125, 255), self.line_end_line[1], 10)
            points: list[tuple[int, ...]] = self.make_line()
            pygame.draw.lines(self.graph_primer_surface, self.line_color, False, points, width=self.line_size)
            if show_points:
                for i in points:
                    pygame.draw.circle(self.graph_primer_surface, [255 - k for k in self.line_color],
                                       i, int(self.line_size / 3))
                    pygame.draw.circle(self.graph_primer_surface, self.line_color, i, int(self.line_size / 5))

    def make_line(self, start_line=None, end_line=None, accuracy=None):
        if start_line is None:
            start_line = self.line_start_line
        if end_line is None:
            end_line = self.line_end_line
        if accuracy is None:
            accuracy = self.line_drawing_accuracy
        points = list()
        for percent in (k / accuracy for k in range(accuracy + 1)):
            start_point = F.mix_point(start_line[0], start_line[1], percent)
            end_point = F.mix_point(end_line[0], end_line[1], percent)
            points.append(F.mix_point(start_point, end_point, percent))
        return tuple(points)
