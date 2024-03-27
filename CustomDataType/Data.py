def convert_path(path: str) -> list[str]:
    ret = []
    old = 0
    for index in range(len(path)):
        if path[index] == "/":
            ret.append(path[old:index])
            old = index + 1
    if path[-1] != "/":
        ret.append(path[old:])
    return ret


def convert_list(path: list) -> str:
    ret = ''
    [ret.join(i) for i in path]
    return ret


class Data:
    name: str
    value: any
    type: str

    def __init__(self, types: str, name: str, value: any = None):
        self.value = value
        self.name = name
        self.value = value

    def set_value(self, value) -> None:
        self.value = value

    def set_name(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_value(self, *args, **kwargs) -> any:
        return self.value


# noinspection PyTypeChecker
class Folder:
    value: dict[Data]
    name: str
    son: dict

    def __init__(self, name: str, father=None, value: dict = None):
        self.value = value if value else dict()
        self.name = name
        self.son = dict()
        self.father = father

    def __getitem__(self, item: str or list) -> any:
        if isinstance(item, str):
            item = convert_path(item)
        if len(item) == 1:
            return self.value[item]
        else:
            return self.son[item[1:]]

    def __setitem__(self, key: str or list, value: any) -> None:
        if isinstance(key, str):
            key = convert_path(key)
        if len(key) > 1:
            self.create_folder(key[:-1])
            self.son[key[0]][key[1:]] = value
        else:
            self.value[key[0]] = Data(types="basic", name=key[0], value=value)

    def __delitem__(self, key: str or list[str]) -> None:
        if isinstance(key, str):
            key = convert_path(key)
        if len(key) > 1:
            self.create_folder(key)
            self.son[key[0]].__delitem__(key[1:])
        else:
            self.value.pop(key[0])

    def create_folder(self, path: str or list) -> None:
        if path:
            if isinstance(path, str):
                path = convert_path(path)
            if not self.son.get(path[0]):
                self.son[path[0]] = Folder(name=path[0], father=self)
            self.son[path[0]].create_folder(path[1:])

    def absolute_path(self, saved: list) -> str:
        saved.append(self.name)
        if self.father:
            return self.father.absolute_path(saved)
        else:
            return convert_list(saved[::-1])


a = Folder(name="Root")
a.create_folder("Picture/1.jpg")
a["Picture/1.jpg/Pixel"] = (255, 255, 255)
pass
