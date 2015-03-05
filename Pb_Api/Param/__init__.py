import pprint

class Pb_Api_Param(object):
#    def __init__(self, **kwargs):
    def __init__(self, required=0, set_by_user=0, value=None, name=None, **kwargs): 
      self._value_default = None
      self.name = name
      self.required = required
      self.is_ready = 0 #should I try that?
      self.value = value
      self.set_by_user = set_by_user
    def __str__(self):
      return pprint.pformat(vars(self))

    def get_value(self):
      if self.set_by_user == 1:
         return self._value
      return self._value_default
    def set_value(self, value):
      self._value = value
      if not self._value is None:
        self.is_ready = 1
      self.set_by_user = 1 #like that? yeah also need method for setting default value
    value = property(get_value, set_value)   
    
    def default(self, value):
      self._value_default = value
 
    @property
    def is_ready(self):
      return self._is_ready or not self.required
    @is_ready.setter
    def is_ready(self, n):
      self._is_ready = n


    def randomize(self):
      pass
