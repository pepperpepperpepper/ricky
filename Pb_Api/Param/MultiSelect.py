import random
from Pb_Api.Param import Pb_Api_Param 

class Pb_Api_Param_MultiSelect(Pb_Api_Param):
    def __init__(self, *args, **kwargs):
      self._options = kwargs['options']
      super(Pb_Api_Param_MultiSelect, self).__init__(*args, **kwargs) 
    def options(self):
      return self._options

    @property
    def value(self):
      return super(Pb_Api_Param_MultiSelect, self).get_value()
    @value.setter
    def value(self, value):
      valid = False
      for i in self.options():
        if value == i['value']: valid = True
      if value is None: valid = True
      if not valid : raise ValueError 
      super(Pb_Api_Param_MultiSelect, self).set_value(value)
    def randomize(self):
       weights_total = sum(map(lambda x: x["weight"], self.options()))
       choice = random.randint(0, weights_total)
       position = 0
       for elem in self.options():
          position += elem["weight"]
          if position >= choice:
              self.value = elem["value"]
              break
    def heaviest(self, param):
       heaviest_idx = 0
       heaviest_weight = 0
       idx = 0
       for elem in self.options():
          if elem["weight"] > heaviest_weight:
              heaviest_weight = elem["weight"]
              heaviest_idx = idx;
          idx += 1
       self.value = self.options()[heaviest_idx]["value"]
