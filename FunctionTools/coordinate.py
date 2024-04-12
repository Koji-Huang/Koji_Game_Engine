
# A Single Num
Num = int

# x and y [x, y]
Point = [int, int]

# start num and cost num [num, rel_num]
Vector = [int, int]

# start num to end num [start_num, end_num]
Range = [int, int]

# width and length [width, height]
Size = [int, int]

# start pos and cost pos: [x, y, rel_x, rel_y]
Rect = [int, int, int, int]

# left-top point with right-down point: [A.x, A.y, B.x, B.y]
Area = [int, int, int, int]


# Left Point


def num_in_range(_num: Num, _range: Range):
    return _range[0] < _num < _range[1] or _range[1] < _num < _range[0]


def num_in_vector(_num: Num, _vector: Vector):
    return num_in_range(_num, (_vector[0], _vector[0] + _vector[1]))


def point_in_area(_point: Point, _area: Area):
    return (num_in_range(_point[0], (_area[0], _area[2]))
            and num_in_range(_point[1], (_area[1], _area[3])))


def point_in_rect(_point: Point, _rect: Rect):
    _rect = [_rect[0], _rect[1], _rect[0] + _rect[2], _rect[1] + _rect[3]]
    return point_in_area(_point, _rect)


def scale_series_proportionality(primer: tuple[int | float, ...], limit: tuple[int | float, ...]) -> tuple[float, ...]:
    proportion = tuple(primer[i] / limit[i] for i in range(len(primer)))
    scale_num = 1 / max(proportion)
    return tuple((i * scale_num for i in primer))


def scale_series_proportionality_int(primer: tuple[int | float, ...], limit: tuple[int | float, ...]) -> tuple[int, ...]:
    return tuple(int(i) for i in scale_series_proportionality(primer, limit))


def scale_series(series: tuple[int | float, ...], ratio: int | float) -> tuple[int | float, ...]:
    return tuple(num * ratio for num in series)


def scale_series_int(series: tuple[int | float, ...], ratio: int | float) -> tuple[int | float, ...]:
    return tuple(int(num * ratio) for num in series)


def scale_series_series(series_series: tuple[tuple[int | float, ...], ...], ratio: int | float):
    return tuple(scale_series(series, ratio) for series in series_series)


def scale_series_series_int(series_series: tuple[tuple[int | float, ...], ...], ratio: int | float):
    return tuple(scale_series_int(series, ratio) for series in series_series)


def mix_num(num_A: Num, num_B: Num, percent: float):
    return num_A * (1 - percent) + num_B * percent


def mix_point(point_A: Point, point_B: Point, percent: float):
    return tuple((mix_num(point_A[0], point_B[0], percent), mix_num(point_A[1], point_B[1], percent)))
