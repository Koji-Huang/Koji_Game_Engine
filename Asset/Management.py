
from Function.parameter import filepath_set
from . import RegisteredAssetType


def load_asset(config):
    from Config.BasicAssetConfig import AssetConfig
    if isinstance(config, str):
        asset = match_asset_type(config)
        load_asset(asset)
    elif isinstance(config, AssetConfig):
        from api import GlobalAPI
        filepath_set(GlobalAPI.AssetManager, config.pat, config)
    else:
        return None


def match_asset_type(config):
    from Config.BasicAssetConfig import AssetConfig
    if isinstance(config, AssetConfig):
        config = config.config_file_format
    return RegisteredAssetType.get(config)


def save_asset(config):
    pass


def import_asset(config):
    pass


def get_asset(key=None, path=None):
    pass


def load_system_asset_type():
    import Config as SystemConfigFile
    RegisteredAssetType["Animation"] = SystemConfigFile.AnimationAssetConfig.Animation
    RegisteredAssetType["animation"] = SystemConfigFile.AnimationAssetConfig.Animation
    RegisteredAssetType["Image"] = SystemConfigFile.ImageAssetConfig.Image
    RegisteredAssetType["image"] = SystemConfigFile.ImageAssetConfig.Image
    RegisteredAssetType["Script"] = SystemConfigFile.ScriptAssetConfig.Script
    RegisteredAssetType["script"] = SystemConfigFile.ScriptAssetConfig.Script
    RegisteredAssetType["Ini"] = SystemConfigFile.Basel.Ini
    RegisteredAssetType["ini"] = SystemConfigFile.Basel.Ini
    RegisteredAssetType["Json"] = SystemConfigFile.Basel.Json
    RegisteredAssetType["json"] = SystemConfigFile.Basel.Json
    RegisteredAssetType["Txt"] = SystemConfigFile.Basel.Txt
    RegisteredAssetType["txt"] = SystemConfigFile.Basel.Txt
