import random
from Pb_Api.Param import Pb_Api_Param 

class Pb_Api_Param_MultiSelect(Pb_Api_Param):
    def __init__(self, *args, **kwargs):
      self._options = kwargs['options'] if options in kwargs else []
      super(Pb_Api_Param_MultiSelect, self).__init__(*args, **kwargs) 
      if len(self._options): 
        self._validate_options()
        self.default(self._choose_heaviest())

    def options(self):
      return self._options
    def _validate_options(self):
      try: 
        int(self._options[0]['weight'])
        self._options[0]['value']
      except Exception as e:
        raise ValueError

    @property
    def value(self):
      return super(Pb_Api_Param_MultiSelect, self).get_value()
    @value.setter
    def value(self, value):
      if not any([ value == i['value'] for i in self.options() ]) and value != None:
        raise ValueError 
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

    def _choose_heaviest(self):
       heaviest_idx = 0
       heaviest_weight = 0
       idx = 0
       if (len(self.options())):
         for elem in self.options():
            if elem["weight"] > heaviest_weight:
                heaviest_weight = elem["weight"]
                heaviest_idx = idx;
            idx += 1
         self.value = self.options()[heaviest_idx]["value"]
       else:
         self.randomize()
    def heaviest(self):
       self.value = self._choose_heaviest()
