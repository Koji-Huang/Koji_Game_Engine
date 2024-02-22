from EventEngine.Event import Event as Event
from EventEngine.Subchannel import Subchannel


class Channel(object):
    # ͨ������
    subchannels: tuple[Subchannel]

    def __init__(self):
        ...

    # Iterable
    def __iter__(self):
        ...

    # Sequence
    def __delitem__(self, key: int or str) -> None:
        ...

    def __getitem__(self, item: int or str) -> Subchannel:
        ...

    def __setitem__(self, key: int or str, value: Subchannel) -> None:
        ...

    def __len__(self) -> int:
        ...

    def addSubChannel(self, channel: Subchannel) -> None:
        ...

    def removeChannel(self, name: str or int) -> None:
        ...

    def setChannel(self, name: str or int) -> None:
        ...

    def getChannel(self, name: str or int) -> Subchannel:
        ...

    def addEvent(self, event: Event) -> None:
        ...

    def removeEvent(self, event: Event) -> None:
        ...

    def getEvent(self, channel: str, index: int) -> Event:
        ...

    def setEvent(self, event: Event) -> None:
        ...

