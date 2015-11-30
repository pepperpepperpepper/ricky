"""
Base option class...essentially a dictionary
but attributes can be accessed with a dot
"""


class Option(dict):
    def __init__(self, **kwargs):
        super(Option, self).__init__(**kwargs)

    def __getattr__(self, attr):
        return self.get(attr)

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__
