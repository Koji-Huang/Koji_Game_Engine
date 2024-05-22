
import Management as AssetManagement


try:
    AssetManagement.load_system_asset_type()
except any as err:
    raise "Unable to load SystemAssetType from SystemConfigFile\n" + err
