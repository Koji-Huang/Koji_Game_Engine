from DataType.SystemComponent import *

from API.Event import Event as __EventAPI
from API.Graphic import GraphicAPI as __GraphicAPI
from API.Thread import ThreadAPI as __ThreadAPI

Registry: RegistryObject
AssetManager: AssetManagerObject
ID_Register: IDRegisterObject


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
