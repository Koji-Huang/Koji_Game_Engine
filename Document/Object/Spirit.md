# Spirit  Class Struct

​	_精灵类的类构造_

---

精灵类是指具有活动功能, 绑定有多个画面效果的 `Graph.Graphic` 对象, 它具有独立的特性

```python
from Graphic import Customized, Graph


class Spirit(Graph):
    # 当前的形态
    _spirit_form_name: tuple[Customized]
    # key: Customized
    _spirit_animation: dict[str, [Customized | None]]

    def graph_draw(self, *args, **kwargs):
        # 覆写父类函数
        pass

        def set_form(self, form: str):

            pass

    def set_animation(self, form: str, animation: Customized) -> None:
        pass

    def del_animation(self, form: str) -> None:
        pass

    def get_animation(self, form: str) -> Customized:
        pass

```

