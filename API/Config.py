from DataType.ConfigFile.Basel import *
from DataType.ConfigFile.Basel.AbstractConfig import Basel as baselConfigObject
from Function.parameter import mapping_merge, mapping_new_copy, filepath_set, filepath_get
from .Global import Registry, AssetManager


def load_config_file(config_path: str, config_type: str = None):
    if config_type is None:
        match config_path[-4:]:
            case 'json':
                obj = json(config_path)
            case '.ini':
                obj = ini(config_path)
            case _:
                obj = txt(config_path)
    else:
        obj = txt(config_path)
    deep_search_config(obj)
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
                deep_search_config(runtime(config_object, path))
        elif isinstance(val, dict):
            deep_search_config(config_object, val, path + "\\" + keys)


def register_config(config_object, keys: set[str] = None) -> None:
    if not keys:
        keys = set(config_object.keys())
    keys -= set(Registry.keys())
    data = mapping_new_copy(config_object._translated_data)
    if Registry.get(config_object.sub_path) is None:
        filepath_set(Registry, config_object.sub_path, mapping_new_copy(data))
    else:
        mapping_merge(filepath_get(Registry[config_object.sub_path]), data)
    for son in config_object.son_config:
        register_config(son)


def overload_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        Registry.update(config_object)
    for key in keys:
        Registry[key] = config_object[key]


def unregister_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        keys = set(config_object.keys())
    for key in keys:
        Registry.pop(key)


def delete_config(config_object, keys: tuple[str] = None) -> None:
    unregister_config(config_object, keys)
    for key in keys:
        config_object.__delitem__(key)


def save_config(config_object) -> None:
    config_object.save()


def save_as_config(config_object, output_path: str) -> None:
    config_object.save(output_path)


def convert_to_asset(config_object):
    name, asset, sub_path = config_object.convert()
    if AssetManager.get(sub_path) is None:
        AssetManager[sub_path] = dict()

    AssetManager[sub_path][name] = mapping_new_copy(asset)
