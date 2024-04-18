from typing import overload


class Package:
    _name: str
    _subtype: str
    def __init__(self, *args, **kwargs):
        """

        """
        pass

    def __copy__(self, copied: Package = None):
        """

        """
        pass

    def __call__(self, *args, **kwargs) -> any:
        """

        """
        pass

    def reload(self):
        """

        """
        pass



class PackageFolder:
    _packages: dict[str, [Package]]
    _subfolder: dict[str, [PackageFolder]]
    _name: str

    def __init__(self, name: str = 'undefined', *args, **kwargs):
        """
        init package resource
        """
        pass

    def __call__(self, *args, **kwargs) -> any:
        """
        get package resource
        :return: any
        """
        pass

    def __copy__(self, copied: PackageFolder = None) -> PackageFolder:
        """
        copy package and send back another
        :return: copy object
        """
        pass

    def reload(self) -> None:
        """
        reload package resource
        :return: None
        """
        pass

    def folder(self) -> tuple[PackageFolder]:
        """
        return son folder
        """
        pass

    @overload
    def package(self, contain_son: bool = False) -> tuple[Package]:
        """
        return tuple of packages on this folder
        """
        pass

    @overload
    def package(self, id: str) -> Package:
        """
        return the package
        it will search in son package
        """
        pass

    @overload
    def package(self, name: str, contain_son: bool = True) -> tuple[Package]:
        """
        return the search package
        """
        pass

    def __getitem__(self, item: str) -> Package | PackageFolder:
        """

        """
        pass

    def __setitem__(self, key: str, value: PackageFolder | Package):
        """

        """
        pass

    def __delitem__(self, key: str):
        """

        """
        pass

    def __iter__(self):
        """
        return package and folder iter
        """
