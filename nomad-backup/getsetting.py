import json

class GetSetting():
    def __init__(self, filename):
        self.filename = filename

    def value(self):
        with open(self.filename) as f:
            data = json.load(f)
            settings = data
            f.close()
        return settings
