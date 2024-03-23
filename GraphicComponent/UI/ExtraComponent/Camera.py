import pygame

from GraphicComponent.UI.Label import Label
from GraphicComponent.Event.MouseEvent import Scrolling


def scale(**kwargs):
    camera = kwargs['graphic_object']
    precise = kwargs['event'].precise_y
    camera.scale(camera.camera_ratio * (1 + 0.1 * precise))


class Camera(Label):
    def __init__(self, pos, size, *args, **kwargs):
        self.camera_pos = (0, 0)
        self.camera_size = size
        self.camera_ratio = 1.0

        self.virtualLabel = Label((0, 0), size)
        self.virtualLabel.virtualFather = self
        self.virtualLabel.graph_active = True

        super().__init__(pos, size, *args, **kwargs)

        self.son.append(self.virtualLabel)

        rollEvent = Scrolling(scale, self)
        self.event_add(pygame.MOUSEWHEEL, rollEvent)

    def tree_add_son(self, son) -> None:
        return self.virtualLabel.tree_add_son(son)

    def tree_remove_son(self, son) -> None:
        return self.virtualLabel.tree_remove_son(son)

    def graph_update(self, mapping_pos: tuple[int, int] = None, mapping_size: tuple[int, int] = None, *args, **kwargs):
        if mapping_pos is None:
            mapping_pos = [0, 0]
        label_size = self.virtualLabel.size()
        pos = list([self.camera_pos[i] - self.camera_size[i] / 2 for i in [0, 1]])
        size = list(self.camera_size)

        if pos[0] < 0:
            if pos[0] + size[0] > 0:
                size[0] += pos[0]
                mapping_pos[0] += -1 * pos[0] * self.camera_ratio
                pos[0] = 0
        if pos[1] < 0:
            if pos[1] + size[1] > 0:
                size[1] += pos[1]
                mapping_pos[1] += -1 * pos[1] * self.camera_ratio
                pos[1] = 0

        if pos[0] >= label_size[0] or pos[1] >= label_size[1] or 0 in size or pos[0] < 0 or pos[1] < 0:
            # area out of label's right, not render
            pass
        else:
            # if size is out of range of subsurface
            if pos[0] + size[0] >= label_size[0]:
                size[0] = label_size[0] - pos[0]
            if pos[1] + size[1] >= label_size[1]:
                size[1] = label_size[1] - pos[1]

            copied_surface = self.virtualLabel.graph_surface.subsurface(pos + size).copy()

            scale_size = tuple(int(i * self.camera_ratio) for i in size)

            scale_surface = pygame.transform.scale(copied_surface, scale_size)

            if mapping_size:
                scale_surface = pygame.transform.scale(scale_surface, mapping_size)

            super().graph_update(*args, **kwargs)
            self.graph_surface.fill((0, 0, 0))
            self.graph_surface.blit(scale_surface, mapping_pos)

    def scale(self, multiple: float):
        self.camera_ratio = multiple
        self.graph_draw()

    def move(self, relative: tuple[int, int]):
        self.camera_pos = tuple(int(relative[i] + self.camera_pos[i]) for i in [0, 1])
        self.graph_draw()

    def focus_on(self, position: tuple[int, int]):
        self.pos = position
        self.graph_draw()

