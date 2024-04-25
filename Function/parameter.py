from typing import TypeVar, Any, Mapping

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_T = TypeVar('_T')


def dict_key_intersection(*args: dict) -> tuple[Any, ...]:
    ret = list()
    for key in args[0].keys():
        for each in args[1:]:
            if each.get(key) is None:
                break
        else:
            ret.append(key)
    return tuple(ret)


def dict_intersection(*args: dict) -> dict[_KT, _VT]:
    ret = dict()
    for key in args[0].keys():
        val = args[0][key]
        for each in args[1:]:
            if each.get(key) != val:
                break
        else:
            ret[key] = val
    return ret


def merge_dict_FIFO(*args) -> dict:
    # First in First out(merge in)
    kwargs = dict()
    for i in args:
        if i is not None:
            kwargs.update(i)
    return kwargs


def merge_dict_FILO(*args) -> dict:
    # First in Last out(merge in)
    return merge_dict_FIFO(*args[::-1])


def mix_series(series_A: tuple[_T, ...], series_B: tuple[_T, ...]):
    ret = list()
    for i in range(series_B.__len__()):
        ret.append(series_B[i])
    if series_A.__len__() > series_B.__len__():
        for i in range(series_B.__len__(), series_A.__len__()):
            ret.append(series_A[i])
    return tuple(ret)


def mapping_merge(target: Mapping, merge_into: Mapping):
    for key, item in merge_into.items():
        # Double of them are mapping
        if isinstance(item, Mapping) and isinstance(target.get(key), Mapping):
            mapping_merge(target[key], item)
        else:
            target[key] = item


def mapping_new_copy(mapping: Mapping) -> dict:
    ret = dict()
    for key, item in mapping.items():
        if isinstance(item, Mapping):
            ret[key] = mapping_new_copy(item)
        else:
            ret[key] = item
    return ret
