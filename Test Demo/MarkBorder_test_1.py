import pygame.font
import math
from GraphicComponent.UI import *
from GraphicComponent import MainWindows
from GraphicComponent.Effect.MarkBorder import mark_component, EdgeType, TextType


Main = MainWindows((1200, 500), pygame.NOFRAME)


A = Label((100, 100), (120, 50))

A.set_color((255, 0, 0, 100))


MarkSurface = Label((0, 0),  (1200, 500))

Main.tree_add_son(A)
Main.tree_add_son(MarkSurface)
# A.graph_active = False

edge = EdgeType()
text = TextType(14, "Hello World")



for i in range(1000000):
    MarkSurface.graph_primer_surface.fill((0, 0, 0))
    mark_component(MarkSurface, edge, text, A.rect())

    Main.update()
    MarkSurface.graph_active = True
    A.graph_active = True

    A.set_color((255, i % 255, 0, 100))
    A.x = math.sin(i / 100) * 500 + 500

