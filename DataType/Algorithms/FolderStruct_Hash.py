from typing import Mapping, Union, Iterable
from ..CustomizedPath import CustomizedPath
from random import randint
folderPath = Union[str, list, tuple, CustomizedPath]


class Folder(Mapping):
    def __init__(self, name: str = 'undefined', hash_width: int = 29, no_son_folder: bool = False):
        if hash_width:
            self._hash = hash_width
        if no_son_folder:
            self._son_folder = None
        else:
            self._son_folder = tuple(dict() for _ in range(self._hash))
        self._values = tuple(dict() for _ in range(self._hash))
        self._name = name
        self.add = self.__setitem__
        self.remove = self.__delitem__
        self.get = self.__getitem__
        self.cd = self.match_son_folder

    def __iter__(self, folder_path: folderPath = None):
        if folder_path:
            son = self.match_son_folder(folder_path)
            return son.__iter__()
        else:
            return iter(self._values)

    def __len__(self, folder_path: folderPath = None):
        if folder_path:
            son = self.match_son_folder(folder_path)
            return son.__len__()
        else:
            return self._values.__len__()

    def __getitem__(self, __key, folder_path: folderPath = None):
        if folder_path:
            son = self.match_son_folder(folder_path)
            return son.__getitem__(__key)
        else:
            index = self.hash_index(__key)
            ret = self._values[index].__getitem__(__key)
            if ret is None and self._son_folder is not None:
                return self._son_folder[index].__getitem__(ret)
            return ret

    def __setitem__(self, key, value=None, folder_path: folderPath = None):
        if folder_path:
            son = self.match_son_folder(folder_path)
            return son.__setitem__(key, value)
        else:
            index = self.hash_index(key)
            if isinstance(key, Folder):
                if self._son_folder is not None:
                    self._son_folder[index][key._name] = key
            else:
                self._values[index][key] = value

    def __delitem__(self, key, folder_path: folderPath = None):
        if folder_path:
            son = self.match_son_folder(folder_path)
            return son.__delitem__(key)
        else:
            index = self.hash_index(key)
            if isinstance(key, Folder) and self._son_folder is not None:
                self._son_folder[index].pop(key)
            else:
                self._values[index].pop(key)

    def hash_index(self, item):
        return hash(item) % self._hash

    def match_son_folder(self, folder_path):
        if self._son_folder is None:
            return None
        if folder_path.__len__() == 0:
            return self
        if not isinstance(folder_path, Iterable):
            folder_path = CustomizedPath(folder_path).__tuple__()
        index = self.hash_index(folder_path[0])
        if self._son_folder[index].__getitem__(folder_path[0]):
            return self._son_folder[index].match_son_folder(folder_path[1:])

    def __hash__(self):
        return hash(id(self) * randint(1, 100))

    def items(self):
        return zip(i.values() for i in self._values)

    def folders(self):
        return zip(i.items() for i in self._son_folder)
