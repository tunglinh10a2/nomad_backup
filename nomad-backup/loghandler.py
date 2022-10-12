import os
import logging
import datetime
import pathlib

class Logging():
    def __init__(self):
        self.log_folder = f'{pathlib.Path().resolve()}/logs'
    
    def create_log_folder_if_not_exist(self):
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

    def settingup_logger(self):
        log_file_info = self.log_folder + '/' + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
        logging.basicConfig(filename=log_file_info,format='%(message)s',filemode='a',level=logging.DEBUG)
        
        return logging.getLogger()
