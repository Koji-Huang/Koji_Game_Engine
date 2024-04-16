from typing import TypeVar
from DataType.Generic.CustomGeneric import CustomGeneric

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_T = TypeVar('_T')


class LinkedListNode:
    value: _T
    next: LinkedListNode | None
    last: LinkedListNode | None

    def __init__(self, value: _T, father: LinkedListNode = None):
        ...

    def __next__(self) -> LinkedList | None:
        ...

    def __reversed__(self):
        ...

    def __len__(self) -> int:
        ...

    def append(self, value: _VT):
        ...

    def insert(self, value: LinkedListNode | any):
        ...

    def remove(self):
        ...


class LinkedList(CustomGeneric[_KT, _VT]):
    size: int
    head: LinkedListNode | None
    tail: LinkedListNode | None
    extract_from_head: bool

    def __init__(self):
        ...

    def append(self, value: _VT):
        ...

    def insert(self, index, value: _VT):
        ...

    def remove(self, value: _T):
        ...

    def size(self):
        ...

    def clear(self):
        ...

    def reverse(self):
        ...

    def show(self):
        ...

    def pop(self, index: int = None):
        ...

    def extend(self, value):
        ...

    def __copy__(self) -> LinkedList:
        ...

    def __get_node__(self, index: int) -> LinkedListNode:
        ...

    def __search_node__(self, value: _T) -> LinkedListNode | None:
        ...

    def __len__(self):
        ...

    def __iter__(self):
        ...

    def __setitem__(self, key, value):
        ...

    def __delitem__(self, key):
        ...

    def   __getitem__(self, item):
        ...

    def __contains__(self, *args, **kwargs) -> tuple[_T]:
        ...

    def __iadd__(self, *args, **kwargs):
        ...

    def __item__(self):
        ...