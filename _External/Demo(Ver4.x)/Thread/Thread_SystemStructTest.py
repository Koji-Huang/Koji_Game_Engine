import Thread
Thread.init()


from Thread.Thread import FunctionThread


def hello_world(*args, **kwargs):
    print("Hello World from Koji!\n")


A = FunctionThread(hello_world, {})
Thread.add_thread(A)


Thread.TRMachine.start()

pass
