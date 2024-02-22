from typing import Union

from ThreadPool import ThreadPool
from ThreadRunningMachine import ThreadRunningMachine


# Type of list[int] and tuple[int]
intLT = Union[list[int], tuple[int]]


class ThreadManager:
    """
    Thread Manager Class
    This class is responsible for creating and managing threads
    But looping is done in a new separate object named Looper
    """

    # the machine
    ThreadRunningMachine: ThreadRunningMachine

    # the pool
    threadPool: ThreadPool

    def __init__(self):
        """
        Initialize the Manager
        """

    def add_thread(self, threadObject: object, place: int = -1) -> None:
        """
        Add thread into the pool.
        :param threadObject: the object to add
        :param place: the place to put, 0 is the head, -1 is the bottom, other is the place
        :return: None
        """

    def add_loop_thread(self, threadObjects: Union[list[object], tuple[object]], places: intLT) -> None:
        """
        add thread into loop thread pool
        :param threadObjects: the objects to add
        :param places: the places to put, 0 is the head, -1 is the bottom, other is the place
        :return: None
        """

    def remove_thread(self, pids: int) -> None:
        """
        remove the thread from pool
        :return: None
        """

    def remove_threads(self, pids: intLT) -> None:
        """
        remove the thread from pool
        :return: None
        """

    def remove_loop_thread(self, pids: int) -> None:
        """
        remove thread from loop thread pool
        :return:
        """

    def remove_loop_threads(self, pids: intLT) -> None:
        """
        remove thread from loop thread pool
        :return:
        """

    def check_threadpool(self) -> None:
        """
        check the thread pool
        :return: None
        """

    def check_loop_threadpool(self) -> None:
        """
        Check the loop thread pool
        :return:
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

    def start_thread(self, pid: int, remove: bool = True):
        """
        Start a thread immediately
        :param pid: the process id of the thread
        :param remove: Remove the process before run it or not
        :return: bool, true mean successful, false mean failure
        """

    def start_threads(self, pids: intLT, remove: Union[list[bool], tuple[bool], None] = None) -> tuple[bool]:
        """
        Start threads immediately
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

    def stop_threads(self, pids: intLT) -> tuple[bool]:
        """
        Stop a thread from pool, and it will be push to the stop pool
        :param pids: the process id of the threads
        :return: tuple of bool, true mean successful, false mean failure
        """

    def get_thread(self, pid: int) -> object:
        """
        get threadObject from the pool
        :param pid: the process id of the threads
        :return: threadObject
        """

    def get_threads(self, pids: intLT) -> tuple[object]:
        """
        get threadObjects from the pool
        :param pids: the process id of the threads
        :return: threadObjects
        """

    def __del__(self):...

    def __iter__(self):...
