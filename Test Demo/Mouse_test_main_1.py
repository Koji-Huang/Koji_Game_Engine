import pygame
from GraphicComponent.UI.Button import Button
from GraphicComponent.MainWindows import MainWindows

Main = MainWindows((900, 400))


def say_hello(*args, **kwargs):
    print("Hello World!")


G = Button((100, 100), (200, 200))
G.graph_primer_surface.fill((255, 255, 255))
Main.tree_add_son(G)

B = Button((400, 100), (200, 200))
B.graph_primer_surface.fill((255, 255, 255))
Main.tree_add_son(B)

C = Button((400, 350), (200, 50))
C.graph_primer_surface.fill((255, 255, 255))
Main.tree_add_son(C)

G.bind_press_function(say_hello, pygame.MOUSEBUTTONDOWN)
B.bind_press_function(say_hello, pygame.MOUSEBUTTONDOWN)
C.bind_press_function(say_hello, pygame.MOUSEBUTTONDOWN)

Clock = pygame.time.Clock()

while True:
    Main.update()
