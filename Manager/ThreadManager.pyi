from typing import Union
from Thread import ThreadRunningMachine, ThreadPool, Thread


# Type of list[int] and tuple[int]
intLT = Union[list[int], tuple[int]]
strLT = Union[list[str], tuple[str]]
ThreadOrPid = Union[list[str, ...], tuple[str, ...], list[Thread, ...], tuple[Thread, ...]]


class ThreadManager:
    """
    Thread Manager Class
    This class is responsible for creating and managing threads
    But looping is done in a new separate object named Looper
    """

    # the machine
    TRMachine: ThreadRunningMachine
    # ID Machine
    ID_DATA: dict[str: int, ...]
    # Recycled ID
    RECYCLED_ID: dict[str: list, ...]

    def __init__(self):
        """
        Initialize the Manager
        """

    def move_thread(self, thread, targetPoolName, create_new_thread=False, remove_from_old_pool=True) -> bool:
        """
        Move thread
        :param thread:  pid or ThreadObject
        :param targetPoolName:
        :param create_new_thread:
        :param remove_from_old_pool:
        :return:
        """

    def move_thread_str(self, thread, targetPoolName, create_new_thread=False, remove_from_old_pool=True) -> bool:
        """
        move thread, match thread is str object ( pid )
        :param thread:
        :param targetPoolName:
        :param create_new_thread:
        :param remove_from_old_pool:
        :return:
        """

    def move_thread_thread(self, thread: Thread, targetPoolName: str, create_new_thread: bool=False, remove_from_old_pool: bool=True) -> bool:
        """
        move thread, match thread is thread
        :param thread:
        :param targetPoolName:
        :param create_new_thread:
        :param remove_from_old_pool:
        :return:
        """

    def move_threads(self, threads: ThreadOrPid, targetPoolName, create_new_thread=False, remove_from_old_pool=True) -> bool:
        """

        :param threads:
        :param targetPoolName:
        :param create_new_thread:
        :param remove_from_old_pool:
        :return:
        """

    def add_thread(self, threadObject, pool="Imme", place=-1, create_new_thread: bool = True):
        """
        Add thread into the targetPoolName.
        :param threadObject: the object to add
        :param place: the place to put, 0 is the head, -1 is the bottom, other is the place
        :param pool: Main, Loop, Imme
        :param create_new_thread: Is it need to create new thread
        :return: threadObject
        """

    def add_threads(self, threadObjects, places=None, pools=None, create_new_thread: bool = True) -> tuple:
        """
        Add thread into the targetPoolName.
        :param threadObjects: the objects to add
        :param places: the places to put, 0 is the head, -1 is the bottom, other is the place
        :param pools: Main, Loop, Imme
        :param create_new_thread: Is it need to create new thread
        :return: None
        """

    def remove_thread(self, removeThread: any, pool: str = 'Main') -> bool:
        """
        remove the thread from targetPoolName
        :param removeThread: pid or ThreadObject
        :param pool: The targetPoolName to remove
        :return: bool of remove if success
        """

    def remove_thread_str(self, removeThread: str, targetPoolName:str=None, level:str=None) -> bool:
        """

        :param removeThread:
        :param targetPoolName:
        :param level:
        :return:
        """

    def remove_thread_thread(self, removeThread: Thread, targetPoolName:str=None, level:str=None) -> bool:
        """

        :param removeThread:
        :param targetPoolName:
        :param level:
        :return:
        """

    def remove_threads(self, pids: ThreadOrPid, pools: iter= None, levels: iter = None) -> None:
        """
        remove the thread from targetPoolName
        :return: None
        """

    def clean_threadpool(self) -> None:
        """
        clean all thread
        :return: None
        """

    def display_threadpool(self, pool=None):
        """
        show the info about thread
        :return: None
        """

    def info_threadpool(self, pool=None):
        """
        return the info of thread targetPoolName
        :return:  dict of information
        """

    def get_thread(self, pid: str, level: str = None,  limit: tuple[str, ...] = None,
                   eliminate: tuple[str, ...] = None) -> tuple[Thread, str, str] or None:
        """
        get threadObject from the targetPoolName
        :param pid: the process id of the threads
        :param level: the level object ;in
        :param limit: limit thread targetPoolName to search
        :param eliminate: eliminate targetPoolName not to search
        :return: threadObject, poolName, levelName
        """

    def get_threads(self, pids: ThreadOrPid,  level: str = None, limit: tuple[str, ...] = None,
                    eliminate: tuple[str, ...] = None) -> tuple[tuple[Thread, str, str], ...]:
        """
        get threadObjects from the targetPoolName
        :param pids: the process id of the threads
        :param level: the level to get
        :param limit: limit thread targetPoolName to search
        :param eliminate: eliminate targetPoolName not to search
        :return: threadObjects
        """

    def get_id(self, objectType: str = 'undefined') -> str:
        """
        control objects id
        :param objectType:
        :return:
        """

    def get_thread_info(self, thread):
        """
        get thread information

        :param thread:
        :return:
        """

    def get_thread_info_str(self, thread):
        """
        'pid': thread.pid, 'level': level, 'pool': pool, 'thread': thread
        :param thread: pid or ThreadObject
        :return: info
        """

    def get_thread_info_thread(self, thread):
        """

        :param thread:
        :return:
        """

    def match_threadpool(self, name: str) ->  Union[ThreadPool, ...] :
        """
        Used To easy get Pool
        :param name: the name of the targetPoolName
        :return: threadPoolObject
        """

    def all_thread_pool(self) -> dict[str: ThreadPool, ...]:
        """
        Return all the {str: threadPoolObject, ...} in dict
        :return:
        """

    def __del__(self):...

    def __iter__(self):...
