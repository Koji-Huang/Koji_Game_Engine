from os.path import abspath, dirname
from .BaselAssetConfig import AssetConfig
from ..Basel.basel import Basel


class Animation(AssetConfig):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.config_type = 'Animation'
        self.frame_info = dict()
        bind = self.bind_config_file
        path = dirname(abspath(file_path)) + '\\'
        match self.config_file_format:
            case 'json' | 'ini':
                self.x = int(bind['Animation']['x'])
                self.y = int(bind['Animation']['y'])
                self.w = int(bind['Animation']['w'])
                self.h = int(bind['Animation']['h'])
                self.frame_size = int(bind['Animation']['frame_size'])
                for i in range(self.frame_size):
                    config = bind['%d' % i]
                    self.frame_info[i] = {
                        'path': path + config['path'],
                        'x': int(config['x']),
                        'y': int(config['y']),
                        'w': int(config['w']),
                        'h': int(config['h']),
                        'a': int(config['a'])}
            case 'txt':
                self.x = int(bind['x'])
                self.y = int(bind['y'])
                self.w = int(bind['w'])
                self.h = int(bind['h'])
                self.frame_size = int(bind['frame_size'])
                for i in range(self.frame_size):
                    self.frame_info[i] = {
                        'x': int(bind['%d_x' % i]),
                        'y': int(bind['%d_y' % i]),
                        'w': int(bind['%d_w' % i]),
                        'h': int(bind['%d_h' % i]),
                        'a': int(bind['%d_a' % i]),
                        'path': path + bind[str(i)]
                    }
            case _ as name:
                raise TypeError(name)

    def info(self, *args):
        ret = Basel.info(self)
        ret['frame_size'] = self.frame_size
        ret['w'] = self.w
        ret['h'] = self.h
        ret['x'] = self.x
        ret['y'] = self.y
        if args is not None:
            for arg in args:
                ret = ret[arg]
        return ret
