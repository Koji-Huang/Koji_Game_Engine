import pygame

from GraphicComponent import MainWindows
from GraphicComponent.UI import Image, Label
from GraphicComponent.UI.ExtraComponent import Camera
from GraphicComponent.Event.MouseEvent import Scrolling

Main = MainWindows((800, 600))

image = Image((0, 0), (400, 600),
              r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\TestInfo\__klee_nahida_qiqi_diona_sayu_and_2_more_genshin_impact_drawn_by_neko_sake1__44cf20a2d68da284b66568fdf5a6972d.png")

Camera_1 = Camera((400, 0), (400, 600), image)


Direct = Label((0, 0), Camera_1.size())
Direct.set_color((255, 255,255,125))
Direct.graph_active = True

image.tree_add_son(Direct)

Main.tree_add_son(Camera_1)
Main.tree_add_son(image)


def scrolling_event(event, *args, **kwargs):
    if pygame.key.get_pressed()[pygame.K_LCTRL]:
        Camera_1.scale(Camera_1.camera_ratio * (1 + event.precise_y * 0.1))
    else:
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            Camera_1.move((event.precise_y * 10, event.precise_x * 10))
        else:
            Camera_1.move((event.precise_x * 10, event.precise_y * 10))
    pos = [Camera_1.camera_pos[i] - Camera_1.size()[i] / 2 for i in [0, 1]]
    size = [Camera_1.size()[i] * Camera_1.camera_ratio for i in [0, 1]]
    Direct.set_pos(pos)
    Direct.set_size(size)


scrolling_event = Scrolling(scrolling_event, Camera_1)

Camera_1.event_add(pygame.MOUSEWHEEL, scrolling_event)

while True:
    Camera_1.graph_active = True
    Main.update()
