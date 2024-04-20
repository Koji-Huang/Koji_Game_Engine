from DataType.ConfigFile.Basel.basel import Basel as __Basic
import re


class Ini(__Basic):
    def __translate_read__(self):
        sub_title = 'undefined'
        self._translated_data.clear()
        for line in self._read_value:
            match_object = re.match(r'\[(.*)\]', line)
            if match_object is not None and match_object.groups().__len__() == 1:
                sub_title = match_object.groups()[0]
            else:
                match_object = re.match(r'(\w*)\s*=\s*(.*)', line)
                if match_object is not None and match_object.groups().__len__() == 2:
                    self.__setitem__(*match_object.groups(), sub_title)

    def __translate_write__(self):
        tmp = list()
        for sub_title in self._translated_data.keys():
            tmp.append(f'\n[{sub_title}]\n')
            for key in self._translated_data[sub_title]:
                tmp.append(f'{key} = {self._translated_data[sub_title][key]}')
        self._read_value = tuple(tmp)

    def __setitem__(self, key, value, sub_title: str = 'undefined'):
        if sub_title not in self.keys():
            self._translated_data[sub_title] = dict()
        self._translated_data[sub_title][key] = value

    def __delitem__(self, key,  sub_title: str = 'undefined'):
        self._translated_data[sub_title].pop(key)
