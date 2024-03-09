from pygame import Surface as _Surface


In_Range = lambda start, end, n: start <= n <= end


def In_Rect(x, w, n):
    return x <= n <= x + w


def Point_in_Rect(point, rect):
    return bool(In_Rect(rect[0], rect[2], point[0])
        and In_Rect(rect[1], rect[3], point[1]))


def Fix_Kwargs(kwargs, mix_in: dict):
    if mix_in:
        for name, value in mix_in.items():
            kwargs[name] = value
        pass


def Mix_Kwargs(kwargs, mix_in: dict):
    a = dict()
    Fix_Kwargs(a, kwargs)
    Fix_Kwargs(a, mix_in)
    return a


class Surface:
    @staticmethod
    def cleaning_surface(i: _Surface) -> None:
        i.fill((0, 0, 0, 0))
        i.set_colorkey((0, 0, 0, 0))

