from GraphicComponent.UI.Label import Label
from Event.UIEvent.Mouse.Click import Click
from Event.UIEvent.Mouse import TypeID


ClickEventTypeID = TypeID['Click']


class Button(Label):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)

    def bind_press_function(self, function, button, **kwargs):
        make_event = Click(self, button)
        make_event.track_function = function
        make_event.track_args = kwargs
        self.event_add(ClickEventTypeID, make_event, **kwargs)

    def unbind_press_function(self, button) -> None:
        if ClickEventTypeID in self.event_type:
            for i in self.event[ClickEventTypeID]:
                i: Click
                if i.event_name == button:
                    self.event_remove(button, i.id)

    def search_press_function(self, button) -> tuple[Click, ...]:
        ret = []
        if ClickEventTypeID in self.event_type:
            for i in self.event[ClickEventTypeID]:
                i: Click
                if i.event_name == button:
                    ret.append(i)
        return tuple(ret)

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Button(self.pos(), self.size())
        super().__copy__(copied)
        return copied
