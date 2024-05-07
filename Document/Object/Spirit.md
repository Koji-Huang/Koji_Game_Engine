# Spirit  Class Struct

​	_精灵类的类构造_

---

## 基类 Spirit

​	精灵类是指具有活动功能, 绑定有多个画面效果的 `Graph.Graphic` 对象, 它具有独立的特性

```python
from Graphic.Customized.Animation import SurfaceAnimation
from Graphic.Basic import Graph


class Spirit(Graph):
    # 当前的形态
    _spirit_form_name: tuple[Animation]
    # key: Customized
    _spirit_animation: dict[str, [Animation | None]]

    def spirit_update(self, *args, **kwargs):

    # 更新精灵对象包含的事件 (不包括图像)

    def graph_draw(self, *args, **kwargs):
        # 覆写父类函数
        pass

    def set_form(self, form: str, animation: Animation) -> None:
        pass

    def del_form(self, form: str) -> None:
        pass

    def get_form(self, form: str) -> Animation:
        pass

```

---

## 事件 Spirit

```python
from Graphic.Customized.Spirit import Basel

class Spirit(Basel):
    # 默认的事件
    _default_event: tuple[str]
    # 载入的事件
    _loaded_event: tuple[str]

    def spirit_update(self, *args, **kwargs):
        # 覆写父类以实现特性

    def set_event(self, form: str, animation: Animation) -> None:
        pass

    def del_event(self, form: str) -> None:
        pass

    def get_event(self, form: str) -> Animation:
        pass
```

---

## 脚本 Spirit

```python
from Graphic.Customized.Spirit import Basel

class Spirit(Basel):
    # 默认的事件
    _default_spirit: tuple[str]
    # 载入的事件
    _loaded_spirit: tuple[str]

    def spirit_update(self, *args, **kwargs):
        # 覆写父类以实现特性

    def set_spirit(self, form: str, animation: Animation) -> None:
        pass

    def del_spirit(self, form: str) -> None:
        pass

    def get_spirit(self, form: str) -> Animation:
        pass
```

