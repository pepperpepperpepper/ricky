import re, random
from Pb_Api.Params import Pb_Api_Params 
from Pb_Api.Param import Pb_Api_Param
from Pb_Api.Param.Option import Pb_Api_Param_Option
from Pb_Api.Param.Options import Pb_Api_Param_Options
from Pb_Api.Param.Username import Pb_Api_Param_Username
from Pb_Api.Param.Image_Url import Pb_Api_Param_Image_Url
from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect
from Pb_Api.Param.NumberRange import Pb_Api_Param_NumberRange
from Pb_Api.Param.Color import Pb_Api_Param_Color

from Pb_Api.ImGradient.options import *


   
class ImGradient_Params(Pb_Api_Params): 
    def __init__(self):
        self.params = [
           Pb_Api_Param_Username(name="username", required=0), 
           Pb_Api_Param_NumberRange(name="width", required=1, options=width_options, min=100, max=800),
           Pb_Api_Param_NumberRange(name="height", required=1, options=height_options, min=100, max=800),
           Pb_Api_Param_Color(name="color1", required=1, options=color1_options),
           Pb_Api_Param_Color(name="color2", required=1, options=color2_options),
           Pb_Api_Param_MultiSelect(name="filetype", required=0, options=filetype_options),
           Pb_Api_Param_MultiSelect(name="gradienttype", required=1, options=gradienttype_options),
           Pb_Api_Param_MultiSelect(name="halftone", required=0, options=halftone_options),
           Pb_Api_Param_MultiSelect(name="bevel", required=0, options=bevel_options),

           Pb_Api_Param_NumberRange(name="stripenumber", required=0, options=stripenumber_options, min=0, max=400),
           Pb_Api_Param_NumberRange(name="stripeintensity", required=0, options=stripeintensity_options, min=0, max=5000),

           Pb_Api_Param_NumberRange(name="blurriness", required=0, options=blurriness_options, min=0, max=200),
#           Pb_Api_Param_NumberRange(name="contrast", required=0, options=contrast_options, min=0, max=200), 
           Pb_Api_Param_NumberRange(name="brightness", required=0, options=brightness_options, min=0, max=200), 
           Pb_Api_Param_NumberRange(name="saturation", required=0, options=saturation_options, min=0, max=200), 
           Pb_Api_Param_NumberRange(name="hue", required=0, options=hue_options, min=0, max=200), 

           Pb_Api_Param_NumberRange(name="percentbeveled", required=0, options=percentbeveled_options, min=0, max=100), 
           Pb_Api_Param_NumberRange(name="rotate", required=0, options=rotate_options, min=0, max=360), 
           Pb_Api_Param_NumberRange(name="tilt", required=0, options=tilt_options, min=0, max=360), 


           Pb_Api_Param_MultiSelect(name="flop", required=0, options=flop_options),
           Pb_Api_Param_MultiSelect(name="flip", required=0, options=flip_options),
        ]
