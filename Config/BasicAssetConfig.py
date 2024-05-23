from .Basel import *
from .Basel.AbstractConfig import Basel


class AssetConfig:
    def __init__(self, file_path):
        if isinstance(file_path, Basel):
            # As same as copy
            self.bind_config_file = file_path
            self.config_type = 'AssetConfig'
            self.file_path = self.bind_config_file.file_path
            self.config_file_format = self.bind_config_file.config_file_format

        elif isinstance(file_path, str):
            # create new config object
            self.file_path = file_path
            self.config_type = 'AssetConfig'
            self.config_file_format = Basel.get_file_type(file_path)

            match self.config_file_format:
                case 'txt':
                    self.bind_config_file = Txt(file_path)

                    self.bind_config_file["__asset__"] = dict()
                    self.bind_config_file["__asset__"]['path'] = self.bind_config_file['__asset_path']
                    self.bind_config_file["__asset__"]['type'] = self.bind_config_file['__asset_type']
                    self.bind_config_file["__asset__"]['name'] = self.bind_config_file['__asset_name']

                    self.config_name = self.bind_config_file['__file__']['name']
                    self.config_type = self.bind_config_file['__file__']['type']
                    self.config_path = self.bind_config_file['__file__']['path']
                case 'json':
                    self.bind_config_file = Json(file_path)
                    self.config_name = self.bind_config_file['__file__']['name']
                    self.config_type = self.bind_config_file['__file__']['type']
                    self.config_path = self.bind_config_file['__file__']['path']
                case 'ini':
                    self.bind_config_file = Ini(file_path)
                    self.config_name = self.bind_config_file['__file__']['name']
                    self.config_type = self.bind_config_file['__file__']['type']
                    self.config_path = self.bind_config_file['__file__']['path']
                case _:
                    raise TypeError(file_path)

        self.asset_name = self.bind_config_file["__asset__"]['name']
        self.asset_type = self.bind_config_file["__asset__"]['type']
        self.asset_path = self.bind_config_file["__asset__"]['path']

    def __getattr__(self, item):
        return self.bind_config_file.__getattribute__(str(item))

    def __setitem__(self, key, value):
        return self.bind_config_file.__setitem__(key, value)

    def __delitem__(self, key):
        return self.bind_config_file.__delitem__(key)

    def __getitem__(self, item):
        return self.bind_config_file.__getitem__(item)

    def info(self, *args):
        ret = self.bind_config_file.info(*args)
        ret['asset path'] = self.asset_path
        ret['asset name'] = self.asset_name
        ret['asset type'] = self.asset_type
        return ret