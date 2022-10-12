from loghandler import Logging
import os
import requests
from http import HTTPStatus
import datetime
from structuredmessage import StructuredMessage

class Nomad():
    def __init__(self, endpoint, backup_folder, token):
        self.endpoint = endpoint
        self.backup_folder = backup_folder
        self.token = token
        self.url = endpoint + 'operator/snapshot'
        
    def create_backup_folder_if_not_exist(self):
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)

    def backup(self):
        log = Logging()
        log.create_log_folder_if_not_exist()
        logger = log.settingup_logger()
        self.create_backup_folder_if_not_exist()

        headers = {}

        if not self.token:
            headers['X-Nomad-Token'] = self.token
        r = requests.get(self.url, headers, allow_redirects=True)

        if (r.status_code == HTTPStatus.OK):
            try:
                if (r.headers.get('Content-Encoding') == 'gzip'):
                    file_name_backup = 'backup_' + datetime.datetime.now().strftime('%Y_%m_%d_%HH_%MM_%SS') + '.tgz'
                    file_path_backup = os.path.join(self.backup_folder, file_name_backup)
                    with open(file_path_backup, 'wb') as f:
                        f.write(r.content)
                        f.close()
            except:
                logger.error(StructuredMessage(Timestamp=datetime.datetime.now().strftime('%Y %m %d %H:%M:%S'), Level='Error', Message='Saved failure'))
        else:
            logger.error(StructuredMessage(Timestamp=datetime.datetime.now().strftime('%Y %m %d %H:%M:%S'), Level='Error', Message='Download failure'))
