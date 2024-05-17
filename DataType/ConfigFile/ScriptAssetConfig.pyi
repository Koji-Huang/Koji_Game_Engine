from .Basel import *
from .BasicAssetConfig import AssetConfig
from Graphic.Customized.Animation.AbstractAnimation import Animation as GraphicAnimationObject
from ScriptSingleAssetConfig import Script as SingleScript


class Script(AssetConfig):
    script: tuple[SingleScript]
