import os.path

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pygame

from Graphic.UI import Label, Button
from Graphic.UI.Text import Text
from Graphic.Basic.MainWindows import MainWindows

from API import EventAPI_type
from API.Global import register_global_environment
register_global_environment()

Main = MainWindows((900, 400))


def say_hello(*args, **kwargs):
    print("Hello World!")


G = Label((100, 100), (300, 300))
G.graph_primer_surface.fill((255, 255, 255))
Main.tree_add_son(G)

D = Button((100, 100), (200, 150))
D.graph_primer_surface.fill((255, 0, 0))
G.tree_add_son(D)


D.bind_press_function(say_hello, 0)

Clock = pygame.time.Clock()

text = Text((300, 300), (300, 300), "Hello World!",
            pygame.font.SysFont(pygame.font.get_fonts()[0], 36), False, (255, 100, 100))

Main.tree_add_son(text)

manager = EventAPI_type()
manager.load_default_event()
manager.graphic_register(Main)


while True:
    Main.update()
    manager.update()
