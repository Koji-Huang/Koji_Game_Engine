import math

import pygame

windows = pygame.display.set_mode((800, 600))

# Image = pygame.Image.load(r'..\picture_2.jpg').convert_alpha()
image = pygame.Surface((800, 600))
image.fill((127, 127, 127))
windows.blit(image, (0, 0))

texture = (r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\Graphic"
           r"\Effect\TextureMapping\Noise\_texture_\MahalanobisClassification(3D)(Double)(3840x3840).png")

texture = pygame.image.load(texture).convert_alpha()

for i in range(10000):
    background = (r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine"
                  r"\Graphic\Effect\TextureMapping\Noise\_texture_\spherical(B-line)(1980x1980)")
    num = int(math.sin(i / 5) * 10) + 10
    index = '\\000%d.png' % (num % 20 + 1) if num % 20 < 9 else '\\00%d.png' % (num % 20 + 1)
    background = pygame.image.load(background + index).convert_alpha()
    background = pygame.transform.scale(background, (800, 600))
    background.blit(texture, (0, 0), special_flags=pygame.BLEND_RGB_MIN)
    windows.blit(background, (0, 0))
    pygame.display.update()
