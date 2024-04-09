class Thread:
    def __init__(self, threadLevel: str = 'undefined', threadName: str = 'undefined', **kwargs):
        self.kwargs = kwargs
        self.threadName = threadName
        self.threadLevel = threadLevel
        self.pid = '0000000'

    def start(self, **kwargs) -> None:
        print("Default ThreadPackage Running----", self.pid)

    def info(self):
        return {"threadLevel": self.threadLevel, "threadName": self.threadName,
                "kwargs": self.kwargs, 'removeThread': self.pid}

    def result(self):
        return self.kwargs.get("result")

    def __del__(self):
        pass

    def __call__(self, **kwargs):
        return self.start(**kwargs)

    def __copy__(self, another=None):
        if another is None:
            copied = Thread()
        else:
            copied = another
        copied.threadLevel = self.threadLevel
        copied.kwargs = self.kwargs.copy()
        return copied

    def __getattr__(self, item):
        try:
            return self.kwargs.get(item)
        except AttributeError:
            return None


class FunctionThread(Thread):

    def __init__(self, function: (), function_kwargs: dict = None, threadLevel: str = 'undefined', **kwargs):
        super().__init__(threadLevel, **kwargs)
        self.function = function
        self.function_kwargs = function_kwargs if function_kwargs else dict()
        self.function_return = None

    def start(self, **kwargs) -> None:
        self.function_return = self.function(**self.function_kwargs, **kwargs)

    def info(self):
        info = super().info()
        info['function'] = self.function
        info['result'] = self.kwargs['result']
        return info

    def __copy__(self, another=None):
        if another is None:
            copied = FunctionThread(function=self.function)
        else:
            copied = another
        super().__copy__(copied)
        copied.function = self.function
        copied.function_kwargs = self.function_kwargs.copy()
        copied.function_return = self.function_return
        return copied

    def result(self):
        return self.function_return

    def __getattr__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            try:
                return self.kwargs.get(item)
            except AttributeError:
                return None
