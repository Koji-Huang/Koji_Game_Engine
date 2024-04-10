
# 事件系统

---
## 背景
因为线程系统那庞大的而混乱的系统体系, 我需要一个更加简单, 容易的接口来运行内容, 所以开发了事件系统
事件系统的根本目的是在于给开发者提供一个简易的接口来编写事件

---

## 数据类型

### 	Event

​		事件对象, 负责实现事件的检查与运行

### 	Inspector

​		触发器对象, 负责参数的获取与传入传出

-----

## 结构

```python
class BasicEvent:
    """
    基础事件对象, 提供模板
    """
    
    event_name: str
        # 事件的名称 (可改)
    track_function: function
        # 触发的函数
    track_args: dict
        # 触发函数时附带的参数
    event_type: int or any
        # 事件类型, 一般定义为 int
    event_type_name: str
        # 事件类型名称
    id: str 
        # 事件 ID

    def __init__(self, *args, **kwargs):
        # 构造函数
        
    def track_check(self,  *args, **kwargs) -> any:
        # 检查事件是否触发, 一般传出 bool, 传出其他参数时请将否设置为 False 或 None
        
    def track_run(self, *args, **kwargs) -> any:
        # 运行事件(无论是否触发), 不过有些事件没触发的情况下可能产生错误

    def update_info(self, **kwargs) -> None:
        # 提供一个更新附带参数的接口, 也可以自定义为更改类参数

    def update_kwargs(self, **kwargs) -> dict:
        # 更新参数用来传递
    
    def delete(self):
        # 删去此事件时会调用的函数, 这个函数会将自己从事件系统中抹除

    def __copy__(self, copied: any = None) -> Event:
        # 拷贝此事件返回副本


class Inspector:
    """
    基础触发器, 提供模板
    """
    target_event_class = BasicEvent
    	# 触发对象的类型, 若类型不符无法初始化触发器
    target_event: BasicEvent
        # 触发的对象

    def __init__(self, target: BasicEvent):
        # 构造函数

    def check(self, **kwargs):
        # 检查事件是否触发

    def trigger(self, **kwargs):
        # 触发事件
```

---

## 运行流程

​	首先, 你需要创造一个 Event 对象, 此时系统会查询对应的 Inspector 与其对接, 你也可以选择自己创建一个 Inspector 对象, Inspector 对象是可以被查询的, 有些 Event 可以不帮定 Inspector 对象(例如 UIEvent 中的), 在系统更新事件系统时, 会遍历所有储存的 Inspector 对象, 并检查是否有触发的对象, 有的话就触发对应的事件.

```Python
# Sample Event_Basic_1
import Engine
from Event import BasicEvent as Event

# 初始化引擎
Engine.init()

# 创建事件对象
A = Event()
Event.name = "Sample"


# 触发的函数
def say_hello(*args, **kwargs):
    print("Hello World!", *args, **kwargs)

    
# 触发检查函数
def check(i: int = None, *args, **kwargs):
    # 父类如果返回否, 则此事件为否, 实际上父类一直都为 True, 这么写是为了让大家明白一般的触发检查函数一般也具备父子级关系
    if super().check() is False:
        return False
    else:
        # 容错写法
        if i is None:
            return False
        return i % 10 == 0

# 改变触发的函数
A.track_function = say_hello
    

# 获取触发器
Inspector_A = Engine.get_inspector(A)


# 如果触发器检擦通过, 触发事件
for i in range(1, 100000):
    if Inspector_A.check(i) == True:
        Inspector_A.trigger()

```

