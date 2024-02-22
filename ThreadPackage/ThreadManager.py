from typing import Union
from ThreadPackage import ThreadRunningMachine

# Type of list[int] and tuple[int]
intLT = Union[list[int], tuple[int]]


class ThreadManager:
    """
    ThreadPackage Manager Class
    This class is responsible for creating and managing threads
    But looping is done in a new separate object named Looper
    """

    # the machine, ThreadPackage Running Machine
    TRMachine: ThreadRunningMachine

    # ID Machine
    ID_Data: dict[str: int, ...]

    # Recycled ID
    Recycled_ID: dict[str: list, ...]

    def __init__(self):
        self.ID_Data = dict()
        self.Recycled_ID = dict()
        self.TRMachine = ThreadRunningMachine()
        self.TRMachine.ThreadManager = self
        self.TRMachine.set_pool_id()

    def add_thread(self, threadObject, place=-1, pool="Stop"):
        if threadObject is not None:
            threadObject = threadObject.__copy__()
            if pool == 'Loop':
                threadObject.RecyclingOrNot = False
            threadObject.pid = self.get_ID('threadObject')
            matchThreadPool = self.match_pool(pool)
            if matchThreadPool is None:
                matchThreadPool = self.TRMachine.ExceThreadPool
                threadObject.ErrorInfo = "PoolNotFound"
            if place == -1:
                matchThreadPool.add(threadObject)
            else:
                matchThreadPool.insert(threadObject, place)
            return threadObject
        return None

    def add_threads(self, threadObjects, places=None, pools=None) -> None:
        if places is None:
            places = [-1 for i in range(len(threadObjects))]
        if pools is None:
            pools = ["Stop" for i in range(len(threadObjects))]
        for threadObject, place, pool in zip(threadObjects, places, pools):
            threadObject = threadObject.__copy__()
            threadObject.pid = self.get_ID('threadObject')
            self.add_thread(threadObject, place, pool)

    def remove_thread(self, pid, pool=None, level=None):
        thread, pool, level = self.get_thread(pid, pool, level)
        if thread is None:
            return False
        else:
            threadPool = self.match_pool(pool)
            if threadPool is not None:
                threadPool.remove(pid, level)
            return False

    def remove_threads(self, pids, pools, levels):
        if pools is None:
            pools = [None for i in range(len(pids))]
        if levels is None:
            levels = [None for i in range(len(pids))]
        for pid, pools, levels in zip(pids, pools, levels):
            self.remove_thread(pid)

    def clean_threadpool(self):
        self.TRMachine.MainThreadPool.clean()
        self.TRMachine.LoopThreadPool.clean()
        self.TRMachine.ImmeThreadPool.clean()
        self.TRMachine.StopThreadPool.clean()

    def display_threadpool(self):
        print("Main ThreadPackage Pool:")
        self.TRMachine.MainThreadPool.display(end="\n|   ")
        print("\nLoop ThreadPackage Pool:")
        self.TRMachine.LoopThreadPool.display(end="\n|   ")
        print("\nImme ThreadPackage Pool:")
        self.TRMachine.ImmeThreadPool.display(end="\n|   ")
        print("\nStop ThreadPackage Pool:")
        self.TRMachine.StopThreadPool.display(end="\n|   ")
        print("\nExce ThreadPackage Pool:")
        self.TRMachine.ExceThreadPool.display(end="\n|   ")
        print("\n")

    def info_threadpool(self):
        info = dict()
        info["MainThreadPool"] = self.TRMachine.MainThreadPool.info()
        info["LoopThreadPool"] = self.TRMachine.LoopThreadPool.info()
        info["ImmeThreadPool"] = self.TRMachine.ImmeThreadPool.info()
        info["StopThreadPool"] = self.TRMachine.StopThreadPool.info()
        info["ExceThreadPool"] = self.TRMachine.ExceThreadPool.info()
        info['ID Data'] = self.ID_Data
        info['Recycled_ID'] = self.Recycled_ID
        info['ThreadRunningMachine'] = self.TRMachine.info()
        return info

    def run_thread(self, pid, remove=True):
        thread, pool, level = self.get_thread(pid)
        if thread is None:
            return False
        else:
            self.match_pool(pool).remove(pid, level)
            self.TRMachine.ImmeThreadPool.insert(thread)
            return True

    def run_threads(self, pids, removes=None):
        return tuple(self.run_thread(pid, remove) for pid, remove in zip(pids, removes)) \
            if removes else tuple(self.run_thread(pid) for pid in pids)

    def start_thread(self, pid, remove=True):
        # find thread Pool to start
        thread = self.TRMachine.StopThreadPool.finding(pid)
        # result can be None
        if thread is None:
            return False

        # get the original pool name
        joinPoolName = thread.OriginalOwner
        if joinPoolName is not None:
            # match pool to join
            joinThreadPool = self.match_pool(joinPoolName)
            # pool is matched
            if joinThreadPool is not None:
                joinThreadPool.insert(thread)
            else:
                # no name matched, error
                self.TRMachine.ExceThreadPool.insert(thread)
                thread.ErrorInfo = "No Such ThreadPackage Pool: " + joinPoolName
                return False
        else:
            # if no pool set, run it in imme
            self.TRMachine.ImmeThreadPool.insert(thread)
        thread.RecyclingOrNot = remove
        return True

    def start_threads(self, pids, removes=None):
        return tuple(self.start_thread(pid, remove) for pid, remove in zip(pids, removes)) \
            if removes else tuple(self.start_thread(pid) for pid in pids)

    def stop_thread(self, pid: int) -> bool:
        thread, pool, level = self.get_thread(pid, eliminate=('Stop', 'Exce'))
        if thread is not None:
            stopPool = self.match_pool('Stop')
            stopPool.add(thread)
            thread.OriginalOwner = pool
            originalPool = self.match_pool(pool)
            originalPool.remove(pid, level)
            return True
        else:
            return False

    def stop_threads(self, pids: intLT) -> tuple[bool, ...]:
        return tuple(self.stop_thread(pid) for pid in pids)

    def get_thread(self, pid, level=None, limit=None, eliminate=None):
        if limit is not None:
            search_range = {i: self.AllThreadPool().get(i) for i in limit}
        else:
            search_range = self.AllThreadPool().copy()
        if eliminate is not None:
            [search_range.pop(i) for i in eliminate]
        for threadPool in search_range:
            threadPoolObject = self.match_pool(threadPool)
            thread = threadPoolObject.finding(pid, level)
            if thread is not None:
                return thread, threadPool, level
        return None, None, None

    def get_threads(self, pids, level=None, limit=None, eliminate=None):
        return tuple(self.get_thread(pid, level, limit, eliminate) for pid in pids)

    def get_ID(self, objectType='undefined'):
        if self.ID_Data.get(objectType) is None:
            self.ID_Data[objectType] = 0
            self.Recycled_ID[objectType] = list()
            return "0000000"
        else:
            if len(self.Recycled_ID[objectType]):
                return self.Recycled_ID[objectType].pop()
            else:
                self.ID_Data[objectType] += 1
                length = len(str(self.ID_Data[objectType]))
                primerText = ''
                for i in range(7 - length):
                    primerText += '0'
                if self.ID_Data[objectType]:
                    return primerText + '%d' % self.ID_Data[objectType]

    def match_pool(self, name):
        collection = self.AllThreadPool()
        if name in collection.keys():
            return collection[name]
        else:
            return None

    def AllThreadPool(self):
        return {'Main': self.TRMachine.MainThreadPool,
                'Loop': self.TRMachine.LoopThreadPool,
                'Imme': self.TRMachine.ImmeThreadPool,
                'Stop': self.TRMachine.StopThreadPool,
                'Exce': self.TRMachine.ExceThreadPool}

    def __del__(self):
        ...

    def __iter__(self):
        return iter(self.AllThreadPool().value)
