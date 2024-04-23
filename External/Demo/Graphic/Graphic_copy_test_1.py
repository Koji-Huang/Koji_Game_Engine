import pygame.font
import math
from Graphic.UI import *
from Graphic.Basel import MainWindows

from API.GlobalAPI import register_global_environment
register_global_environment()

Main = MainWindows((1200, 500), pygame.NOFRAME)


A = Label((100, 100), (120, 50))

A.set_color((255, 0, 0, 100))

B = A.__copy__()

Main.tree_add_son(A)
Main.tree_add_son(B)

for i in range(1000000):
    Main.update()
    A.graph_active = True
    B.graph_active = True

    A.set_color((255, i % 255, 0, 100))
    A.x = math.sin(i / 100) * 500 + 500

