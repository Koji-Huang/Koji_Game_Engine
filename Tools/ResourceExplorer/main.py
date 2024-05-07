import os

import pygame.display

import API.Global

os.path.join("../../../Koji_Game_Engine")


from API import *


def main():
    API.GlobalAPI.register_global_environment()
    _global = API.ConfigAPI.load_config_file("config.json")
    API.ConfigAPI.register_config(_global)
    for config in API.GlobalAPI.Registry['System']['Environment']['start_up config']:
        son = API.ConfigAPI.load_config_file(config)
        if son.config_type == "Asset":
            API.ConfigAPI.convert_to_asset(son)
        else:
            API.ConfigAPI.register_config(son)

    API.ThreadAPI = API.ThreadAPI_type()
    API.GraphicAPI = API.GraphicAPI_type(size=API.GlobalAPI.Registry['System']['Screen']['size'])
    pygame.display.set_caption(API.GlobalAPI.Registry['System']['Screen']['title'])
    API.EventAPI = API.EventAPI_type()
    API.EventAPI.load_default_event()
    pass


if __name__ == "__main__":
    main()
