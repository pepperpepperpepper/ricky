import re
from ricky.params import Params as _Params
from ricky.param.username import Username
from ricky.param.multiselect import MultiSelect
from ricky.param.numberrange import NumberRange
from ricky.param.color import Color
from ricky.imgradient.selections import *


class Params(_Params):
    def __init__(self):
        super(Params, self).__init__(
            Username(name="username", required=0),
            NumberRange(
                name="width",
                required=1,
                selections=width_selections,
                min=10,
                max=800
            ),
            NumberRange(
                name="height",
                required=1,
                selections=height_selections,
                min=10,
                max=800
            ),
            Color(name="color1", required=1, selections=color1_selections),
            Color(name="color2", required=1, selections=color2_selections),
            MultiSelect(
                name="filetype",
                required=0,
                selections=filetype_selections
            ),
            MultiSelect(
                name="gradienttype",
                required=1,
                selections=gradienttype_selections
            ),
            MultiSelect(
                name="halftone",
                required=0,
                selections=halftone_selections
            ),
            MultiSelect(name="bevel", required=0, selections=bevel_selections),

            NumberRange(
                name="stripenumber",
                required=0,
                selections=stripenumber_selections,
                min=0,
                max=400
            ),
            NumberRange(
                name="stripeintensity",
                required=0,
                selections=stripeintensity_selections,
                min=0,
                max=5000
            ),

            NumberRange(
                name="blurriness",
                required=0,
                selections=blurriness_selections,
                min=0,
                max=200
            ),
  #          NumberRange(
  #              name="contrast",
  #              required=0,
  #              selections=contrast_selections,
  #              min=0,
  #              max=200
  #          ),
            NumberRange(
                name="brightness",
                required=0,
                selections=brightness_selections,
                min=0,
                max=200
            ),
            NumberRange(
                name="saturation",
                required=0,
                selections=saturation_selections,
                min=0,
                max=200
            ),
            NumberRange(
                name="hue",
                required=0,
                selections=hue_selections,
                min=0,
                max=200
            ),
            NumberRange(
                name="percentbeveled",
                required=0,
                selections=percentbeveled_selections,
                min=0,
                max=100
            ),
            NumberRange(
                name="rotate",
                required=0,
                selections=rotate_selections,
                min=0,
                max=360
            ),
            NumberRange(
                name="tilt",
                required=0,
                selections=tilt_selections,
                min=0,
                max=360
            ),
            MultiSelect(name="flop", required=0, selections=flop_selections),
            MultiSelect(name="flip", required=0, selections=flip_selections),
        )
