import math
from functools import partial


Registry: dict = dict()
Global_ID_Register: any


class IdPackage:
    def __init__(self, name: str):
        self.name = name
        self.__id_limit = dict()
        self.__id_max = dict()
        self.__id_recycle = dict()
        self.__id_register = set()
        self.__is_customized = False

    def __call__(self, object_type: str = 'undefined', *args, **kwargs):
        if object_type not in self.__id_register:
            self.__id_register.add(object_type)
            if self.__id_max.get(object_type) is None:
                self.__id_max[object_type] = 0
            if self.__id_limit.get(object_type) is None:
                self.__id_limit[object_type] = 7
            if self.__id_recycle.get(object_type) is None:
                self.__id_recycle[object_type] = list()

        if self.__id_recycle[object_type]:
            return self.__id_register.pop()
        else:
            num = self.__id_max[object_type] + 1
            self.__id_max[object_type] += 1

            return '0' * (self.__id_limit[object_type] - int(math.log10(num))) + '%d' % num

    def recycle(self, instance, object_type: str = 'undefined'):
        self.__id_recycle[object_type].add(instance)

    def reset_type(self, object_type: str = 'undefined'):
        if object_type in self.__id_register is None:
            self.__id_register.remove(object_type)
        if self.__id_max.get(object_type) is None:
            self.__id_max[object_type] = 0
        if self.__id_limit.get(object_type) is None:
            self.__id_limit[object_type] = 10 ** 7
        if self.__id_recycle.get(object_type) is None:
            self.__id_recycle[object_type] = list()

    def customized(self, object_type, limit_range: int = None):
        self.__id_limit[object_type] = limit_range
        if self.__is_customized is False:
            return partial(self.__call__, object_type=object_type), \
                partial(self.recycle, object_type=object_type), partial(self.reset_type, object_type=object_type)


class ID:
    def __init__(self):
        self.__id_package = dict()
        self.get = self.__call__

    def __call__(self, object_type: str, sub_type: str = 'undefined', *args, **kwargs):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = IdPackage(sub_type)
        return self.__id_package()

    def recycle(self, object_type: str, instance, sub_type: str = 'undefined'):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = IdPackage(sub_type)
        return self.__id_package[sub_type].recycle(object_type, instance)

    def reset_type(self, object_type: str, sub_type: str = 'undefined'):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = IdPackage(sub_type)
        return self.__id_package[sub_type].reset_type(object_type)

    def customized(self, object_type, sub_type: str = 'undefined', limit_range: int = None):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = IdPackage(sub_type)
        return self.__id_package[sub_type].customized(object_type, limit_range)


def register_global_environment_id():
    global Global_ID_Register
    Global_ID_Register = ID()

    from Thread import Thread as __ThreadFile
    _get, _recycle, _reset = Global_ID_Register.customized('Thread', 'ThreadSystem')
    __ThreadFile._id_get = _get
    __ThreadFile._id_recycle = _recycle

    from Event import Basic as __EventFile
    from Manager import EventManager as __EventManager
    _get, _recycle, _reset = Global_ID_Register.customized('Event', 'EventSystem')
    __EventFile._event_id_get = _get
    __EventFile._event_id_recycle = _recycle
    __EventManager._event_id_get = _get
    __EventManager._event_id_recycle = _recycle

    _get, _recycle, _reset = Global_ID_Register.customized('Inspector', 'EventSystem')
    __EventFile._inspector_id_get = _get
    __EventFile._inspector_id_recycle = _recycle
    __EventManager._inspector_id_get = _get
    __EventManager._inspector_id_recycle = _recycle

    from Graphic import RootPackage as __GraphicFile
    _get, _recycle, _reset = Global_ID_Register.customized('Graphic', 'EventSystem')
    __GraphicFile._graphic_id_get = _get
    __GraphicFile._graphic_id_recycle = _recycle


