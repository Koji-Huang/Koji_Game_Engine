from pygame.image import load as load_image

from Asset.StandardDataType.Package import Package as _Package


class Package(_Package):
    def __init__(self, image_path: str, name: str = 'undefined', *args, **kwargs):
        super().__init__(name=name, *args, **kwargs)
        self._subtype = 'Graphic'
        self._name = name
        self._path = image_path
        pass

    def __copy__(self, copied=None):
        if copied is None:
            copied = Package(self._path)
        super().__copy__(copied)
        return copied

    def __call__(self, *args, **kwargs):
        return self._surface.copy

    def reload(self):
        pass

    def __pygame_Surface__(self):
        return self._surface.copy