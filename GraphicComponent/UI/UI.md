# UI 控件

---

## 目录

### 	[Label](#Label)

### 	[Text](#Text)

### 	[Image](#Image)

### 	[Buttom](#Buttom)

---

## <a id='Label'>Label</a>

​	Label 类 提供了基础的 UI 控件的函数(并且重载只用覆写 Label 就可以覆写整个 UI 系统)

```Python
class Label(Graphic):
    # 规定 Label 类的子类为 Graphic 对象
    son: set[Graphic]

    def __init__(self, pos, size, *args, **kwargs) -> None:
        # 构造函数

    def set_color(self, color: tuple[int, ...] or list[int, ...]) -> None:
        # 用实色填充
```

### 示例程序

```Python
from GraphicComponent import MainWindows
from GraphicComponent.UI import Label

# 创建窗体
windows = MainWindows((800, 600))

# 创建 Label 对象
Label_R = Label((10, 10), (100, 100))
Label_G = Label((120, 10), (100, 100))
Label_B = Label((230, 10), (100, 100))
Label_A = Label((0, 100), (340, 20))

# 给 Label 对象上色
Label_R.set_color((255, 0, 0))
Label_G.set_color((0, 255, 0))
Label_B.set_color((0, 0, 255))
Label_R.set_color((255, 255, 255, 125))

# 向窗体添加 Label 对象
windows.tree_add_son(Label_R)
windows.tree_add_son(Label_G)
windows.tree_add_son(Label_B)
windows.tree_add_son(Label_R)

# 显示更新
while True:
    windows.update()
```

---

## <a id="Text">Text</a>

​	Text 类 能在屏幕上显示文字

```Python
class Text(Label):
    # 当前显示的文字
    text: str
    # 渲染用到的 Pygame.Font 对象
    font: pygame.font.Font
    # 抗锯齿
    antialias: bool
    # 字体颜色
    color: tuple[int, ...] or list[int, ...]

    def __init__(self, pos, size, text: str, font: pygame.font.Font, antialias: bool = True,
                 color: tuple[int, ...] or list[int, ...] = (255, 255, 255), *args, **kwargs):
        # 构造函数

    def change_text_text(self, text: str):
        # 改变显示的文本

    def change_text_font(self, font: pygame.font.Font):
        # 改变字体

    def change_text_color(self, color: tuple[int, ...] or list[int, ...] = (255, 255, 255)):
        # 改变字体的颜色

    def change_text_antialiasing(self, antialiasing: bool):
        # 改变抗锯齿选项

    def graph_draw(self) -> None:
        # 重载父类
```

---

## <a id="Image">Image</a>

​	Image 类 用于显示图像

​	layout_mode: 

  		0. 保持图像原比例缩放
  		1. 强制缩放至控件比例
  		2. 不进行缩放直接绘制

```Python
class Image(Label):
    # 布局模式
    layout_mode: int
    # 缩放是否抗锯齿
    antialiasing: bool
    # 图像载入的 Surface
    image_surface: pygame.Surface
        
    def __init__(self, pos, size, image: str | pygame.Surface, alpha: int = 255, layout_mode=0,
                 antialiasing: bool = True, *args, **kwargs):
		# 构造函数, 注意: image 不仅可以是文件路径, 也可以是pygame.Surface 实例, 这是个调用, 并不会产生新的 Surface 对象

    def change_image_object(self, image: str | pygame.Surface):
    	# 改变图像
    
    def change_image_setting(self, alpha=255, layout_mode=0, antialiasing=True):
        # 设置图像属性
        
    def graph_draw(self):
        # 重载父类函数
```

---

## <a id="Buttom">Buttom</a>

​	按钮对象, 正在编写 Event 结构, 暂不做定性描述