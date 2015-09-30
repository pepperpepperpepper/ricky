from ricky.config import USERNAME
from ricky.param.string import String

class Username(String):
    def __init__(self, **kwargs):
      super(Username, self).__init__(**kwargs)
      self.default(USERNAME)
