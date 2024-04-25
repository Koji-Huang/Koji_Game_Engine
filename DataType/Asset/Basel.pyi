from typing import overload
from DataType.ConfigFile.Asset.BaselAssetConfig import AssetConfig


class Asset:
    name: str
    type: str
    path: str
    configObject: AssetConfig

    def __init__(self, assetConfigObject: AssetConfig, *args, **kwargs):
        """

        """
        pass

    def __copy__(self, copied: Asset = None):
        """

        """
        pass

    def __call__(self, *args, **kwargs) -> any:
        """

        """
        pass

    def convert(self) -> any:
        """

        """
        pass

    def load(self, *args, **kwargs):
        """

        """
        pass



class AssetFolder:
    _name: str
    _assets: dict[str, [Asset]]
    _folder: dict[str, [AssetFolder]]
    _converted: dict[str, [any]]

    def __init__(self, name: str = 'undefined', *args, **kwargs):
        """
        init package resource
        """
        pass

    def __call__(self, *args, **kwargs) -> any:
        """
        get package resource
        :return: any
        """
        pass

    def __copy__(self, copied: AssetFolder = None) -> AssetFolder:
        """
        copy package and send back another
        :return: copy object
        """
        pass

    def reload(self) -> None:
        """
        reload package resource
        :return: None
        """
        pass

    def folder(self) -> tuple[AssetFolder]:
        """
        return son folder
        """
        pass

    @overload
    def package(self, contain_son: bool = False) -> tuple[Asset]:
        """
        return tuple of packages on this folder
        """
        pass

    @overload
    def package(self, id: str) -> Asset:
        """
        return the package
        it will search in son package
        """
        pass

    @overload
    def package(self, name: str, contain_son: bool = True) -> tuple[Asset]:
        """
        return the search package
        """
        pass

    def __getitem__(self, item: str) -> Asset | AssetFolder:
        """

        """
        pass

    def __setitem__(self, key: str, value: AssetFolder | Asset):
        """

        """
        pass

    def __delitem__(self, key: str):
        """

        """
        pass

    def __iter__(self):
        """
        return package and folder iter
        """
