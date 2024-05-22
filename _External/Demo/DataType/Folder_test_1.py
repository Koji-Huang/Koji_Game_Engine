from DataType.Folder.FolderStruct_Hash import Folder
from math import sqrt, pi
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

size = 100000

Main = Folder(hash_width=int(sqrt(size) * pi / 3))
# with PyCallGraph(output=GraphvizOutput()):
Main["1\\"] = Folder()
Main["1\\2\\"] = Folder()
Main["1\\2\\3"] = 4
print(Main["1\\2\\3"])
pass
