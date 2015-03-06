from config import USERNAME
from Pb_Api.Param.String import Pb_Api_Param_String

class Pb_Api_Param_Username(Pb_Api_Param_String):
    def __init__(self, **kwargs):
      super(Pb_Api_Param_Username, self).__init__(**kwargs) 
      self.default(USERNAME)