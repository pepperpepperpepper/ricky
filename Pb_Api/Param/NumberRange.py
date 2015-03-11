import sys
from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect
import random
class Pb_Api_Param_NumberRange(Pb_Api_Param_MultiSelect): 
    def __init__(self, **kwargs):
      super(Pb_Api_Param_NumberRange, self).__init__(**kwargs)  
      self.range_min = kwargs['min']
      self.range_max = kwargs['max']
    def randomize(self):
       weights_total = sum(map(lambda x: x["weight"], self.options())) + self.range_max - self.range_min
       choice = random.randint(0, weights_total)
       position = 0
       for elem in self.options():
          position += elem["weight"] 
          if position >= choice:
              self.value = elem["value"]
              return
       self.value = random.randint(self.range_min,self.range_max)
    @property
    def value(self):
      return super(Pb_Api_Param_MultiSelect, self).get_value()
    @value.setter
    def value(self, value):
      self._value = value
      if not self._value is None:
        self.is_ready = 1
      self.set_by_user = 1 
