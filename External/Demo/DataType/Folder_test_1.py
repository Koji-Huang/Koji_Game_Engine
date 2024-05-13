from DataType.Algorithms.FolderStruct_Hash import Folder
from math import sqrt, pi
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

size = 100000

Main = Folder(hash_width=int(sqrt(size) * pi / 3))
with PyCallGraph(output=GraphvizOutput()):
    for i in range(size):
        Main.add(Folder(i, hash_width=1))
for i, value in enumerate(Main.folders()):
    print("Index: ", i, " | Size:", len(value[0]))
