#!/usr/bin/python2.7
import re
from Pb_Api.Params import Pb_Api_Params 
from Pb_Api.Param import Pb_Api_Param
from Pb_Api.Param.Option import Pb_Api_Param_Option
from Pb_Api.Param.Options import Pb_Api_Param_Options
from Pb_Api.Param.Username import Pb_Api_Param_Username
from Pb_Api.Param.Image_Url import Pb_Api_Param_Image_Url
from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect

from config import PATTERN_BASE_URL

class Pattern_Url_Option(Pb_Api_Param_Option):
  def __init__(self, **kwargs):
    super(Pb_Api_Param_Option, self).__init__(**kwargs) 
  @classmethod
  def from_name(cls, **kwargs):
    formatted = "{}/{}.png".format(PATTERN_BASE_URL, kwargs["value"])
    return cls(weight=kwargs["weight"], value=formatted )

class ImPattern_Params(Pb_Api_Params): 
    def __init__(self):
        self.params = [
           Pb_Api_Param_Username(name="username", required=0), 
           Pb_Api_Param_Image_Url(name="image_url", required=1),
           Pb_Api_Param_MultiSelect(name="pattern_url", required=1, options=pattern_url_options)
        ]

pattern_url_options = Pb_Api_Param_Options([  
  Pattern_Url_Option.from_name(weight=0, value=i) for i in range(1,100) ] + [
  Pattern_Url_Option.from_name(weight=0, value="a{}".format(i)) for i in range(0, 42) 
])

pattern_url_options.search("a10").weight = 20;
