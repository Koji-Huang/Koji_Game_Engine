from typing import overload, Union, Iterable
from .AbstractAsset import Asset
from DataType.Algorithms.FolderStruct_Hash import Folder, folderPath


QuoteDataType = Union[Folder, AssetQuote, folderPath]


class AssetQuote(Folder[str, [Asset, any]]):
    __readable = tuple[bool]
    __writeable = tuple[bool]
    __savable = tuple[bool]
    __tmp_asset_poor: Folder
    __quotes: tuple[QuoteDataType]

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
    @overload
    def __init__(self,
                 path: Iterable[QuoteDataType],
                 readable: tuple[bool] | bool = True,
                 writeable: tuple[bool] | bool = True,
                 savable: tuple[bool] | bool = True): pass
    def __init__(self, folder_info, readable = True, writeable = True, savable = True):
        pass

    @overload
    def add_quote(self, asset_info: QuoteDataType,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None: pass
    @overload
    def add_quote(self, asset_info: Iterable[QuoteDataType],
                  readable: tuple[bool] | bool = True,
                  writeable: tuple[bool] | bool = True,
                  savable: tuple[bool] | bool = True) -> None: pass
    def add_quote(self, asset_info):
        pass

    @overload
    def remove_quote(self,
                     asset_info: QuoteDataType) -> None: pass
    @overload
    def remove_quote(self,
                     asset_info: Iterable[QuoteDataType]) -> None: pass
    def remove_quote(self, asset_info) -> None: pass

    def get_quote(self) -> tuple[QuoteDataType]:
        pass

    def get_quote_folder(self) -> tuple[Folder]:
        pass


@overload
def customize_path(
        asset_path: QuoteDataType) -> AssetQuote: pass
@overload
def customize_path(
        asset_folder: Iterable[QuoteDataType]) -> AssetQuote: pass
def customize_path(
        asset_info) -> AssetQuote:
    pass
