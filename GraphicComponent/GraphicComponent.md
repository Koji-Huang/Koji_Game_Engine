



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

### 示例程序

​	下面这个例子主要是针对与父子级关系编写的

```Python
from GraphicComponent.Root import Root

# 创建对象
Root_A = Root()
Root_B = Root()
Root_C = Root()

# 绑定父子级关系
Root_A.tree_add_son(Root_B)
Root_B.tree_add_son(Root_C)

# 输出父子级信息
print(f"Root_A.son: {Root_A.son}\nRoot_B.son:  {Root_B.son}")

# find_father, goto_father 函数检测
print(f"Root_C.find_root: {Root_C.tree_find_root}")
print(f"Root_C.goto_father(1): {Root_C.tree_goto_father(1)}")

# 将 Root_C 与 Root_B 解绑
Root_B.tree_remove_son(Root_C)

# find_father, goto_father 函数检测
print(f"Root_A.son: {Root_A.son}\nRoot_B.son:  {Root_B.son}")
print(f"Root_C.find_root: {Root_C.tree_find_root}")
print(f"Root_C.goto_father(1): {Root_C.tree_goto_father(1)}")

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

### 实例程序

```Python
from GraphicComponent.Surface import Surface

# 创建 Surface 对象
Surface_A = Surface((0, 0), (200, 200))
Surface_B = Surface((200, 0), (200, 200))
Surface_C = Surface((0, 0), (100, 100))

# 初始坐标
print(f"A.pos={A.pos()}, A.size={A.size()}, A.rect={A.rect()}")
print(f"B.pos={B.pos()}, B.size={B.size()}, B.rect={B.rect()}")
print(f"C.pos={C.pos()}, C.size={C.size()}, C.rect={C.rect()}")

# 改变 C 的坐标
print("Change Surface_C pos")
Surface_C.set_pos((100, 0))
print(f"C.pos={C.pos()}, C.size={C.size()}, C.rect={C.rect()}")

# 改变 C 的大小
print("Change Surface_C size")
Surface_C.set_size((300, 200))
print(f"C.pos={C.pos()}, C.size={C.size()}, C.rect={C.rect()}")

# 'is_covered 是否覆盖'函数功能检测
print("is_covered")
print(f"\tA to B:{A.is_covered(B)}")
print(f"\tA to C:{A.is_covered(C)}")
print(f"\tB to A:{B.is_covered(A)}")
print(f"\tB to C:{B.is_covered(C)}")
print(f"\tC to A:{C.is_covered(A)}")
print(f"\tC to B:{C.is_covered(B)}")

# 'is_crashed 是否碰撞'函数功能检测
print(f"is_crashed")
print(f"\tA to B:{A.is_crashed(B)}")
print(f"\tA to C:{A.is_crashed(C)}")
print(f"\tB to A:{B.is_crashed(A)}")
print(f"\tB to C:{B.is_crashed(C)}")
print(f"\tC to A:{C.is_crashed(A)}")
print(f"\tC to B:{C.is_crashed(B)}")
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

Graph 的示例程序与 MainWindows 的组成一个示例, 在下面

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

### 示例程序

```python
from GraphicComponent import MainWindows, Graphic
import pygame

# 创建窗口对象
windows = MainWindows((800, 600))

# 创建 Graphic 对象
Graphic_A = Graphic((0, 0), (400, 600))
Graphic_B = Graphic((100, 100), (300, 500))
Graphic_C = Graphic((100, 100), (300, 500))

# 绑定父子级关系
windows.tree_add_son(Graphic_A)
Graphic_A.tree_add_son(Graphic_B)
Graphic_B.tree_add_son(Graphic_C)

# 给各个 Graphic 对象上色, A 为红色, B 为绿色, C 为蓝色
Graphic_A.graph_primer_surface.fill((255, 0, 0))
Graphic_B.graph_primer_surface.fill((0, 255, 0))
Graphic_C.graph_primer_surface.fill((0, 0, 255))

# 让 C 状态设置为不活跃, 即不更新图像
Graphic_C.graph_active = False

# 让 B 状态为活跃, 即更新图像
Graphic_B.graph_active = True

for i in range(1, 100000):
    # 设置更新速度限制
    sleep(0.1)
    
    # 每十秒将 C 的活跃状态更新
    if i % 10 == 0:
        Graphic_C.graph_active = bool(Graphic_C.graph_active - 1)
    
    # 更新窗体和 Pygame
    windows.graph_update()
    pygame.event.get()
```

---

## <a id="UI">UI</a>

​	UI 库提供了一个简易的 UI 系统, 这里是已经实现了的 UI对象, 详细信息请看 UI.md

​	Label, Text, Label, Image

---