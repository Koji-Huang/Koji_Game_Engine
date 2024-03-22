from math import sin

import pygame.time

import GraphicComponentManager
from GraphicComponent.UI import *

Manager = GraphicComponentManager.GraphicComponentManager()

Manager.set_debug(True)
Manager.debug.textType.color = (0, 255, 230)
Manager.debug.info_alpha = 255

Label_1 = Label((100, 100), (100, 100))
Label_1.set_color((255, 0, 0))
Label_2 = Label((250, 100), (100, 100))
Label_2.set_color((0, 255, 0))
Label_3 = Label((400, 100), (100, 100))
Label_3.set_color((0, 0, 255))

Manager.add_component(Label_1)
Manager.add_component(Label_3)
Manager.add_component(Label_2)


def insert_function(self, *args, **kwargs):
    print(self.ID)


Manager.debug.one_layer = True
Manager.debug.info_alpha = 200
times = pygame.time.Clock()

for i in range(1, 1000000):
    times.tick_busy_loop()
    if i % 100 == 0:
        print(times.get_fps())
    Label_1.set_pos(((int(sin(i / 300) * 100) + 100), int(sin(i / 800) * 100) + 100))
    Label_2.set_pos(((int(sin(i / 700) * 100) + 100), int(sin(i / 900) * 100) + 100))
    Label_3.set_pos(((int(sin(i / 500) * 100) + 100), int(sin(i / 400) * 100) + 100))
    Manager.graphic_update()
    Manager.event_update()
