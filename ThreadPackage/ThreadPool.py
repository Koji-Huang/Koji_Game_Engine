from ThreadPackage.Thread import Thread
from CustomDataType import LinkedList

class ThreadPool:
    def __init__(self) -> None:
        self.threads = dict()
        self.threadLevel = set()
        self.name = 'undefined'
        self.id = '000'

    def classify(self) -> None:
        """
        classify for all threads
        :return: None
        """

    def add(self, thread: Thread) -> None:
        if self.threads.get(thread.threadLevel):
            self.threads[thread.threadLevel].append(thread)
        else:
            self.threadLevel.add(thread.threadLevel)
            self.threads[thread.threadLevel] = LinkedList()
            self.threads[thread.threadLevel].append(thread)

    def remove(self, removeThread: str, level: str = None) -> bool:
        if isinstance(removeThread, Thread):
            pid = removeThread.pid
        else:
            pid = removeThread
        if level:
            for thread in self.threads.get(level):
                # Search Each ThreadPackage
                if pid == thread.pid:
                    # if id is the same one
                    self.threads[level].remove(thread)
                    if len(self.threads[level]) == 0:
                        # if no such type of thread remain, delete the type from the dict
                        self.threads.pop(level)
                    return True
        else:
            for threads in self.threads.values():
                # Search Each Type of Threads
                for thread in threads:
                    # Search Each ThreadPackage
                    if pid == thread.pid:
                        # if id is the same one
                        threads.remove(thread)
                        if len(threads) == 0:
                            # if no such type of thread remain, delete the type from the dict
                            self.threads.pop(thread.threadLevel)
                        return True

    def finding(self, findThread, level=None):
        if isinstance(findThread, Thread):
            pid = findThread.pid
        else:
            pid = findThread
        if level:
            get_val = self.threads.get(level)
            if get_val is not None:
                for thread in get_val:
                    # Search Each ThreadPackage
                    if pid == thread.pid:
                        # if id is the same one
                        return thread
            else:
                return None
        else:
            for threads in self.threads.values():
                # Search Each Type of Threads
                for thread in threads:
                    # Search Each ThreadPackage
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
            raise 'No ThreadPackage Remain'
        for level in self.threadLevel:
            if self.threads.get(level):
                # May Cause Error
                return self.threads[level].extract(0)

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
        return len(self.threads)
