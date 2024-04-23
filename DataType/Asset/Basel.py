from abc import abstractmethod, ABCMeta


class Asset(metaclass=ABCMeta):
    def __init__(self, config_path: str, name: str = 'undefined', *args, **kwargs):
        self.config_path = config_path
        self.config_type = 'basic_package'
        self.config_name = name

    def __copy__(self, copied = None):
        if copied is None:
            copied = Asset()
        copied.__name = self.config_name
        copied.__subtype = self.config_type
        return copied

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def convert(self):
        pass


class AssetFolder:
    def __init__(self, name: str = 'undefined', *args, **kwargs):
        self._packages = dict()
        self._subfolder = dict()
        self._name = name

    def __call__(self, *args, **kwargs) -> any:
        mix = self._packages.copy()
        mix.update(self._subfolder)
        return mix

    def __copy__(self, copied = None):
        if copied is None:
            copied = AssetFolder()
        for key, value in self._packages.items():
            copied._packages[key] = value.__copy__()
        for key, value in self._subfolder.items():
            copied._subfolder[key] = value.__copy__()
        return copied

    def reload(self) -> None:
        for value in self._packages.values():
            value.load()
        for value in self._subfolder.values():
            value.load()

    def folder(self):
        return tuple(self._subfolder.values())

    def package(self, *args, **kwargs):
        return tuple(self._packages.values())

    def __getitem__(self, item):
        return self._packages.get(item) if (
                item in self._packages.keys()) else self._subfolder.get(item)

    def __setitem__(self, key, value):
        if isinstance(value, Asset):
            self._packages[key] = value
        if isinstance(value, AssetFolder):
            self._subfolder[key] = value

    def __delitem__(self, key):
        return self._packages.__delitem__(key) if (
                key in self._packages.keys()) else self._subfolder.__delitem__(key)

    def __iter__(self):
        return iter(tuple(self._packages.values()) + tuple(self._subfolder.values()))
