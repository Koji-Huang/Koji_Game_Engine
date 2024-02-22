from EventEngine.Event import Event as Event


class Subchannel(object):
    events: tuple[Event]
    name: str

    def __init__(self, name: str):
        ...

    def __call__(self, *args, **kwargs) -> Event or tuple[Event]:
        ...

    # 根据 [] 获取元素
    def __getitem__(self, item: int) -> Event:
        ...

    def __setitem__(self, key: int, value: Event) -> None:
        ...

    def __delitem__(self, key: int) -> None:
        ...

    def __len__(self) -> int:
        ...

    # 添加
    def __add__(self, other: Event) -> None:
        ...

    # 删除
    def __sub__(self, other: Event) -> None:
        ...

    # 迭代器实例
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

