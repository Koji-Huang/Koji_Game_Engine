from abc import abstractmethod

import pygame
from ..Basel.AbstractConfig import Basel


class AssetConfig(Basel):
    bind_config_file: Basel

    def __init__(self, file_path: str):
        pass

    def __translate_write__(self):
        pass

    def __translate_read__(self):
        pass

    def info(self, *args):
        pass
