from Thread import *
from API import ThreadAPI_type
from API import GlobalAPI


GlobalAPI.register_global_environment()


Manager = ThreadAPI_type()


def hello_world(*args, **kwargs):
    print("Hello World")


add = FunctionThread(hello_world)


Manager.add_thread(add, pool='Main')


Manager.TRMachine.start()

