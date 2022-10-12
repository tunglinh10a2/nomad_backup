from distutils.debug import DEBUG
from setting import Setting 
from nomad import Nomad

# Read setting endpoint
settings = Setting(filename='setting.json').get()

nomad_backup = Nomad(endpoint=settings['nomad']['endpoint'],backup_folder=settings['nomad']['backup_folder'],token=settings['nomad']['token'])
nomad_backup.backup()
