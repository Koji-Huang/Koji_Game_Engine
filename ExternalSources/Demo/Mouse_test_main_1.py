import pygame
from Graphic.UI.Button import Button
from Graphic.UI.Text import Text
from Graphic.MainWindows import MainWindows

Main = MainWindows((900, 400))

count = 0


def say_hello(*args, **kwargs):
    print("Hello World!")


G = Button((100, 100), (200, 200))
G.graph_primer_surface.fill((255, 255, 255))
Main.tree_add_son(G)

G.bind_press_function(say_hello, pygame.MOUSEBUTTONDOWN)

Clock = pygame.time.Clock()

text = Text((300, 300), (300, 300), "Hello World!",
            pygame.font.SysFont(pygame.font.get_fonts()[0], 36), False, (255, 100, 100))

Main.tree_add_son(text)

while True:
    Main.update()

