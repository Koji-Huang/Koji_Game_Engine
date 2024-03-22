import pygame

from GraphicComponent.UI.Label import Label
from GraphicComponent.Event.MouseEvent import Scrolling


def scale(**kwargs):
    camera = kwargs['graphic_object']
    precise = kwargs['event'].precise_y
    camera.scale(camera.scaleRatio * (1 + 0.1 * precise))



class Camera(Label):
    def __init__(self, pos, size, *args, **kwargs):
        self.scaleRatio = 1
        self.virtualLabel = Label((0, 0), size)
        self.virtualLabel_size = size
        self.virtualLabel.virtualFather = self
        self.virtualLabel.graph_active = True
        self.relative_pos = (0, 0)
        super().__init__(pos, size, *args, **kwargs)
        self.son.append(self.virtualLabel)
        rollEvent = Scrolling(scale, self)
        self.event_add(pygame.MOUSEWHEEL, rollEvent)

    def tree_add_son(self, son) -> None:
        return self.virtualLabel.tree_add_son(son)

    def tree_remove_son(self, son) -> None:
        return self.virtualLabel.tree_remove_son(son)

    def graph_update(self, *args, **kwargs):
        super().graph_update(*args, **kwargs)
        self.graph_surface.fill((0, 0, 0))

        copied_pos = tuple(int(self.scaleRatio * i) for i in self.relative_pos)

        copied_rect = [copied_pos[0], copied_pos[1],
                       self.virtualLabel_size[0], self.virtualLabel_size[1]]

        if copied_rect[2] > self.virtualLabel_size[0]: copied_rect[2] = self.virtualLabel_size[0]
        if copied_rect[3] > self.virtualLabel_size[1]: copied_rect[3] = self.virtualLabel_size[1]
        if copied_rect[0] < 0: copied_rect[0] = 0
        if copied_rect[1] < 0: copied_rect[1] = 0

        mapping_size = tuple(i * self.scaleRatio for i in self.virtualLabel_size)
        mapping_pos = tuple(i * self.scaleRatio for i in self.relative_pos)

        copied_surface = pygame.transform.smoothscale(
            self.virtualLabel.graph_surface.subsurface(copied_rect), mapping_size)

        self.graph_surface.blit(copied_surface, mapping_pos)

    def scale(self, multiple: float):
        self.scaleRatio = multiple
        self.graph_draw()

    def move(self, relative: tuple[int, int]):
        self.relative_pos = tuple(int(relative[i] + self.relative_pos()[i]) for i in [0, 1])
        self.graph_draw()
