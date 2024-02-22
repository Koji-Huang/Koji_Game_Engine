import pygame.image

from GraphicComponent.UI.Label import Label


class Image(Label):
    def __init__(self, pos, size, image_path: str, alpha: int = 255, *args, **kwargs):
        super().__init__(pos, size, *args, *kwargs)
        self.graph_primer_surface = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), size)
        self.graph_primer_surface.set_alpha(alpha)
