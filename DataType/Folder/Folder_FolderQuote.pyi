from typing import overload, Union, Mapping
from .FolderStruct_Hash import Folder


QuoteDataType = Union[Folder, FolderQuote]


class FolderQuote(Mapping):
    __readable = bool
    __writeable = bool
    __savable = bool
    __quote_object: Folder
    __disable_outer_get: bool
    __tmp_attr: Folder | None
    __quote_info: QuoteDataType | None

    readable = bool
    writeable = bool
    savable = bool
    disable_outer_get: bool
    quote_info: QuoteDataType | None

    @overload
    def __init__(self,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True): pass
    @overload
    def __init__(self,
                 path: QuoteDataType,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True): pass
    def __init__(self, folder_info, readable = True, writeable = True, savable = True):
        pass

    def set_quote(self, asset_info: QuoteDataType,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None:
        pass

    def remove_quote(self) -> None:
        pass

    def get_quote_folder(self) -> Folder:
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass

    def __len__(self) -> int:
        pass

    def items(self):
        pass

    def get(self, __key: any) -> any:
        pass

    def keys(self) -> any:
        pass

    def values(self):
        pass

    def get_quote_attr(self, item):
        pass