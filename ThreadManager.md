# Thread Manager

---

## 介绍:

​	Thread Manager 是一个上层的接口, 用于控制和管理 TRMachine (Thread Running Machine), 较 TRMachine 实现了删除, 添加, 插入等操作, Thread Manager 会在构造时创建 TRMachine 对象

```Python
intLT = Union[list[int], tuple[int]]
strLT = Union[list[str], tuple[str]]
ThreadOrPid = Union[list[str, ...], tuple[str, ...], list[Thread, ...], tuple[Thread, ...]]


class ThreadManager:
    # TRMachine 对象
    TRMachine: ThreadRunningMachine
    # ID 数据
    ID_DATA: dict[str: int, ...]
    # 回收的 ID
    RECYCLED_ID: dict[str: list, ...]

    def __init__(self):
        """
        构造函数
        """

    def move_thread(self, thread, targetPoolName, create_new_thread=False, remove_from_old_pool=True) -> bool:
        """
        在线程池之间移动线程
        :param thread: 线程对象 或者 PID
        :param targetPoolName: 目标线程池
        :param create_new_thread: 是否创建新线程
        :param remove_from_old_pool: 是否旧线程池中去除
        :return: 是否成功移动
        """

    def move_thread_str(self, thread, targetPoolName, create_new_thread=False, remove_from_old_pool=True) -> bool:
        """
        在线程池之间移动线程(通过 PID)
        :param thread: PID
        :param targetPoolName: 目标线程池
        :param create_new_thread: 是否创建新线程
        :param remove_from_old_pool: 是否旧线程池中去除
        :return: 是否成功移动
        """

    def move_thread_thread(self, thread: Thread, targetPoolName: str, create_new_thread: bool=False, remove_from_old_pool: bool=True) -> bool:
        """
        在线程池之间移动线程 (通过线程对象)
        :param thread: 线程对象
        :param targetPoolName: 目标线程池
        :param create_new_thread: 是否创建新线程
        :param remove_from_old_pool: 是否旧线程池中去除
        :return: 是否成功移动
        """

    def move_threads(self, threads: ThreadOrPid, targetPoolName, create_new_thread=False, remove_from_old_pool=True) -> bool:
        """
		将大量线程移动
        :param thread: 线程对象 或者 PID 组成的组
        :param targetPoolName: 目标线程池
        :param create_new_thread: 是否创建新线程
        :param remove_from_old_pool: 是否旧线程池中去除
        :return: 是否成功移动
        """

    def add_thread(self, threadObject: Thread, place: int = -1, pool: str = "Main", create_new_thread: bool = True) -> Thread:
        """
        添加线程
        :param threadObject: 线程对象
        :param place: 线程的插入位置, 默认为尾
        :param pool: 要插入的线程池, 默认为主线程池
        :param create_new_thread: 是否创建新线程
        :return: 插入的线程
        """

    def add_threads(self, threadObjects, places=None, pools=None, create_new_thread: bool = True) -> None:
        """
        添加线程
        :param threadObject: 线程对象元组
        :param place: 线程的插入位置元组, 默认为尾
        :param pool: 要插入的线程池元组, 默认为主线程池
        :param create_new_thread: 是否创建新线程
        :return: 插入的线程元组
        """

    def remove_thread(self, removeThread: any, pool: str = 'Main') -> bool:
        """
        移除线程(只会移除一次, 对于一次性存在与多个线程池的对象只会移除出一个池子)
        :param removeThread: 线程对象 或 PID
        :param pool: 移除的线程池
        :return: 是否移除成功
        """

    def remove_thread_str(self, removeThread: str, targetPoolName:str=None, level:str=None) -> bool:
        """
		通过 PID 移除线程
        :param removeThread: PID
        :param targetPoolName: 移除的线程池
        :param level: 线程等级
        :return: 是否移除成功
        """

    def remove_thread_thread(self, removeThread: Thread, targetPoolName:str=None, level:str=None) -> bool:
        """
		通过 线程对象 移除线程
        :param removeThread: 线程对象
        :param targetPoolName: 移除的线程池
        :param level: 线程等级
        :return: 是否移除成功
        """

    def remove_threads(self, pids: ThreadOrPid, pools: iter= None, levels: iter = None) -> None:
        """
       	移除大量线程
        :return: 是否成功
        """

    def clean_threadpool(self) -> None:
        """
        移除所有线程
        :return: None
        """

    def display_threadpool(self, pool=None):
        """
        在控制台输出线程池的信息, 默认输出所有的信息
        :return: None
        """

    def info_threadpool(self, pool=None):
        """
        返回线程池的信息, 默认返回所有线程池的信息
        :return: 信息
        """

    def get_thread(self, pid: str, level: str = None,  limit: tuple[str, ...] = None,
                   eliminate: tuple[str, ...] = None) -> tuple[Thread, str, str] or None:
        """
        获取线程对象
        :param pid: PID
        :param level: 线程等级
        :param limit: 线程池查找范围
        :param eliminate: 排除的线程池
        :return: threadObject, poolName, levelName - 线程对象, 线程池名称, 线程等级
        """

    def get_threads(self, pids: ThreadOrPid,  level: str = None, limit: tuple[str, ...] = None,
                    eliminate: tuple[str, ...] = None) -> tuple[tuple[Thread, str, str], ...]:
        """
        get_thread 的批量版本
        :param pids: the process id of the threads
        :param level: the level to get
        :param limit: limit thread targetPoolName to search
        :param eliminate: eliminate targetPoolName not to search
        :return: threadObjects
        """

    def get_id(self, objectType: str = 'undefined') -> str:
        """
       	给某个对象赋予 ID
        :param objectType: 对象类型(str)
        :return: ID
        """

    def get_thread_info(self, thread):
        """
        获取线程信息
        :param thread: 线程对象 或 PID
        :return:信息
        """

    def get_thread_info_str(self, thread):
        """
        通过 PID 获取线程信息
        :param thread: PID
        :return: info
        """

    def get_thread_info_thread(self, thread):
        """
		通过 线程对象 获取线程信息
        :param thread: 线程对象
        :return:
        """

    def match_threadpool(self, name: str) ->  Union[ThreadPool, ...] :
        """
        匹配线程池
        :param name: 线程池名称
        :return: 线程池对象
        """

    def all_thread_pool(self) -> dict[str: ThreadPool, ...]:
        """
        Return all the {str: threadPoolObject, ...} in dict
        :return:
        """

    def __del__(self):
        # 删除自己

    def __iter__(self):
        # 由线程池组成的迭代器
```