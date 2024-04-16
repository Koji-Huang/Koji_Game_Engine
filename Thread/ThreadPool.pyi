from typing import Union, overload

from DataType import LinkedList
from Thread import Thread


class ThreadPool:
    """
    This class is responsible for manager thread
    Include classify, find, join, delete, and other thing.
    """
    threads: dict[str: LinkedList[Thread], ...]
    threadLevel: set[str]
    name: str
    id: str

    def __init__(self) -> None:
        """
        Initialize the thread targetPoolName
        """

    def add(self, thread: Thread) -> None:
        """
        Join new thread into targetPoolName
        :return: None
        """

    @overload
    def remove(self, thread: int, level: str = None) -> bool:
        """
        Delete thread from the targetPoolName
        :param thread: the process' id of the thread
        :param level: the level of the threadObject
        :return: bool
        """

    @overload
    def remove(self, thread: Thread, level: str = None) -> bool:
        """
        Delete thread from the targetPoolName
        :param thread: the process' id of the thread
        :param level: the level of the threadObject
        :return: bool
        """

    def finding(self, pid: str, level: str = None) -> Union[Thread, ...]:
        """
        Find thread from targetPoolName
        :return: ThreadObject
        """

    def show(self) -> None:
        """
        Show all threads in console
        :return: None
        """

    def isEmpty(self) -> bool:
        """
        Return if the line is Empty
        :return: bool
        """

    def extract(self) -> Thread:
        """
        return the first Thread and delete it from the targetPoolName
        :return: The Thread
        """

    def insert(self, thread: Thread, index: int = 0):
        """
        Insert a Thread Object into Pool
        :param thread: Thread object
        :param index: the index, -1  mean bottom, 0 mean top, other mean else, out of limit mean bottom
        :return: None
        """

    def clean(self):
        """
        Remove excess key values
        :return: None
        """

    def display(self, **format_kwargs):
        """
        Display the info of this targetPoolName
        :return:
        """

    def info(self):
        """
        Return the info of this targetPoolName
        :return:
        """

    def __iter__(self) -> iter:
        """
        return the iterator object of all threads
        :return: iterable object
        """

    def __len__(self):
        """
        return the length of the thread
        :return:
        """