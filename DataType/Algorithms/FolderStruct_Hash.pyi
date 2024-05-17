from typing import Mapping, Iterable, Hashable, Union, overload, ItemsView, TypeVar
from ..CustomizedPath import CustomizedPath
folderPath = Union[str, list, tuple, CustomizedPath]

_T = TypeVar("_T")


class Folder(Mapping[_T]):
    _name: str
    _hash: int
    _son_folder: tuple[dict[str, [Folder, ...]], ...] or None
    _values: tuple[dict[str, [any, ...]], ...]

    def __init__(self, name: str = 'undefined', hash_width: int = None, no_son_folder: bool = False):...

    def __iter__(self, folder_path: folderPath = None) -> Iterable:...

    def __len__(self, folder_path: folderPath = None) -> int:...

    @overload
    def __getitem__(self, __key: Hashable) -> _T:
        """
        Use key to get item
        """
    @overload
    def __getitem__(self, __key: Hashable, folder_path: folderPath = None) -> _T:
        """
        Use key and path to get value
        """
    @overload
    def __getitem__(self, __key: folderPath | CustomizedPath) -> Folder:
        """
        Use path to get folder
        """
    def __getitem__(self, __key: Hashable, folder_path: folderPath = None) -> _T:
        pass

    @overload
    def __setitem__(self, key: Folder | folderPath) -> None:...
    @overload
    def __setitem__(self, key: Hashable, value: _T | Folder) -> None:...
    @overload
    def __setitem__(self, key: Hashable, value: _T | Folder, folder_path: folderPath) -> None:...
    def __setitem__(self, key, value = None, folder_path = None) -> None:...

    @overload
    def __delitem__(self, key: Hashable, is_folder: bool = False) -> None:...
    @overload
    def __delitem__(self, key: Hashable, folder_path: folderPath = None, is_folder: bool = False) -> None:...
    def __delitem__(self, key, folder_path: folderPath = None, is_folder: bool = False) -> None:...

    def __hash__(self):...

    def hash_index(self, item: Hashable) -> int:...

    def match_son_folder(self, folder_path: folderPath) -> Folder:...

    @overload
    def set(self, key: Folder) -> None:...
    @overload
    def set(self, key: Hashable, value: _T | Folder) -> None:...
    @overload
    def set(self, key: Hashable, value: _T | Folder, folder_path: folderPath) -> None:...
    def set(self, key, value, folder_path = None) -> None:...

    @overload
    def get(self, __key: Hashable) -> _T:
        """
        Use key to get item
        """
    @overload
    def get(self, __key: Hashable, folder_path: folderPath = None) -> _T:
        """
        Use key and path to get value
        """
    @overload
    def get(self, __key: folderPath | CustomizedPath) -> Folder:
        """
        Use path to get folder
        """
    def get(self, __key: Hashable, folder_path: folderPath = None) -> _T:
        pass

    @overload
    def remove(self, key: Hashable, is_folder: bool = False) -> None:...
    @overload
    def remove(self, key: Hashable, folder_path: folderPath = None, is_folder: bool = False) -> None:...
    def remove(self, key, folder_path: folderPath = None, is_folder: bool = False) -> None:...

    def items(self) -> ItemsView[_T]:
        pass

    def folders(self) -> ItemsView[Folder]:
        pass

    def create_folder(self, path) -> Folder:
        pass

    def keys(self) -> tuple(str):
        pass