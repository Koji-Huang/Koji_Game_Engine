import pygame.font

from Graphic.UI import *
from Graphic import *

Main = MainWindows((1024, 600))
pygame.font.init()
Button = Button((100, 100), (300, 300))


def func(*args, **kwargs):
    print("Hello World!")


Button.set_color((200, 200, 200, 100))
Main.tree_add_son(Button)

Button.bind_press_function(func, pygame.MOUSEBUTTONDOWN)

Scale = Button.__copy__()
Scale.camera_scale(400, 400, True)
Scale.set_pos((200, 200))

Main.tree_add_son(Scale)



while True:
    Main.update()

