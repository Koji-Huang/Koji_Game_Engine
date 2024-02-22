from EventEngine.Event import Event as Event
from EventEngine.Subchannel import Subchannel


class Channel(object):
    # 通道对象
    channels: tuple[Subchannel]

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

    def addSubchannel(self, subchannel: Subchannel) -> None:
        ...

    def removeSubchannel(self, name: str or int) -> None:
        ...

    def setSubchannel(self, name: str or int) -> None:
        ...

    def getSubchannel(self, name: str or int) -> Subchannel:
        ...

    def addEvent(self, event: Event) -> None:
        ...

    def removeEvent(self, event: Event) -> None:
        ...

    def getEvent(self, subchannel: str, index: int) -> Event:
        ...

    def setEvent(self, event: Event) -> None:
        ...

