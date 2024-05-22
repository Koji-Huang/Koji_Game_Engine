from typing import overload, Union
from .AbstractAsset import Asset
from DataType.Folder.FolderStruct_Hash import Folder, folderPath
from DataType.Folder.Folder_ValueQuote import ValueQuote

QuoteDataType = Union[Folder, AssetQuote, folderPath]


class AssetQuote(ValueQuote):
    @overload
    def __init__(self,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True,
                 disable_outer_get: bool = False): pass
    @overload
    def __init__(self,
                 path: str,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True,
                 disable_outer_get: bool = False): pass
    @overload
    def __init__(self,
                 asset: Asset,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True,
                 disable_outer_get: bool = False): pass
    @overload
    def __init__(self,
                 path: QuoteDataType,
                 key: any,
                 readable: bool = True,
                 writeable: bool = True,
                 savable: bool = True,
                 disable_outer_get: bool = False): pass
    def __init__(self, folder = None, key = None, readable = True, writeable = True, savable = True,
                 disable_outer_get: bool = False):
        pass

    @overload
    def set_quote(self,
                  path: str,
                  key: str,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None:...
    @overload
    def set_quote(self,
                  path: str,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True, *args) -> None:...

    @overload
    def set_quote(self,
                  asset: Asset,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True, *args) -> None:...

    def set_quote(self,
                  folder: QuoteDataType,
                  key: str,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None:
        pass

    def get_quote(self) -> Asset or None:
        pass

