from DataType.Folder.Folder_ValueQuote import ValueQuote
from .AbstractAsset import Asset
from DataType.CustomizedPath import CustomizedPath
from API.Global import AssetManager


class AssetQuote(ValueQuote):
    def __init__(self, folder=None, key=None, readable=True, writeable=True, savable=True,
                 disable_outer_get: bool = False):
        if isinstance(folder, Asset):
            savable = writeable
            writeable = readable
            readable = key
            key = folder.name
            folder = AssetManager[folder.path]
        if isinstance(folder, str):
            if isinstance(key, str):
                path = CustomizedPath(folder, is_folder=True)
                folder = AssetManager[path]
                savable *= savable
                writeable *= writeable
                readable *= readable
            if isinstance(key, bool):
                path = CustomizedPath(folder)
                folder = AssetManager[path[:-1]]
                key = path[-1]
                savable *= writeable
                writeable *= readable
                readable *= key
        # Normal
        super().__init__(folder, key, readable, writeable, savable,disable_outer_get)

    def set_quote(self,
                  folder: any,
                  key: str,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None:
        if isinstance(folder, Asset):
            self.savable *= writeable
            self.writeable *= readable
            self.readable *= key
            self.quote_key = folder.name
            self.quote_Folder = AssetManager[folder.path]
        elif isinstance(folder, str):
            if isinstance(key, str):
                path = CustomizedPath(folder, is_folder=True)
                self.quote_Folder = AssetManager[path]
                self.quote_key = key
                self.savable *= savable
                self.writeable *= writeable
                self.readable *= readable
            if isinstance(key, bool):
                path = CustomizedPath(folder)
                self.quote_Folder = AssetManager[path[:-1]]
                self.quote_key = path[-1]
                self.savable *= writeable
                self.writeable *= readable
                self.readable *= key
        else:
            super().set_quote(folder, key, readable, writeable, savable)
