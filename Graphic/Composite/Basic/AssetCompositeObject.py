from typing import overload
from DataType.Asset.AbstractAsset import Asset as AssetObject
from .BasicCompositeObject import CompositeObject
import API.Asset as AssetAPI


class AssetCompositeObject(CompositeObject):
    AssetAPI = AssetAPI

    def asset_bind(self, asset: AssetObject):
        pass

    def asset_unbind(self, asset: AssetObject):
        pass
