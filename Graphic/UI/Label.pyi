from Graphic.Basic.Graph import Graph


class Label(Graph):
    son: set[Graph]

    def __init__(self, pos, size, *args, **kwargs) -> None:...

    def set_color(self, color: tuple[int, ...] or list[int, ...]) -> None:...

