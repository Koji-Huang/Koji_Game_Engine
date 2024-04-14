from Event.Basic import BasicEvent as Event, Inspector
from DataType.LinkedList import LinkedList
from Graphic.MainWindows import MainWindows


class EventManager:
    # event type id to Event Object
    __registered_event_class: dict[str: Event, ...]
    # event type id to Inspector Object
    __registered_inspector_class: dict[str: Inspector, ...]
    # as name
    __event_type_id: set[str]
    # event name
    __registered_name: dict[str: any]
    # Instantiation inspector object
    __instantiation_inspectors: dict[str: LinkedList[Inspector, ...], ...]

    def __init__(self, *args, **kwargs):
        ...

    def register_new_event(self,
                           inspector_class: Inspector.__class__,
                           event_class: Event.__class__,
                           event_type_id: int = None,
                           event_default_name: str = 'undefined') -> str:
        """
        Register a new event type
        :param event_class: event's class (not Instantiation)
        :param inspector_class: inspector's class (not Instantiation)
        :param event_type_id: The id to register, if value == None, it will give a usable id back and register.
        :param event_default_name: the default name to set the event
        :return: The event's id
        """

    def load_default_event(self) -> None:
        """
        Load System Default Event
        """

    def spare_event_type_id(self) -> str:
        ...

    def __initialize_inspector_id(self):
        """
        Give initialize inspector an id
        """

    def load_event_package(self, package: any) -> None:
        """
        Load a format package
        """

    def create_instantiation_inspector(self, event_type: str, inspector_init_kwargs: dict, event_init_kwargs: dict) -> Inspector:
        """
        Create an instantiation Inspector with event
        :param event_type: the event_type_id
        :param inspector_init_kwargs: the init kwargs of inspector
        :param  event_init_kwargs: the init kwargs of event
        :return: the Inspector, if result is None,
            that mean the init of inspector or event may error and
            error raise had been eliminated.
        """

    def update_an_inspector_id(self, inspector_id: str, event_type_id: int = None):
        """
        Start an inspection.
        :param inspector_id: the id of instantiation inspector
        :param event_type_id: the type of event
        :return: bool of whether start
        """

    def update_an_inspector(self, inspector: Inspector):

        """
        Start an inspection.
        :param inspector: inspector
        :return: bool of whether start
        """

    def match_inspector_id(self, inspector_id: str, event_type_id: str = None) -> Inspector:
        """
        Match an inspetor by id.
        :param inspector_id: the id of inspector
        :param event_type_id: the event_type_id of inspector
        :return: the Inspector
        """

    def match_inspector_type(self, inspector_type: str) -> tuple[Inspector, ...]:
        """
        Match inspector by event_type
        :param inspector_type: the type of inspector
        :return: the tuple of matched Inspector
        """

    def match_event_id(self, event_id: str, event_type_id: str = None) -> Event:
        """
        Match an event by id.
        :param event_id: the id of event
        :param event_type_id: the event_type_id of inspector
        :return: the Event
        """

    def match_event_type(self, event_type: str) -> tuple[Event, ...]:
        """
        Match events by event_type
        :param event_type: the type of event
        :return: the tuple of matched Event
        """

    def show(self):
        """
        print the info of event
        :param
        """

    def info(self, name: str or tuple[str, ...]):
        """
        The info of the manager
        :return: the info
        """

    def update(self):
        """
        Update all the Registered Inspector
        """

    def graphic_register(self, main_widows: MainWindows):
        """
        ...
        """

    def update_pygame_event(self):
        """

        """
