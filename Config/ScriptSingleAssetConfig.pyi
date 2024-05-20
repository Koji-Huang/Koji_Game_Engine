from .BasicAssetConfig import AssetConfig
import ScriptAssetConfig


class Script(AssetConfig):
    bind_config_file: ScriptAssetConfig
    script: dict[str, [...]]

    def __init__(self, father_script, script_name):
        """

        """
