from GraphicComponent.UI.Label import Label


class BesselCurve(Label):
    # the width of line
    line_size: int
    # the color of line
    line_color: tuple[int, int, int, int]
    # the start line ( x, y )
    line_start_line: tuple[tuple[int, ...], ...]
    # the end line ( x, y )
    line_end_line: tuple[tuple[int, ...], ...]
    # how much times draw once
    line_drawing_accuracy: int

    def __init__(self, pos, size, *args, **kwargs):
        """

        :param pos:
        :param size:
        :param args:
        :param kwargs:
        """

    def set_point(self, start_line: tuple[tuple[int, ...], ...], end_line: tuple[tuple[int, ...], ...]):
        """
        Set BesselCurve Marking Point
        :param start_line: Start Line
        :param end_line: End Line
        :return:
        """

    def set_line_size(self, size: int):
        """

        :param size:
        :return:
        """

    def set_line_color(self, color: tuple[int, int, int, int]):
        """

        :param color:
        :return:
        """

    def draw_line(self, show_control_points: bool = True, show_points: bool = False):
        """

        :param show_points:
        :param show_control_points:
        :param self:
        :return:
        """

    def make_line(self, start_line=None, end_line=None, accuracy=None):
        """

        :param start_line:
        :param end_line:
        :param accuracy:
        :return:
        """
