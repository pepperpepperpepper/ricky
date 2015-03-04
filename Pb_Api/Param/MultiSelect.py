from Pb_Api.Param import Pb_Api_Param 

class Pb_Api_Param_MultiSelect(Pb_Api_Param):
    def __init__(self, options):
      super(Pb_Api_Param_MultiSelect, self).__init__(*args, **kwargs) 
    def options(self):
      return self.options
    def value(self, *args):
      if len(args) > 1:
        valid = False
        for i in self.options:
          if args[0] == i['value']: valid = True
        if not valid : raise ValueError 
        super(Pb_Api_Param_MultiSelect, self).value(args[0])
    def randomize(self):
      pass
