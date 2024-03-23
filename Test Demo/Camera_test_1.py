import pygame

from GraphicComponent import MainWindows
from GraphicComponent.UI import Label, Button, Image
from GraphicComponent.UI.ExtraComponent import Camera


Main = MainWindows((800, 600))


Camera_1 = Camera((0, 100), (800, 500))


def be_big(*args, **kwargs):
    Camera_1.scale(Camera_1.camera_ratio + 0.1)

def move(*args, **kwargs):
    Camera_1.move((10, 10))


Big = Button((0, 0), (400, 100))
Big.set_color((100, 100, 100))
Big.bind_press_function(be_big, pygame.MOUSEBUTTONUP)

Move = Button((400, 0), (400, 100))
Move.set_color((100, 100, 100))
Move.bind_press_function(move, pygame.MOUSEBUTTONUP)


Main.tree_add_son(Big)
Main.tree_add_son(Move)
Main.tree_add_son(Camera_1)

image = Image((0, 0), (800, 600), r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\TestInfo\__klee_nahida_qiqi_diona_sayu_and_2_more_genshin_impact_drawn_by_neko_sake1__44cf20a2d68da284b66568fdf5a6972d.png")

Camera_1.tree_add_son(image)


while True:
    Camera_1.graph_active = True
    Main.update()

