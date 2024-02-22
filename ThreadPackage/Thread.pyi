from types import FunctionType

"""
ThreadPackage Object:

    This object is used to run thread and collect info.
    
    Manifestation parameters:
        threadLevel:
            the level thread be in, level is used to grade thread
        kwargs:
            collection of invisible kwargs
        pid:
            the id of the process
        
    Invisible parameters:
        ErrorInfo:
             if the thread got error, it will be putted into ExecThreadPool 
             and Record Error Info to analysis
        OriginalOwner:
            when the ThreadPackage is be putted into StopThreadPool,
            it will record the original Pool Name to recovery
        RecyclingOrNot:
            When a ThreadPackage run. It might not run twice, so it should be recycle.
            This object  is used to tell the system if it should be recycled. 
"""
class Thread:
    threadLevel: str
    kwargs: dict
    pid: str

    def __init__(self, threadLevel: str = 'undefined', **kwargs):
        """
        Initialize the threadObject
        :param threadLevel: the process' level
        :param kwargs: other kwargs
        """

    def start(self, **kwargs) -> None:
        """
        Start run the ThreadPackage
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

    def __call__(self, **kwargs) -> any:
        ...

    def __copy__(self) -> Thread:
        ...

    def __getattr__(self, item):
        ...


"""
FunctionThread

    This object is used to build thread witch only run a function quickly
    This object is callable, when it  called, it will start the function
    
    Manifestation parameters:
        function: the function to run
        function_kwargs: the parameters to remain
        function_return: the return value of the function
    
    Invisible parameters:
        None
"""
class FunctionThread(Thread):
    function: FunctionType
    function_kwargs: dict
    function_return: any

    def __init__(self, function: FunctionType, function_kwargs: dict, threadLevel: str = 'undefined', **kwargs):
        """
        This ThreadPackage can receive a function to run
        :param function: the run function
        :param function_kwargs: the kwargs of the function
        :param threadLevel: the process' level
        :param kwargs: other args
        """
        ...

    def start(self, **kwargs) -> None:
        ...

    def info(self):
        ...

    def __copy__(self):
        ...

    def __getattr__(self, item):
        ...