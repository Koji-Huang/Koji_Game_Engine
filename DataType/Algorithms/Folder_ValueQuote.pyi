from typing import overload, Union, TypeVar
from .FolderStruct_Hash import Folder


QuoteFolder = Union[Folder, ValueQuote]
QuoteDataType = TypeVar("QuoteDataType")


class ValueQuote(QuoteDataType):
    __readable: bool
    __writeable: bool
    __savable: bool
    __quote_Folder: Folder | None
    __quote_key: any
    __tmp_attr: Folder | None
    __disable_outer_get: bool
    readable: bool
    writeable: bool
    savable: bool
    quote_Folder: Folder | None
    quote_key: any
    disable_outer_get: bool

    @overload
    def __init__(self,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True,
                 disable_outer_get: bool = False): pass
    @overload
    def __init__(self,
                 path: QuoteFolder,
                 key: any,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True,
                 disable_outer_get: bool = False): pass
    def __init__(self, folder = None, key = None, readable = True, writeable = True, savable = True,
                 disable_outer_get: bool = False):
        pass

    def set_quote(self,
                  folder: QuoteFolder,
                  key: str,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None:
        pass

    def remove_quote(self) -> None:
        pass

    def get_quote_key(self) -> QuoteDataType:
        pass

    def get_quote_folder(self) -> Folder:
        pass

    def get_quote_attr(self, item):
        pass