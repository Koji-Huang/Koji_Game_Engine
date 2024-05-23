from threading import Thread as processThread
from .ThreadPool import ThreadPool


class ThreadRunningMachine:
    """
    This class is responsible for run and stop looping
    """

    def __init__(self):
        self.MainThreadPool = ThreadPool()
        self.LoopThreadPool = ThreadPool()
        self.ImmeThreadPool = ThreadPool()
        self.StopThreadPool = ThreadPool()
        self.ExceThreadPool = ThreadPool()
        self.loopProcess = processThread(target=self.loop)
        self.runningStatus = 0
        self.recordMode = False
        from . import Management as ThreadManager
        self.ThreadManager = ThreadManager

    def start(self) -> None:
        self.runningStatus = 1
        self.loopProcess = processThread(target=self.loop)
        self.loopProcess.start()

    def over(self) -> None:
        self.runningStatus = 0

    def pause(self) -> None:
        self.runningStatus = 2

    def once(self) -> None:
        if self.ThreadManager is None:
            from . import Management
            self.ThreadManager = Management
        kwargs = {"TRMachine": self, "ThreadManager": self.ThreadManager}
        self.runningStatus = 1
        # Put Loop into Main
        loopThreadPackage = tuple(thread for threads in self.LoopThreadPool.threads.values() for thread in threads)
        self.ThreadManager.move_threads(loopThreadPackage, 'Main', create_new_thread=False, remove_from_old_pool=False)
        # Run Function
        while self.runningStatus == 1:
            while self.ImmeThreadPool.isEmpty() and not self.MainThreadPool.isEmpty():
                run_thread = self.MainThreadPool.extract()
                run_thread(**kwargs)
            while not self.ImmeThreadPool.isEmpty():
                run_thread = self.ImmeThreadPool.extract()
                run_thread(**kwargs)
            if self.ImmeThreadPool.isEmpty() and self.MainThreadPool.isEmpty():
                return

    def loop(self):
        self.runningStatus = 1
        while True:
            # Check if ThreadPool is Empty
            if False not in [
                self.MainThreadPool.isEmpty(),
                self.LoopThreadPool.isEmpty(),
                self.ImmeThreadPool.isEmpty()
            ]:
                self.runningStatus = 0
                return 0
            # Running State is Running
            if self.runningStatus == 1:
                self.once()
            # Running State if Over
            elif self.runningStatus == 0:
                self.clean_pool()
                return 0
            # Running State is Pause
            elif self.runningStatus == 2:
                continue
            # Running State is Error
            elif self.runningStatus == 3:
                # Fix in Future
                return 3
            else:
                self.runningStatus = 3

    def info(self):
        info = dict()
        info['ThreadPool'] = self.get_all_pool()
        info["RunningStatus"] = self.runningStatus
        info["RecordMode"] = self.recordMode
        return info

    def clean_pool(self):
        self.MainThreadPool.clean()
        self.LoopThreadPool.clean()
        self.ImmeThreadPool.clean()
        self.StopThreadPool.clean()
        self.ExceThreadPool.clean()

    def get_all_pool(self):
        info = dict()
        info["Main"] = self.MainThreadPool
        info["Loop"] = self.LoopThreadPool
        info["Imme"] = self.ImmeThreadPool
        info["Stop"] = self.StopThreadPool
        info["Exce"] = self.ExceThreadPool
        return info