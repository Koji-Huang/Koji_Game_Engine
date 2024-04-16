from ThreadPool import ThreadPool
from Manager.ThreadManager import ThreadManager
from threading import Thread as processThread



class ThreadRunningMachine:
    """
    This class is responsible for run and stop looping
    """

    # Main Thread Pool
    MainThreadPool: ThreadPool
    # Loop Thread Pool
    LoopThreadPool: ThreadPool
    # Immediately Thread Pool
    ImmeThreadPool: ThreadPool
    # Stopped Thread Pool
    StopThreadPool: ThreadPool
    # Exception Thread Pool
    ExceThreadPool: ThreadPool
    # Loop function in processThread
    loopProcess: processThread

    runningStatus: int
    recordMode: bool
    ThreadManager: ThreadManager

    def __init__(self):
        """
        Initialize the loop Machine
        """

    def start(self) -> None:
        """
        start the loop
        :return: None
        """

    def over(self):
        """
        stop the loop
        :return: None
        """

    def pause(self) -> None:
        """
        Pause the running
        :return:
        """

    def once(self) -> None:
        """
        run all the thread for one times
        :return: any
        """

    def loop(self):
        """
        Main Loop Function
        :return: any
        """

    def info(self):
        """
        return the info of this machine
        :return:
        """

    def clean_pool(self):
        """
        Clean Thread Pool
        """

    def get_all_pool(self):
        """
        Get dict of All Thread Pool
        :return: dict
        """