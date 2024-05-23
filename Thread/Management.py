from typing import Union as _Union
from .Thread import Thread as _ThreadType
from .ThreadRunningMachine import ThreadRunningMachine as _ThreadRunningMachineType
strLT = _Union[list[str], tuple[str]]


ID_DATA: dict
RECYCLED_ID: dict
TRMachine: _ThreadRunningMachineType


def init():
    global ID_DATA, RECYCLED_ID, TRMachine
    ID_DATA = dict()
    RECYCLED_ID = dict()
    TRMachine = _ThreadRunningMachineType()


def move_thread(thread, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
    global ID_DATA, RECYCLED_ID, TRMachine
    if isinstance(thread, _ThreadType):
        return move_thread_thread(thread, targetPoolName, create_new_thread, remove_from_old_pool)
    if isinstance(thread, str):
        return move_thread_str(thread, targetPoolName, create_new_thread, remove_from_old_pool)
    raise "Thread Not Implemented"


def move_thread_str(thread: str, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
    global ID_DATA, RECYCLED_ID, TRMachine
    thread, old_pool_name = get_thread(thread)
    if thread is None:
        return False
    # match target thread targetPoolName
    target_pool = match_threadpool(targetPoolName)
    if target_pool is None:
        return False
    # match kwargs
    if remove_from_old_pool:
        old_pool = match_threadpool(old_pool_name)
        old_pool.remove(thread)
    if create_new_thread:
        thread = thread.__copy__()
        thread.pid = get_id('threadObject')
    # add thread
    target_pool.add(thread)
    return True


def move_thread_thread(thread: _ThreadType, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
    global ID_DATA, RECYCLED_ID, TRMachine
    old_pool_name = get_thread(pid=thread.pid, level=thread.threadLevel)[1]
    # match target thread targetPoolName
    target_pool = match_threadpool(targetPoolName)
    if target_pool is None:
        return False
    # match kwargs
    if remove_from_old_pool:
        match_threadpool(old_pool_name).remove(thread)
    if create_new_thread:
        thread = thread.__copy__()
        thread.pid = get_id('threadObject')
    # add thread
    target_pool.add(thread)
    return True


def move_threads(threads, targetPoolName, create_new_thread=False, remove_from_old_pool=True):
    global ID_DATA, RECYCLED_ID, TRMachine
    return [move_thread(thread, targetPoolName, create_new_thread, remove_from_old_pool) for thread in threads]


def add_thread(thread_object, pool="Imme", place=-1, create_new_thread: bool = True):
    global ID_DATA, RECYCLED_ID, TRMachine
    if thread_object is not None:
        # copy the thread object
        if create_new_thread:
            thread_object = thread_object.__copy__()
            thread_object.pid = get_id('threadObject')
        # match thread targetPoolName
        match_thread_pool = match_threadpool(pool)
        if match_thread_pool is None:
            match_thread_pool = TRMachine.ExceThreadPool
            thread_object.ErrorInfo = "PoolNotFound"
        # put thread into targetPoolName
        if place == -1:
            match_thread_pool.add(thread_object)
        else:
            match_thread_pool.insert(thread_object, place)
        # return result
        return thread_object
    else:
        return None


def add_threads(threadObjects, places=None, pools=None, create_new_thread=True):
    global ID_DATA, RECYCLED_ID, TRMachine
    ret = []
    if places is None:
        places = [-1 for _ in range(len(threadObjects))]
    if pools is None:
        pools = ["Stop" for _ in range(len(threadObjects))]
    for threadObject, place, pool in zip(threadObjects, places, pools):
        ret.append(add_thread(threadObject, place, pool, create_new_thread))
    return tuple(ret)


def remove_thread(removeThread, targetPoolName=None, level=None):
    global ID_DATA, RECYCLED_ID, TRMachine
    if isinstance(removeThread, _ThreadType):
        return remove_thread_thread(removeThread, targetPoolName, level)
    if isinstance(removeThread, str):
        return remove_thread_str(removeThread, targetPoolName, level)
    return False


def remove_thread_str(removeThread, target_pool_name=None, level=None):
    global ID_DATA, RECYCLED_ID, TRMachine
    thread, target_pool_name, level = get_thread(removeThread, target_pool_name, level)
    # Match _ThreadType Pool
    target_pool = match_threadpool(target_pool_name)
    # deal with things
    if thread is not None and target_pool is not None:
        target_pool.remove(thread, level)
        return True
    else:
        return False


def remove_thread_thread(removeThread, target_pool_name=None, level=None):
    global ID_DATA, RECYCLED_ID, TRMachine
    thread, target_pool_name, level = get_thread(removeThread.pid, target_pool_name, level)
    # Match _ThreadType Pool
    target_pool = match_threadpool(target_pool_name)
    # deal with things
    if thread is not None and target_pool is not None:
        target_pool.remove(thread, level)
        return True
    else:
        return False


def remove_threads(pids, pools, levels):
    global ID_DATA, RECYCLED_ID, TRMachine
    ret = []
    if pools is None:
        pools = [None for _ in range(len(pids))]
    if levels is None:
        levels = [None for _ in range(len(pids))]
    for pid, pools, levels in zip(pids, pools, levels):
        ret.append(remove_thread(pid))
    return tuple(ret)


def get_thread(pid, level=None, limit=None, eliminate=None):
    global ID_DATA, RECYCLED_ID, TRMachine
    if limit is not None:
        search_range = {i: all_thread_pool().get(i) for i in limit}
    else:
        search_range = all_thread_pool().value()
    if eliminate is not None:
        [search_range.pop(i) for i in eliminate]
    for threadPool in search_range:
        thread_pool_object = match_threadpool(threadPool)
        thread = thread_pool_object.finding(pid, level)
        if thread is not None:
            return thread, threadPool, level
    return None, None, None


def get_threads(pids, level=None, limit=None, eliminate=None):
    global ID_DATA, RECYCLED_ID, TRMachine
    return tuple(get_thread(pid, level, limit, eliminate) for pid in pids)


def get_id(objectType='undefined'):
    global ID_DATA, RECYCLED_ID, TRMachine
    if ID_DATA.get(objectType) is None:
        ID_DATA[objectType] = 0
        RECYCLED_ID[objectType] = list()
        return "0000000"
    else:
        if len(RECYCLED_ID[objectType]):
            return RECYCLED_ID[objectType].pop()
        else:
            ID_DATA[objectType] += 1
            length = len(str(ID_DATA[objectType]))
            primer_text = ''
            for i in range(7 - length):
                primer_text += '0'
            if ID_DATA[objectType]:
                return primer_text + '%d' % ID_DATA[objectType]


def get_thread_info(thread):
    global ID_DATA, RECYCLED_ID, TRMachine
    if isinstance(thread, _ThreadType):
        return get_thread_info_thread(thread)
    if isinstance(thread, str):
        return get_thread_info_str(thread)
    raise "No Info Available"


def get_thread_info_str(thread):
    global ID_DATA, RECYCLED_ID, TRMachine
    thread, pool, level = get_thread(thread)
    return {'pid': thread.pid, 'level': level, 'pool': pool, 'thread': thread}


def get_thread_info_thread(thread):
    global ID_DATA, RECYCLED_ID, TRMachine
    thread, pool, level = get_thread(thread.pid)
    return {'pid': thread.pid, 'level': level, 'pool': pool, 'thread': thread}


def match_threadpool(name):
    global ID_DATA, RECYCLED_ID, TRMachine
    collection = all_thread_pool()
    if name in collection.keys():
        return collection[name]
    else:
        return None


def clean_threadpool():
    global ID_DATA, RECYCLED_ID, TRMachine
    TRMachine.clean_pool()


def display_threadpool(pool=None):
    global ID_DATA, RECYCLED_ID, TRMachine
    if pool:
        match_threadpool(pool).display()
    else:
        print("Main Thread Pool:")
        TRMachine.MainThreadPool.display(end="\n|   ")
        print("\nLoop Thread Pool:")
        TRMachine.LoopThreadPool.display(end="\n|   ")
        print("\nImme Thread Pool:")
        TRMachine.ImmeThreadPool.display(end="\n|   ")
        print("\nStop Thread Pool:")
        TRMachine.StopThreadPool.display(end="\n|   ")
        print("\nExce Thread Pool:")
        TRMachine.ExceThreadPool.display(end="\n|   ")
        print("\n")


def info_threadpool(pool=None):
    global ID_DATA, RECYCLED_ID, TRMachine
    if pool:
        return match_threadpool(pool).info()
    else:
        info = dict()
        info["MainThreadPool"] = TRMachine.MainThreadPool.info()
        info["LoopThreadPool"] = TRMachine.LoopThreadPool.info()
        info["ImmeThreadPool"] = TRMachine.ImmeThreadPool.info()
        info["StopThreadPool"] = TRMachine.StopThreadPool.info()
        info["ExceThreadPool"] = TRMachine.ExceThreadPool.info()
        return info


def all_thread_pool():
    global ID_DATA, RECYCLED_ID, TRMachine
    return TRMachine.get_all_pool()


def __iter__():
    global ID_DATA, RECYCLED_ID, TRMachine
    return iter(all_thread_pool().value)
