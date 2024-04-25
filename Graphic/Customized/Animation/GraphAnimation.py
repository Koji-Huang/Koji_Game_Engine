from Graphic.Customized.Animation.Basel import Animation as Basel
from DataType.Generic.LinkedList import LinkedList


class Animation(Basel):
    def __init__(self, pos, size, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)

    def draw_frame(self, frame):
        self.animation_frame[frame].graph_active = True
        self.animation_frame[frame].graph_update()
        self.graph_primer_surface = self.animation_frame[frame].graph_surface.copy()

    def __copy__(self, copied: any = None):
        super().__copy__(copied)

    def set_size(self, size):
        super().set_size(size)

        if self.primer_frame is None or len(self.primer_frame) != len(self.animation_frame):
            if len(self.animation_frame) != 0:
                self.primer_frame = self.animation_frame.__copy__()
        self.animation_frame = LinkedList()
        for frame in self.primer_frame:
            self.animation_frame.append(frame.__copy__())
            self.animation_frame.tail.value.set_size(size)
