import Asset
from Asset.TestStruct.EmptyAsset import AssetType, test_config

Asset.load_system_asset_type()

G = AssetType(test_config)


G
