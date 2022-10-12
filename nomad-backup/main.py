from distutils.debug import DEBUG
from time import timezone
import requests
import datetime
import os
import pathlib
import logging
import json

dest_folder = '/opt/backup/nomad/'
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

log_folder = f'{pathlib.Path().resolve()}/logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

url = 'http://localhost:4646/v1/operator/snapshot'
r = requests.get(url, allow_redirects=True)


# Create and configure logger
log_file_info = log_folder + '/' + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
logging.basicConfig(filename=log_file_info,
                    format='%(message)s',
                    filemode='a',
                    level=logging.DEBUG
                    )
 
# Creating an object
logger = logging.getLogger()

class StructuredMessage(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return '%s' % (json.dumps(self.kwargs))
m = StructuredMessage   # optional, to improve readability

if (r.status_code == 200):
    try:
        if (r.headers.get('Content-Encoding') == 'gzip'):
            file_name_backup = 'backup_' + datetime.datetime.now().strftime('%Y_%m_%d_%HH_%MM_%SS') + '.tgz'
            file_path_backup = os.path.join(dest_folder, file_name_backup)
            with open(file_path_backup, 'wb') as f:
                f.write(r.content)
                f.close()
    except:
        logger.error(m(Timestamp=datetime.datetime.now().strftime('%Y %m %d %H:%M:%S'),Level='Error',Message='Saved failure'))
else:
    logger.error(m(Timestamp=datetime.datetime.now().strftime('%Y %m %d %H:%M:%S'),Level='Error',Message='Download failure'))

