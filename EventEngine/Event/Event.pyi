from EventEngine.Subchannel.Subchannel import Subchannel
from types import FunctionType


class Event(object):
     name: str
     operation: FunctionType
     subchannel: Subchannel
     monitoring: tuple[Event]
     fatherEvent: Event

     def __init__(self, name: str, operation: FunctionType, subchannel: Subchannel = None,
                  monitoring: tuple[Event] = None, fatherEvent: Event = None):
         ...

     def __call__(self, *args, **kwargs):
         ...

     def delete(self):
         ...

     def run(self):
         ...

