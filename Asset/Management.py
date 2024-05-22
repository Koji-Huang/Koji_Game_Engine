
from Function.parameter import filepath_set
from DataType.SystemComponent.AssetRegister import AssetManager

RegisteredAssetType = dict()
RegisteredAsset = AssetManager()


def load_asset(config):
    from Config.BasicAssetConfig import AssetConfig
    if isinstance(config, str):
        asset = match_asset_type(config)
        load_asset(asset)
    elif isinstance(config, AssetConfig):
        from API import GlobalAPI
        filepath_set(GlobalAPI.AssetManager, config.sub_path, config)
    else:
        return None


def match_asset_type(config):
    pass


def save_asset(config):
    pass


def import_asset(config):
    pass


def get_asset(key=None, path=None):
    pass


def load_system_asset_type():
    global RegisteredAssetType
    import Config as SystemConfigFile
    RegisteredAssetType["Animation"] = SystemConfigFile.AnimationAssetConfigObject
    RegisteredAssetType["animation"] = SystemConfigFile.AnimationAssetConfigObject
    RegisteredAssetType["Image"] = SystemConfigFile.ImageAssetConfigObject
    RegisteredAssetType["image"] = SystemConfigFile.ImageAssetConfigObject
    RegisteredAssetType["Script"] = SystemConfigFile.ScriptAssetConfigObject
    RegisteredAssetType["script"] = SystemConfigFile.ScriptAssetConfigObject
    RegisteredAssetType["Ini"] = SystemConfigFile.Basel.Ini
    RegisteredAssetType["ini"] = SystemConfigFile.Basel.Ini
    RegisteredAssetType["Json"] = SystemConfigFile.Basel.Json
    RegisteredAssetType["json"] = SystemConfigFile.Basel.Json
    RegisteredAssetType["Txt"] = SystemConfigFile.Basel.Txt
    RegisteredAssetType["txt"] = SystemConfigFile.Basel.Txt
