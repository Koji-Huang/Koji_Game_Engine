import pygame

from GraphicComponent.UI.Label import Label


class Camera(Label):
    def __init__(self, pos, size, bind_component: any = None, *args, **kwargs):
        self.camera_pos = (0, 0)
        self.camera_ratio = 1.0
        if bind_component is None:
            self.virtualLabel = Label((0, 0), size)
        else:
            self.virtualLabel = bind_component
        self.virtualLabel.virtualFather = self
        self.virtualLabel.graph_active = True

        super().__init__(pos, size, *args, **kwargs)

        self.son.append(self.virtualLabel)

    def tree_add_son(self, son) -> None:
        return self.virtualLabel.tree_add_son(son)

    def tree_remove_son(self, son) -> None:
        return self.virtualLabel.tree_remove_son(son)

    def graph_update(self, mapping_pos: tuple[int, int] = None, mapping_size: tuple[int, int] = None, *args, **kwargs):
        if mapping_pos is None:
            mapping_pos = [0, 0]
        label_size = self.virtualLabel.size()
        size = list(int(i * self.camera_ratio) for i in self.size())
        pos = list([self.camera_pos[i] - (self.size()[i] / 2) / self.camera_ratio for i in [0, 1]])

        if pos[0] < 0:
            if pos[0] + size[0] > 0:
                size[0] += pos[0]
                mapping_pos[0] += -1 * pos[0]
                pos[0] = 0
        if pos[1] < 0:
            if pos[1] + size[1] > 0:
                size[1] += pos[1]
                mapping_pos[1] += -1 * pos[1]
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

            scale_size = list(int(i * self.camera_ratio) for i in size)

            copied_surface = self.virtualLabel.graph_surface.subsurface(pos + size).copy()

            # # Scale to max range
            # A_k = self.size()[0] / self.size()[1]
            # B_k = scale_size[0] / scale_size[1]
            # if A_k > B_k:
            #     scale_size[0] *= self.size()[1] / scale_size[1]
            #     scale_size[1] = self.size()[1]
            # if A_k < B_k:
            #     scale_size[1] *= self.size()[0] / scale_size[0]
            #     scale_size[0] = self.size()[0]
            # if A_k == B_k:
            #     scale_size[1] = self.size()[1]
            #     scale_size[0] = self.size()[0]

            # # Keep in Center
            # if scale_size[0] < self.size()[0]:
            #     mapping_pos[0] = (self.size()[0] - scale_size[0]) / 2
            #
            # if scale_size[1] < self.size()[1]:
            #     mapping_pos[1] = (self.size()[1] - scale_size[1]) / 2

            scale_surface = pygame.transform.scale(copied_surface, scale_size)

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
        self.camera_pos = position
        self.graph_draw()

    def event_spread(self, event_name, **event_args):
        super().event_spread(event_name, **event_args)