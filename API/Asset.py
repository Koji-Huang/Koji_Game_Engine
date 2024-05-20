from typing import overload
from Config.BasicAssetConfig import AssetConfig
from API import GlobalAPI
from Function.parameter import filepath_set


def load_asset(config):
    if isinstance(config, str):
        asset = match_asset_type(config)
        load_asset(asset)
    elif isinstance(config, AssetConfig):
        filepath_set(GlobalAPI.AssetManager, config.sub_path, config)
    else:
        return None


def match_asset_type(config):
    pass


def save_asset(config):
    pass


def import_asset(config):
    pass

@overload
def get_asset():
    pass
@overload
def get_asset(path):
    pass
@overload
def get_asset(key, path):
    pass
def get_asset(key = None, path = None):
    pass