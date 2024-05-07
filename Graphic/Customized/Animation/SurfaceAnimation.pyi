import pygame
from Graphic.Customized.Animation.AbstractAnimation import Animation as Basel
from DataType.Generic.LinkedList import LinkedList

class Animation(Basel):
    animation_frame: LinkedList[int, [pygame.Surface]]
    def __init__(self, pos, size, *args, **kwargs):
        pass

    def draw_frame(self, frame):
        pass

    def __copy__(self, copied: any = None):
        pass