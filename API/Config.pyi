from DataType.ConfigFile.Basel.AbstractConfig import Basel as ConfigObject



def load_config_file(config_path: str, config_type: str = None) -> ConfigObject:
    ...

def register_config(config_object: ConfigObject, keys: set[str] = None) -> None:
    ...

def overload_config(config_object: ConfigObject, keys: set[str] = None) -> None:
    ...

def unregister_config(config_object: ConfigObject, keys: set[str] = None) -> None:
    ...

def delete_config(config_object: ConfigObject, keys: set[str] = None) -> None:
    ...

def save_config(config_object: ConfigObject, keys: set[str] = None) -> None:
    ...

def save_as_config(config_object: ConfigObject, output_path: str, keys: set[str] = None) -> None:
    ...


def convert_to_asset(config_object: ConfigObject):
    ...