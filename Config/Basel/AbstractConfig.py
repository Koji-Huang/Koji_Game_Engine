import os.path
from abc import abstractmethod, ABCMeta
from typing import Mapping

from Function.parameter import mapping_new_copy, filepath_get, filepath_del, filepath_set


class Basel(Mapping, metaclass=ABCMeta):
    def __init__(self, file_path: str):
        self.config_name = 'undefined'
        self.config_type = 'Basel'
        self.config_path = 'undefined'
        self.config_file_format = None
        self._read_value = tuple()
        self._translated_data = dict()
        self.file_path = file_path
        self.son_config = tuple()
        self.config_file_format = self.get_file_type(self)

        self.read()

        self.config_path = self._translated_data['__file__']['path']
        self.config_type = self._translated_data['__file__']['type']
        self.config_name = self._translated_data['__file__']['name']
        self.__iter__ = self._translated_data.__iter__
        self.__len__ = self._translated_data.__len__
        self.items = self._translated_data.items
        self.keys = self._translated_data.keys
        self.values = self._translated_data.values
        # self._translated_data['configObject'] = self
        pass

    def read(self):
        # deal with quit.
        with open(self.file_path, 'r') as file:
            self._read_value = tuple(file.readlines())
        self.__translate_read__()

    @staticmethod
    def get_file_type(self):
        if isinstance(self, str):
            end_str = ''
            for char in self[::-1]:
                if char == '.':
                    break
                else:
                    end_str += char
            return end_str[::-1]
        else:
            if self.config_file_format is None:
                end_str = ''
                for char in self.file_path[::-1]:
                    if char == '.':
                        break
                    else:
                        end_str += char
                return end_str[::-1]
            else:
                return self.config_file_format

    def write(self, key, value):
        self._translated_data[key] = value
        self.save()

    def save(self, file_path=None):
        with open(self.file_path if file_path is None else file_path, 'w') as file:
            self.__translate_write__()
            mix = ''
            for i in self._read_value:
                mix += i
                mix += '\n'
            file.write(mix)

    def update(self, collection: dict):
        self._translated_data.update(collection)

    @abstractmethod
    def __translate_read__(self):
        """
        translate data into standard data
        :return: None
        """
        pass

    @abstractmethod
    def __translate_write__(self):
        """
        translate data into standard data
        :return: None
        """
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def __setitem__(self, key, value):
        filepath_set(self._translated_data, key, value)

    def __getitem__(self, item):
        return filepath_get(self._translated_data, item)

    def __delitem__(self, key):
        filepath_del(self._translated_data, key)

    def __dict__(self):
        return self._translated_data

    def convert(self) -> any:
        asset = mapping_new_copy(self._translated_data)
        asset.pop("__file__")
        asset['ConfigObject'] = self
        return self.config_name, asset, self.config_path

    def info(self, *args):
        info = dict()
        info['config_type'] = self.config_type
        info['config_path'] = self.config_path
        info['config_name'] = self.config_name
        info['config_file_format'] = self.config_file_format
        info['config_type'] = self.config_type
        return info

    def detail_info(self, *args):
        return dict()

    def __iter__(self):
        pass

    def __len__(self):
        pass
