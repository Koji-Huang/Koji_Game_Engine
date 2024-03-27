import pygame
from GraphicComponent.UI import Image, Label
from GraphicComponent.UI.ExtraComponent import Camera
from GraphicComponent.Event.MouseEvent import Scrolling
from GraphicComponent.Event.Event import Event
from GraphicComponentManager import GraphicComponentManager as Manager

Root = Manager()
Root.set_debug(True)
Root.debug.textType.color = (255, 0, 0, 255)

image = Image((0, 0), (400, 600),
              r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\TestInfo\__klee_nahida_qiqi_diona_sayu_and_2_more_genshin_impact_drawn_by_neko_sake1__44cf20a2d68da284b66568fdf5a6972d.png")

Camera_1 = Camera((450, 50), (300, 500), image)


Direct = Label((0, 0), Camera_1.size())
Direct.set_color((255, 255,255,125))
Direct.graph_active = True

image.tree_add_son(Direct)

Root.add_component(Camera_1)
Root.add_component(Direct)


def scrolling_event(event, *args, **kwargs):
    if pygame.key.get_pressed()[pygame.K_LCTRL]:

        Camera_1.scale(Camera_1.camera_ratio * (1 + event.precise_y * 0.1))
    else:
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            Camera_1.move((event.precise_y * 10, event.precise_x * 10))
        else:
            Camera_1.move((event.precise_x * 10, event.precise_y * 10))

    primer_surface_size = [i / Camera_1.camera_ratio for i in Camera_1.size()]
    primer_surface_pos = list(Camera_1.camera_pos[i] - primer_surface_size[i] / 2 for i in [0, 1])

    Direct.set_pos(primer_surface_pos)
    Direct.set_size(primer_surface_size)


def follow_mouse(event, *args, **kwargs):
    object = kwargs['graphic_object']
    rel_pos = object.real_pos()
    pos = list([int(event.pos[i]) for i in [0, 1]])
    object: Label
    center_pos = list([pos[i] - object.size()[i] / 2 for i in [0, 1]])
    object.set_pos(center_pos)
    Camera_1.move_to(pos)
    Camera_1.graph_active = True
    image.graph_active = True
    # # Very Strange Graphic
    # scale = pygame.transform.scale(Camera_1.graph_surface, Direct.size())
    # scale.set_alpha(255)
    # Direct.graph_surface.blit(scale, (0, 0))


scrolling_event = Scrolling(scrolling_event, Camera_1)
follow_event = Event(Camera_1)
follow_event.track_function = follow_mouse

Camera_1.event_add(pygame.MOUSEWHEEL, scrolling_event)
Direct.event_add(pygame.MOUSEMOTION, follow_event)

while True:
    Camera_1.graph_active = True
    Root.graphic_update()
    Root.event_update()
