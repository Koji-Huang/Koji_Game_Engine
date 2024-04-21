from Manager.ConfigManager import *


config = load_config_file('Basel.ini')
register_config(config)

import GlobalConstant

print(GlobalConstant.Registry)
GlobalConstant.register_global_environment()
pass