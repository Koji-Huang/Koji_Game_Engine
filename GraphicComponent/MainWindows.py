from GraphicComponent.Graph import Graph
import pygame


class MainWindows(Graph):
    def __init__(self, size, *args, **kwargs):
        self.windows_surface = pygame.display.set_mode(size, *args, **kwargs)
        self.graph_primer_surface = pygame.Surface(size)
        self.graph_primer_surface.fill((0, 0, 0))
        self.x = 0
        self.y = 0
        pygame.font.init()
        super().__init__((0, 0), size)

    def graph_draw(self, *args,
                   **kwargs):
        self.windows_surface.blit(self.graph_surface, (0, 0))

    def update(self):
        self.graph_update()
        # self.event_update()

    def graph_update(self, *args, **kwargs):
        super().graph_update()
        pygame.display.update()

    def event_update(self, **kwargs):
        for event in pygame.event.get():
            self.event_spread(event.type, event=event)
