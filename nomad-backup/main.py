from distutils.debug import DEBUG
from getsetting import GetSetting 
from nomad import Nomad

# Read setting endpoint
settings = GetSetting(filename='setting.json').value()


nomad_backup = Nomad(endpoint=settings['nomad']['endpoint'],backup_folder=settings['nomad']['backup_folder'])
nomad_backup.backup()
