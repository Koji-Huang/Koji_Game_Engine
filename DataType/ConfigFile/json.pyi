from DataType.ConfigFile.basic import CustomFile as __Basic


class Json(__Basic):
    _translated_data: dict
    _file_path: str

    def read(self):
        """
        read info from file
        :return: None
        """
        pass

    def write(self, key: str, value: any):
        """
        write info into file.
        """
        pass

    def save(self):
        """
        save changes
        :return: None
        """
        pass

    def __translate_read__(self):
        """
        translate data into standard data
        :return: None
        """
        pass

    def __translate_write__(self):
        """
        translate data into standard data
        :return: None
        """
        pass
