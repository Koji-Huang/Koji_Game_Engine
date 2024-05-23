from typing import Callable
from DataType.Generic.LinkedList import LinkedList

_event_id_get: Callable[[], str]
_event_id_recycle: Callable[[str], None]
_inspector_id_get: Callable[[], str]
_inspector_id_recycle: Callable[[str], None]

__registered_event_class: dict
__registered_inspector_class: dict
__event_type_id: set
__registered_name: dict
__instantiation_inspectors: dict


def init():
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    __registered_name = dict()
    __registered_event_class = dict()
    __registered_inspector_class = dict()
    __instantiation_inspectors = dict()
    __event_type_id = set()


def register_new_event(inspector_class, event_class, event_type_id , event_default_name):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    if event_type_id in __event_type_id:
        raise (f'EventManager - Register Error\nRegister ID had been registered.\n'
               f'inspector_class: {inspector_class} | Register ID: {event_type_id}')
    if event_type_id is None:
        event_type_id = spare_event_type_id()
    __event_type_id.add(event_type_id)
    __registered_name[event_type_id] = event_default_name
    __registered_event_class[event_type_id] = event_class
    __registered_inspector_class[event_type_id] = inspector_class
    return event_type_id


def spare_event_type_id():
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    return _event_id_get()


def __initialize_inspector_id():
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    return _inspector_id_get()


def load_default_event():
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    import Event
    load_event_package(Event)


def load_event_package(package):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    for package_name in package.Name.keys():
        try:
            package.TypeID[package_name]
        except ValueError:
            package.TypeID[package_name] = None
        if isinstance(package.TypeID[package_name], str):
            register_new_event(
                package.Inspector[package_name],
                package.Event[package_name],
                package.TypeID[package_name],
                package.Name[package_name]
            )
        else:
            exec("load_event_package(package.%s)" % package_name)


def create_instantiation_inspector(event_type, inspector_init_kwargs, event_init_kwargs):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    new_event = __registered_event_class[event_type](**event_init_kwargs)
    new_event.event_type = event_type
    new_inspector = __registered_inspector_class[event_type](new_event, **inspector_init_kwargs)
    if __instantiation_inspectors.get(event_type) is None:
        __instantiation_inspectors[event_type] = LinkedList()
    __instantiation_inspectors[event_type].append(new_inspector)
    return new_inspector


def update_an_inspector_id(inspector_id, event_type_id):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    return update_an_inspector(match_inspector_id(inspector_id, event_type_id))


def update_an_inspector(inspector):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    if inspector.is_active():
        inspector.update_kwargs()
        if inspector.check() is True:
            inspector.trigger()


def match_inspector_id(inspector_id, event_type_id):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    if event_type_id:
        for inspector in match_inspector_type(event_type_id):
            if inspector.id == inspector_id:
                return inspector
    else:
        for event_type_id in __event_type_id:
            match_inspector_id(inspector_id, event_type_id)


def match_inspector_type(inspector_type):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    return __instantiation_inspectors.get(inspector_type)


def match_event_id(event_id, event_type_id):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    if event_type_id:
        for event in match_event_type(event_type_id):
            if event.id == event_id:
                return event
    else:
        for event_type_id in __event_type_id:
            match_event_id(event_id, event_type_id)


def match_event_type(event_type_id):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    return tuple(inspector.target_event for inspector in match_inspector_type(event_type_id))


def show():
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    """
    print the info of event
    :param
    """


def info(name):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    """
    The info of the manager
    :return: the info
    """


def update():
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    for inspectors in __instantiation_inspectors.values():
        for inspector in inspectors:
            update_an_inspector(inspector)


def graphic_register(main_windows):
    global __registered_name, __registered_event_class, __registered_inspector_class, \
        __instantiation_inspectors, __event_type_id
    create_instantiation_inspector('001001001', {}, {'component': main_windows, 'skip_track': True})
    create_instantiation_inspector('001001002', {}, {'component': main_windows, 'skip_track': True})
    create_instantiation_inspector('001001003', {}, {'component': main_windows, 'skip_track': True})
    create_instantiation_inspector('001001004', {}, {'component': main_windows, 'skip_track': True})
    pass
