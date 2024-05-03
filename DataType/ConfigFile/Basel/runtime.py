from DataType.ConfigFile.Basel.basel import Basel


class Runtime(Basel):
    def __translate_read__(self):
        pass

    def __translate_write__(self):
        pass

    def __init__(self, bind_object, bind_path):
        self.bind_object = bind_object
        self.bind_path = bind_path
        super().__init__(bind_object.file_path)
        bind_object.son_config += (self, )

    def read(self):
        self._translated_data = self.bind_object[self.bind_path]

    def get_file_type(self):
        return None

    def write(self, key, value):
        self._translated_data[key] = value

    def save(self, file_path=None):
        pass

    def __getitem__(self, item):
        return self.bind_object[self.bind_path]

    def __setitem__(self, key, value):
        self.bind_object[self.bind_path][key] = value

    def __delitem__(self, key):
        self.bind_object.__delitem__(self.bind_path + "\\" + key)