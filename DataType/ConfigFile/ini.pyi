from DataType.ConfigFile.basic import CustomFile as __Basic


class Ini(__Basic):
    _translated_data: dict
    _file_path: str

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

    def __setitem__(self, key, value, sub_title: str = 'undefined'):
        pass



    def __delitem__(self, key,  sub_title: str = 'undefined'):
        pass