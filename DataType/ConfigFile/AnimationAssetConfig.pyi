from .Basel import *
from .BasicAssetConfig import AssetConfig
from Graphic.Customized.Animation.AbstractAnimation import Animation as GraphicAnimationObject


class Animation(AssetConfig):
    x: int
    y: int
    w: int
    h: int
    frame_size: int
    frame_info: dict[int: [dict[str, [str, int]]]]

    def convert(self) -> GraphicAnimationObject:
        pass