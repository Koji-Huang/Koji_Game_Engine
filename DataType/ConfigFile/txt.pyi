from DataType.ConfigFile.basic import CustomFile as __Basic


class Txt(__Basic):
    """
    Config Object only save String Format
    """

    def __translate_read__(self):
        ...

    def __translate_write__(self):
        ...