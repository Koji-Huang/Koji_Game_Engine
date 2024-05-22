from . import BasicEvent
from . import UIEvent
from .main import *
from .Management import EventManagement as EventManagementType

Name: dict[str: str] = {
    "Basic": "Basic Event",
    "UIEvent": "UI Event"
}

Inspector: dict[str: any] = {
    "Basic": BasicEvent.Inspector,
    "UIEvent": UIEvent.Inspector
}

Event: dict[str: any] = {
    "Basic": BasicEvent.BasicEvent,
    "UIEvent": UIEvent.Event
}

TypeID: dict[str: str] = {
    "Basic": '000000000',
    "UIEvent": UIEvent.TypeID
}


EventManagement = EventManagementType()
