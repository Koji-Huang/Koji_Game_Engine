import Event
from Event import BasicEvent

def hello_world(*args, **kwargs):
    print("Hello World!", str(args), str(kwargs))

Event.init()

Event.load_default_event()

A = Event.create_instantiation_inspector("000000000", {}, {})
A.target_event.track_function = hello_world


Event.update()
pass
