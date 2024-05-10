from pygame.image import load as load_image
from DataType.Asset.AbstractAsset import Asset as AssetObject
from DataType.ConfigFile.AnimationAssetConfig import Animation as AnimationConfigObject
from Graphic.Customized.Animation import GraphAnimation as GraphAnimationObject
from Graphic.Basic.Graph import Graph


class Package(AssetObject):
    def __init__(self, config: AnimationConfigObject, *args, **kwargs):
        super().__init__(config, *args, **kwargs)
        self.animation_type = 'GraphAnimation'

    def __call__(self, *args, **kwargs):
        return self.convert()

    def convert(self):
        animation = GraphAnimationObject((self.configObject.x, self.y), (self.configObject.w, self.configObject.h))
        for i in range(self.configObject.frame_size):
            info = self.configObject.frame_info[i]
            surface = Graph((info['x'], info['y']), (info['w'], info['h']), load_image(info['path']))
            surface.graph_surface.set_alpha(info['a'])
            animation.animation_add_frame(surface)
        return animation

    def __getattr__(self, item):
        return self.configObject.__getattribute__(item)
