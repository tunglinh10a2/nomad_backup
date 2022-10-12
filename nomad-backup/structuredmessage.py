import json

class StructuredMessage(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return '%s' % (json.dumps(self.kwargs))
