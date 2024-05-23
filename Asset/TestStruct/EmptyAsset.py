from ..AbstractAsset import Asset as AssetObject
from Config.Basel.JsonConfig import Json

test_config = Json("config.json")


class AssetType(AssetObject):

    def __init__(self, config: any = None, *args, **kwargs):
        super().__init__(config, *args, **kwargs)
        self.type = 'EMPTYASSET'

    def __call__(self, *args, **kwargs):
        print("I HAD CALLLLLLLLLLLLLLLED!!!!!")

    def convert(self):
        print("I HAD CONVVVVVVVVVVVVVVERTED!!!!!")
        return None

    def __getattr__(self, item):
        return self.configObject.__getattribute__(item)

    def is_active(self):
        return self.saved_animation is not None
