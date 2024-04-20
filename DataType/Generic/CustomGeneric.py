from abc import ABCMeta, abstractmethod
from typing import TypeVar, Iterable

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_T = TypeVar('_T')


class CustomGeneric(metaclass=ABCMeta):
    extract_from_head = True

    @abstractmethod
    def __init__(self):
        """
        Basic Custom Generic Template
        """
        pass

    @abstractmethod
    def append(self, value):
        """
        Append a value to the end of the list
        :param value: value to be appended
        """
        pass

    @abstractmethod
    def insert(self, index, value):
        """
        Append a value to the beginning of the generic
        :param index: index of the value to be appended
        :param value: value to be appended
        :return: None
        """
        pass

    @abstractmethod
    def remove(self, value):
        """
        Remove a value from the end of the generic
        :param value: value to be removed
        :return: None
        """
        pass

    @abstractmethod
    def size(self):
        """
        Return the size of the generic
        :return: size of the generic
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Remove all values from the generic
        :return: None
        """
        pass

    @abstractmethod
    def reverse(self):
        """
        Reverse the generic order
        :return: None
        """
        pass

    @abstractmethod
    def show(self):
        """
        Print the generic order
        :return: None
        """
        pass

    @abstractmethod
    def pop(self, index=None):
        """
        Extract a value from the generic
        :param index: index of the value to be extracted, defaults to CustomGeneric.extract_from_end
        """
        pass

    @abstractmethod
    def extend(self, value: Iterable[_T]):
        """
        merge another Sequence
        """
        pass

    @abstractmethod
    def __item__(self):
        """
        Return the generic item
        :return: generic item
        """
        pass

    @abstractmethod
    def __copy__(self):
        """
        Return a new copy of the generic
        :return: a copy of the generic
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        Return the size of the generic
        :return: size of the generic
        """
        pass

    @abstractmethod
    def __iter__(self):
        """
        Return an iterator over the generic
        :return: an iterator over the generic
        """
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        """
        Set a value in the generic
        :param key: key of the value to be set
        :param value: value to be set
        :return: None
        """
        pass

    @abstractmethod
    def __delitem__(self, key):
        """
        Delete a value from the generic
        :param key: key of the value to be deleted
        :return: None
        """
        pass

    @abstractmethod
    def __getitem__(self, item):
        """
        Get a value from the generic
        :param item: key of the value to be get
        :return: value from the generic
        """
        pass

    @abstractmethod
    def __contains__(self, *args, **kwargs):
        """
        Check if a value is in the generic
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: True if value is in the generic
        """
        pass

    @abstractmethod
    def __iadd__(self, *args, **kwargs):
        """
        add a value to the generic
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: None
        """
        pass
