import sys
import pygame.time
from math import sin, cos, log

sys.path.append(r'..\..\..\Koji_Game_Engine')

from API import GlobalAPI
from API import GraphicAPI_type
from API import EventAPI_type
from Event.UIEvent.Mouse.Click import Click
from Graphic.UI import *

GlobalAPI.register_global_environment()
GraphicManager = GraphicAPI_type()
EventManager = EventAPI_type()
EventManager.load_default_event()


def say_hello(*args, **kwargs):
    print('hello~')


Label_collection: list[Label] = []
Color = ((255, 0, 0), (0, 255, 0), (0, 0, 255))

EventManager.graphic_register(GraphicManager.windows)

for i in range(50):
    Label_collection.append(Label((100, 100), (100, 100)))
    Label_collection[-1].set_color(Color[i % 3])
    GraphicManager.component_add(Label_collection[-1])
    Event = Click(Label_collection[-1], 0)
    Event.track_function = say_hello
    Label_collection[-1].event_add('001001001', Event)

predict_x = lambda k, i: int(int(sin(log(k, 3) * i / 300) * log(k, 5) * 20) + log(k, 8) * 50 * log(k))
predict_y = lambda k, i: int(int(cos(log(k, 4) * i / 300) * log(k, 6) * 20) + log(k, 7) * 50 * log(k))


def insert_function(self, *args, **kwargs):
    print(self.id)


GraphicManager.set_debug(True)
GraphicManager.debug.textType.color = (0, 255, 230)
GraphicManager.debug.one_layer = True
GraphicManager.debug.info_alpha = 200

times = pygame.time.Clock()

for i in range(1, 1000000):
    times.tick_busy_loop()
    if i % 100 == 0:
        print(times.get_fps())
    for index, value in enumerate(Label_collection):
        Label_collection[index].set_pos((predict_x(1.0 * index / Label_collection.__len__() * 45 + 10, i),
                                         predict_y(1.0 * index / Label_collection.__len__() * 45 + 10, i)))
    GraphicManager.graphic_update()
    EventManager.update()
