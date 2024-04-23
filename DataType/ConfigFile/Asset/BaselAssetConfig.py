import pygame
from ..Basel import *
from ..Basel.basel import Basel
from abc import abstractmethod


class AssetConfig:
    bind_config_file: Basel

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config_type = 'AssetConfig'
        self.config_file_format = Basel.get_file_type(file_path)
        match self.config_file_format:
            case 'txt':
                self.bind_config_file = txt(file_path)
                self.config_name = self.bind_config_file['__name']
                self.config_type = self.bind_config_file['__config_type']
                self.sub_path = self.bind_config_file['__sub_path']
            case 'json':
                self.bind_config_file = json(file_path)
                self.config_name = self.bind_config_file['__file__']['name']
                self.config_type = self.bind_config_file['__file__']['config_type']
                self.sub_path = self.bind_config_file['__file__']['sub_path']
            case 'ini':
                self.bind_config_file = ini(file_path)
                self.config_name = self.bind_config_file['__file__']['name']
                self.config_type = self.bind_config_file['__file__']['config_type']
                self.sub_path = self.bind_config_file['__file__']['sub_path']
            case _:
                raise TypeError(file_path)

    def __getattr__(self, item):
        return self.bind_config_file[str(item)]

