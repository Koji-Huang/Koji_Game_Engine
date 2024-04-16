from Manager.ConfigManager import *


config = load_config_file('config.ini')
register_config(config)

import GlobalConstant

print(GlobalConstant.Registry)
GlobalConstant.register_global_environment_id()
pass