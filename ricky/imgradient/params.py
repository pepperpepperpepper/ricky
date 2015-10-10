import re
from ricky.params import Params as _Params
from ricky.param.username import Username
from ricky.param.multiselect import MultiSelect
from ricky.param.numberrange import NumberRange
from ricky.param.color import Color
from ricky.imgradient.options import *


class Params(_Params):
    def __init__(self):
        super(Params, self).__init__(
            Username(name="username", required=0),
            NumberRange(
                name="width",
                required=1,
                options=width_options,
                min=10,
                max=800
            ),
            NumberRange(
                name="height",
                required=1,
                options=height_options,
                min=10,
                max=800
            ),
            Color(name="color1", required=1, options=color1_options),
            Color(name="color2", required=1, options=color2_options),
            MultiSelect(
                name="filetype",
                required=0,
                options=filetype_options
            ),
            MultiSelect(
                name="gradienttype",
                required=1,
                options=gradienttype_options
            ),
            MultiSelect(
                name="halftone",
                required=0,
                options=halftone_options
            ),
            MultiSelect(name="bevel", required=0, options=bevel_options),

            NumberRange(
                name="stripenumber",
                required=0,
                options=stripenumber_options,
                min=0,
                max=400
            ),
            NumberRange(
                name="stripeintensity",
                required=0,
                options=stripeintensity_options,
                min=0,
                max=5000
            ),

            NumberRange(
                name="blurriness",
                required=0,
                options=blurriness_options,
                min=0,
                max=200
            ),
  #          NumberRange(
  #              name="contrast",
  #              required=0,
  #              options=contrast_options,
  #              min=0,
  #              max=200
  #          ),
            NumberRange(
                name="brightness",
                required=0,
                options=brightness_options,
                min=0,
                max=200
            ),
            NumberRange(
                name="saturation",
                required=0,
                options=saturation_options,
                min=0,
                max=200
            ),
            NumberRange(
                name="hue",
                required=0,
                options=hue_options,
                min=0,
                max=200
            ),
            NumberRange(
                name="percentbeveled",
                required=0,
                options=percentbeveled_options,
                min=0,
                max=100
            ),
            NumberRange(
                name="rotate",
                required=0,
                options=rotate_options,
                min=0,
                max=360
            ),
            NumberRange(
                name="tilt",
                required=0,
                options=tilt_options,
                min=0,
                max=360
            ),
            MultiSelect(name="flop", required=0, options=flop_options),
            MultiSelect(name="flip", required=0, options=flip_options),
        )
