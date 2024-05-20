from types import CodeType
from ...PackagedCallable import PackagedCallable
from ..AbstractAsset import Asset
from ...ConfigFile.ScriptSingleAssetConfig import Script


class BasicScriptAsset(Asset):
    script_file: str
    script_code: str
    script_flags: dict
    script_local: dict
    compile_code: CodeType

    def __init__(self, config: Script, *args, **kwargs):
        """

        """
        pass

    def __copy__(self, copied: BasicScriptAsset = None):
        """

        """
        pass

    def __call__(self, *args, **kwargs):
        """

        """
        pass

    def convert(self) -> PackagedCallable:
        """

        """
        pass

    def result(self):
        """

        """
        pass