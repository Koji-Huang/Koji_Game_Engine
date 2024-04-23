import os.path
from abc import abstractmethod, ABCMeta


class Basel(metaclass=ABCMeta):

    def __init__(self, file_path: str):
        self.config_name = 'undefined'
        self.config_type = 'Basel'
        self.sub_path = 'undefined'
        self.config_file_format = None
        self._read_value = tuple()
        self._translated_data = dict()
        self.file_path = file_path
        self.config_file_format = self.get_file_type()
        self.read()
        self.__translate_read__()

    def read(self):
        # deal with quit.
        with open(self.file_path, 'r') as file:
            self._read_value = tuple(file.readlines())

    def get_file_type(self):
        if isinstance(self, str):
            end_str = ''
            for char in self[::-1]:
                if char == '.': break
                else: end_str += char
            return end_str[::-1]
        else:
            if self.config_file_format is None:
                end_str = ''
                for char in self.file_path[::-1]:
                    if char == '.': break
                    else: end_str += char
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
        return self._translated_data.keys()

    def values(self):
        return self._translated_data.values()

    def __setitem__(self, key, value):
        self._translated_data[key] = value

    def __getitem__(self, item):
        if item not in self.keys():
            self._translated_data[item] = dict()
        return self._translated_data[item]

    def __delitem__(self, key):
        self._translated_data.pop(key)

    def items(self):
        return self.keys(), self.values()

    def __enter__(self):
        return self.keys(), self.values()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __dict__(self):
        return self._translated_data

    def __file__(self):
        return os.path.abspath(self.file_path)

    def __path__(self):
        return os.path.dirname(self.__file__())

    def convert(self) -> any:
        return self._translated_data

    def info(self, *args):
        pass

    def detail_info(self, *args):
        pass