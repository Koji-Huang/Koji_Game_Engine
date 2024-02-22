from Thread import Thread


class ThreadPool:
    """
    This class is responsible for manager thread
    Include classify, find, join, delete, and other thing.
    """
    threads: dict[str: list[Thread], ...]
    threadLevel: tuple[str, ...]

    def __init__(self) -> None:
        """
        Initialize the thread pool
        """

    def classify(self) -> None:
        """
        classify for all threads
        :return: None
        """

    def add(self, thread: Thread) -> None:
        """
        Join new thread into pool
        :return: None
        """

    def merge(self, another: ThreadPool) -> None:
        """
        Merge this and another ThreadPool
        Only self change
        :param another: Another Threadpool
        :return: None
        """

    def remove(self, pid: int, level: str = None) -> bool:
        """
        Delete thread from the pool
        :param pid: the process' id of the thread
        :param level: the level of the threadObject
        :return: bool
        """

    def finding(self, pid: int, level: str) -> Thread:
        """
        Find thread from pool
        :return: ThreadObject
        """

    def show(self) -> None:
        """
        Show all threads in console
        :return: None
        """

    def record(self) -> dict:
        """
        Output all threads to record
        :return: the record
        """

    def isEmpty(self) -> bool:
        """
        Return if the line is Empty
        :return: bool
        """

    def extract(self) -> Thread:
        """
        return the first Thread and delete it from the pool
        :return: The Thread
        """

    def insert(self, thread: Thread, index: int = 0):
        """
        Insert a Thread Object into Pool
        :param thread: Thread object
        :param index: the index
        :return: None
        """

    def __iter__(self) -> tuple[Thread]:
        """
        return the iterator object of all threads
        :return: iterable object
        """

    def __len__(self):
        """
        return the length of the thread
        :return:
        """