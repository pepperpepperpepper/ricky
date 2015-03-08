from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect
class Pb_Api_Param_Bool(Pb_Api_Param_MultiSelect): 
    def __init__(self, **kwargs):
      super(Pb_Api_Param_Bool, self).__init__(**kwargs)  
      if len(this.options()) != 2:
        raise ValueError
