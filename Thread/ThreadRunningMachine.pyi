from ThreadPool import ThreadPool
from threading import Thread as processThread

class ThreadRunningMachine:
    """
    This class is responsible for run and stop looping
    """

    mainThreadPool: ThreadPool
    LoopThreadPool: ThreadPool
    loopProcess: processThread
    runningStatus: int
    recordMode: bool

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
