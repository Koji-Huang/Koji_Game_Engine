from GraphicComponent.Root import Root

class Surface(Root):
    x: int
    y: int
    w: int
    h: int

    def __init__(self, pos:tuple or list, size: tuple or list, *args, **kwargs):...

    def pos(self) -> tuple[int, int]:...

    def size(self) -> tuple[int, int]:...

    def set_pos(self, pos:tuple[int, int]) -> None:...

    def set_size(self, size:tuple[int, int]) -> None:...

    def set_rect(self, rect:tuple[int, int, int, int]):...

    def rect(self) -> tuple[int, int, int, int]:...

    def real_pos(self) -> tuple[int, int]:...

    def real_size(self) -> tuple[int, int]:...

    def real_rect(self) -> tuple[int, int, int, int]:...

    def is_covered(self, another: Surface = None) -> bool:...

    def is_crash(self, another: Surface = None)->bool:...

    def scale(self, w: int, h: int):...
