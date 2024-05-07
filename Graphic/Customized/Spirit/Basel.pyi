from Graphic.Customized.Animation import SurfaceAnimation
from Graphic.Basic import Graph


class Spirit(Graph):
    # 当前形态的键
    _spirit_now: str
    # 储存的的形态
    _spirit_form: tuple[Animation]
    # key: Customized
    _spirit_animation: dict[str, [Animation or None]]

    def graph_draw(self, *args, **kwargs):
        pass

    def add_form(self, form: str, animation: Animation) -> None:
        pass

    def set_form(self, form: str) -> None:
        pass

    def del_form(self, form: str) -> None:
        pass

    def get_form(self, form: str) -> Animation:
        pass