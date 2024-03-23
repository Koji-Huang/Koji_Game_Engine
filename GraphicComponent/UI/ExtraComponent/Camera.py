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
        primer_surface_size = [i / self.camera_ratio for i in self.size()]
        primer_surface_pos = list(self.camera_pos[i] - primer_surface_size[i] / 2 for i in [0, 1])
        render_size = list(self.size())

        if primer_surface_pos[0] < 0:
            if primer_surface_pos[0] + primer_surface_size[0] > 0:
                primer_surface_size[0] += primer_surface_pos[0]
                mapping_pos[0] += -1 * primer_surface_pos[0]
                primer_surface_pos[0] = 0
        if primer_surface_pos[1] < 0:
            if primer_surface_pos[1] + primer_surface_size[1] > 0:
                primer_surface_size[1] += primer_surface_pos[1]
                mapping_pos[1] += -1 * primer_surface_pos[1]
                primer_surface_pos[1] = 0

        if primer_surface_pos[0] >= label_size[0] or primer_surface_pos[1] >= label_size[1] or 0 in primer_surface_size or primer_surface_pos[0] < 0 or primer_surface_pos[1] < 0:
            # area out of label's right, not render
            self.graph_surface.fill((50, 50, 50))
        else:
            # if size is out of range of subsurface
            if primer_surface_pos[0] + primer_surface_size[0] >= label_size[0]:
                primer_surface_size[0] = label_size[0] - primer_surface_pos[0]

            if primer_surface_pos[1] + primer_surface_size[1] >= label_size[1]:
                primer_surface_size[1] = label_size[1] - primer_surface_pos[1]

            primer_surface = self.virtualLabel.graph_surface.subsurface(primer_surface_pos + primer_surface_size).copy()

            scale_surface = pygame.transform.smoothscale(primer_surface, [i * self.camera_ratio for i in primer_surface_size])

            super().graph_update(*args, **kwargs)
            self.graph_surface.fill((50, 50, 50))
            self.graph_surface.blit(scale_surface, mapping_pos)

    def scale(self, multiple: float):
        self.camera_ratio = multiple
        self.graph_draw()

    def move(self, relative: tuple[int, int]):
        self.camera_pos = tuple(int(relative[i] + self.camera_pos[i]) for i in [0, 1])
        self.graph_draw()

    def move_to(self, position: tuple[int, int]):
        self.camera_pos = position
        self.graph_draw()

    def event_spread(self, event_name, **event_args):
        super().event_spread(event_name, **event_args)