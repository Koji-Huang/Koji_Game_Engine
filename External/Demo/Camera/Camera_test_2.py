import pygame
from Graphic.UI import Image, Label
from Graphic.UI.ExtraComponent import Camera
from Event.UIEvent.Mouse.MouseScrollEvent import Scroll
from Event.UIEvent.UIEvent import Basic
from Graphic.Basic import MainWindows
from API import Global
from API import GraphicAPI_type
from API import EventAPI_type


GlobalAPI.register_global_environment()
EventManager = EventAPI_type()
EventManager.load_default_event()
Main = MainWindows((800, 600))
Root = GraphicAPI_type(Main)

Root.set_debug(True)
Root.debug.textType.color = (255, 0, 0, 255)

image = Image((0, 0), (400, 600),
              r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\External\picture_1.png")

Camera_1 = Camera((450, 50), (300, 500), image)


Direct = Label((0, 0), Camera_1.size())
Direct.set_color((255, 255,255,125))
Direct.graph_active = True

image.tree_add_son(Direct)

Root.component_add(Camera_1)
Root.component_add(Direct)


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


def follow_mouse(event, *args, **kwargs):
    object = kwargs['graphic_object']
    rel_pos = object.real_pos()
    pos = list([int(event.graphic_object[i]) for i in [0, 1]])
    object: Label
    center_pos = list([pos[i] - object.size()[i] / 2 for i in [0, 1]])
    object.set_pos(center_pos)
    Camera_1.camera_move_to(pos)
    Camera_1.graph_active = True
    image.graph_active = True
    # # Very Strange Graphic
    # scale = pygame.transform.scale(Camera_1.graph_surface, Direct.size())
    # scale.set_alpha(255)
    # Direct.graph_surface.blit(scale, (0, 0))


scrolling_event = Scroll(scrolling_event, Camera_1)
follow_event = Basic(Camera_1)
follow_event.track_function = follow_mouse

Camera_1.event_add(pygame.MOUSEWHEEL, scrolling_event)
Direct.event_add(pygame.MOUSEMOTION, follow_event)

while True:
    Camera_1.graph_active = True
    Root.graphic_update()
    Root.event_update()
