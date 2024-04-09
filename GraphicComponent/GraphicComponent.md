# Graphic Component 图像控件

---

## 介绍

​		图像控件是一整套严密的系统, 系统整体用严格的父子级关系来进行运动, 这个文件夹内存放的就是最基础的一些控件对象, 在这里会一口气介绍完所有的基础控件的类型与使用方法

---

## 目录

- [Root](#Root)
- [Surface](#Surface)
- [Graphic](#Graphic)
- [MainWindows](#MainWindows)
- [UI](#UI)

---

## <a id='Root'>Root</a>

​	Root 类 是所有控件类的父类, 实现的功能是:

  - 父子树与父子级操作

  - 对 Event 对象的管理和传递

  - 删除操作

  - ID 系统

    

    ```Python
    class Root:
        # 父对象
        father: Root
        # 绑定的事件
        event: dict[str:list[Event], ]
    	# 绑定事件的类型(用于快速匹配)
        event_type: set[any]
        # 绑定的子对象
        son: LinkedList
        # ID
        id: str
    
        def __init__(self, *args, **kwargs) -> None:
            # 构造函数, 无传入
    
        def update(self, *args) -> None:
            # 更新对象状态
    
        def __update__(self) -> None:
            # 更新子对象
    
        def tree_add_son(self, son: Root) -> None:
            # 添加子对象
    
        def tree_remove_son(self, son: Root) -> None:
            # 移除子对象
    
        def tree_find_root(self) -> Root:
            # 寻找最上层的父对象
    
        def tree_goto_father(self, general: int) -> Root:
            # 向上跳转一定层级的父对象并返回
    
        def event_add(self, event_type: int, event: Event, **kwargs) -> None:
            # 添加事件
    
        def event_remove(self, event_type: int, event: str or Event) -> None:
            # 移除事件
    
        def event_spread(self, event_name, **event_args):
            # 向下传递事件
    
        def event_check(self, event_object: Event, *args, **kwargs) -> bool:
            # 检查事件是否触发
    
        def event_run(self, event_object: Event, *args, **kwargs) -> any:
            # 运行事件
    
        def event_clean(self) -> None:
            # 向下清理多余的事件与类型
    
        def event_tree(self) -> list:
            # 返回一个列表, 内容是事件类型构成的树
    
        def event_value(self) -> list:
            # 返回一个列表, 内容是事件返回值构成的树
    
        def event_tree_update(self, another_set):
            # 向上更新事件树, 添加与移除事件都会触发该函数
    
        def delete(self)->None:
            # 删除自己(绑定的事件也会一同被删除)
    
        def delete_with_son(self)->None:
            # 删除自己和子类(绑定的事件也会一同被删除)
    
        def __copy__(self, copied: any = None):
            # 拷贝一个副本, 但是没有父类绑定着它
    ```

---

## <a id='Surface'>Surface</a>

​	Surface 类 实现的功能是坐标功能

```Python
from GraphicComponent.Root import Root

class Surface(Root):
    x: int
    y: int
    w: int
    h: int

    def __init__(self, pos:tuple or list, size: tuple or list, *args, **kwargs):
		# 构造函数

    def pos(self) -> tuple[int, int]:
        # 获取相对坐标

    def size(self) -> tuple[int, int]:
        # 获取控件大小

    def rect(self) -> tuple[int, int, int, int]:
        # 获取相对坐标去控件大小

    def set_pos(self, pos:tuple[int, int]) -> None:
        # 设置相对坐标

    def set_size(self, size:tuple[int, int]) -> None:
        # 设置控件大小

    def set_rect(self, rect:tuple[int, int, int, int]):
        # 设置相对坐标与控件大小

    def real_pos(self) -> tuple[int, int]:
		# 获取绝对坐标

    def real_size(self) -> tuple[int, int]:
        # 获取绝对控件大小

    def real_rect(self) -> tuple[int, int, int, int]:
        # 获取绝对坐标与绝对控件大小

    def is_covered(self, another: Surface = None) -> bool:
        # 判断当前控件是否被另一控件覆盖

    def is_crash(self, another: Surface = None)->bool:
        # 判断当前控件是否与另一控件碰撞
    
    def scale(self, w: int, h: int):
        # 缩放控件
```

---

## <a id='Graphic'>Graphic</a>

​	Graphic 类 实现的功能是图像的绘制 

```Python
class Graphic(Surface):
    # 控件是否活跃(需要重绘)
    graph_active: bool
	# 叠加图层
    graph_surface: pygame.Surface
    # 原始图层
    graph_primer_surface: pygame.Surface
    # 绘制保留的参数
    graph_kwargs: dict

    def __init__(self, pos, size, *args, **kwargs):
        # 构造函数

    def graph_check(self):
        # 检查控件是否活跃(子控件活跃则自己也活跃)

    def graph_update(self, *args, **kwargs):
        # 更新原始图层

    def graph_draw(self, *args, **kwargs):
        # 更新叠加图层
```

---

## <a id='MainWindows'>MainWindows</a>

​	MainWindows 类负责创建 Pygame 窗口并覆写了相关函数

```python
class MainWindows(Graphic):
	# 窗口的 Surface
    windows_surface: pygame.Surface

    def __init__(self, size: tuple[int, int], pygame_parament: tuple or list = (), *args, **kwargs):
    	# 构造函数, 在这里会创建窗口

    def graph_draw(self, *args, **kwargs):
    	# 刷新窗口

    def update(self, *args) -> None:
    	# 同时更新图像和事件

    def graph_update(self, *args, **kwargs):
    	# 绘制并刷新窗口

    def event_update(self):
    	# 更新 Pygame 事件
```

---

## <a id="UI">UI</a>

​	UI 库提供了一个简易的 UI 系统, 这里是已经实现了的 UI对象, 详细信息请看 UI.md

​	Label, Text, Label, Image

---