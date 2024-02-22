from threading import Thread as processThread
from ThreadPackage import ThreadPool


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
    # 0: Over, 1: Running, 2. Pause, 3. Error
    runningStatus: int
    # A processThread object to fix
    loopProcess: processThread
    recordMode: bool
    ThreadManager: any

    def __init__(self):
        self.MainThreadPool = ThreadPool()
        self.LoopThreadPool = ThreadPool()
        self.ImmeThreadPool = ThreadPool()
        self.StopThreadPool = ThreadPool()
        self.ExceThreadPool = ThreadPool()
        self.loopProcess = processThread(target=self.loop)
        self.runningStatus = 0

    def start(self) -> None:
        self.runningStatus = 1
        self.recordMode = False
        self.loopProcess = processThread(target=ThreadPool)
        self.run()

    def stop(self) -> None:
        self.runningStatus = 0

    def pause(self) -> None:
        self.runningStatus = 2

    def run(self):
        self.runningStatus = 1
        self.loopProcess.start()

    def once(self) -> None:
        kwargs = {"TRMachine": self, "ThreadManager": self.ThreadManager}
        self.runningStatus = 1
        self.MainThreadPool.merge(self.LoopThreadPool)
        while self.runningStatus == 1:
            while self.ImmeThreadPool.isEmpty() and not self.MainThreadPool.isEmpty():
                RunThread = self.MainThreadPool.extract()
                RunThread(**kwargs)
            while not self.ImmeThreadPool.isEmpty():
                RunThread = self.ImmeThreadPool.extract()
                RunThread(**kwargs)
            if self.ImmeThreadPool.isEmpty() and self.MainThreadPool.isEmpty():
                self.runningStatus = 0

    def loop(self):
        while self.runningStatus == 1:
            self.once()
            if self.runningStatus == 0 and self.LoopThreadPool.isEmpty():
                return None

    def info(self):
        info = dict()
        info["MainThreadPool"] = self.MainThreadPool
        info["LoopThreadPool"] = self.LoopThreadPool
        info["ImmeThreadPool"] = self.ImmeThreadPool
        info["RunningStatus"] = self.runningStatus
        info["RecordMode"] = self.recordMode
        return info

    def set_pool_id(self):
        self.MainThreadPool.id = self.ThreadManager.get_ID("poolObject")
        self.LoopThreadPool.id = self.ThreadManager.get_ID("poolObject")
        self.ImmeThreadPool.id = self.ThreadManager.get_ID("poolObject")
        self.StopThreadPool.id = self.ThreadManager.get_ID("poolObject")
        self.ExceThreadPool.id = self.ThreadManager.get_ID("poolObject")
