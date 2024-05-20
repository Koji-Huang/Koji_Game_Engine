import pygame
from DataType.ConfigFile import GraphicAnimationObject as AnimationConfigObject
from DataType.Asset.AbstractAsset import Asset as AssetObject
from Graphic.Customized.Animation import BaselAnimation as AnimationObject


class Package(AssetObject):

    configObject: AnimationConfigObject
    saved_animation: AnimationObject
    animation_type: str
    frames_info: list[dict[str: [str]]]
    frame_size: int

    def __init__(self, config: AnimationConfigObject, *args, **kwargs):
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