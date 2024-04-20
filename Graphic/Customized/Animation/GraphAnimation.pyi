from Graphic.Customized.Animation.Basel import Animation as Basel
from DataType.Generic.LinkedList import LinkedList


class Animation(Basel):
    _animation_frame: LinkedList[Basel]
    def __init__(self, pos, size, *args, **kwargs):
        pass

    def draw_frame(self, frame):
        pass

    def __copy__(self, copied: any = None):
        pass