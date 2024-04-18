from API import GlobalAPI
from API import GraphicAPI_type
from API import EventAPI_type
from Asset.StandardDataType.Graphic.Animation import Package

GlobalAPI.register_global_environment()
GraphicManager = GraphicAPI_type()
EventManager = EventAPI_type()
EventManager.load_default_event()


TXT = Package("..\\..\\Graphic\\Effect\\TextureMapping\\Noise\\_texture_\\gradient(quadratic)(1980x1980)\\config.txt")
INI = Package("..\\..\\Graphic\\Effect\\TextureMapping\\Noise\\_texture_\\gradient(quadratic)(1980x1980)\\config.ini")
JSON = Package("..\\..\\Graphic\\Effect\\TextureMapping\\Noise\\_texture_\\gradient(quadratic)(1980x1980)\\config.json")


pass
