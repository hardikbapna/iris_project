#Loads config files

import yaml
import os


CONFIG_PATH = "C:\\Users\\Hardik\\PycharmProjects\\iris\\iris_project\\config_files"

class Configuration():

    def load_config(self, config_name):

        try:
            print("In func: load_config")
            with open(os.path.join(CONFIG_PATH,config_name)) as file:
                config = yaml.safe_load(file)

            return config

        except Exception as e:
            print("Configuration file could not be read because:- {}".format(e))

