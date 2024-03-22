from typing import TypeVar, Generic

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_T = TypeVar('_T')


class CustomGeneric(Generic[_KT, _VT]):
    extract_from_head: bool = True

    def __init__(self):
        """
        Basic Custom Generic Template
        """
        pass

    def append(self, value: _VT):
        """
        Append a value to the end of the list
        :param value: value to be appended
        """
        pass

    def insert(self, index, value: _VT) -> None:
        """
        Append a value to the beginning of the generic
        :param index: index of the value to be appended
        :param value: value to be appended
        :return: None
        """
        pass

    def remove(self, value: _T) -> None:
        """
        Remove a value from the end of the generic
        :param value: value to be removed
        :return: None
        """
        pass

    def size(self) -> int:
        """
        Return the size of the generic
        :return: size of the generic
        """
        pass

    def clear(self) -> None:
        """
        Remove all values from the generic
        :return: None
        """
        pass

    def reverse(self) -> None:
        """
        Reverse the generic order
        :return: None
        """
        pass

    def show(self) -> None:
        """
        Print the generic order
        :return: None
        """
        pass

    def extract(self, index: int = None) -> any or None:
        """
        Extract a value from the generic
        :param index: index of the value to be extracted, defaults to CustomGeneric.extract_from_head
        """
        pass

    def __item__(self) -> tuple:
        """
        Return the generic item
        :return: generic item
        """
        pass

    def __copy__(self) -> any:
        """
        Return a new copy of the generic
        :return: a copy of the generic
        """
        pass

    def __len__(self) -> int:
        """
        Return the size of the generic
        :return: size of the generic
        """
        pass

    def __iter__(self) -> iter:
        """
        Return an iterator over the generic
        :return: an iterator over the generic
        """
        pass

    def __setitem__(self, key, value) -> None:
        """
        Set a value in the generic
        :param key: key of the value to be set
        :param value: value to be set
        :return: None
        """
        pass

    def __delitem__(self, key) -> None:
        """
        Delete a value from the generic
        :param key: key of the value to be deleted
        :return: None
        """
        pass

    def __getitem__(self, item) -> _T:
        """
        Get a value from the generic
        :param item: key of the value to be get
        :return: value from the generic
        """
        pass

    def __contains__(self, *args, **kwargs) -> bool:
        """
        Check if a value is in the generic
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: True if value is in the generic
        """
        pass

    def __iadd__(self, *args, **kwargs) -> CustomGeneric:
        """
        add a value to the generic
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: None
        """
        pass
