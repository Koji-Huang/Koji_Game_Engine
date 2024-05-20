from typing import TypeVar
from .FolderStruct_Hash import Folder

QuoteDataType = TypeVar("QuoteDataType")


class ValueQuote(QuoteDataType):
    def __init__(self, folder=None, key=None, readable=True, writeable=True, savable=True,
                 disable_outer_get: bool = False):
        self.__quote_Folder = None
        self.__quote_key = key
        self.__readable = readable
        self.__writeable = writeable
        self.__savable = savable
        self.__tmp_attr = None if savable else Folder()
        self.__disable_outer_get = disable_outer_get
        self.set_quote(folder, key)

    def set_quote(self,
                  folder,
                  key: str,
                  readable: bool = True,
                  writeable: bool = True,
                  savable: bool = True) -> None:
        if isinstance(folder, ValueQuote):
            self.set_quote(
                folder.get_quote_folder(),
                key,
                folder.__readable * readable,
                folder.__writeable * writeable,
                folder.__savable * savable)
        if isinstance(folder, Folder):
            readable *= self.__readable
            writeable *= self.__writeable
            savable *= self.__savable
            self.__tmp_attr.clear()
            self.__quote_Folder = folder
            self.__quote_key = key

    def remove_quote(self) -> None:
        self.__quote_Folder = None
        self.__quote_key = None
        self.__tmp_attr.clear()

    def get_quote_key(self) -> QuoteDataType:
        if self.disable_outer_get:
            return self.__quote_key
        else:
            raise "This quote is disabled to get outer info"

    def get_quote_folder(self) -> Folder:
        if self.disable_outer_get:
            return self.__quote_Folder
        else:
            raise "This quote is disabled to get outer info"

    def get_quote_attr(self, item):
        match item:
            case "quote_Folder":
                return self.__quote_Folder
            case "quote_key":
                return self.__quote_key
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
                        return self.__quote_Folder.__getattribute__(item)
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
                    return self.__quote_Folder[self.__quote_key].__getattribute__(item)
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
                return self.__quote_Folder[self.__quote_key].__setattr__(key, value)
            else:
                return self.__tmp_attr.__setattr__(key, value)
        else:
            raise "This Quote is not Changeable"

    def __delattr__(self, key):
        if self.__writeable:
            if self.__savable:
                return self.__quote_Folder[self.__quote_key].__delitem__(key)
            else:
                return self.__tmp_attr.__delitem__(key)
        else:
            raise "This Quote is not Changeable"
