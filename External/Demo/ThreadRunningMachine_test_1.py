from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from Thread import *
from API import ThreadAPI_type
from API import GlobalAPI

with PyCallGraph(output=GraphvizOutput()):

    GlobalAPI.register_global_environment()


    Manager = ThreadAPI_type()


    def hello_world(*args, **kwargs):
        print("Hello World")


    add = FunctionThread(hello_world)


    Manager.add_thread(add, pool='Main')


    Manager.TRMachine.start()

