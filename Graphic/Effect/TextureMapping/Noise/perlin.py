import pygame
import numpy


def noise(surface: pygame.Surface, seed: int = 0, scale: float = 0.1, clamp: float = None, enable: bool = True):
    w = int(surface.get_width() * scale) + 2
    h = int(surface.get_height() * scale) + 2
    numpy.random.seed = seed
    _mapping = numpy.random.rand(w, h)
    surface_array = pygame.surfarray.pixels3d(surface)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            x1 = _mapping[int(x * scale)][int(y * scale)]
            x2 = _mapping[int(x * scale + 1)][int(y * scale)]
            y1 = _mapping[int(x * scale)][int(y * scale)]
            y2 = _mapping[int(x * scale)][int(y * scale + 1)]
            xx1 = x1 * (1 - x * scale % 1)
            xx2 = x2 * (x * scale % 1)
            yy1 = y1 * (1 - y * scale % 1)
            yy2 = y2 * (y * scale % 1)
            xxx1 = xx1 ** 2 + yy1 ** 2
            xxx2 = xx1 ** 2 + yy2 ** 2
            yyy1 = xx1 ** 2 + yy2 ** 2
            yyy2 = xx2 ** 2 + yy2 ** 2
            near_num = (x1 * xxx1 + x2 * xxx2 + y1 * yyy1 + y2 * yyy2) / 4
            color_num = tuple((int(near_num * 255), int(near_num * 255), int(near_num * 255)))

            if clamp:
                color_num = color_num * clamp + surface_array[x][y] * (1 - clamp)

            surface_array[x][y] = color_num
