from .Basic import *


GraphicWindows: MainWindows
GraphicDebug: any
__debug_mode: bool


def init(mainWindowsObject: MainWindows = None, flags=None, *args, **kwargs):
    global GraphicWindows, GraphicDebug, __debug_mode
    __debug_mode = False
    GraphicDebug = None
    if isinstance(mainWindowsObject, MainWindows):
        GraphicWindows = mainWindowsObject
    elif isinstance(mainWindowsObject, tuple):
        create_windows(mainWindowsObject, flags, *args, **kwargs)
    else:
        pass
    

def create_windows(size, flags, *args, **kwargs):
    global GraphicWindows, GraphicDebug, __debug_mode
    GraphicWindows = MainWindows(size, flags, *args, **kwargs)


def general_info():
    global GraphicWindows, GraphicDebug, __debug_mode
    

def component_type(start_component: Root = None):
    global GraphicWindows, GraphicDebug, __debug_mode
    if start_component is None:
        start_component = GraphicWindows
    ret = set()
    ret.add(start_component.__str__())
    for son in start_component.son:
        ret.update(component_type(son))
    return ret


def component_tree(start_component: Root = None) -> dict[Root: set, ]:
    global GraphicWindows, GraphicDebug, __debug_mode
    if start_component is None:
        start_component = GraphicWindows
    ret = dict()
    son_ret = set()
    for son in start_component.son:
        son_ret.update(component_tree(son))
    ret[start_component] = son_ret
    return ret


def component_find(ID: str, start_component: Root = None) -> Root | None:
    global GraphicWindows, GraphicDebug, __debug_mode
    if start_component is None:
        start_component = GraphicWindows
    if start_component.id == ID:
        return start_component
    else:
        for son in start_component.son:
            ret = component_find(ID, son)
            if ret is not None:
                return ret
    return None


def components_find(ID: tuple[str, ], start_component: Root = None) -> tuple[Root | None, ]:
    global GraphicWindows, GraphicDebug, __debug_mode
    ret = list()
    for each_ID in ID:
        ret.append(component_find(each_ID, start_component))
    return tuple(ret)


def components_find_type(component_types: str, start_component: Root = None) -> tuple[Root,]:
    global GraphicWindows, GraphicDebug, __debug_mode
    ret = list()
    if start_component is None:
        start_component = GraphicWindows
    if start_component.__str__() == component_types:
        ret.append(start_component)
    for son in start_component.son:
        ret += components_find_type(component_types, son)
    return tuple(ret)


def component_add(component: Root, father_component: Root = None) -> None:
    global GraphicWindows, GraphicDebug, __debug_mode
    if father_component is None:
        father_component = GraphicWindows
    father_component.tree_add_son(component)


def components_add(component: tuple[Root, ], father_component: Root = None) -> None:
    global GraphicWindows, GraphicDebug, __debug_mode
    if father_component is None:
        father_component = GraphicWindows
    for each in component:
        component_add(each, father_component)


def component_remove(target: str | Root) -> None:
    global GraphicWindows, GraphicDebug, __debug_mode
    if isinstance(target, str):
        target = component_find(target, GraphicWindows)
    if isinstance(target, Root):
        target.delete_with_son()


def components_remove(target: tuple[str or Root, ]) -> None:
    global GraphicWindows, GraphicDebug, __debug_mode
    for i in target:
        component_remove(i)


def graphic_update():
    global GraphicWindows, GraphicDebug, __debug_mode
    if __debug_mode:
        Graph.graph_update(GraphicWindows)
        GraphicWindows.windows_surface.blit(GraphicWindows.graph_surface, (0, 0))
        GraphicDebug.graphic_debug()
    else:
        GraphicWindows.graph_update()


def event_get(pid: str, event_type: str = None, component: Root = None):
    global GraphicWindows, GraphicDebug, __debug_mode
    if component is None:
        component = GraphicWindows
    if event_type is not None:
        if event_type in component.event_type:
            for event in component.event[event_type]:
                if event.id == pid:
                    return event, component, event_type
        else:
            return None
    else:
        for event_type in component.event_type:
            for event in component.event[event_type]:
                if event.id == pid:
                    return event, component, event_type
    for son in component.son:
        son_result = event_get(pid, event_type, son)
        if son_result is not None:
            return son_result, component, event_type
    return None


def event_remove(pid: str, event_type: str = None, component: Root = None) -> None:
    global GraphicWindows, GraphicDebug, __debug_mode
    event, component, event_type = event_get(pid, event_type, component)
    component.event_remove(event_type, pid)


def event_add(event, event_type: int = 0, father_component: Root = None) -> None:
    global GraphicWindows, GraphicDebug, __debug_mode
    if father_component is None:
        father_component = GraphicWindows
    father_component.event_add(event_type, event)


def event_tree(start_component: str | Root = None, event_type: str = None):
    global GraphicWindows, GraphicDebug, __debug_mode
    if start_component is None:
        start_component = GraphicWindows
    ret = dict()
    if event_type is None:
        copied = start_component.event.copy()
        collections = list()
        for son in start_component.son:
            collections.append(event_tree(son))
    else:
        copied = start_component.event[event_type].copy()
        collections = list()
        for son in start_component.son:
            collections.append(event_tree(son))
    ret[start_component.id] = {copied: collections}
    return ret


def event_id_tree(start_component: str | Root, event_type: str = None):
    global GraphicWindows, GraphicDebug, __debug_mode
    if start_component is None:
        start_component = GraphicWindows
    ret = dict()
    if event_type is None:
        copied = {event_type: event.id for event_type in start_component.event_type
                  for event in start_component.event[event_type]}
        collections = list()
        for son in start_component.son:
            collections.append(event_id_tree(son))
    else:
        copied = [event.id for event in start_component.event[event_type]]
        collections = list()
        for son in start_component.son:
            collections.append(event_id_tree(son))
    ret[start_component.id] = {copied: collections}
    return ret


def event_type_tree(start_component: str | Root, event_type: str = None):
    global GraphicWindows, GraphicDebug, __debug_mode
    if start_component is None:
        start_component = GraphicWindows
    ret = dict()
    if event_type is None:
        copied = start_component.event_type.copy()
        collections = list()
        for son in start_component.son:
            collections.append(event_type_tree(son))
    else:
        copied = [event_type]
        collections = list()
        for son in start_component.son:
            collections.append(event_type_tree(son))
    ret[start_component.id] = {copied: collections}
    return ret


def event_update():
    global GraphicWindows, GraphicDebug, __debug_mode
    GraphicWindows.event_update()
    if __debug_mode:
        GraphicDebug.event_debug()


def set_debug(enable: bool = None):
    global GraphicWindows, GraphicDebug, __debug_mode
    if enable:
        __debug_mode = True
        if GraphicDebug is None:
            from .Debug import GraphicDebug
            GraphicDebug = GraphicDebug(GraphicWindows, GraphicWindows)
    else:
        __debug_mode = False


def update_component_event(component: Root, event_type: int, event, **kwargs):
    global GraphicWindows, GraphicDebug, __debug_mode
    if component is None:
        component = GraphicWindows
    component.event_spread(event_type, event=event, **kwargs)


def update_component_graphic(component: Root, *args, **kwargs):
    global GraphicWindows, GraphicDebug, __debug_mode
    if component is not None:
        component = GraphicWindows
    component.graph_update(*args, **kwargs)
