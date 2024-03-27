from typing import Union
from ThreadPackage import ThreadRunningMachine, Thread

strLT = Union[list[str], tuple[str]]


class ThreadManager:
    """
    ThreadPackage Manager Class
    This class is responsible for creating and managing threads
    But looping is done in a new separate object named Looper
    """
    def __init__(self):
        self.ID_DATA = dict()
        self.RECYCLED_ID = dict()
        self.TRMachine = ThreadRunningMachine()
        self.TRMachine.ThreadManager = self
        self.TRMachine.set_pool_id()

    def move_thread(self, thread, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
        if isinstance(thread, Thread):
            return self.move_thread_thread(thread, targetPoolName, create_new_thread, remove_from_old_pool)
        if isinstance(thread, str):
            return self.move_thread_str(thread, targetPoolName, create_new_thread, remove_from_old_pool)
        raise "Thread Not Implemented"

    def move_thread_str(self, thread: str, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
        thread, oldPoolName = self.get_thread(thread)
        if thread is None:
            return False
        # match target thread targetPoolName
        targetPool = self.match_threadpool(targetPoolName)
        if targetPool is None:
            return False
        # match kwargs
        if remove_from_old_pool:
            oldPool = self.match_threadpool(oldPoolName)
            oldPool.remove(thread)
        if create_new_thread:
            thread = thread.__copy__()
        # add thread
        targetPool.add(thread)
        return True

    def move_thread_thread(self, thread: Thread, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
        oldPoolName = self.get_thread(pid=thread.pid, level=thread.threadLevel)[1]
        # match target thread targetPoolName
        targetPool = self.match_threadpool(targetPoolName)
        if targetPool is None:
            return False
        # match kwargs
        if remove_from_old_pool:
            oldPool = self.match_threadpool(oldPoolName)
            oldPool.remove(thread)
        if create_new_thread:
            thread = thread.__copy__()
            thread.pid = self.get_id('threadObject')
        # add thread
        targetPool.add(thread)
        return True

    def move_threads(self, threads, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
        return [self.move_thread(thread, targetPoolName, create_new_thread, remove_from_old_pool) for thread in threads]

    def add_thread(self, threadObject, place=-1, pool="Imme"):
        if threadObject is not None:
            # copy the thread object
            threadObject = threadObject.__copy__()
            threadObject.pid = self.get_id('threadObject')
            # match thread targetPoolName
            matchThreadPool = self.match_threadpool(pool)
            if matchThreadPool is None:
                matchThreadPool = self.TRMachine.ExceThreadPool
                threadObject.ErrorInfo = "PoolNotFound"
            # put thread into targetPoolName
            if place == -1:
                matchThreadPool.add(threadObject)
            else:
                matchThreadPool.insert(threadObject, place)
            # return result
            return threadObject
        else:
            return None

    def add_threads(self, threadObjects, places=None, pools=None) -> None:
        if places is None:
            places = [-1 for _ in range(len(threadObjects))]
        if pools is None:
            pools = ["Stop" for _ in range(len(threadObjects))]
        for threadObject, place, pool in zip(threadObjects, places, pools):
            self.add_thread(threadObject, place, pool)

    def remove_thread(self, removeThread, targetPoolName=None, level=None):
        if isinstance(removeThread, Thread):
            return self.remove_thread_thread(removeThread, targetPoolName, level)
        if isinstance(removeThread, str):
            return self.remove_thread_str(removeThread, targetPoolName, level)
        return False

    def remove_thread_str(self, removeThread, targetPoolName=None, level=None):
        thread, targetPoolName, level = self.get_thread(removeThread, targetPoolName, level)
        # Match Thread Pool
        targetPool = self.match_threadpool(targetPoolName)
        # deal with things
        if thread is not None and targetPool is not None:
            targetPool.remove(thread, level)
            return True
        else:
            return False

    def remove_thread_thread(self, removeThread, targetPoolName=None, level=None):
        thread, targetPoolName, level = self.get_thread(removeThread.pid, targetPoolName, level)
        # Match Thread Pool
        targetPool = self.match_threadpool(targetPoolName)
        # deal with things
        if thread is not None and targetPool is not None:
            targetPool.remove(thread, level)
            return True
        else:
            return False

    def remove_threads(self, pids, pools, levels):
        if pools is None:
            pools = [None for _ in range(len(pids))]
        if levels is None:
            levels = [None for _ in range(len(pids))]
        for pid, pools, levels in zip(pids, pools, levels):
            self.remove_thread(pid)

    def get_thread(self, pid, level=None, limit=None, eliminate=None):
        if limit is not None:
            search_range = {i: self.all_thread_pool().get(i) for i in limit}
        else:
            search_range = self.all_thread_pool().copy()
        if eliminate is not None:
            [search_range.pop(i) for i in eliminate]
        for threadPool in search_range:
            threadPoolObject = self.match_threadpool(threadPool)
            thread = threadPoolObject.finding(pid, level)
            if thread is not None:
                return thread, threadPool, level
        return None, None, None

    def get_threads(self, pids, level=None, limit=None, eliminate=None):
        return tuple(self.get_thread(pid, level, limit, eliminate) for pid in pids)

    def get_id(self, objectType='undefined'):
        if self.ID_DATA.get(objectType) is None:
            self.ID_DATA[objectType] = 0
            self.RECYCLED_ID[objectType] = list()
            return "0000000"
        else:
            if len(self.RECYCLED_ID[objectType]):
                return self.RECYCLED_ID[objectType].pop()
            else:
                self.ID_DATA[objectType] += 1
                length = len(str(self.ID_DATA[objectType]))
                primerText = ''
                for i in range(7 - length):
                    primerText += '0'
                if self.ID_DATA[objectType]:
                    return primerText + '%d' % self.ID_DATA[objectType]

    def get_thread_info(self, thread):
        if isinstance(thread, Thread):
            return self.get_thread_info_thread(thread)
        if isinstance(thread, str):
            return self.get_thread_info_str(thread)
        raise "No Info Available"

    def get_thread_info_str(self, thread):
        thread, pool, level = self.get_thread(thread)
        return {'pid': thread.pid, 'level': level, 'pool': pool, 'thread': thread}

    def get_thread_info_thread(self, thread):
        thread, pool, level = self.get_thread(thread.pid)
        return {'pid': thread.pid, 'level': level, 'pool': pool, 'thread': thread}

    def match_threadpool(self, name):
        collection = self.all_thread_pool()
        if name in collection.keys():
            return collection[name]
        else:
            return None

    def clean_threadpool(self):
        self.TRMachine.MainThreadPool.clean()
        self.TRMachine.LoopThreadPool.clean()
        self.TRMachine.ImmeThreadPool.clean()
        self.TRMachine.StopThreadPool.clean()
        self.TRMachine.ExceThreadPool.clean()

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
        info['ID Data'] = self.ID_DATA
        info['Recycled_ID'] = self.RECYCLED_ID
        info['ThreadRunningMachine'] = self.TRMachine.info()
        return info

    def all_thread_pool(self):
        return {'Main': self.TRMachine.MainThreadPool,
                'Loop': self.TRMachine.LoopThreadPool,
                'Imme': self.TRMachine.ImmeThreadPool,
                'Stop': self.TRMachine.StopThreadPool,
                'Exce': self.TRMachine.ExceThreadPool}

    def __del__(self):
        ...

    def __iter__(self):
        return iter(self.all_thread_pool().value)
