from .Thread import Thread
from DataType import LinkedList


class ThreadPool:
    def __init__(self) -> None:
        self.threads = dict()
        self.threadLevel = set()
        self.name = 'undefined'
        self.id = '000'

    def add(self, thread: Thread) -> None:
        if self.threads.get(thread.threadLevel):
            self.threads[thread.threadLevel].append(thread)
        else:
            self.threadLevel.add(thread.threadLevel)
            self.threads[thread.threadLevel] = LinkedList()
            self.threads[thread.threadLevel].append(thread)

    def remove(self, thread: str, level: str = None) -> bool:
        if isinstance(thread, Thread):
            pid = thread.pid
        else:
            pid = thread
        if level:
            for _thread in self.threads.get(level):
                # Search Each Thread
                if pid == _thread.pid:
                    # if id is the same one
                    self.threads[level].remove(_thread)
                    if len(self.threads[level]) == 0:
                        # if no such type of thread remain, delete the type from the dict
                        self.threads.pop(level)
                    return True
        else:
            for threads in self.threads.values():
                # Search Each Type of Threads
                for _thread in threads:
                    # Search Each Thread
                    if pid == _thread.pid:
                        # if id is the same one
                        threads.remove(_thread)
                        if len(threads) == 0:
                            # if no such type of thread remain, delete the type from the dict
                            self.threads.pop(_thread.threadLevel)
                        return True
        return False

    def finding(self, findThread, level=None):
        if isinstance(findThread, Thread):
            pid = findThread.pid
        else:
            pid = findThread
        if level:
            get_val = self.threads.get(level)
            if get_val is not None:
                for thread in get_val:
                    # Search Each Thread
                    if pid == thread.pid:
                        # if id is the same one
                        return thread
            else:
                return None
        else:
            for threads in self.threads.values():
                # Search Each Type of Threads
                for thread in threads:
                    # Search Each Thread
                    if pid == thread.pid:
                        # if id is the same one
                        return thread
        return None

    def show(self) -> None:
        for threads in self.threads.values():
            for thread in threads:
                print(thread.info())

    def isEmpty(self) -> bool:
        for value in self.threads.values():
            if len(value):
                return False
        return True

    def extract(self) -> Thread:
        if self.isEmpty():
            raise 'No Thread Remain'
        for level in self.threadLevel:
            if self.threads.get(level):
                # May Cause Error
                return self.threads[level].pop(0)

    def insert(self, thread: Thread, index: int = 0):
        if self.threads.get(thread.threadLevel):
            if index == -1:
                self.threads[thread.threadLevel].append(thread)
            self.threads[thread.threadLevel].insert(index, thread)
        else:
            if index != 0:
                raise IndexError('list is Empty, but index set%d' % index)
            self.threads[thread.threadLevel] = LinkedList()
            self.threads[thread.threadLevel].append(thread)
            self.threadLevel += (thread.threadLevel,)

    def clean(self):
        PassState = list()
        for key in self.threadLevel:
            get = self.threads.get(key)
            if get == [] or get is None:
                self.threads.pop(key)
            else:
                PassState.append(key)
        self.threadLevel = set(PassState)

    def display(self, **format_kwargs):
        print(**format_kwargs)
        print("ID: ", self.id, **format_kwargs)
        print("Length': ", self.__len__(), **format_kwargs)
        print("Threads ID:", **format_kwargs)
        for level in self.threadLevel:
            print("| ", level, "[%s]" % len(self.threadLevel), ": ", **format_kwargs)
            for thread, index in enumerate(self.threads[level]):
                thread: Thread
                print("| %s - " % index, thread.pid, **format_kwargs)

    def info(self):
        return {"ID": self.id, "Length": len(self), "Threads": {key: value.pid for key, value in self.threads.items()}}

    def __iter__(self) -> iter:
        return iter(self.threads.values())

    def __len__(self):
        length = 0
        for i in self.threads.values():
            length += i.size
        return length
