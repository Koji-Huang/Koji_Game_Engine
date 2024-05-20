from typing import Mapping
from .FolderStruct_Hash import Folder


class FolderQuote(Mapping):
    def __init__(self, folder_info, readable=True, writeable=True, savable=True, disable_outer_get=False):
        self.__quote_info = None
        self.__quote_object = None
        self.__readable = readable
        self.__writeable = writeable
        self.__savable = savable
        self.__disable_outer_get = disable_outer_get
        self.__tmp_attr = Folder("TMP Asset Poor")
        self.set_quote(folder_info)

    def set_quote(self, asset_info,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None:
        if isinstance(asset_info, FolderQuote):
            self.set_quote(
                asset_info.get_quote_folder(),
                asset_info.__readable * readable,
                asset_info.__writeable * writeable,
                asset_info.__savable * savable)
        if isinstance(asset_info, Folder):
            readable *= self.__readable
            writeable *= self.__writeable
            savable *= self.__savable
            self.__tmp_attr.clear()
            self.__quote_info = asset_info

    def remove_quote(self) -> None:
        self.__quote_info = None
        self.__tmp_attr.clear()

    def get_quote_folder(self) -> Folder:
        if self.__disable_outer_get:
            raise "This quote is disabled to get outer info"
        else:
            return self.__quote_object

    def get_quote_attr(self, item):
        match item:
            case "__quote_info":
                return self.__quote_info
            case "readable":
                return self.__readable
            case "writeable":
                return self.__writeable
            case "savable":
                return self.__savable
            case "disable_outer_get":
                return self.__disable_outer_get
            case _:
                return None

    def __len__(self):
        return self.__quote_object.__len__()

    def __iter__(self):
        return self.__quote_object.__iter__()

    def __getattr__(self, item):
        if self.__readable:
            if not self.__savable:
                # Value can't save to primer object
                try:
                    # Check tmp enviro have the valur or not
                    return self.__tmp_attr.__getattribute__(item)
                except any:
                    try:
                        # Check quote object have the valur or not
                        return self.__quote_object.__getattribute__(item)
                    except any as err:
                        # Check the item is belonged to self
                        val = self.get_quote_attr(item)
                        if val is None:
                            raise err
                        else:
                            return val
            else:
                # Value if savable
                try:
                    return self.__quote_object.__getattribute__(item)
                except any as err:
                    # Check the item is belonged to self
                    val = self.get_quote_attr(item)
                    if val is None:
                        raise err
                    else:
                        return val
        else:
            raise "This Quote is not Readable"

    def __setattr__(self, key, value):
        if self.__writeable:
            if self.__savable:
                return self.__quote_object.__setattr__(key, value)
            else:
                return self.__tmp_attr.__setattr__(key, value)
        else:
            raise "This Quote is not Changeable"

    def __delattr__(self, key):
        if self.__writeable:
            if self.__savable:
                return self.__quote_object.__delitem__(key)
            else:
                return self.__tmp_attr.__delitem__(key)
        else:
            raise "This Quote is not Changeable"
