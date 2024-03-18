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
    event_name: any
    track_function: any
    track_index: int
    track_args: dict
    event_id: int or any
    id: str

    def __init__(self):
        self.track_args = dict()
        self.id = give_id()

    def track_check(self, *args, **kwargs):
        return True

    def track_run(self, *args, **kwargs):
        return self.track_function(*args, *self.track_args, **kwargs)

    def update_info(self, **kwargs):
        for update_name, update_value in kwargs.items():
            self.track_args.update({update_name: update_value})
