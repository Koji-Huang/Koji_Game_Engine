from GraphicComponent import Graphic


class Label(Graphic):
    son: set[Graphic]

    def __init__(self, pos, size, *args, **kwargs) -> None:...

    def set_color(self, color: tuple[int, ...] or list[int, ...]) -> None:...

