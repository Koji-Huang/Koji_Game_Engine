# UI Event 对象

---

## 背景

​	UI Event 是适用于 UI 系统的一种特殊事件, 这种事件的触发会随着 UI 父子级关系向子传递, 而触发器一般向最底层的 UI 对象传参让它沿着 Graphic 中预留有的 Event API 传参来触发各个 UI 的事件

---

## 结构

```Python
class UIEvent:
    def __init__(self, graphic_object: Label, *args, **kwargs):
        # 构造函数, 需要传入绑定的 UI 对象

    def track_check(self, *args, **kwargs):
        # 因为是基型, 没有具体的实现方法, 仅仅调用父类而已

    def track_run(self, *args, **kwargs):
        # 调用父类, 但是传入一个参数: graphic_object, 用于指定事件触发的 UI 对象

    def update_info(self, graphic_object=None, **kwargs):
        # 可以修改 graphic_object

    def delete(self):
        # 删除自己的同时也从父类上解除绑定

    def __copy__(self, copied: any = None):
        # 拷贝项虽然指向着同一个父类, 但是父类不绑定拷贝项


class Inspector(FatherInspector):
    def __init__(self, target: Basic):
        # 调用父类

    def check(self, **kwargs):
        # 调用父类

    def trigger(self, **kwargs):
        # 触发事件的同时向 UI 对象下传播事件参数

    def spread(self, **kwargs):
        # 调用 UI 对象的 event_spread

    def component_spread_args(self, args: dict = None, component=None):
        # 向下传参时用到的函数
```

---

## 运行流程

​	首先创建一个 UI 对象, 再创建 UIEvent 对象对它经行绑定, 下面是一个示例程序

```python
# Sample Event_UIEvent_Basic_1
import Engine
from GraphicComponent.UI import Label
from Event.UIEvent import Basic as Event
from random import randint

# 初始化引擎
Engine.init()

# 创建 UI 对象
Label_1 = Label((200, 100), (200, 200))


# 打印坐标
def print_pos(graphic_object: Label, *args, **kwargs):
    print(Label.get_pos())


# 改变坐标
def change_pos(graphic_object: Label, *args, **kwargs):
    Label.get_pos((randint(0, 800), randint(0, 600)))


# 创建事件对象
Event_print = Event(Label_1)
Event_change = Event(Label_1)

# 改变触发函数
Event_print.track_function = print_pos
Event_change.track_function = change_pos

# 向系统添加 UI 对象
Engine.GraphicManager.component_add(Label_1)

# 系统循环
Engine.loop()
```

