from DataType.ConfigFile.Basel import *
from Function.parameter import mapping_merge, mapping_new_copy
from API import GlobalAPI


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
    return obj


def register_config(config_object, keys: set[str] = None) -> None:
    if not keys:
        keys = set(config_object.keys())
    keys -= set(GlobalAPI.Registry.keys())
    if GlobalAPI.Registry.get(config_object.sub_path) is None:
        GlobalAPI.Registry[config_object.sub_path] = mapping_new_copy(config_object._translated_data)
    else:
        mapping_merge(GlobalAPI.Registry[config_object.sub_path], config_object._translated_data)


def overload_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        GlobalAPI.Registry.update(config_object)
    for key in keys:
        GlobalAPI.Registry[key] = config_object[key]


def unregister_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        keys = set(config_object.keys())
    for key in keys:
        GlobalAPI.Registry.pop(key)


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
    if GlobalAPI.Asset.get(sub_path) is None:
        GlobalAPI.Asset[sub_path] = dict()

    GlobalAPI.Asset[sub_path][name] = mapping_new_copy(asset)
