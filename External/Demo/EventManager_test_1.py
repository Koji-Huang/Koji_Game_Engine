import pygame
from GraphicComponent.UI import Label, Button
from GraphicComponent.UI.Text import Text
from GraphicComponent.MainWindows import MainWindows
from Manager.EventManager import EventManager

Main = MainWindows((900, 400))

count = 0


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

manager = EventManager()
manager.load_default_event()
manager.graphic_register(Main)

while True:
    Main.update()
    manager.update()

