
from .AnimationAssetConfig import Animation as AnimationAssetConfigObject
from .ImageAssetConfig import Image as ImageAssetConfigObject
from .ScriptAssetConfig import Script as ScriptAssetConfigObject


def get_file_type(file_name):
    if isinstance(file_name, str):
        end_str = ''
        for char in file_name[::-1]:
            if char == '.': break
            else: end_str += char
        return end_str[::-1]



