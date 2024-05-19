from typing import Mapping, Union, Iterable
from ..CustomizedPath import CustomizedPath
from random import randint

folderPath = Union[str, list, tuple, CustomizedPath]


def path_include_folder(path):
    if isinstance(path, CustomizedPath):
        return True
    if isinstance(path, str):
        return '\\' in path
    if isinstance(path, Iterable):
        for i in path:
            if isinstance(i, str) is False:
                return False
        return True


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
        self.set = self.__setitem__
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

        # if target the folder_path
        if folder_path:
            folder_path = CustomizedPath(folder_path, True)
            matched = self.match_son_folder(folder_path)
            return matched.__getitem__(__key) if matched is not None else None

        # if __key include path
        elif path_include_folder(__key):
            path = CustomizedPath(__key)
            if path.is_folder:
                return self.match_son_folder(path)
            else:
                folder = self.match_son_folder(path[:-1])
                return folder.__getitem__(path[-1]) if folder is not None else None

        else:
            # Hash get
            line = self._values[self.hash_index(__key)]
            if __key in line.keys():
                return line[__key]
            else:
                return None

    def __setitem__(self, key, value=None, folder_path: folderPath = None):
        if folder_path:
            folder_path = CustomizedPath(folder_path, True)
            matched = self.match_son_folder(folder_path)
            if matched is None:
                matched = self.create_folder(folder_path)
            return matched.__setitem__(key, value)
        elif path_include_folder(key):
            folder_path = CustomizedPath(key)
            if folder_path.is_folder:
                if value is None:
                    self.create_folder(folder_path)
                else:
                    matched = self.create_folder(folder_path[:-1])
                    value._name = folder_path[-1]
                    matched.__setitem__(value)
            else:
                return self.__setitem__(folder_path[-1], value, folder_path.folder())
        else:

            # Normal Key-Value Parameter
            if isinstance(key, Folder):
                # Key is Folder
                self._son_folder[self.hash_index(key._name)][key._name] = key

            elif isinstance(value, Folder):
                # Value is Folder
                value._name = key
                self._son_folder[self.hash_index(key)][key] = key

            else:
                # value is normal value
                self._values[self.hash_index(key)][key] = value

            return

    def __delitem__(self, key, folder_path: folderPath = None, is_folder: bool = False) -> None:
        if path_include_folder(key):
            path = CustomizedPath(key)
            matched = self.match_son_folder(path[:-1])
            if matched is not None:
                return matched.__delitem__(path[-1], path.is_folder)
        if folder_path:
            son = self.match_son_folder(folder_path)
            return son.__delitem__(key, is_folder)
        else:
            index = self.hash_index(key)
            if (isinstance(key, Folder) or is_folder) and self._son_folder is not None:
                self._son_folder[index].pop(key)
            else:
                self._values[index].pop(key)

    def hash_index(self, item):
        try:
            return hash(item) % self._hash
        except TypeError:
            return hash(id(item)) % self._hash

    def match_son_folder(self, folder_path):
        if self._son_folder is None:
            return None
        if folder_path.__len__() == 0:
            return self
        if not isinstance(folder_path, Iterable):
            folder_path = CustomizedPath(folder_path).__tuple__()
        index = self.hash_index(folder_path[0])
        if folder_path[0] in self._son_folder[index]:
            return self._son_folder[index][folder_path[0]].match_son_folder(folder_path[1:])

    def __hash__(self):
        return hash(id(self) * randint(1, 100))

    def items(self):
        return zip(i.values() for i in self._values)

    def folders(self):
        return zip(i.items() for i in self._son_folder)

    def create_folder(self, path):
        folder_path = CustomizedPath(path, True)
        x = self
        for name in folder_path:
            if name not in x._son_folder[x.hash_index(name)]:
                new_folder = Folder(name)
                x._son_folder[x.hash_index(name)][name] = new_folder
            else:
                new_folder = x._son_folder[x.hash_index(name)][name]
            x = new_folder
        return x

    def keys(self):
        x = list()
        for line in self._values:
            x += line.keys()
        return tuple(x)

    def update(self, another):
        for key, value in another.items():
            if isinstance(value, Mapping):
                self[key] = Folder(key)
                self[key].update(value)
            else:
                self[key] = value
