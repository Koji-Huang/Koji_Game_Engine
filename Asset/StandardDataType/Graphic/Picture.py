from pygame.image import load as load_image

from Asset.StandardDataType.Graphic.Basic import Package as _Package


class Package(_Package):
    def __init__(self, image_path: str, name: str = 'undefined', *args, **kwargs):
        super().__init__(image_path, name=name, *args, **kwargs)
        self._surface = load_image(self._path)

    def __copy__(self, copied=None):
        if copied is None:
            copied = Package(self._path)
        super().__copy__(copied)
        return copied

    def __call__(self, *args, **kwargs):
        return self._surface.copy

    def reload(self):
        super().reload()
        self._surface = load_image(self._path)

    def __pygame_Surface__(self):
        return self._surface.copy
