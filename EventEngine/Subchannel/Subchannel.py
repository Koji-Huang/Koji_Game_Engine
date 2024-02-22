from EventEngine.Event import Event as Event
from EventEngine.Channel.BasicEventChannel import Channel


class Subchannel(object):
    channel: Channel
    events: tuple[Event]
    name: str

    def __init__(self, name: str, channel: Channel, events: tuple[Event] or None = None) -> None:
        ...

    def __call__(self, *args, **kwargs) -> Event or tuple[Event]:
        ...

    # ���� [] ��ȡԪ��
    def __getitem__(self, item: int) -> Event:
        ...

    def __setitem__(self, key: int, value: Event) -> None:
        ...

    def __delitem__(self, key: int) -> None:
        ...

    def __len__(self) -> int:
        ...

    # ���
    def __add__(self, other: Event) -> None:
        ...

    # ɾ��
    def __sub__(self, other: Event) -> None:
        ...

    # ������ʵ��
    def __iter__(self):
        ...

    def run(self) -> None:
        ...

    def add(self, event: Event) -> None:
        ...

    def remove(self, event: Event) -> None:
        ...

    def remove_index(self, index) -> None:
        ...

    def get(self, index: int) -> Event:
        ...

