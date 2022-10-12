import json

class Setting():
    def __init__(self, filename):
        self.filename = filename

    def get(self):
        with open(self.filename) as f:
            data = json.load(f)
            settings = data
            f.close()
        return settings
