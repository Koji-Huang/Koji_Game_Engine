from pygame.image import load as load_image
from API.ConfigAPI import load_config_file
from DataType.ConfigFile import ini, txt, json
from Asset.StandardDataType.Graphic.Basic import Package as _Package


class Package(_Package):
    def __init__(self, config_path: str, name: str = 'undefined', *args, **kwargs):
        super().__init__(config_path, name=name, *args, **kwargs)
        self.reload()

    def __copy__(self, copied=None):
        if copied is None:
            copied = Package(self._path)
        super().__copy__(copied)
        return copied

    def __call__(self, *args, **kwargs):
        return self._surface.copy

    def reload(self):
        super().reload()
        self._config_object = load_config_file(self._path)
        match self._config_object.get_file_type():
            case 'txt':
                self._frame_size = int(self._config_object['frame_size'])
                self._animation_name = self._config_object['name']
                self._sub_path = self._config_object['sub_path']
            case 'ini':
                self._frame_size = int(self._config_object['Animation']['frame_size'])
                self._animation_name = self._config_object['file']['name']
                self._sub_path = self._config_object['file']['sub_path']
            case 'json':
                self._frame_size = self._config_object['file']['frame_size']
                self._animation_name = self._config_object['file']['name']
                self._sub_path = self._config_object['file']['sub_path']

        self._frames = [None] * self._frame_size
        self._frames_info = [None] * self._frame_size

        for frame in range(self._frame_size):
            self.load_frame(frame + 1)

    def load_frame(self, frame, file_type: str = None):
        if file_type is None:
            file_type = self._config_object.get_file_type()
        file_folder = self._config_object.__path__() + "\\"
        match file_type:
            case 'txt':
                self._frames[frame - 1] = load_image(file_folder + self._config_object["%d" % frame])
                self._frames_info[frame - 1] = {
                    'x': int(self._config_object['%d_x' % frame]),
                    'y': int(self._config_object['%d_y' % frame]),
                    'w': int(self._config_object['%d_w' % frame]),
                    'h': int(self._config_object['%d_h' % frame]),
                    'a': int(self._config_object['%d_a' % frame])
                }
            case 'ini':
                config: dict[str: [str]] = self._config_object["%d" % frame]
                self._frames[frame - 1] = load_image(file_folder + config['path'])
                self._frames_info[frame - 1] = {
                    'x': int(config['x']),
                    'y': int(config['y']),
                    'w': int(config['w']),
                    'h': int(config['h']),
                    'a': int(config['a'])
                }
            case 'json':
                config: dict[str: [str | int]] = self._config_object["%d" % frame]
                self._frames[frame - 1] = load_image(file_folder + config['path'])
                self._frames_info[frame - 1] = {
                    'x': config['x'],
                    'y': config['y'],
                    'w': config['w'],
                    'h': config['h'],
                    'a': config['a']
                }
            case _:
                raise "File not matched to Animation"

"""
Animation Config File Struct


txt:

config_type = Animation
name = str
sub_path = str
frame_size = int

1 = ...
2 = ...
3 = ...
...

1_x = ...
1_y = ...
1_w = ...
1_h = ...
1_a = ...
...
2_xxx = ...
...
3_xxx = ...
...
...


ini:

[file]
config_type = Animation
name = str
sub_path = str

[Animation]
frame_size = int

[1]
path = str
x = int
y = int
w = int
h = int
a = int

[2]
...

[3]
...
...



json:

{
    file =  {
        config_type = "Animation";
        name = "...";
        sub_path = "...";
    };
    
    1 = {
        path = str;
        x = int;
        y = int;
        w = int;
        h = int;
        a = int;
    };
    
    2 = {
        ...
    };
    
    3 = {
        ...
    };

    ...
}

"""