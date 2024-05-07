from abc import abstractmethod, ABCMeta
from Function.parameter import mapping_new_copy, mapping_merge


class Asset(metaclass=ABCMeta):
    def __init__(self, config, *args, **kwargs):
        self.configObject = config
        self.load()

    def __copy__(self, copied = None):
        if copied is None:
            copied = Asset(self.configObject)
        copied.configObject = self.configObject
        copied.name = self.name
        copied.path = self.path
        copied.type = self.type
        return copied

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def convert(self):
        pass

    def load(self, *args, **kwargs):
        self.name = self.configObject['__asset__']['name']
        self.path = self.configObject['__asset__']['path']
        self.type = self.configObject['__asset__']['type']
        pass


class AssetFolder:
    def __init__(self, name: str = 'undefined', *args, **kwargs):
        self._name = name
        self._assets = dict()
        self._folder = dict()
        self._converted = dict()

    def __call__(self, *args, **kwargs) -> any:
        mix = mapping_new_copy(self._assets)
        mix.update(self._folder)
        return mix

    def __copy__(self, copied = None):
        if copied is None:
            copied = AssetFolder()
        for key, value in self._assets.items():
            copied._assets[key] = value.__copy__()
        for key, value in self._folder.items():
            copied._folder[key] = value.__copy__()
        for key, value in self._converted.items():
            copied._folder[key] = value
        return copied

    def reload(self) -> None:
        for value in self._assets.values():
            value.load()
        for value in self._folder.values():
            value.reload()

    def folder(self):
        return tuple(self._folder.values())

    def package(self, *args, **kwargs):
        return tuple(self._assets.values())

    def __getitem__(self, item):
        return self._assets.get(item) if (
                item in self._assets.keys()) else self._folder.get(item)

    def __setitem__(self, key, value):
        if isinstance(value, Asset):
            self._assets[key] = value
        if isinstance(value, AssetFolder):
            self._folder[key] = value

    def __delitem__(self, key):
        return self._assets.__delitem__(key) if (
                key in self._assets.keys()) else self._folder.__delitem__(key)

    def __iter__(self):
        return iter(tuple(self._assets.values()) + tuple(self._folder.values()))
