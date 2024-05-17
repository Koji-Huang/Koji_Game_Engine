from DataType.ConfigFile.Basel import *
from DataType.ConfigFile.Basel.AbstractConfig import Basel


class AssetConfig:
    bind_config_file: Basel

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config_type = 'AssetConfig'
        self.config_file_format = Basel.get_file_type(file_path)
        match self.config_file_format:
            case 'txt':
                self.bind_config_file = txt(file_path)

                self.bind_config_file["__asset__"] = dict()

                self.bind_config_file["__asset__"]['path'] = self.bind_config_file['__asset_path']
                self.bind_config_file["__asset__"]['type'] = self.bind_config_file['__asset_type']
                self.bind_config_file["__asset__"]['name'] = self.bind_config_file['__asset_name']

                self.config_name = self.bind_config_file['__file__']['name']
                self.config_type = self.bind_config_file['__file__']['type']
                self.config_path = self.bind_config_file['__file__']['path']
            case 'json':
                self.bind_config_file = json(file_path)
                self.config_name = self.bind_config_file['__file__']['name']
                self.config_type = self.bind_config_file['__file__']['type']
                self.config_path = self.bind_config_file['__file__']['path']
            case 'ini':
                self.bind_config_file = ini(file_path)
                self.config_name = self.bind_config_file['__file__']['name']
                self.config_type = self.bind_config_file['__file__']['type']
                self.config_path = self.bind_config_file['__file__']['path']
            case _:
                raise TypeError(file_path)

    def __getattr__(self, item):
        return self.bind_config_file.__getitem__(str(item))

    def __setitem__(self, key, value):
        return self.bind_config_file.__setitem__(key, value)

    def __delitem__(self, key):
        return self.bind_config_file.__delitem__(key)

    def __getitem__(self, item):
        return self.bind_config_file.__getitem__(item)


