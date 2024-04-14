# Thread Running Machine

---

## 介绍

​	Thread Running Machine(简称 TRMachine), 是为了运行线程而存在的一套系统, 因为 TRMachine 实际上可以有很多个(但不建议这么做), 所以并没有叫做 Thread Running System. 它负责底层的功能

​	Thread Running Machine 需要绑定 Thread Manager 一起使用

```Python
class ThreadRunningMachine:
    # 主线程池
    MainThreadPool: ThreadPool
    # 循环线程池
    LoopThreadPool: ThreadPool
    # 紧急线程池
    ImmeThreadPool: ThreadPool
    # 停止线程池
    StopThreadPool: ThreadPool
    # 错误线程池
    ExceThreadPool: ThreadPool
    # 主循环的函数线程 (不是线程池也不是线程, 是 Python 的 Thread 对象 )
    loopProcess: processThread

    # 运行标志 - [0: 运行结束, 1: 正在运行, 2: 暂停, 3: 错误]
    runningStatus: int
    # 是否记录线程信息
    recordMode: bool
    # 绑定的 Thread Manager (向外提供API的管理对象) 对象, 这个参数由 Thread Manager 提供
    ThreadManager: ThreadManager

    def __init__(self):
        """
        构造函数
        """

    def start(self) -> None:
        """
        开始运行线程系统
        :return: None
        """

    def stop(self):
        """
        结束系统
        :return: None
        """

    def pause(self) -> None:
        """
        暂停系统
        :return:
        """

    def once(self) -> None:
        """
        运行一次线程池
        :return: any
        """

    def loop(self):
        """
        主循环函数
        :return: any
        """

    def info(self):
        """
        返回此 TRMcahine 的信息
        :return:
        """
    
    def clean_pool(self):
        """
        移除所有的线程
        """
    
    def get_all_pool(self):
        """
        获取所有的线程池
        """
```