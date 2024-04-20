from Graphic.Customized.Animation.Basel import Animation as Basel


class Animation(Basel):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)

    def draw_frame(self, frame):
        frame = int(frame)
        self.graph_primer_surface.blit(self._animation_frame[frame], (0, 0))

    def __copy__(self, copied: any = None):
        super().__copy__(copied)
