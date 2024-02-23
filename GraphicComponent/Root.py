import Functions as F
from GraphicComponent.Event import Event

ID_Index = 0
ID_Receive = set()


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
    """
    Root of the Object System
    """
    father: None
    event: dict[str:list[Event]]
    event_track_type: set
    son: set
    ID: str

    def __init__(self, father=None, *args, **kwargs):
        """
        Init root.
        :param father: the father of this object
        :return: None
        """
        self.father = father
        self.son = set()
        self.event_track_type = set()
        self.event = dict()
        self.ID = give_id()
        for name, value in kwargs.items():
            if name == "father":
                self.tree_bind_father(value)

    def update(self):
        """
        Basic Update Function.
        Used customized each object's characteristic
        :return:
        """
        pass

    def __update__(self):
        """
        Real Update Function
        Used to spread update info into depth
        :return:
        """
        self.update()
        for i in self.son:
            i.__update__()

    def tree_add_son(self, son):
        self.son.add(son)
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

    def tree_bind_father(self, father):
        father.tree_add_son(self)

    def event_spread(self, event_name, **event_args):
        """
        This function is used to spread event and turn to next level.
        Nothing will be return
        :return: None
        """
        if event_name in self.event_track_type:
            temp_args = self.event_receive(event_name, **event_args)

            for name, value in self.event.items():
                if name == "OverSpread" and value:
                    return None
                if name == "Fix_args":
                    for name, values in value.items():
                        event_args[name] = values

            for son in self.son:
                son.event_spread(event_name, **F.Mix_Kwargs(event_args, temp_args))
            return None

    def event_receive(self, event_name, **event_args):
        """
        This function is used to receive event argument
        :return:
        """
        if event_name in self.event_track_type:
            if event_name in self.event.keys():
                for i in self.event[event_name]:
                    if i.track_check(**event_args):
                        return i.track_run(**event_args)
        return event_args

    def event_tree_build(self):
        """
        Up to down to build the event tree
        :return:
        """
        event_type = set(self.event.keys())
        for i in self.son:
            event_type.update(i.event_tree_build())
        self.event_track_type = event_type
        return event_type

    def event_tree_update(self, event_track_collection):
        """
        Down to Up to update event
        :return:
        """
        self.event_track_type.update(event_track_collection)
        if self.father:
            self.father.event_tree_update(self.event_track_type)

    def event_add_event(self, event_type, event, **kwargs):
        self.event: dict
        if event_type in self.event.keys():
            self.event[event_type].append(event)
        else:
            self.event.__setitem__(event_type, [event, ])
        event.update_info(**kwargs)
        self.event_tree_update({event_type})

    def event_remove_event(self, event_type: int, event_id: str):
        if event_type in self.event_track_type:
            for event in self.event[event_type]:
                if event.id == event_id:
                    self.event[event_type].pop(event)

    def delete(self) -> str:
        """
        Return ID and Delete the Object
        Warming It Might Make Trouble
        :return: self. ID
        """
        if self.father:
            self.father.son.remove(self)
            self.father.event_tree_build()
            self.father.event_tree_update(set())
        tmp = self.ID
        del self
        ID_Receive.add(tmp)
        return tmp

    def delete_with_son(self):
        if self.son:
            for son in self.son:
                if son != self:
                    son.delete_with_son()
        self.delete()

    def __del__(self):
        self.delete()
