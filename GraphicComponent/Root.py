from GraphicComponent.Event import Event
from CustomDataType import LinkedList
ID_Index = 0
ID_Receive = LinkedList()


def give_id() -> str:
    global ID_Index, ID_Receive
    if ID_Receive:
        tmp = next(iter(ID_Receive))
        ID_Receive.remove(tmp)
        return str(tmp)
    else:
        ID_Index += 1
        return str(ID_Index)


class Root:
    father: None
    event: dict[str:list[Event]]
    event_track_type: set
    son: LinkedList
    ID: str

    def __init__(self, father=None, *args, **kwargs):
        self.father = father
        self.son = LinkedList()
        self.event_track_type = set()
        self.event = dict()
        self.id = give_id()
        for name, value in kwargs.items():
            if name == "father":
                value.tree_add_son(self)

    def update(self):
        pass

    def __update__(self):
        self.update()
        for i in self.son:
            i.__update__()

    def tree_add_son(self, son):
        self.son.append(son)
        son.father = self
        self.event_tree_update(son.event_track_type)
        pass

    def tree_remove_son(self, son):
        self.son.remove(son)
        son.father = None

    def tree_find_root(self):
        if self.father:
            return self.father.tree_find_root()
        else:
            return self

    def tree_goto_father(self, general: int):
        if self.father and general:
            return self.father.tree_goto_father(general - 1)
        else:
            return self

    def event_check(self, eventObject: Event, *args, **kwargs) -> bool:
        return eventObject.track_check(*args, **kwargs)

    def event_run(self, eventObject: Event, *args, **kwargs) -> any:
        return eventObject.track_run(*args, **kwargs)

    def event_clean(self) -> None:
        event_type = set(self.event.keys())
        for i in self.son:
            event_type.update(i.event.keys())
        self.event_track_type = event_type

    def event_tree(self) -> list:
        return list((self.event_track_type, (i.event_tree() for i in self.son)))

    def event_type(self) -> set:
        return self.event_track_type

    def event_value(self) -> list:
        return [i for i in self.event.items()]

    def event_add(self, event_type, event, **kwargs):
        if event_type in self.event.keys():
            self.event[event_type].append(event)
        else:
            self.event.__setitem__(event_type, [event, ])
        if kwargs:
            event.update_info(**kwargs)
        self.event_tree_update({event_type})
        event.graphic_object = self

    def event_remove(self, event_type: int, event_id: str):
        if event_type in self.event_track_type:
            for event in self.event[event_type]:
                if event.id == event_id:
                    self.event[event_type].pop(event)

    def event_spread(self, event_name, **event_args):
        if event_name in self.event.keys():
            for event in self.event[event_name]:
                if self.event_check(event, **event_args):
                    self.event_run(event, **event_args)
        for son in self.son:
            son.event_spread(event_name, **event_args)
        return None

    def event_tree_update(self, another_set):
        self.event_track_type.update(another_set)
        if self.father:
            self.father.event_tree_update(self.event_track_type)

    def delete(self) -> str:
        # Event Object
        for i in self.event.items():
            for event in i:
                event.delete()
        # Root Object
        if self.father:
            self.father.son.remove(self)
            self.father.event_clean()
        tmp = self.id
        ID_Receive.append(tmp)
        del self
        return tmp

    def delete_with_son(self):
        if self.son:
            for son in self.son:
                if son != self:
                    son.delete_with_son()
        self.delete()

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Root()
            copied.id = give_id()
        for event_type in self.event.keys():
            for event in self.event[event_type]:
                copy_event = event.__copy__()
                copied.event_add(event_type, copy_event)
        return copied
