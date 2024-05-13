from typing import Callable


class PackagedCallable(Callable):

    def __init__(self, function: Callable = None, *args, **kwargs):
        self.save_function = function
        self.save_args = args if args is not None else tuple()
        self.save_kwargs = kwargs if kwargs is not None else dict()

    def __call__(self, *args, **kwargs):
        args += self.save_args
        kwargs.update(self.save_kwargs)

        self.save_function(*args, **kwargs)
