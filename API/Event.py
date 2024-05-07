from typing import Callable
from Event.BasicEvent import BasicEvent as Event, Inspector
from DataType.Generic.LinkedList import LinkedList


_event_id_get: Callable[[], str]
_event_id_recycle: Callable[[str], None]
_inspector_id_get: Callable[[], str]
_inspector_id_recycle: Callable[[str], None]


class EventAPI:
    def __init__(self, *args, **kwargs):
        self.__registered_name = dict()
        self.__registered_event_class = dict()
        self.__registered_inspector_class = dict()
        self.__instantiation_inspectors = dict()
        self.__event_type_id = set()

    def register_new_event(self,
                           inspector_class: Inspector.__class__,
                           event_class: Event.__class__,
                           event_type_id: int = None,
                           event_default_name: str = 'undefined') -> str:
        if event_type_id in self.__event_type_id:
            raise (f'EventManager - Register Error\nRegister ID had been registered.\n'
                   f'inspector_class: {inspector_class} | Register ID: {event_type_id}')
        if event_type_id is None:
            event_type_id = self.spare_event_type_id()
        self.__event_type_id.add(event_type_id)
        self.__registered_name[event_type_id] = event_default_name
        self.__registered_event_class[event_type_id] = event_class
        self.__registered_inspector_class[event_type_id] = inspector_class
        return event_type_id

    def spare_event_type_id(self):
        return _event_id_get()

    def __initialize_inspector_id(self):
        return _inspector_id_get()

    def load_default_event(self) -> None:
        import Event
        self.load_event_package(Event)

    def load_event_package(self, package: any) -> None:
        for package_name in package.Name.keys():
            try:
                package.TypeID[package_name]
            except ValueError:
                package.TypeID[package_name] = None
            if isinstance(package.TypeID[package_name], str):
                self.register_new_event(
                    package.Inspector[package_name],
                    package.Event[package_name],
                    package.TypeID[package_name],
                    package.Name[package_name]
                )
            else:
                exec("self.load_event_package(package.%s)" % package_name)

    def create_instantiation_inspector(self, event_type: str, inspector_init_kwargs: dict, event_init_kwargs: dict):
        new_event = self.__registered_event_class[event_type](**event_init_kwargs)
        new_event.event_type = event_type
        new_inspector: Inspector = self.__registered_inspector_class[event_type](new_event, **inspector_init_kwargs)
        if self.__instantiation_inspectors.get(event_type) is None:
            self.__instantiation_inspectors[event_type] = LinkedList()
        self.__instantiation_inspectors[event_type].append(new_inspector)
        return new_inspector

    def update_an_inspector_id(self, inspector_id: str, event_type_id: int = None):
        return self.update_an_inspector(self.match_inspector_id(inspector_id, event_type_id))

    @staticmethod
    def update_an_inspector(inspector: Inspector):
        if inspector.is_active():
            inspector.update_kwargs()
            if inspector.check() is True:
                inspector.trigger()

    def match_inspector_id(self, inspector_id: str, event_type_id: str = None) -> Inspector:
        if event_type_id:
            for inspector in self.match_inspector_type(event_type_id):
                if inspector.id == inspector_id:
                    return inspector
        else:
            for event_type_id in self.__event_type_id:
                self.match_inspector_id(inspector_id, event_type_id)

    def match_inspector_type(self, inspector_type: str) -> tuple[Inspector, ...]:
        return self.__instantiation_inspectors.get(inspector_type)

    def match_event_id(self, event_id: str, event_type_id: str = None) -> Event:
        if event_type_id:
            for event in self.match_event_type(event_type_id):
                if event.id == event_id:
                    return event
        else:
            for event_type_id in self.__event_type_id:
                self.match_event_id(event_id, event_type_id)

    def match_event_type(self, event_type_id: str) -> tuple[Event, ...]:
        return tuple(inspector.target_event for inspector in self.match_inspector_type(event_type_id))

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
        for inspectors in self.__instantiation_inspectors.values():
            for inspector in inspectors:
                self.update_an_inspector(inspector)

    def graphic_register(self, main_windows):
        self.create_instantiation_inspector('001001001', {}, {'component': main_windows, 'skip_track': True})
        self.create_instantiation_inspector('001001002', {}, {'component': main_windows, 'skip_track': True})
        self.create_instantiation_inspector('001001003', {}, {'component': main_windows, 'skip_track': True})
        self.create_instantiation_inspector('001001004', {}, {'component': main_windows, 'skip_track': True})
        pass
