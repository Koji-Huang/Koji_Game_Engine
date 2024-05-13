from DataType.ConfigFile.ScriptAssetConfig import Script
from DataType.Asset.Script.BasicScriptObject import BasicScriptObject

A = Script(".json")
B = BasicScriptObject(A.script[0])
D = B.convert()
D()
D()

pass