from .ConfigRegistry import Registry as RegistryObject

# Global Constant
ConfigRegistry = RegistryObject()
ConfigRegistryType = dict()


from . import Basel
ConfigRegistryType['Basic'] = Basel.AbstractConfig
ConfigRegistryType['Abstract'] = Basel.AbstractConfig
ConfigRegistryType['Txt'] = Basel.Txt
ConfigRegistryType['txt'] = Basel.Txt
ConfigRegistryType['Json'] = Basel.Json
ConfigRegistryType['json'] = Basel.Json
ConfigRegistryType['Ini'] = Basel.Ini
ConfigRegistryType['ini'] = Basel.Ini

from .ScriptAssetConfig import Script as __script
ConfigRegistryType['Script'] = __script
ConfigRegistryType['script'] = __script
from .AnimationAssetConfig import Animation as __animation
ConfigRegistryType['Animation'] = __animation
ConfigRegistryType['animation'] = __animation
from .ImageAssetConfig import Image as __image
ConfigRegistryType['Image'] = __image
ConfigRegistryType['image'] = __image
from .ScriptSingleAssetConfig import Script as __script
ConfigRegistryType['SingleScript'] = __script
ConfigRegistryType['singleScript'] = __script
ConfigRegistryType['single_script'] = __script


def get_file_type(file_name):
    if isinstance(file_name, str):
        end_str = ''
        for char in file_name[::-1]:
            if char == '.': break
            else: end_str += char
        return end_str[::-1]


from .Management import *
