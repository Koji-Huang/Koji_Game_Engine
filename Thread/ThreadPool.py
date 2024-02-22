from Thread.Thread import Thread


class ThreadPool:
    threads: dict[str: list[Thread], ...]
    threadLevel: tuple[str, ...]

    def __init__(self) -> None:
        self.threads = dict()
        self.threadLevel = tuple()

    def classify(self) -> None:
        """
        classify for all threads
        :return: None
        """

    def add(self, thread: Thread) -> None:
        if self.threads.get(thread.threadLevel):
            self.threads[thread.threadLevel].append(thread)
        else:
            self.threadLevel += (thread.threadLevel, )
            self.threads[thread.threadLevel] = list()
            self.threads[thread.threadLevel].append(thread)

    def remove(self, pid: int, level: str = None) -> bool:
        if level:
            for thread in self.threads.get(level):
                # Search Each Thread
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
                    # Search Each Thread
                    if pid == thread.pid:
                        # if id is the same one
                        threads.remove(thread)
                        if len(threads) == 0:
                            # if no such type of thread remain, delete the type from the dict
                            self.threads.pop(thread.threadLevel)
                        return True

    def finding(self, pid, level) -> Thread:
        if level:
            for thread in self.threads.get(level):
                # Search Each Thread
                if pid == thread.pid:
                    # if id is the same one
                    return thread
        else:
            for threads in self.threads.values():
                # Search Each Type of Threads
                for thread in threads:
                    # Search Each Thread
                    if pid == thread.pid:
                        # if id is the same one
                        return thread

    def show(self) -> None:
        for threads in self.threads.values():
            for thread in threads:
                print(thread.info())

    def merge(self, another):
        for key, value in another.threads.items():
            if self.threads.get(key):
                self.threads[key].extend(value)
            else:
                self.threadLevel += (key, )
                self.threads[key] = value

    def record(self) -> dict:
        return self.threads

    def isEmpty(self) -> bool:
        for value in self.threads.values():
            if len(value):
                return False
        return True

    def extract(self) -> Thread:
        if self.isEmpty():
            raise 'No Thread Remain'
        for level in self.threadLevel:
            for threads in self.threads.get(level):
                return self.threads[level].pop(0)

    def insert(self, thread: Thread, index: int = 0):
        if self.threads.get(thread.threadLevel):
            self.threads[thread.threadLevel].insert(index, thread)
        else:
            if index != 0:
                raise IndexError('list is Empty, but index set%d' % index)
            self.threads[thread.threadLevel] = [thread, ]
            self.threadLevel += (thread.threadLevel, )

    def __iter__(self) -> tuple[Thread]:
        return iter(self.threads.values())

    def __len__(self):
        return len(self.threads)
