from math import sin

import pygame.font

from GraphicComponent.Effect.MarkBorder import EdgeType, TextType, mark_component
from GraphicComponent.UI import *
from GraphicComponent import MainWindows

Main = MainWindows((1200, 500), pygame.NOFRAME)

image = Image((0, 0), (1200, 600), r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\TestInfo\__klee_nahida_qiqi_diona_sayu_and_2_more_genshin_impact_drawn_by_neko_sake1__44cf20a2d68da284b66568fdf5a6972d.png")
# image = Label((0, 0), (1200, 300))
A = Label((100, 100), (120, 50))
B = Label((200, 100), (120, 50))
C = Label((300, 100), (100, 50))
D = Label((100, 75), (300, 50))
E = Label((30, 10), (100, 50))
F = Label((60, 20), (100, 50))

A1 = Label((100, 100), (120, 50))
B1 = Label((200, 100), (120, 50))
C1 = Label((300, 100), (100, 50))
D1 = Label((100, 75), (300, 50))
E1 = Label((30, 10), (100, 50))
F1 = Label((60, 20), (100, 50))

A2 = Label((100, 100), (120, 50))
B2 = Label((200, 100), (120, 50))
C2 = Label((300, 100), (100, 50))
D2 = Label((100, 75), (300, 50))
E2 = Label((30, 10), (100, 50))
F2 = Label((60, 20), (100, 50))

A3 = Label((100, 100), (120, 50))
B3 = Label((200, 100), (120, 50))
C3 = Label((300, 100), (100, 50))
D3 = Label((100, 75), (300, 50))
E3 = Label((30, 10), (100, 50))
F3 = Label((60, 20), (100, 50))

A4 = Label((100, 100), (120, 50))
B4 = Label((200, 100), (120, 50))
C4 = Label((300, 100), (100, 50))
D4 = Label((100, 75), (300, 50))
E4 = Label((30, 10), (100, 50))
F4 = Label((60, 20), (100, 50))

A5 = Label((100, 100), (120, 50))
B5 = Label((200, 100), (120, 50))
C5 = Label((300, 100), (100, 50))
D5 = Label((100, 75), (300, 50))
E5 = Label((30, 10), (100, 50))
F5 = Label((60, 20), (100, 50))

text = Text((300, 300), (300, 300), "Hello World!",
            pygame.font.SysFont(pygame.font.get_fonts()[0], 36), False, (255, 100, 100))

A1.x += 130
B1.x += 130
C1.x += 130
D1.x += 130
E1.x += 130
F1.x += 130

A2.x += 350
B2.x += 350
C2.x += 350
D2.x += 350
E2.x += 350
F2.x += 350

A3.x += 500
B3.x += 500
C3.x += 500
D3.x += 500
E3.x += 500
F3.x += 500

A4.x += 800
B4.x += 800
C4.x += 800
D4.x += 800
E4.x += 800
F4.x += 800

A.set_color((255, 0, 0, 100))
B.set_color((0, 255, 0, 100))
C.set_color((0, 0, 255, 100))
D.set_color((255, 255, 255, 100))
E.set_color((0, 0, 255, 100))
F.set_color((0, 0, 255, 100))

A1.set_color((255, 0, 0, 100))
B1.set_color((0, 255, 0, 100))
C1.set_color((0, 0, 255, 100))
D1.set_color((255, 255, 255, 100))
E1.set_color((0, 0, 255, 100))
F1.set_color((0, 0, 255, 100))

A2.set_color((255, 0, 0, 100))
B2.set_color((0, 255, 0, 100))
C2.set_color((0, 0, 255, 100))
D2.set_color((255, 255, 255, 100))
E2.set_color((0, 0, 255, 100))
F2.set_color((0, 0, 255, 100))

A3.set_color((255, 0, 0, 100))
B3.set_color((0, 255, 0, 100))
C3.set_color((0, 0, 255, 100))
D3.set_color((255, 255, 255, 100))
E3.set_color((0, 0, 255, 100))
F3.set_color((0, 0, 255, 100))

A4.set_color((255, 0, 0, 100))
B4.set_color((0, 255, 0, 100))
C4.set_color((0, 0, 255, 100))
D4.set_color((255, 255, 255, 100))
E4.set_color((0, 0, 255, 100))
F4.set_color((0, 0, 255, 100))

Main.tree_add_son(image)
Main.tree_add_son(A)
image.tree_add_son(B)
image.tree_add_son(C)
image.tree_add_son(D)
image.tree_add_son(E)
image.tree_add_son(F)
image.tree_add_son(A1)
image.tree_add_son(B1)
image.tree_add_son(C1)
image.tree_add_son(D1)
image.tree_add_son(E1)
image.tree_add_son(F1)
image.tree_add_son(A2)
image.tree_add_son(B2)
image.tree_add_son(C2)
image.tree_add_son(D2)
image.tree_add_son(E2)
image.tree_add_son(F2)
image.tree_add_son(A3)
image.tree_add_son(B3)
image.tree_add_son(C3)
image.tree_add_son(D3)
image.tree_add_son(E3)
image.tree_add_son(F3)
image.tree_add_son(A4)
image.tree_add_son(B4)
image.tree_add_son(C4)
image.tree_add_son(D4)
image.tree_add_son(E4)
image.tree_add_son(F4)
Main.tree_add_son(text)

Clock = pygame.time.Clock()


edge = EdgeType(1, color=(255, 0, 0,  86))
textType = TextType(14, "Hello World")

MarkSurface = Label((0, 0),  (1200, 500))
MarkSurface.graph_surface.set_colorkey((0, 0, 0))
Main.tree_add_son(MarkSurface)

for i in range(1000000):
    A1.graph_active = True

    A1.y += int(sin(i / 40) * 5)
    B2.y += int(sin(i / 40) * 5)
    C3.y += int(sin(i / 40) * 5)
    D1.y += int(sin(i / 40) * 5)
    E4.y += int(sin(i / 40) * 5)
    F3.y += int(sin(i / 40) * 5)
    Clock.tick_busy_loop(1000)
    Main.update()
    if not (i % 60):
        text.change_text(str(Clock.get_fps()))
    A.x += 1
    if pygame.time.get_ticks() > 12000:
        quit()

    MarkSurface.graph_primer_surface.fill((0, 0, 0, 255))
    MarkSurface.graph_active = True

    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        for k in ['1', '2', '3', '4']:
            exec('textType.change_text(\'%s%s\')' % (i,  k))
            exec("mark_component(MarkSurface, edge, textType, %s%s.rect())" % (i,  k))

