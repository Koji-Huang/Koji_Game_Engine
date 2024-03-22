from ThreadPackage import *


Manager = ThreadManager()


def hello_world(*args, **kwargs):
    print("Hello World")


add = FunctionThread(hello_world)


Manager.add_thread(add, pool='Main')


Manager.TRMachine.run()

