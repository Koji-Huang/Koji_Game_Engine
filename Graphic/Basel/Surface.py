from Graphic.Basel.Root import Root
from Function.coordinate import point_in_rect


class Surface(Root):
    def __init__(self, pos, size, *args, **kwargs):
        """
        Input position
        :param pos: the position of rect   x, y
        :param size: the size of the object
        :param kwargs: x, y, w, h, size, rel_pos
        """
        super().__init__(*args, **kwargs)
        self.set_pos(pos)
        self.set_size(size)

    def pos(self):
        return tuple((self.x, self.y))

    def size(self):
        return tuple((self.w, self.h))

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def set_size(self, size):
        self.w = size[0]
        self.h = size[1]

    # noinspection PyTypeChecker
    def set_rect(self, rect):
        self.set_pos((rect[0], rect[1]))
        self.set_size((rect[2], rect[3]))

    def rect(self):
        return tuple((self.x, self.y, self.w, self.h))

    def real_pos(self):
        pos = (0, 0)
        if self.father and isinstance(self.father, Surface):
            pos = self.father.real_pos()
        return tuple((pos[0] + self.x, pos[1] + self.y))

    def real_size(self):
        size = (0, 0)
        if self.father and isinstance(self.father, Surface):
            size = self.father.real_pos()
        size[0] += self.w
        size[1] += self.h
        return size

    def real_rect(self):
        rect = [0, 0, 0, 0]
        if self.father and isinstance(self.father, Surface):
            rect = list(self.father.real_rect())
        rect[0] += self.x
        rect[1] += self.y
        rect[2] = self.w
        rect[3] = self.h
        return tuple(rect)

    def is_covered(self, another=None):
        """
        another ∪ self == self
        Is This Object total be covered by another
        :param another:  object
        :return:
        """
        if another:
            return (self.x > another.x) and (self.y < another.y) \
                and (self.x + self.w < another.x + another.w) \
                and (self.y + self.h < another.y + another.h)
        else:
            return False

    def is_crash(self, another=None):
        """
        self ∪ another != ∅
        Is self and another have any union position
        :param another:
        :return:
        """
        if another:
            return bool(point_in_rect((self.x, self.y), another.rect()) or
                        point_in_rect((self.x + self.w, self.y + self.h), another.rect()) or
                        point_in_rect((another.x + another.w, another.y), self.rect()) or
                        point_in_rect((another.x, another.y + another.h), self.rect())
                        )
        else:
            return False

    def scale(self, w: int, h: int):
        self.w = w
        self.h = h
        return None


    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Surface(self.pos(), self.size())
        else:
            copied: Surface
            copied.set_rect(self.rect())
        super().__copy__(copied)
        return copied


__dict__ = ['MainWindows']
