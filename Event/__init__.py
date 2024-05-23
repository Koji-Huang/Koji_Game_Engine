from . import BasicEvent
from . import UIEvent

from Global import ID_Register
from Event import BasicEvent as __EventFile
from Event import Management as __EventManager

_get, _recycle, _reset = ID_Register.customized('Event', 'EventSystem')
__EventFile._event_id_get = _get
__EventFile._event_id_recycle = _recycle
__EventManager._event_id_get = _get
__EventManager._event_id_recycle = _recycle

_get, _recycle, _reset = ID_Register.customized('Inspector', 'EventSystem')
__EventFile._inspector_id_get = _get
__EventFile._inspector_id_recycle = _recycle
__EventManager._inspector_id_get = _get
__EventManager._inspector_id_recycle = _recycle


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

from .Management import *
