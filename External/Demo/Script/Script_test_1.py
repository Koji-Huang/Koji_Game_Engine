from DataType.ConfigFile.ScriptAssetConfig import Script
from DataType.Asset.Script.BasicScriptAsset import BasicScriptAsset

A = Script(".json")
B = BasicScriptAsset(A.script[0])
D = B.convert()
D()
D()

pass