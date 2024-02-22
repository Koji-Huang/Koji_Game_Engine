from GraphicComponent.Graphic import Graphic
import pygame


class MainWindows(Graphic):
    def __init__(self, size, *args, **kwargs):
        self.windows_surface = pygame.display.set_mode(size, *args, **kwargs)
        super().__init__((0, 0), size)
        self.graph_primer_surface = pygame.Surface(size)
        self.graph_primer_surface.fill((0, 0, 0))
        self.x = 0
        self.y = 0
        pygame.font.init()

    def __graph_update(self, *args,
                       **kwargs):
        ...

    def update(self):
        self.graph_update()
        self.windows_surface.blit(self.graph_surface, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            self.event_spread(event.type, event=event)