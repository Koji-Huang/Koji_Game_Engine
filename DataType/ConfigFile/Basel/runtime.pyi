from DataType.ConfigFile.Basel.basel import Basel

class Runtime(Basel):
    bind_object: Basel
    bind_path: str

    def __translate_read__(self):
        pass

    def __translate_write__(self):
        pass

    def __init__(self, bind_object: Basel, bind_path: str):
        pass

    def read(self):
        pass

    def get_file_type(self):
        pass

    def write(self, key, value):
        pass

    def save(self, file_path=None):
        pass