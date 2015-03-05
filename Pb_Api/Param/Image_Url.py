from config import TEST_URL
from Pb_Api.Param.String import Pb_Api_Param_String

class Pb_Api_Param_Image_Url(Pb_Api_Param_String): 
    def __init__(self, *args, **kwargs):
      super(Pb_Api_Param_Image_Url, self).__init__(*args, **kwargs) 
      self.value(TEST_URL, default=1) 
