import pygame.image
from FunctionTools.coordinate import scale_series_proportionality_int
from Graphic.UI.Label import Label


class Image(Label):
    def __init__(self, pos, size, image: str or pygame.Surface, alpha: int = 255, layout_mode=0,
                 antialiasing: bool = True, *args, **kwargs):
        super().__init__(pos, size, *args, **kwargs)
        if isinstance(image, str):
            self.image_surface = pygame.image.load(image).convert_alpha()
        elif isinstance(image, pygame.Surface):
            self.image_surface = image
        else:
            raise TypeError(image)
        self.layout_mode = layout_mode
        self.image_antialiasing = antialiasing
        self.graph_draw()
        self.graph_primer_surface.set_alpha(alpha)

    def change_image_object(self, image):
        if isinstance(image, str):
            self.image_surface = pygame.image.load(image).convert_alpha()
        elif isinstance(image, pygame.Surface):
            self.image_surface = image
        else:
            raise TypeError(image)
        self.graph_active = True

    def change_image_setting(self, alpha=None, layout_mode=None, antialiasing=None):
        if layout_mode:
            self.layout_mode = layout_mode
        if antialiasing:
            self.image_antialiasing = antialiasing
        if alpha:
            self.graph_primer_surface.set_alpha(alpha)
        self.graph_active = True

    def graph_draw(self):
        super().graph_draw()
        if self.graph_active:
            if self.layout_mode == 0:
                if self.image_antialiasing:
                    scale_surface = pygame.transform.smoothscale(
                        self.image_surface,
                        scale_series_proportionality_int(self.image_surface.get_size(), self.size()))
                else:
                    scale_surface = pygame.transform.scale(
                        self.image_surface,
                        scale_series_proportionality_int(self.image_surface.get_size(), self.size()))
                self.graph_primer_surface.blit(scale_surface,
                                               (int((self.size()[0] - scale_surface.get_size()[0]) / 2),
                                                int((self.size()[1] - scale_surface.get_size()[1]) / 2)))
            if self.layout_mode == 1:
                if self.image_antialiasing:
                    scale_surface = pygame.transform.smoothscale(self.image_surface, self.size())
                else:
                    scale_surface = pygame.transform.scale(self.image_surface, self.size())
                self.graph_primer_surface.blit(scale_surface, (0, 0))
            if self.layout_mode == 2:
                self.graph_primer_surface.blit(self.image_surface, (0, 0))
