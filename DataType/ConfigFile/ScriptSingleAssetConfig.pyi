from .Basel import *
from .BasicAssetConfig import AssetConfig
from Graphic.Customized.Animation.AbstractAnimation import Animation as GraphicAnimationObject
import ScriptAssetConfig


class Script(AssetConfig):
    bind_config_file: ScriptAssetConfig
    script: dict[str, [...]]

    def __init__(self, father_script, script_name):
        """

        """
