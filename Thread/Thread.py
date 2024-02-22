from types import FunctionType


class Thread:
    threadLevel: str
    kwargs: dict

    def __init__(self, threadLevel: str = 'undefined', **kwargs):
        self.kwargs = kwargs
        self.threadLevel = threadLevel

    def start(self, **kwargs) -> None:
        print("Default Thread Running----")

    def info(self):
        return {"threadLevel": self.threadLevel, "kwargs": self.kwargs}

    def result(self):
        return self.kwargs.get("result")

    def __del__(self):
        pass

    def __getitem__(self, item):
        return self.kwargs.get(item)

    def __call__(self, **kwargs):
        return self.start(**kwargs)


class FunctionThread(Thread):
    def __init__(self, function: FunctionType, function_kwargs: dict, threadLevel: str = 'undefined', **kwargs):
        super().__init__(threadLevel, **kwargs)
        self.function = function
        self.kwargs['function_kwargs'] = function_kwargs

    def start(self, **kwargs) -> None:
        self.kwargs.update(kwargs)
        self.kwargs["result"] = self.function(**self.kwargs.get('function_kwargs'), **kwargs)

    def info(self):
        info = super(FunctionThread, self).info()
        info['function'] = self.function
        info['result'] = self.kwargs['result']
        return info
