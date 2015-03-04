class Pb_Api_Param(object):
    def name(self):
      return self.name
    def required(self):
      return self.required

    def manually_set(self, *args):
      if len(args) >= 1:
        self._manually_set = args[0]
      return self._manually_set

    def value(self, *args, **kwargs):
      if len(args) >= 1:
        self._value = args[0]
        if not 'autogenerated' in kwargs:
          self.manually_set(1)
        self.is_ready(1)
      return self._value
    
    def is_ready(self, *args):
      if len(args) >= 1:
        self._is_ready = args[0]
      return self._is_ready or not self.required()
