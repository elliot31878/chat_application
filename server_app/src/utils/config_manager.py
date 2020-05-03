"""
---- this class created at (Sunday , May , 5/3/2020) by MR.ROBOT 

---- this class for handle app Config (0-0)
"""
from json import loads as json_loads

from easydict import EasyDict as edict

from commons.constants.paths import APP_SETTING_PATH


class ConfigManager:
    def __init__(self):
        super().__init__()
        self.config_path=APP_SETTING_PATH

    def __read_config__(self):
        """
        this method for read config file
        Returns:
            [dict] -- [return dictionary from my config ().json) ]
        """
        with open(self.config_path,'r')as file:
            configs=json_loads(file.read().strip("\n"))
        return configs

    @property
    def get(self):
        """
        this method for get value in dictianory
        Returns:
            [object] -- [key value dictionary]
        """
        e_dict=edict(self.__read_config__())
        return e_dict
