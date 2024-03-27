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
        self.loopProcess = processThread(target=self.loop)
        self.loopProcess.start()

    def stop(self) -> None:
        self.runningStatus = 0

    def pause(self) -> None:
        self.runningStatus = 2

    def once(self) -> None:
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
                self.ThreadManager.clean_threadpool()
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
        info["MainThreadPool"] = self.MainThreadPool
        info["LoopThreadPool"] = self.LoopThreadPool
        info["ImmeThreadPool"] = self.ImmeThreadPool
        info["StopThreadPool"] = self.StopThreadPool
        info["ExceThreadPool"] = self.ExceThreadPool
        info["RunningStatus"] = self.runningStatus
        info["RecordMode"] = self.recordMode
        return info

    def set_pool_id(self):
        self.MainThreadPool.id = self.ThreadManager.get_id("poolObject")
        self.LoopThreadPool.id = self.ThreadManager.get_id("poolObject")
        self.ImmeThreadPool.id = self.ThreadManager.get_id("poolObject")
        self.StopThreadPool.id = self.ThreadManager.get_id("poolObject")
        self.ExceThreadPool.id = self.ThreadManager.get_id("poolObject")
