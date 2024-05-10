from .BasicAssetConfig import AssetConfig


class Script(AssetConfig):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.config_type = 'Script'
        match self.config_file_format:
            case 'json':
                pass
            case 'ini':
                ...
            case 'txt':
                ...
            case _ as name:
                raise TypeError(name)

