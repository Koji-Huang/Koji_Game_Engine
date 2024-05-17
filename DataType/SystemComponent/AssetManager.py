from DataType.Algorithms.FolderStruct_Hash import Folder
from DataType.Asset.AbstractAsset import Asset


class AssetManager(Folder[Asset]):
    def __init__(self):
        super().__init__()

    def __getitem__(self, __key, folder_path=None, get_source=False):
        get = super().__getitem__(__key, folder_path)
        if get_source is False and isinstance(get, Asset):
            return get.convert()
        else:
            return get

    def __delitem__(self, key, folder_path=None, is_folder: bool = False) -> None:
        item = super().__getitem__(key, folder_path)
        if item is not None and isinstance(item, Asset):
            item.delete()
        super().__delitem__(key, folder_path, is_folder)

    def set_active(self, key, folder_path=None):
        item = super().__getitem__(key, folder_path)
        if item and item.is_active() is False:
            super().__getitem__(key, folder_path).convert()

    def get_active(self, key, folder_path=None):
        item = super().__getitem__(key, folder_path)
        return item.is_active() if item else False

    def is_active(self, key, folder_path=None):
        return self.get_active(key, folder_path)
