import math
from functools import partial


class _IdPackage:
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
                self.__id_recycle[object_type] = set()

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
            self.__id_recycle[object_type] = set()

    def customized(self, object_type, limit_range: int = None):
        self.__id_limit[object_type] = limit_range
        if self.__is_customized is False:
            return partial(self.__call__, object_type=object_type), \
                partial(self.recycle, object_type=object_type), partial(self.reset_type, object_type=object_type)


class IDRegister:
    def __init__(self):
        self.__id_package = dict()
        self.get = self.__call__

    def __call__(self, object_type: str, sub_type: str = 'undefined', *args, **kwargs):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = _IdPackage(sub_type)
        return self.__id_package()

    def recycle(self, object_type: str, instance, sub_type: str = 'undefined'):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = _IdPackage(sub_type)
        return self.__id_package[sub_type].recycle(object_type, instance)

    def reset_type(self, object_type: str, sub_type: str = 'undefined'):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = _IdPackage(sub_type)
        return self.__id_package[sub_type].reset_type(object_type)

    def customized(self, object_type, sub_type: str = 'undefined', limit_range: int = None):
        if self.__id_package.get(sub_type) is None:
            self.__id_package[sub_type] = _IdPackage(sub_type)
        return self.__id_package[sub_type].customized(object_type, limit_range)