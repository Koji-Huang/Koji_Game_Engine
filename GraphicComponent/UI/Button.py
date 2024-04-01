from GlobalConstant import EventConstant
from GraphicComponent.UI.Label import Label
from GraphicComponent.Event.MouseEvent import *


class Button(Label):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)

    def bind_press_function(self, function, button, **kwargs):
        make_event = Press(function, button, self)
        self.event_add(EventConstant.MouseButtonUp, make_event, **kwargs)

    def unbind_press_function(self, button) -> None:
        if EventConstant.MouseButtonPress in self.event_type:
            for i in self.event[EventConstant.MouseButtonUp]:
                i: Press
                if i.event_name == button:
                    self.event_remove(button, i.id)

    def search_press_function(self, button) -> tuple[Press, ...]:
        ret = []
        if EventConstant.MouseButtonUp in self.event_type:
            for i in self.event[EventConstant.MouseButtonUp]:
                i: Press
                if i.event_name == button:
                    ret.append(i)
        return tuple(ret)

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Button(self.pos(), self.size())
        super().__copy__(copied)
        return copied
