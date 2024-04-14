import pygame
from GraphicComponent.UI import Label, Button
from GraphicComponent.UI.Text import Text
from GraphicComponent.MainWindows import MainWindows
from Manager.EventManager import EventManager
from Event.UIEvent.Mouse.Scroll import Scroll
from Event.UIEvent.Mouse.Press import Press
from Event.UIEvent.Mouse.Click import Click
from Event.UIEvent.Mouse.Drag import Drag
Main = MainWindows((900, 400))

count = 0



def say_hello(*args, **kwargs):
    print(kwargs)


def _drag(start_pos, end_pos, relative_pos, *args, **kwargs):
    print(f"start_pos: {start_pos}\nend_pos: {end_pos}\nrelative_pos: {relative_pos}")


G = Label((100, 100), (300, 300))
G.graph_primer_surface.fill((255, 255, 255))
Main.tree_add_son(G)

D = Label((100, 100), (200, 150))
D.graph_primer_surface.fill((255, 0, 0))
G.tree_add_son(D)

# Drag Test
# DragEvent = Drag(D, 0)
# DragEvent.track_function = _drag
#
# D.event_add('001001002', DragEvent)

PressEvent = Click(D, 0)
PressEvent.track_function = say_hello
D.event_add('001001001', PressEvent)


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

