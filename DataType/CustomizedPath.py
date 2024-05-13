from typing import Iterable
from Function.parameter import filepath_analysis


class CustomizedPath:
    _convert_path: tuple

    def __init__(self, path: str or Iterable):
        if isinstance(path, str):
            self._convert_path = filepath_analysis(path)
        else:
            self._convert_path = tuple(path)

    def __str__(self):
        ret = ''
        for i in self._convert_path:
            ret += i + "\\"
        return ret[:-1]

    def __iter__(self):
        return self._convert_path.__iter__()

    def __tuple__(self):
        return self._convert_path

    def __list__(self):
        return list(self._convert_path)

    def __len__(self):
        return len(self._convert_path)

    def __setitem__(self, key, value):
        self._convert_path = ((self._convert_path[:key] if key > 0 else ()) +
                              (value, ) + (self._convert_path[:key + 1] if key + 1 < self._convert_path.__len__() else ()))

    def __getitem__(self, item):
        return self._convert_path[item]

    def __delitem__(self, key):
        self._convert_path = self._convert_path[:key] + self._convert_path[key+1:]

    def __copy__(self):
        return CustomizedPath(self)

    def __add__(self, other):
        if not isinstance(other, CustomizedPath):
            other = filepath_analysis(other)
        return CustomizedPath(other + self._convert_path)

    def __iadd__(self, other):
        if not isinstance(other, CustomizedPath):
            other = filepath_analysis(other)
        self._convert_path += other

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if not isinstance(other, CustomizedPath):
            other = filepath_analysis(other)
        else:
            other = other._convert_path
        return self._convert_path == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.__str__()
