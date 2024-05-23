from .Basel.AbstractConfig import Basel as baselConfigObject
from .Basel import *
from Function.parameter import mapping_merge, mapping_new_copy
from . import ConfigRegistry, ConfigRegistryType


def load_config_file(config_path: str, config_type: str = None):
    if config_type is None:
        match config_path[-4:]:
            case 'json':
                obj = Json(config_path)
            case '.ini':
                obj = Ini(config_path)
            case _:
                obj = Txt(config_path)
    else:
        obj = Txt(config_path)
    deep_search_config(obj)

    matched = match_config_object(obj.config_type)
    if matched != obj.__class__ and matched is not None:
        obj = matched(obj)
    return obj


def deep_search_config(config_object: baselConfigObject, data: dict = None, path=""):
    if data is None:
        data = config_object._translated_data
    for keys, val in data.items():
        if keys == "__file__" and path:
            if isinstance(val, str):
                config_object.son_config += (load_config_file(val), )
            if isinstance(val, list):
                for i in val:
                    config_object.son_config += (load_config_file(i), )
            if isinstance(val, dict):
                deep_search_config(Runtime(config_object, path))
        elif isinstance(val, dict):
            deep_search_config(config_object, val, path + "\\" + keys)


def register_config(config_object, keys: set[str] = None) -> None:
    if not keys:
        keys = set(config_object.keys())
    keys -= set(ConfigRegistry.keys())
    data = mapping_new_copy(config_object._translated_data)
    if ConfigRegistry.get(config_object.config_path) is None:
        ConfigRegistry[config_object.config_path] = mapping_new_copy(data)
    else:
        mapping_merge(ConfigRegistry[config_object.config_path], data)
    for son in config_object.son_config:
        register_config(son)


def overload_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        ConfigRegistry.update(config_object)
    for key in keys:
        ConfigRegistry[key] = config_object[key]


def unregister_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        keys = set(config_object.keys())
    for key in keys:
        ConfigRegistry.remove(key)


def delete_config(config_object, keys: tuple[str] = None) -> None:
    unregister_config(config_object, keys)
    for key in keys:
        config_object.__delitem__(key)


def save_config(config_object) -> None:
    config_object.save()


def save_as_config(config_object, output_path: str) -> None:
    config_object.save(output_path)


def convert_to_asset(config_object):
    from api import AssetAPI
    asset_manager = AssetAPI.RegisteredAsset

    name, asset, sub_path = config_object.convert()
    if asset_manager.get(sub_path) is None:
        asset_manager[sub_path] = dict()

    asset_manager[sub_path][name] = mapping_new_copy(asset)


def match_config_object(config_type: str):
    registry = ConfigRegistryType
    return registry[config_type]
