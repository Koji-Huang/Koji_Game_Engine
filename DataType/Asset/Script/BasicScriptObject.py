from ..AbstractAsset import Asset
from ...PackagedCallable import PackagedCallable


class BasicScriptObject(AssetManager):

    def __init__(self, config, *args, **kwargs):
        super().__init__(config, *args, **kwargs)
        self.script_file = config['path']
        with open(config['path']) as file:
            self.script_code = file.read()
        self.script_flags = config['flags']
        self.compile_code = None
        self.script_local = dict()
        pass

    def __copy__(self, copied=None):
        if copied is None:
            copied = BasicScriptObject(self.configObject)
        super().__copy__(copied)
        copied.script_file = self.script_file
        copied.script_code = self.script_code
        copied.script_flags = self.script_flags
        copied.compile_code = self.compile_code
        return copied

    def __call__(self, *args, **kwargs):
        self.convert()()

    def convert(self):
        if self.compile_code is None:
            self.compile_code = compile(self.script_code, '', 'exec')
        return PackagedCallable(exec, self.compile_code, self.script_flags, self.script_local)

    def __getattr__(self, item):
        return self.script_local.get(item)

    def is_active(self):
        return self.compile_code is not None
