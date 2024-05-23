import api
import Graphic
import Asset
import DataType
import Event
import Thread
import Function


BasicEnvironment = {'API': api, "Function": Function}
GraphicEnvironment = {"Graphic": Graphic}
AssetEnvironment = {'Asset': Asset}
DataTypeEnvironment = {'DataType': DataType}
EventEnvironment = {'Event': Event}
ThreadEnvironment = {'Thread': Thread}
ScriptEnvironment = {"Script": globals()}


class Script:
    def __init__(self):
        self.source = str()
        self.flags = dict()
        self.run_result = dict()
        self.compile_source = None
        self.flags = BasicEnvironment
        self.record_back = False

    def write(self, string):
        if isinstance(string, str):
            self.source = string

    def check(self):
        return bool(self.compile_source)

    def run(self):
        if self.compile_source is None:
            self.compile_source = compile(self.source, 'script', 'exec')
        exec(self.compile_source, __globals=self.flags, __locals=self.run_result)
        if self.record_back:
            self.flags.update(self.run_result)

    def result(self):
        return self.run_result
