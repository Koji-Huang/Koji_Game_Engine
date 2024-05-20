from .BasicAssetConfig import AssetConfig
from ScriptSingleAssetConfig import Script as SingleScript


class Script(AssetConfig):
    script: tuple[SingleScript]
