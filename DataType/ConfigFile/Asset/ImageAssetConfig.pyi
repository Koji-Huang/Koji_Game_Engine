import pygame
from .BasicAssetConfig import AssetConfig


class Image(AssetConfig):
    w: int
    h: int
    alpha: int
    path: str

    def __init__(self, file_path: str):
        pass

    def convert(self) -> pygame.Surface:
        pass