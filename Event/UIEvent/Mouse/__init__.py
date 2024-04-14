from Event.UIEvent.Mouse import Basic, Click, Drag, Press, Scroll


Name: dict[str: str] = {
    "Basic": "Basic Mouse Event",
    "Click": "Mouse Click Event",
    "Drag": "Mouse Drag Event",
    "Press": "Mouse Press Event",
    "Scroll": "Mouse Scroll Event"
}

Inspector: dict[str: any] = {
    "Basic": Basic.Inspector,
    "Click": Click.Inspector,
    "Drag": Drag.Inspector,
    "Press": Press.Inspector,
    "Scroll": Scroll.Inspector
}

Event: dict[str: any] = {
    "Basic": Basic.Basic,
    "Click": Click.Click,
    "Drag": Drag.Drag,
    "Press": Press.Press,
    "Scroll": Scroll.Scroll
}


TypeID: dict[str: str] = {
    "Basic": "001001000",
    "Click": "001001001",
    "Drag": '001001002',
    "Press": '001001003',
    "Scroll": "001001004",
}