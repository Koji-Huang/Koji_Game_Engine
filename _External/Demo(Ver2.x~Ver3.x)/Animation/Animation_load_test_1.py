from API import GraphicAPI_type
from API import EventAPI_type
from Asset.Graphic import Package as AnimationAsset
from DataType.ConfigFile import Animation as AnimationConfig

GlobalAPI.register_global_environment()
GraphicManager = GraphicAPI_type()
EventManager = EventAPI_type()
EventManager.load_default_event()


txt_config = AnimationConfig(
    r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\External\AnimationDemoPicture\config.txt")
ini_config = AnimationConfig(
    r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\External\AnimationDemoPicture\config.ini")
json_config = AnimationConfig(
    r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\External\AnimationDemoPicture\config.json")


txt = AnimationAsset(txt_config)
ini = AnimationAsset(ini_config)
json = AnimationAsset(json_config)

pass
