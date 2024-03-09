import pygame.font

from GraphicComponent.UI import *
from GraphicComponent import *

Main = MainWindows((1024, 600))
pygame.font.init()
Button = Button((100, 100), (300, 300))


def func(*args, **kwargs):
    print("Hello World!")


Button.set_color((200, 200, 200, 100))
Main.tree_add_son(Button)

Button.bind_press_function(func, pygame.MOUSEBUTTONDOWN)

Scale = Button.__copy__()
Scale.graph_scale_self(400, 400, True)
Scale.set_pos((200, 200))

Main.tree_add_son(Scale)

Main.event_tree_build()


while True:
    Main.update()

