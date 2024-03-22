from GraphicComponent.UI import Label


class Camera(Label):
    son: list[Label, ...]
    scaleRatio: float
    relative_pos: tuple[int, int]
    virtualLabel: Label

    def __init__(self, pos, size, *args, **kwargs):
        """

        """

    def tree_add_son(self, son) -> None:
        """

        """

    def tree_remove_son(self, son) -> None:
        """

        """

    def scale(self, multiple: float):
        """

        """

    def move(self, relative: tuple[int, int]):
        """

        """