"""
    created at feb 05/2020 by topcodermc
    - this handle app configs 
"""

from json import loads as json_loads

from easydict import EasyDict as edict

from commons.constants.paths import APP_SETTING_PATH

class ConfigManager:

    def __init__(self):
        self.config_path = APP_SETTING_PATH
    
    def __read_config__(self):
        with open(self.config_path, 'r') as file:
            configs = json_loads(file.read().strip("\n"))
        return configs

    def get(self):
        dict_e = edict(self.__read_config__())
        return dict_e
