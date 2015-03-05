class Pb_Api_Param(object):
    def __init__(self, *args, **kwargs):
      self._name = kwargs['name']
      self._value = kwargs['value']
    def name(self):
      return self._name
    def required(self):
      return self._required

    def is_default(self, a=0):
      if a: self._is_default = 1
      return self._is_default

    def value(self, *args, **kwargs):
      if len(args) >= 1:
        self._value = args[0]
        if 'default' in kwargs:
          self.is_default(1)
        self.is_ready(1)
      return self._value
    
    def is_ready(self, *args):
      if len(args) >= 1:
        self._is_ready = args[0]
      return self._is_ready or not self.required()
