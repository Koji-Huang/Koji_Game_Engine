import pygame


def make_custom_event(name: any, value: any):
    ...


'''
    Engine BasicEvent Add args:
        xxx-xx-xxxx
        Engine_Version - BasicEvent Type - BasicEvent
        
        Sample:
            engine_version: 2.03 -> 2.03
            mouse_event: 1 -> 01
            keep_event: 0001
            MouseKeepEvent:  203010001
'''


class EventConstant:
    MouseClickEvent: int = pygame.MOUSEBUTTONDOWN
    MouseMoveEvent: int = pygame.MOUSEMOTION
    MouseWheelEvent: int = pygame.MOUSEWHEEL
