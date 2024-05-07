import Event.UIEvent.Keyboard
import Event.UIEvent.Mouse
import Event.UIEvent.Screen
import Event.UIEvent.UIEvent
import Event.BasicEvent as BasicEvent

Name: dict[str: str] = {
    "Basic": "Basic UI Event",
    "Keyboard": "Keyboard Event",
    "Mouse": "Mouse Event",
    "Screen": "Screen Event"
}

Inspector: dict[str: any] = {
    "Basic": BasicEvent.Inspector,
    "Keyboard": Keyboard.Inspector,
    "Mouse": Mouse.Inspector,
    "Screen": Screen.Inspector
}

Event: dict[str: any] = {
    "Basic": BasicEvent.BasicEvent,
    "Keyboard": Keyboard.Event,
    "Mouse": Mouse.Event,
    "Screen": Screen.Event,
}

TypeID: dict[str: str] = {
    "Basic": "00100000",
    "Keyboard": Keyboard.TypeID,
    "Mouse": Mouse.TypeID,
    "Screen": Screen.TypeID
}

