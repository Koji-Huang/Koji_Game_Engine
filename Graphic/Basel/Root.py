__dict__ = ['Root']

from typing import Callable
from DataType import LinkedList

ID_Index = 0
ID_Receive = LinkedList()

_graphic_id_get: Callable[[], str]
_graphic_id_recycle: Callable[[str], None]


class Root:
    def __init__(self, father=None, *args, **kwargs):
        self.father = father
        self.son = LinkedList()
        self.event_type = set()
        self.event_type_match = dict()
        self.event = dict()
        self.id = _graphic_id_get()
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
        self.event_tree_update(son.event_type)
        pass

    def tree_remove_son(self, son):
        self.son.remove(son)
        self.spread_type_update(son, decrease=True, increase=False)
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

    def event_check(self, event_object, *args, **kwargs) -> bool:
        return event_object.track_check(*args, **kwargs)

    def event_run(self, event_object, *args, **kwargs) -> any:
        return event_object.track_run(*args, **kwargs)

    def event_clean(self) -> None:
        event_type = set(self.event.keys())
        for i in self.son:
            event_type.update(i.event.keys())
        self.event_type = event_type

    def event_tree(self) -> list:
        return list((self.event_type, (i.event_tree() for i in self.son)))

    def event_value(self) -> list:
        return [i for i in self.event.items()]

    def event_add(self, event_type, event, **kwargs):
        if event_type in self.event.keys():
            self.event[event_type].append(event)
        else:
            self.event.__setitem__(event_type, [event, ])
            self.event_type.add(event_type)
        if kwargs:
            event.update_info(**kwargs)
        self.event_tree_update({event_type})
        event.graphic_object = self

    def event_remove(self, event_type, event):
        from Event.UIEvent.Basic import Basic as Event
        if event_type in self.event_type:
            if isinstance(event, str):
                for event in self.event[event_type]:
                    if event.id == event:
                        self.event[event_type].pop(event)
            elif isinstance(event, Event):
                self.event[event_type].pop(event)
            else:
                pass
            if len(self.event[event_type]) == 0:
                self.event_type.remove(event_type)
                self.event.pop(event_type)

    def event_spread(self, event_name, inspector: any = None, **event_args: dict):
        spread_event_kwargs = event_args
        if event_name in self.event.keys():
            for event in self.event[event_name]:
                if self.event_check(event, **event_args):
                    self.event_run(event, **event_args)
        if inspector:
            spread_event_kwargs.update(inspector.target_event.update_kwargs(component=self, **event_args.copy()))
        if self.event_type_match.get(event_name):
            for son in self.event_type_match[event_name]:
                son.event_spread(event_name, inspector, **spread_event_kwargs)
        return None

    def event_tree_update(self, another_set):
        self.event_type.update(another_set)
        if self.father:
            self.father.event_tree_update(self.event_type)
            self.father.spread_type_update(self)

    def delete(self) -> str:
        for i in self.event.items():
            for event in i:
                event.delete()
        # Root Object
        if self.father:
            self.father.son.remove(self)
            self.father.event_clean()
        tmp = self.id
        _graphic_id_recycle(tmp)
        del self
        return tmp

    def delete_with_son(self):
        if self.son:
            for son in self.son:
                if son != self:
                    son.delete_with_son()
        self.delete()

    def spread_type_update(self, son=None, increase: bool = True, decrease: bool = False):
        if son:
            if increase:
                for event in son.event_type:
                    if self.event_type_match.get(event) is None:
                        self.event_type_match[event] = set()
                    self.event_type_match[event].add(son)
            if decrease:
                for event in son.event_type:
                    if self.event_type_match.get(event):
                        self.event_type_match[event].remove(son)
        else:
            for son in self.son:
                self.spread_type_update(son, increase, decrease)

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Root()
        for event_type in self.event.keys():
            for event in self.event[event_type]:
                copy_event = event.__copy__()
                copied.event_add(event_type, copy_event)
        return copied
