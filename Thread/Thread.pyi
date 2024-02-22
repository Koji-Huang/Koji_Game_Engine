from types import FunctionType


class Thread:
    threadLevel: str
    kwargs: dict

    def __init__(self, threadLevel: str = 'undefined', **kwargs):
        """
        Initialize the threadObject
        :param threadLevel: the process' level
        :param kwargs: other kwargs
        """

    def start(self, **kwargs) -> None:
        """
        Start run the Thread
        :return:
        """

    def info(self) -> dict:
        """
        return the info of this object
        :return: dict of information
        """

    def result(self) -> dict:
        """
        the result args
        :return: the args
        """

    def __del__(self) -> None:
        ...

    def __getitem__(self, item: str) -> any:
        ...

    def __call__(self, **kwargs) -> any:
        ...


class FunctionThread(Thread):
    function: FunctionType

    def __init__(self, function: FunctionType, function_kwargs: dict, threadLevel: str = 'undefined', **kwargs):
        """
        This Thread can receive a function to run
        :param function: the run function
        :param function_kwargs: the kwargs of the function
        :param threadLevel: the process' level
        :param kwargs: other args
        """
        ...

    def start(self, **kwargs) -> None:
        ...