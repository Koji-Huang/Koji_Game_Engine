from API import GlobalAPI
from API import GraphicAPI_type
from API import EventAPI_type
from DataType.Asset.Graphic.Animation import Package

GlobalAPI.register_global_environment()
GraphicManager = GraphicAPI_type()
EventManager = EventAPI_type()
EventManager.load_default_event()


TXT = Package(
    "../../Graphic/EffectFunction\\TextureMapping\\Noise\\_texture_\\gradient(quadratic)(1980x1980)\\Basel.txt")
INI = Package(
    "../../Graphic/EffectFunction\\TextureMapping\\Noise\\_texture_\\gradient(quadratic)(1980x1980)\\Basel.ini")
JSON = Package(
    "../../Graphic/EffectFunction\\TextureMapping\\Noise\\_texture_\\gradient(quadratic)(1980x1980)\\Basel.json")


pass
