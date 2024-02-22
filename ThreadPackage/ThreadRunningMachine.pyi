from ThreadPool import ThreadPool
from threading import Thread as processThread

class ThreadRunningMachine:
    """
    This class is responsible for run and stop looping
    """

    # Main ThreadPackage Pool
    MainThreadPool: ThreadPool
    # Loop ThreadPackage Pool
    LoopThreadPool: ThreadPool
    # Immediately ThreadPackage Pool
    ImmeThreadPool: ThreadPool
    # Stopped ThreadPackage Pool
    StopThreadPool: ThreadPool
    # Exception ThreadPackage Pool
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

    def stop(self):
        """
        stop the loop
        :return: None
        """

    def run(self):
        """
        a function to run a single thread
        :return: any
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

    def set_pool_id(self):
        """
        Set Pools' id info
        :return: None
        """
