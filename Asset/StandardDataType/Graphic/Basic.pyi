import pygame

from Asset.StandardDataType.Package import Package as _Package


class Package(_Package):
    _path: str
    _surface: pygame.Surface

    def __init__(self, image_path: str, name: str = 'undefined', *args, **kwargs):
        """

        """
        pass

    def __copy__(self, copied: Package = None):
        """

        """
        pass

    def __call__(self, *args, **kwargs) -> pygame.Surface:
        """

        """
        pass

    def reload(self):
        """

        """
        pass

    def __pygame_Surface__(self):
        """

        """
        pass
