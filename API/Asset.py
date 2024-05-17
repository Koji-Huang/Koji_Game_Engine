from typing import overload
from DataType.ConfigFile.BasicAssetConfig import AssetConfig
from API import GlobalAPI
from Function.parameter import filepath_set


@overload
def load_asset(configObject: AssetConfig):...
@overload
def load_asset(file: str):...


def load_asset(config):
    if isinstance(config, str):
        asset = match_asset_type(config)
        load_asset(asset)
    elif isinstance(config, AssetConfig):
        filepath_set(GlobalAPI.Asset, config.sub_path, config)
    else:
        return None


def match_asset_type(config):
    pass


def save_asset(config):
    pass


def import_asset(config):
    pass
