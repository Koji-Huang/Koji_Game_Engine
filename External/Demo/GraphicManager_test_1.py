from math import sin, cos, log

import pygame.time
import GlobalConstant
import Manager.GraphicManager as GraphicManager
import Manager.EventManager as EventManager
from Event.UIEvent.Mouse.Click import Click
from Graphic.UI import *


GlobalConstant.register_global_environment_id()


def say_hello(*args, **kwargs):
    print('hello~')


Manager = GraphicManager.GraphicComponentManager()
EventManager = EventManager.EventManager()

Label_collection: list[Label] = []
Color = ((255, 0, 0), (0, 255, 0), (0, 0, 255))


EventManager.load_default_event()
EventManager.graphic_register(Manager.windows)


for i in range(50):
    Label_collection.append(Label((100, 100), (100, 100)))
    # Label_collection[-1].set_color(Color[i % 3])
    Manager.component_add(Label_collection[-1])
    Event = Click(Label_collection[-1], 0)
    Event.track_function = say_hello
    Label_collection[-1].event_add('001001001', Event)


predict_x = lambda k, i: int(int(sin(log(k, 3) * i / 300) * log(k, 5) * 20) + log(k, 8) * 50 * log(k))
predict_y = lambda k, i: int(int(cos(log(k, 4) * i / 300) * log(k, 6) * 20) + log(k, 7) * 50 * log(k))


def insert_function(self, *args, **kwargs):
    print(self.id)


Manager.set_debug(True)
Manager.debug.textType.color = (0, 255, 230)
Manager.debug.info_alpha = 255
Manager.debug.one_layer = True
Manager.debug.info_alpha = 200

times = pygame.time.Clock()

for i in range(1, 1000000):
    times.tick_busy_loop()
    if i % 100 == 0:
        print(times.get_fps())
    for index, value in enumerate(Label_collection):
        Label_collection[index].set_pos((predict_x(1.0 * index / Label_collection.__len__() * 45 + 10, i),
                                         predict_y(1.0 * index / Label_collection.__len__() * 45 + 10, i)))
    Manager.graphic_update()
    EventManager.update()
