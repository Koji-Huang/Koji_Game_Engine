from Event.UIEvent.Mouse import MouseBasicEvent, MouseClickEvent, MouseDragEvent, MousePressEvent, MouseScrollEvent


Name: dict[str: str] = {
    "Basic": "Basic Mouse Event",
    "Click": "Mouse Click Event",
    "Drag": "Mouse Drag Event",
    "Press": "Mouse Press Event",
    "Scroll": "Mouse Scroll Event"
}

Inspector: dict[str: any] = {
    "Basic": MouseBasicEvent.Inspector,
    "Click": MouseClickEvent.Inspector,
    "Drag": MouseDragEvent.Inspector,
    "Press": MousePressEvent.Inspector,
    "Scroll": MouseScrollEvent.Inspector
}

Event: dict[str: any] = {
    "Basic": MouseBasicEvent.Basic,
    "Click": MouseClickEvent.Click,
    "Drag": MouseDragEvent.Drag,
    "Press": MousePressEvent.Press,
    "Scroll": MouseScrollEvent.Scroll
}


TypeID: dict[str: str] = {
    "Basic": "001001000",
    "Click": "001001001",
    "Drag": '001001002',
    "Press": '001001003',
    "Scroll": "001001004",
}