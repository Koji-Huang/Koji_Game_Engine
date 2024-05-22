
import Management as AssetManagement
from .AssetRegister import AssetManager as AssetManagerType

RegisteredAssetType = dict()
AssetRegistry = AssetManagerType()


try:
    AssetManagement.load_system_asset_type()
except any as err:
    raise "Unable to load SystemAssetType from SystemConfigFile\n" + err
