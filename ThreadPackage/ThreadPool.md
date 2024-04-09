# Thread Pool

---

## 介绍

​	线程池对象是为了管理线程的对象, 它可以按线程等级高低与进出顺序来运行线程

```Python
class ThreadPool:
    # 存储的线程对象 格式: {线程等级: 线程链表[线程对象] | ...}
    threads: dict[str: LinkedList[Thread], ...]
    # 线程等级排序
    threadLevel: set[str]
    # 线程池名称
    name: str
    # 线程池
    id: str

    def __init__(self) -> None:
        """
        构造函数
        """

    def add(self, thread: Thread) -> None:
        """
        添加线程
        :return: 无
        """

    def remove(self, pid: int or Thread, level: str = None) -> bool:
        """
        移除一个线程
        :param pid: 线程对象或者PID
        :param level: 线程等级
        :return: 是否移除成功
        """

    def finding(self, pid: str, level: str = None) -> Union[Thread, ...]:
        """
        用PID从线程池中查找线程对象
        :param pid: PID
        :param level: 线程等级
        :return: 线程对象或者一无所有
        """

    def show(self) -> None:
        """
        在控制台上输出所有线程的信息
        :return: 无
        """

    def isEmpty(self) -> bool:
        """
        线程池是不是空了
        :return: bool
        """

    def extract(self) -> Thread:
        """
        获取一个线程对象并从线程池中去除
        :return: 线程对象
        """

    def insert(self, thread: Thread, index: int = 0):
        """
        插入一个线程对象
        :param thread: 线程对象
        :param index: 在同线程等级中要插入的位置, 默认为头, -1 与 超出范围 为尾
        :return: 无
        """

    def clean(self):
        """
        去除空闲的线程等级与线程线
        :return: 
        """

    def display(self, **format_kwargs):
        """
        打印线程池的详细信息
        :return:无
        """

    def info(self):
        """
        返回线程池的详细信息
        :return:
        """

    def __iter__(self) -> iter:
        """
        由所有线程对象组成的迭代器
        :return: 迭代器对象
        """

    def __len__(self):
        """
        返回当前有多少个线程等级
        :return:
        """
```