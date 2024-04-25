from DataType.ConfigFile.Basel.basel import Basel as __Basic
import re


class Txt(__Basic):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def __translate_read__(self):
        for line in self._read_value:
            match_object = re.match(r'(\w*)\s*=\s*(.*)', line)
            if match_object is not None and match_object.groups().__len__() == 2:
                self.__setitem__(*match_object.groups())
        self.__setitem__("__file__", dict())
        self['__file__']['name'] = self['__config_name']
        self['__file__']['path'] = self['__config_path']
        self['__file__']['type'] = self['__config_type']

    def __translate_write__(self):
        tmp = list()
        for key in self.keys():
            tmp.append(f"{key} = {self._translated_data[key]}")
        self._read_value = tuple(tmp)
