from GraphicComponent.UI import Label


class Camera(Label):
    son: list[Label, ...]
    virtualLabel: Label
    camera_pos: tuple[int, int]
    camera_ratio: float

    def __init__(self, pos, size, bind_component: any = None, *args, **kwargs):
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

    def move_to(self, position: tuple[int, int]):
        """

        """