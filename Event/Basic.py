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


class BasicEvent:
    def __init__(self, *args, **kwargs):
        self.event_type_name = "Event_Basic"
        self.event_name = 'undefined'
        self.track_args = dict()
        self.id = give_id()

    def track_check(self, *args, **kwargs):
        return True

    def track_run(self, *args, **kwargs):
        return self.track_function(*args, *self.track_args, **kwargs)

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
            copied = BasicEvent()
        copied.event_name = self.event_name
        copied.track_function = self.track_function
        copied.track_args = self.track_args
        copied.event_type = give_id()

        return copied


class Inspector:
    target_event_class = BasicEvent

    def __init__(self, target: BasicEvent):
        if isinstance(target, self.target_event_class):
            self.target_event = target
        else:
            raise f"Error Event Type for inspect\nTarget Event: {self.target_event_class}\nInput Event: {target}\n"

    def check(self, **kwargs):
        if kwargs is not None:
            self.target_event.update_info(**kwargs)
        return self.target_event.track_check(**kwargs)

    def trigger(self, **kwargs):
        return self.target_event.track_run(**kwargs)
