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


class Event:
    def __init__(self, graphic_object: any):
        self.graphic_object = graphic_object
        self.track_args = dict()
        self.id = give_id()

    def track_check(self, *args, **kwargs):
        return True

    def track_run(self, *args, **kwargs):
        return self.track_function(graphic_object=self.graphic_object, *args, *self.track_args, **kwargs)

    def update_info(self, **kwargs):
        for update_name, update_value in kwargs.items():
            self.track_args.update({update_name: update_value})

    def delete(self):
        tmp = self.id
        ID_Receive.add(self.id)
        del self
        return tmp

    def __copy__(self, copied: any = None):
        if copied is None:
            copied = Event(self.graphic_object)

        copied.event_name = self.event_name
        copied.track_function = self.track_function
        copied.track_args = self.track_args
        copied.event_id = give_id()

        return copied
