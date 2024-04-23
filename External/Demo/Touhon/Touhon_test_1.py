import math

import pygame.event
import pygame.time
from API import GlobalAPI, GraphicAPI_type, ThreadAPI_type, EventAPI_type
from Graphic.UI.Image import Image
import API


GlobalAPI.register_global_environment()
API.GraphicAPI = GraphicAPI_type()
API.EventAPI = EventAPI_type()
API.ThreadAPI = ThreadAPI_type()
API.EventAPI.load_default_event()


Barrage = Image((0, 0), (12, 12), r"C:\Users\Administrator\Pictures\Pixel Studio\Untitled 04-18-2024 03-03-55.png")
Barrage.graph_active = True
Barrage_num = 2000


Barrage_collection = list()
for i in range(Barrage_num):
    copied = Barrage.__copy__()
    copied.k = i
    Barrage_collection.append(copied)
    API.GraphicAPI.windows.tree_add_son(copied)
    Barrage.graph_update()


Clock = pygame.time.Clock()
# API.GraphicAPI.set_debug(True)


while True:
    Clock.tick_busy_loop(1000)
    print(Clock.get_fps())
    for index, value in enumerate(Barrage_collection):
        place = 3.14159 * 2 * (index / Barrage_num + 1)
        value.set_pos((int(math.sin(place * value.k / 100) * 400 * index / Barrage_num + 400), int(math.cos(place * value.k * index / Barrage_num / 100) * 300 + 300)))
        value.graph_active = True
        value.k += 0.01 * 3.1415
    API.GraphicAPI.graphic_update()
    API.EventAPI.update()
    pygame.event.get()