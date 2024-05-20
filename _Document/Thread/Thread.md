# Thread

---

## 介绍

​	Thread 对象是为了线程系统创造出来的基础对象, 这里会讲 Thread (基础线程类) 和 FunctionThread (单函数线程类)

---

## Thread

​	Thread 对象非常简洁

```Python
class Thread:
    # 函数名称
    threadName: str
    # 函数线程等级
    threadLevel: str
    # 动态参数
    kwargs: dict
    # 线程 ID
    pid: str


    def __init__(self, threadLevel: str = 'undefined', threadName: str = 'undefined', **kwargs):
        # 构造函数

    def start(self, **kwargs) -> None:
        # 运行此线程

    def info(self) -> dict:
        # 获取此线程的信息

    def result(self) -> dict:
        # 获取此线程的运行结果, 相当于一个输出API

    def __del__(self) -> None:
        # 删除此线程

    def __call__(self, **kwargs) -> any:
        # 运行此线程, 调用 start()

    def __copy__(self, another: Thread = None) -> Thread:
        # 复制此线程, 但不加入线程池中

    def __getattr__(self, item):
        # 重载函数, 可以获取 Thread.kwargs 里的参数
```

---

## FunctionThread

​	FunctionThread 为运行函数提供了一个建议的接口, 它会在 start 时调用那条函数

```Python
class FunctionThread(Thread):
	# 调用的函数
    function: ()
    # 向调用函数传参的值
    function_kwargs: dict
    # 函数返回值
    function_return: any

    def __init__(self, function: (), function_kwargs: dict = None, threadLevel: str = 'undefined', **kwargs):
        # 构造函数

    def start(self, **kwargs) -> None:
        # 运行函数

    def info(self):
        # 返回值中增加了 function(调用函数) 和 result(函数返回值) 两项

    def __copy__(self, another: FunctionThread = None):
        # 继承父类

    def result(self):
        # 返回函数的返回值

    def __getattr__(self, item):
        # 重载函数
       
```