from DataType.Folder.FolderStruct_Hash import Folder


class Registry(Folder):
    def __init__(self):
        super().__init__()

    def __getitem__(self, __key, folder_path=None):
        return super().__getitem__(__key, folder_path)

    def __setitem__(self, key, value=None, folder_path=None):
        return super().__setitem__(key, value, folder_path)

    def __delitem__(self, key, folder_path=None, is_folder: bool = False):
        return super().__delitem__(key, folder_path, is_folder)
