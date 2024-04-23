from Graphic.Customized.Animation.Basel import Animation as Basel


class Animation(Basel):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)

    def draw_frame(self, frame):
        self.animation_frame[frame].graph_update()
        self.graph_primer_surface.blit(self.animation_frame[frame].graph_surface, (0, 0))

    def __copy__(self, copied: any = None):
        super().__copy__(copied)
