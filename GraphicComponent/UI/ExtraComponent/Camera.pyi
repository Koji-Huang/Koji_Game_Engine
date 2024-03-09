from GraphicComponent.UI import Label


class Camera(Label):
    son: list[Label, ...]
    scaleRatio: float
    allScaleRatio: float

    def __init__(self, pos, size, *args, **kwargs):
        """

        :param pos:
        :param size:
        :param args:
        :param kwargs:
        """

    def scale_son(self, son: Label, ratio: float, pos: tuple):
        """

        :param son:
        :param ratio:
        :param pos:
        :return:
        """
