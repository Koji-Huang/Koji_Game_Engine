from DataType.ConfigFile import Script
from Asset.Script import BasicScriptAsset

A = Script(".json")
B = BasicScriptAsset(A.script[0])
D = B.convert()
D()
D()

pass