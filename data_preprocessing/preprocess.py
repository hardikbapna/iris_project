import pandas as pd
from config_files.load_configurations import Configuration

class Preprocessor():

    def __init__(self):
        print("In init of class Preprocessor")
        self.config_obj = Configuration()
        self.read_data()


    def read_data(self):

        try:
            print("In func: read_data")
            config = self.config_obj.load_config('config_preprocessing.yaml')
            raw_data = pd.read_csv(config["data_path"])
            #print(raw_data.head(5))

        except Exception as e:
            print("Could not read the data because:- {}".format(e))