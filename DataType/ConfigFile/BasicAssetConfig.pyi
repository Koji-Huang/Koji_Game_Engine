from typing import overload

from .Basel.AbstractConfig import Basel


class AssetConfig(Basel):
    bind_config_file: Basel

    @overload
    def __init__(self, file_path: str):
        pass
    @overload
    def __init__(self, config: Basel):
        pass

    def __translate_write__(self):
        pass

    def __translate_read__(self):
        pass

    def info(self, *args):
        pass
