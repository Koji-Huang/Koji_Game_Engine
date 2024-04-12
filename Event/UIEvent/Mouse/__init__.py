from Event.UIEvent.Mouse import Basic, Click, Move, Press, Scroll


Name: dict[str: str] = {
    "Basic": "Basic Mouse Event",
    "Click": "Mouse Click Event",
    # "Move",
    # "Press",
    # "Scroll"
}

Inspector: dict[str: any] = {
    "Basic": Basic.Inspector,
    "Click": Click.Inspector,
    # "Move": Move.Inspector,
    # "Press": Press.Inspector,
    # "Scroll": Scroll.Inspector
}

Event: dict[str: any] = {
    "Basic": Basic.Basic,
    "Click": Click.Click,
    # "Move": Move.Move,
    # "Press": Press.Press,
    # "Scroll": Scroll.Sccroll
}


TypeID: dict[str: str] = {
    "Basic": "001001000",
    "Click": "001001001",
    # "Move": '001001002',
    # "Press": '001001003',
    # "Scroll": "001001004",
}