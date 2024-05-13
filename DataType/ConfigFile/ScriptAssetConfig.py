from .BasicAssetConfig import AssetConfig
from .ScriptSingleAssetConfig import Script as SingleScript


class Script(AssetConfig):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.config_type = 'Script'
        self.script = tuple(SingleScript(self, name) for name in self.bind_config_file["Script"]['name'])

    def info(self, *args):
        ret = super().info(*args)
        ret['script_size'] = self.script.__len__()
        ret['script_name'] = [script['name'] for script in self.script]
        return ret