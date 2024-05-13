from typing import Callable


class PackagedCallable(Callable):
    save_function: Callable
    save_kwargs: dict
    save_args: tuple

    def __init__(self, function: Callable = None, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        pass


