import pygame.font

from Graphic.UI import *
from Graphic.Basel import MainWindows
from API import EventAPI_type


from API.GlobalAPI import register_global_environment
register_global_environment()


Main = MainWindows((1024, 600))
pygame.font.init()
Button = Button((100, 100), (300, 300))

Manager = EventAPI_type()
Manager.load_default_event()
Manager.graphic_register(Main)

def func(*args, **kwargs):
    print("Hello World!")


Button.set_color((200, 200, 200, 100))
Main.tree_add_son(Button)

Button.bind_press_function(func, 0)

Scale = Button.__copy__()
Scale.set_pos((200, 200))

Main.tree_add_son(Scale)




while True:
    Main.update()
    Manager.update()
