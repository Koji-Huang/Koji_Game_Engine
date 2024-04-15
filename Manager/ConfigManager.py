from DataType.ConfigFile import *
import GlobalConstant


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
    keys -= set(GlobalConstant.Registry.keys())
    for key in keys:
        GlobalConstant.Registry[key] = config_object[key]


def overload_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        GlobalConstant.Registry.update(config_object)
    for key in keys:
        GlobalConstant.Registry[key] = config_object[key]


def unregister_config(config_object, keys: tuple[str] = None) -> None:
    if keys is None:
        keys = set(config_object.keys())
    for key in keys:
        GlobalConstant.Registry.pop(key)


def delete_config(config_object, keys: tuple[str] = None) -> None:
    unregister_config(config_object, keys)
    for key in keys:
        config_object.__delitem__(key)


def save_config(config_object) -> None:
    config_object.save()


def save_as_config(config_object, output_path: str) -> None:
    config_object.save(output_path)
