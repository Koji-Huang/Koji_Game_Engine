import pygame

from GraphicComponent import MainWindows
from GraphicComponent.UI import Image, Label
from GraphicComponent.UI.ExtraComponent import Camera

Main = MainWindows((800, 600))

image = Image((0, 0), (400, 600),
              r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\TestInfo\__klee_nahida_qiqi_diona_sayu_and_2_more_genshin_impact_drawn_by_neko_sake1__44cf20a2d68da284b66568fdf5a6972d.png")

Camera_1 = Camera((500, 200), (200, 300), image)


Direct = Label((0, 0), Camera_1.size())
Direct.set_color((255, 255,255,125))
Direct.graph_active = True

image.tree_add_son(Direct)

Main.tree_add_son(Camera_1)
Main.tree_add_son(image)


def scrolling_event(event, *args, **kwargs):
    if pygame.key.get_pressed()[pygame.K_LCTRL]:

        Camera_1.camera_scale(Camera_1.camera_ratio * (1 + event.precise_y * 0.1))
    else:
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            Camera_1.camera_move((event.precise_y * 10, event.precise_x * 10))
        else:
            Camera_1.camera_move((event.precise_x * 10, event.precise_y * 10))

    primer_surface_size = [i / Camera_1.camera_ratio for i in Camera_1.size()]
    primer_surface_pos = list(Camera_1.camera_pos[i] - primer_surface_size[i] / 2 for i in [0, 1])

    Direct.set_pos(primer_surface_pos)
    Direct.set_size(primer_surface_size)


while True:
    Camera_1.graph_active = True
    Main.update()
