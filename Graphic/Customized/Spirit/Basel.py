from Graphic.Basic import Graph
import Graphic.Customized.Animation.AbstractAnimation as Animation


class Spirit(Graph):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)
        self._spirit_now = 'undefined'
        self._spirit_form = tuple()
        self._spirit_animation = dict()
        self.get_form = self._spirit_animation.get

    def graph_draw(self, *args, **kwargs):
        if self._spirit_now is not 'undefined':
            self.son = list()

        draw_animation = self._spirit_animation.get(self._spirit_now)
        if draw_animation is not None:
            draw_animation: Animation
            draw_animation.graph_update()
            self.son = [draw_animation,]

        super().graph_draw(*args, **kwargs)
        return

    def add_form(self, form, animation) -> None:
        self._spirit_animation[form] = animation
        self._spirit_form += (form, )

    def set_form(self, form) -> None:
        if form in self._spirit_form:
            self._spirit_now = form

    def del_form(self, form) -> None:
        self._spirit_form -= (form, )
        self._spirit_animation.pop(form)
        if form == self._spirit_now:
            self._spirit_now = 'undefined'
