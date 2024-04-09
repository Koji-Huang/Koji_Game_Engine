# Graphic Manager

---

## 介绍

​	这玩意建立了MainWindows的接口, 用起来更容易

```Python
class GraphicComponentManager:
    # MainWindows 对象
    windows: MainWindows
    # 是否开启 Debug 模式
    __debug_mode: bool
    # debug 工具
    debug: GraphicComponentDebug | None
        
    def __init__(self, mainWindowsObject: MainWindows = None, size: tuple[int, ...] = (800, 600), ):
        # 构造函数

    def general_info(self) -> dict:
        # 获取全局信息

    def component_type(self, start_component: Root = None) -> set[str | ...]:
        # 获取控件类型树

    def component_tree(self, start_component: Root = None) -> dict[set, ...]:
        # 获取控件树

    def component_find(self, id: str, start_component: Root = None) -> Root | None:
        # 查找控件

    def components_find(self, id: tuple[str, ...], start_component: Root = None) -> tuple[Root | None, ...]:
        # 查找大量控件

    def components_find_type(self, component_type: str, start_component: Root = None) -> tuple[Root, ...]:
        # 获取同一类型的控件

    def component_add(self, component: Root, father_component: Root = None) -> None:
        # 添加控件, 默认添加至根控件

    def components_add(self, component: tuple[Root, ...], father_component: Root =  None) -> None:
        # 添加大量控件

    def component_remove(self, target: str or Root) -> None:
        # 移除控件( ID 或 控件对象 )

    def components_remove(self, target: tuple[str or Root, ...]) -> None:
        # 移除大量控件

    def graphic_update(self) -> None:
        # 更新图像

    def event_get(self, pid: str, event_type: str, component: Root = None) -> Event | Root | str:
        # 在控件上查找图形事件类

    def event_remove(self, pid: str) -> None:
        # 在控件上移除图形事件类

    def event_add(self, event: Event, event_type: int = 0, father_component: Root = None) -> None:
        # 添加图形事件

    def event_tree(self, start_component: str | Root):
        # 图形事件树

    def event_id_tree(self, start_component: str | Root):
        # 图形事件PID树

    def event_type_tree(self, start_component: str | Root):
        # 图形事件类型树

    def event_update(self):
        # 更新事件

    def set_debug(self, enable: bool = None):
        # 设置 Debug 模式

    def update_component_event(self, component: Root, event_type: int, event: Event, *args, **kwargs) -> any:
        # 更新指定控件的指定图形事件

    def update_component_graphic(self, component: Root, *args, **kwargs) -> any:
       # 更新指定控件的图像


class GraphicComponentDebug:
    # 原本的图形更新函数
    __graphic_update_function: any
    # 插入的图形更新函数
    __graphic_insert_function: list
    # Debug 附属的控件
    __debug_component: Graphic
    # Debug 用的 Lable
    __debug_Label: Label
    # 是否将 Debug 信息显示在同一图层
    one_layer: bool = True
    # Debug 字体类型
    textType: TextType
    # Debug 框类型
    edgeType: EdgeType
    # Debug 数据显示的 MainWindows 对象
    windows: MainWindows
    # Debug 数据的 Alpha 显示效果
    info_alpha: int

    def __init__(self, component: Graphic, windows: MainWindows):
        # 构造函数

    def graphic_debug(self):
        # 图像 Debug

    def overwrite_add_graphic_function(self, function):
        # 添加图像 Debug 函数

    def graphic_update(self):
        # 更新 Debug 图像

    def graphic_debug_component(self, component: Graphic):
        # Debug 控件 (图像)

    def graphic_debug_single(self, component: Graphic):
        # Debug 单个控件 (图像)

    def overwrite_graphic_core(debug, enable: bool = True):
        # 覆盖 Graphic 的核心使它可以插入函数
        
    def event_debug(self):
        # 未实现

    def debug(self):
        # debug 事件与图像
```