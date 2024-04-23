import pygame
from DataType.ConfigFile.Asset import AnimationConfig as AnimationConfigObject
from DataType.Asset.Basel import Asset as AssetObject
from Graphic.Customized.Animation import BaselAnimation as AnimationObject


class Package(AssetObject):
    configObject: AnimationConfigObject
    animation_type: str
    frames_info: list[dict[str: [str]]]
    frame_size: int

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

    def convert(self) -> AnimationObject:
        """

        """
        pass