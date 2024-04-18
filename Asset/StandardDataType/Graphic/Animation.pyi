import pygame
from API.ConfigAPI import ConfigObject as ConfigObject
from DataType.ConfigFile import ini, txt, json
from Asset.StandardDataType.Graphic.Basic import Package as _Package


class Package(_Package):
    _path: str
    _frame_size: int
    _frames: list[pygame.Surface]
    _frames_info: list[dict[str: [str]]]
    _animation_name = str
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

    def reload(self):
        """

        """
        pass

    def load_frame(self, frame):
        """

        """
        pass

    def __pygame_Surface__(self):
        """

        """
        pass
