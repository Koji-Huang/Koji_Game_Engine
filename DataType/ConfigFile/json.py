from DataType.ConfigFile.basic import CustomFile as __Basic
import json as _json


class Json(__Basic):
    def read(self):
        with open(self._file_path, 'r+') as file:
            self._translated_data = _json.load(file)

    def save(self):
        with open(self._file_path, 'w+') as file:
            _json.dump(self._translated_data, file)

    def __translate_read__(self):
        pass

    def __translate_write__(self):
        pass
