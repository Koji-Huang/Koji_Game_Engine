from typing import overload, Iterator

from Config.Basel.AbstractConfig import Basel


class AssetConfig(Basel):
    asset_name: str
    asset_path: str
    asset_type: str

    def __len__(self) -> int:
        pass

    def __iter__(self) -> Iterator:
        pass

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
