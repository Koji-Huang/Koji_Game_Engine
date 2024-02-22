from Thread import ThreadPool
from threading import Thread as processThread


class ThreadRunningMachine:
    """
    This class is responsible for run and stop looping
    """

    mainThreadPool: ThreadPool
    LoopThreadPool: ThreadPool
    # 0: Over, 1: Running, 2. Pause, 3. Error
    runningStatus: int
    # A processThread object to fix
    loopProcess: processThread
    recordMode: bool

    def __init__(self):
        self.mainThreadPool = ThreadPool()
        self.LoopThreadPool = ThreadPool()
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
        self.loop()

    def once(self) -> None:
        self.runningStatus = 1
        NowPool = ThreadPool()
        NowPool.merge(self.mainThreadPool)
        NowPool.merge(self.LoopThreadPool)
        while not NowPool.isEmpty() and self.runningStatus == 1:
            RunThread = NowPool.extract()
            RunThread(InsertPoolFunction=NowPool.insert)

    def loop(self):
        while self.runningStatus == 1:
            self.once()
