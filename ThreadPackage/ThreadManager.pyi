from typing import Union
from ThreadPackage import ThreadRunningMachine, ThreadPool, Thread


# Type of list[int] and tuple[int]
intLT = Union[list[int], tuple[int]]


class ThreadManager:
    """
    ThreadPackage Manager Class
    This class is responsible for creating and managing threads
    But looping is done in a new separate object named Looper
    """

    # the machine
    TRMachine: ThreadRunningMachine
    # ID Machine
    ID_Data: dict[str: int, ...]
    # Recycled ID
    Recycled_ID: dict[str: list, ...]

    def __init__(self):
        """
        Initialize the Manager
        """

    def add_thread(self, threadObject: Thread, place: int = -1, pool: str = "Main") -> Thread:
        """
        Add thread into the pool.
        :param threadObject: the object to add
        :param place: the place to put, 0 is the head, -1 is the bottom, other is the place
        :param pool: Main, Loop, Imme
        :return: threadObject
        """

    def add_threads(self, threadObjects: Union[list[Thread], tuple[Thread]], places: intLT) -> None:
        """
        Add thread into the pool.
        :param threadObjects: the objects to add
        :param places: the places to put, 0 is the head, -1 is the bottom, other is the place
        :return: None
        """

    def remove_thread(self, pid: int, pool: str = 'Main') -> bool:
        """
        remove the thread from pool
        :param pid: the process id of the thread
        :param pool: The pool to remove
        :return: bool of remove if success
        """

    def remove_threads(self, pids: intLT, pools: iter= None, levels: iter = None) -> None:
        """
        remove the thread from pool
        :return: None
        """

    def clean_threadpool(self) -> None:
        """
        check the thread pool
        :return: None
        """

    def display_threadpool(self) -> None:
        """
        show the info about thread
        :return: None
        """

    def info_threadpool(self) -> dict:
        """
        return the info of thread pool
        :return:  dict of information
        """


    def run_thread(self, pid: int, remove: bool = True):
        """
        Run a ThreadPackage Immediately
        :param pid: the process id of the thread
        :param remove: Remove the process if it moved
        :return: bool, true mean successful, false mean failure
        """

    def run_threads(self, pids: intLT, removes: Union[list[bool], tuple[bool], None] = None) -> tuple[bool, ...]:
        """
        Run Threads Immediately
        :param pids: the processes id of the thread
        :param removes: Remove the processes if it moved
        :return: bool, true mean successful, false mean failure
        """

    def start_thread(self, pid: int, remove: bool = True) -> bool:
        """
        Start a thread from StopThreadPool
        :param pid: the process id of the thread
        :param remove: Remove the process if it moved
        :return: bool, true mean successful, false mean failure
        """

    def start_threads(self, pids: intLT, remove: Union[list[bool], tuple[bool], None] = None) -> tuple[bool, ...]:
        """
        Start threads from StopThreadPool
        :param pids: the process id of the threads
        :param remove: Remove the process before run it or not
        :return: tuple of bool, true mean successful, false mean failure
        """

    def stop_thread(self, pid: int) -> bool:
        """
        Stop a thread from pool, and it will be push to the stop pool
        :param pid: the process id of the thread
        :return:  bool, true mean successful, false mean failure
        """

    def stop_threads(self, pids: intLT) -> tuple[bool, ...]:
        """
        Stop a thread from pool, and it will be push to the stop pool
        :param pids: the process id of the threads
        :return: tuple of bool, true mean successful, false mean failure
        """

    def get_thread(self, pid: int, level: str = None,  limit: tuple[str, ...] = None, eliminate: tuple[str, ...] = None) -> tuple[Thread, str, str] or None:
        """
        get threadObject from the pool
        :param pid: the process id of the threads
        :param level: the level object ;in
        :param limit: limit thread pool to search
        :param eliminate: eliminate pool not to search
        :return: threadObject, poolName, levelName
        """

    def get_threads(self, pids: intLT,  level: str = None, limit: tuple[str, ...] = None, eliminate: tuple[str, ...] = None) -> tuple[tuple[Thread, str, str], ...]:
        """
        get threadObjects from the pool
        :param pids: the process id of the threads
        :param level: the level to get
        :param limit: limit thread pool to search
        :param eliminate: eliminate pool not to search
        :return: threadObjects
        """

    def get_ID(self, objectType: str = 'undefined') -> str:
        """
        control objects id
        :param objectType:
        :return:
        """

    def match_pool(self, name: str) ->  Union[ThreadPool, ...] :
        """
        Used To easy get Pool
        :param name: the name of the pool
        :return: threadPoolObject
        """

    def AllThreadPool(self) -> dict[str: ThreadPool, ...]:
        """
        Return all the {str: threadPoolObject, ...} in dict
        :return:
        """

    def __del__(self):...

    def __iter__(self):...
