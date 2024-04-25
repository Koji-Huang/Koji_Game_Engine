from typing import Callable

from API.Event import Event as __EventAPI
from API.Graphic import GraphicAPI as __GraphicAPI
from API.Thread import ThreadAPI as __ThreadAPI

Registry: dict
Asset: dict
Global_ID_Register: ID

class _IdPackage:
    name: str
    __id_limit: dict[str: int]
    __id_max: dict[str: int]
    __id_recycle: dict[str: list[int]]
    __id_register: set[str]
    __is_customized: bool

    def __init__(self, name: str):
        """

        """

    def __call__(self, object_type: str, *args, **kwargs) -> str:
        """

        """

    def recycle(self, object_type: str, instance) -> None:
        """

        """

    def reset_type(self, object_type: str) -> None:
        """

        """

    def get(self, object_type: str, *args, **kwargs) -> str:
        """

        """

    def customized(self, object_type) -> (Callable[[], str], Callable[[], str], Callable[[], str]):
        """

        """


class ID:
    __id_package: dict[str: _IdPackage]

    def __init__(self):
        """

        """

    def __call__(self, object_type: str, *args, **kwargs):
        """

        """

    def recycle(self, object_type: str, instance):
        """

        """

    def reset_type(self, object_type: str):
        """

        """

    def get(self, object_type: str, *args, **kwargs):
        """

        """

    def customized(self, object_type, sub_type: str = 'undefined', limit_range: int = None) ->  (Callable[[], str], Callable[[], str], Callable[[], str]):
        """

        """


Global_ID_Manager: ID
Global_Event_API: __EventAPI
Global_Graphic_API: __GraphicAPI
Global_Thread_API: __ThreadAPI
Global_Resource: dict[str: any]
Global_Setting: dict[str: any]


Engine_Path: str
Environment_Path: str
General_Config_File_Path: str


def register_global_environment():
    """

    """
    pass
