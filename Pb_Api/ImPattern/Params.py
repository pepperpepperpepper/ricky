#!/usr/bin/python2.7
from Pb_Api.Params import Pb_Api_Params 
from Pb_Api.Param.Username import Pb_Api_Param_Username
from Pb_Api.Param.String import Pb_Api_Param_String
from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect

pattern_url_options = [
    { "value":"1.png", "weight":1 },
    { "value":"2.png", "weight":1 },
]
class ImPattern_Params(Pb_Api_Params): 
    def __init__(self):
        self.params = [
           Pb_Api_Param_Username(name="username", required=1), 
           Pb_Api_Param_Image_Url(name="image_url", required=1),
           Pb_Api_Param_MultiSelect(name="pattern_url", required=1, options=pattern_url_options
           ),
        ]
