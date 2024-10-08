from typing import overload
from Config.BasicAssetConfig import AssetConfig
from Asset.AbstractAsset import Asset as AssetObject
from .AssetRegister import AssetManager


RegisteredAssetType: dict[str, [AssetObject]]
RegisteredAsset: AssetManager

@overload
def load_asset(configObject: AssetConfig):...
@overload
def load_asset(asset_type: str): ...
def load_asset(config):...

@overload
def get_asset():...
@overload
def get_asset(path):...
@overload
def get_asset(key, path):...
def get_asset(key = None, path = None):...

@overload
def save_asset(config: AssetConfig):...
@overload
def save_asset(path: str):...
def save_asset(config):...

@overload
def import_asset(config):...
@overload
def import_asset(file):...
def import_asset(config):...

@overload
def match_asset_type(config: AssetConfig) -> type(AssetObject):...
@overload
def match_asset_type(type_name: str) -> type(AssetObject):...
def match_asset_type(config) -> type(AssetObject):...


@overload
def create_asset(config) -> type(AssetConfig):...
@overload
def create_asset(file_path) -> type(AssetConfig):...
def create_asset(config) -> type(AssetConfig):...


def load_system_asset_type():
    pass
