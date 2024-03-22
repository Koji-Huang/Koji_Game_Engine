import pygame

from GraphicComponent import MainWindows
from GraphicComponent.UI import Label, Button
from GraphicComponent.UI.ExtraComponent import Camera


Main = MainWindows((800, 600))


Camera_1 = Camera((0, 100), (800, 500))


def be_big(*args, **kwargs):
    Camera_1.scale(Camera_1.scaleRatio + 0.1)


Big = Button((0, 0), (800, 100))
Big.bind_press_function(be_big, pygame.MOUSEBUTTONUP)


Main.tree_add_son(Big)
Main.tree_add_son(Camera_1)

L1 = Label((0, 0), (100, 100))
L1.set_color((255, 0, 0))

L2 = Label((150, 150), (100, 100))
L2.set_color((0, 255, 0))

L3 = Label((300, 300), (100, 100))
L3.set_color((0, 0, 255))

Camera_1.tree_add_son(L1)
Camera_1.tree_add_son(L2)
Camera_1.tree_add_son(L3)


while True:
    Camera_1.graph_active = True
    Main.update()

