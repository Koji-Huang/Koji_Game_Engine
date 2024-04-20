from abc import abstractmethod, ABCMeta


class Basel(metaclass=ABCMeta):
    config_name: str
    config_type: str
    sub_path: str
    file_path: str
    config_file_format: str
    _read_value: tuple[str]
    _translated_data: dict

    def __init__(self, file_path: str):
        """
        ConfigFile is a standard class for config.ini file read.
        :param file_path: the path of file
        """
        pass

    def read(self):
        """
        read info from file
        :return: None
        """
        pass

    def get_file_type(self):
        ...

    def write(self, key: str, value: str):
        """
        write info into file.
        """
        pass

    def save(self, file_path=None):
        """
        save changes
        :return: None
        """
        pass

    def update(self, collection: dict):
        """
        Update data form another dict
        """
        pass

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

    def keys(self) -> tuple:
        """
        Return the keys of data
        :param: tuple of keys
        """

    def values(self) -> tuple:
        """
        Return the values of data
        :param: tuple of values
        """

    def __setitem__(self, key: str, value: str):
        pass

    def __getitem__(self, item: str) -> any:
        pass

    def __delitem__(self, key: str):
        pass

    def items(self):
        """

        """
        pass

    def __enter__(self):
        """

        """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __dict__(self):
        """

        """
        pass