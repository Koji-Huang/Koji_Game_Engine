from Basel import *
from .BasicAssetConfig import AssetConfig
from Graphic.Customized.Animation.AbstractAnimation import Animation as GraphicAnimationObject


class Script(AssetConfig):
    script: list[dict[str, [...]]]
