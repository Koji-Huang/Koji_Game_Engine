from GraphicComponent import Event
from CustomDataType import LinkedList


class Root:
    father: Root
    event: dict[str:list[Event], ...]
    event_track_type: set[any]
    son: LinkedList[Root]
    ID: str

    def __init__(self, *args, **kwargs) -> None:...

    def update(self, *args) -> None:...

    def __update__(self) -> None:...

    def tree_add_son(self, son: Root) -> None:...

    def tree_remove_son(self, son: Root) -> None:...

    def tree_find_root(self) -> Root:...

    def tree_goto_father(self, general: int) -> Root:...

    def event_add(self, event_type: int, event: Event, **kwargs) -> None:...

    def event_remove(self, event_type: int, event_id: str) -> None:...

    def event_spread(self, event_name, **event_args):...

    def event_check(self, eventObject: Event, *args, **kwargs) -> bool:...

    def event_run(self, eventObject: Event, *args, **kwargs) -> any:...

    def event_clean(self) -> None:...

    def event_tree(self) -> list:...

    def event_type(self) -> set:...

    def event_value(self) -> list:...

    def event_tree_update(self, another_set):...

    def delete(self)->None:...

    def delete_with_son(self)->None:...

    def __copy__(self, copied: any = None):...
