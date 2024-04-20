import pygame
from API.ConfigAPI import ConfigObject as ConfigObject
from DataType.ConfigFile import ini, txt, json
from DataType.Asset.Graphic.Basel import Package as _Package
from Graphic.Customized.Animation import BaselAnimation as AnimationObject


class Package(_Package):
    _path: str
    _frame_size: int
    _frames: list[pygame.Surface]
    _frames_info: list[dict[str: [str]]]
    _animation_name = str
    _animation_type: str
    _sub_path = str
    _config_object: [ConfigObject | ini | txt | json]

    def __init__(self, image_path: str, name: str = 'undefined', *args, **kwargs):
        """

        """
        pass

    def __copy__(self, copied: Package = None):
        """

        """
        pass

    def __call__(self, *args, **kwargs) -> pygame.Surface:
        """

        """
        pass

    def load(self):
        """

        """
        pass

    def load_frame(self, frame):
        """

        """
        pass

    def convert(self) -> AnimationObject:
        """

        """
        pass