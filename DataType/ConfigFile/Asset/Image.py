import pygame
from ..Basel import ini, txt
from .BaselAssetConfig import AssetConfig
from ..Basel.basel import Basel


class Image(AssetConfig):

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.config_type = 'Image'

        match self.config_file_format:
            case 'txt':
                self.w = self.bind_config_file['image_w']
                self.h = self.bind_config_file['image_h']
                self.path = self.bind_config_file['image_path']
                self.alpha = self.bind_config_file['image_alpha']
            case 'ini':
                self.w = self.bind_config_file['w']
                self.h = self.bind_config_file['h']
                self.path = self.bind_config_file['path']
                self.alpha = self.bind_config_file['alpha']
            case _:
                raise TypeError(file_path)

    def convert(self) -> pygame.Surface:
        surface = pygame.Surface((self.w, self.h))
        surface.blit((pygame.image.load(self.path)), (0, 0))
        surface.set_alpha(self.alpha)
        return surface

    def info(self, *args):
        ret = Basel.info(self)
        ret['path'] = self.path
        ret['w'] = self.w
        ret['h'] = self.h
        ret['alpha'] = self.alpha
        if args is not None:
            for arg in args:
                ret = ret[arg]
        return ret
