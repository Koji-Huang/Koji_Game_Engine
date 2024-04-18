import Graphic.Effect.TextureMapping.Noise.perlin as perlin
import pygame.event
import pygame.time
from API import GlobalAPI, GraphicAPI_type, ThreadAPI_type, EventAPI_type
from Graphic.UI.Label import Label
import API


GlobalAPI.register_global_environment()
API.GraphicAPI = GraphicAPI_type()
API.EventAPI = EventAPI_type()
API.ThreadAPI = ThreadAPI_type()
API.EventAPI.load_default_event()


D = Label((0, 0), (100, 200))
E = Label((100, 0), (100, 200))
API.GraphicAPI.component_add(D)
API.GraphicAPI.component_add(E)


Clock = pygame.time.Clock()
# API.GraphicAPI.set_debug(True)


while True:
    perlin.noise(D.graph_primer_surface)
    perlin.noise(E.graph_primer_surface, enable=False)
    D.graph_active = True
    E.graph_active = True
    Clock.tick_busy_loop(1000)
    print(Clock.get_fps())
    API.GraphicAPI.graphic_update()
    API.EventAPI.update()
    pygame.event.get()