from types import FunctionType


class Thread:
    threadLevel: str
    kwargs: dict
    pid: str

    def __init__(self, threadLevel: str = 'undefined', **kwargs):
        self.kwargs = kwargs
        self.threadLevel = threadLevel
        self.pid = '0000000'

    def start(self, **kwargs) -> None:
        print("Default ThreadPackage Running----")

    def info(self):
        return {"threadLevel": self.threadLevel, "kwargs": self.kwargs, 'pid': self.pid}

    def result(self):
        return self.kwargs.get("result")

    def __del__(self):
        pass

    def __call__(self, **kwargs):
        return self.start(**kwargs)

    def __copy__(self):
        copied = Thread()
        copied.threadLevel = self.threadLevel
        copied.kwargs = self.kwargs.copy()
        return copied

    def __getattr__(self, item):
        try:
            return self.kwargs.get(item)
        except AttributeError:
            return None


class FunctionThread(Thread):

    def __init__(self, function: FunctionType, function_kwargs: dict, threadLevel: str = 'undefined', **kwargs):
        super().__init__(threadLevel, **kwargs)
        self.function = function
        self.function_kwargs = function_kwargs
        self.function_return = None

    def start(self, **kwargs) -> None:
        self.function_return = self.function(**self.function_kwargs, **kwargs)

    def info(self):
        info = super().info()
        info['function'] = self.function
        info['result'] = self.kwargs['result']
        return info

    def __copy__(self):
        copied = super().__copy__()
        copied.function = self.function
        copied.function_kwargs = self.function_kwargs.copy()
        copied.function_return = self.function_return
        return copied

    def __getattr__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            try:
                return self.kwargs.get(item)
            except AttributeError:
                return None

