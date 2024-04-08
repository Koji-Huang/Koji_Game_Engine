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
        event: dict[str:list[Event], ...]
    	# 绑定事件的类型(用于快速匹配)
        event_type: set[any]
        # 绑定的子对象
        son: LinkedList
        # ID
        id: str
    
        def __init__(self, *args, **kwargs) -> None:...
            # 构造函数, 无传入
    
        def update(self, *args) -> None:...
            # 更新对象状态
    
        def __update__(self) -> None:...
            # 更新子对象
    
        def tree_add_son(self, son: Root) -> None:...
            # 添加子对象
    
        def tree_remove_son(self, son: Root) -> None:...
            # 移除子对象
    
        def tree_find_root(self) -> Root:...
            # 寻找最上层的父对象
    
        def tree_goto_father(self, general: int) -> Root:...
            # 向上跳转一定层级的父对象并返回
    
        def event_add(self, event_type: int, event: Event, **kwargs) -> None:...
            # 添加事件
    
        def event_remove(self, event_type: int, event: str or Event) -> None:...
            # 移除事件
    
        def event_spread(self, event_name, **event_args):...
            # 向下传递事件
    
        def event_check(self, event_object: Event, *args, **kwargs) -> bool:...
            # 检查事件是否触发
    
        def event_run(self, event_object: Event, *args, **kwargs) -> any:...
            # 运行事件
    
        def event_clean(self) -> None:...
            # 向下清理多余的事件与类型
    
        def event_tree(self) -> list:...
            # 返回一个列表, 内容是事件类型构成的树
    
        def event_value(self) -> list:...
            # 返回一个列表, 内容是事件返回值构成的树
    
        def event_tree_update(self, another_set):...
            # 向上更新事件树, 添加与移除事件都会触发该函数
    
        def delete(self)->None:...
            # 删除自己(绑定的事件也会一同被删除)
    
        def delete_with_son(self)->None:...
            # 删除自己和子类(绑定的事件也会一同被删除)
    
        def __copy__(self, copied: any = None):...
            # 拷贝一个副本, 但是没有父类绑定着它
    ```

---

## <a id='Surface'>Surface</a>

---

## <a id='Graphic'>Graphic</a>

---

## <a id='MainWindows'>MainWindows</a>

---

## <a id="UI">UI</a>

---