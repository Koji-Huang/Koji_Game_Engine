

from Global import ID_Register
from .Basic import RootPackage as __GraphicFile
_get, _recycle, _reset = ID_Register.customized('Graphic', 'EventSystem')
__GraphicFile._graphic_id_get = _get
__GraphicFile._graphic_id_recycle = _recycle

from .Management import *
