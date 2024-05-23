from Global import ID_Register
from . import Thread as __ThreadFile

import Thread.Thread as ThreadPackage
import Thread.ThreadPool as ThreadPoolPackage
import Thread.ThreadRunningMachine as ThreadRunningMachinePackage

from Thread.Thread import Thread, FunctionThread
from Thread.ThreadPool import ThreadPool
from Thread.ThreadRunningMachine import ThreadRunningMachine

_get, _recycle, _reset = ID_Register.customized('Thread', 'ThreadSystem')
__ThreadFile._thread_id_get = _get
__ThreadFile._thread_id_recycle = _recycle


from .Management import *


def __getattr__(name):
    if name == 'TRMachine':
        return Management.TRMachine
    if name == 'RECYCLED_ID':
        return Management.RECYCLED_ID
    if name == 'ID_DATA':
        return Management.ID_DATA
    raise AttributeError(f"Attribute {name} not found.")