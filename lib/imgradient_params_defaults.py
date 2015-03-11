#!/usr/bin/python2.7
import random
from config import USERNAME, TEST_URL
from lib.utils import Pb_Api_Params

#            "width", "height", 
#            "color1", "color2", 
#            "stripes",
#            "stripenumber", "stripeintensity", 
#            "blurriness", 
#            "contrast", 
#            "brightness", "saturation", "hue",
#            "halftone", 
#            "bevel", "percentbeveled",
#            "rotate", "flip", "flop", "tilt", 
#            "filetype",
#            "gradienttype", 
#            "username",

class ImGradientParams_FromDefaults(Pb_Api_Params):
    def __init__(self):



    def from_random(self):
        return {
            "username" : USERNAME, 
            "width" : self._weighted_choice( self.weighted_width ),
            "height" : self._weighted_choice( self.weighted_height ),
            "color1" : self._weighted_choice( self.weighted_colors ),
            "color2" : self._weighted_choice( self.weighted_colors ),
            "stripenumber" : self._weighted_choice( self.weighted_stripenumber ),
            "stripeintensity" : self._weighted_choice( self.weighted_stripeintensity ),
            "blurriness" : self._weighted_choice( self.weighted_blurriness ),
            "contrast" : self._weighted_choice( self.weighted_contrast ),
            "brightness" : self._weighted_choice( self.weighted_brightness ),
            "saturation" : self._weighted_choice( self.weighted_saturation ),
            "hue" : self._weighted_choice( self.weighted_hue ),
            "halftone" : self._weighted_choice( self.weighted_halftone ),
            "bevel" : self._weighted_choice( self.weighted_bevel ),
            "percentbeveled" : self._weighted_choice( self.weighted_percentbeveled ),
            "rotate" : self._weighted_choice( self.weighted_rotate ),
            "flip" : self._weighted_choice( self.weighted_flip ),
            "flop" : self._weighted_choice( self.weighted_flop ),
            "tilt" : self._weighted_choice( self.weighted_tilt ),
            "filetype" : self._weighted_choice( self.weighted_filetype ),
            "gradienttype" : self._weighted_choice( self.weighted_gradienttype ),
        }
    def from_default(self):
        return {
            "url" : url,
            "username" : USERNAME, 
            "width" : self._default_choice( self.weighted_width ),
            "height" : self._default_choice( self.weighted_height ),
            "color1" : self._default_choice( self.weighted_colors ),
            "color2" : self._default_choice( self.weighted_colors ),
            "stripenumber" : self._default_choice( self.weighted_stripenumber ),
            "stripeintensity" : self._default_choice( self.weighted_stripeintensity ),
            "blurriness" : self._default_choice( self.weighted_blurriness ),
            "contrast" : self._default_choice( self.weighted_contrast ),
            "brightness" : self._default_choice( self.weighted_brightness ),
            "saturation" : self._default_choice( self.weighted_saturation ),
            "hue" : self._default_choice( self.weighted_hue ),
            "halftone" : self._default_choice( self.weighted_halftone ),
            "bevel" : self._default_choice( self.weighted_bevel ),
            "percentbeveled" : self._default_choice( self.weighted_percentbeveled ),
            "rotate" : self._default_choice( self.weighted_rotate ),
            "flip" : self._default_choice( self.weighted_flip ),
            "flop" : self._default_choice( self.weighted_flop ),
            "tilt" : self._default_choice( self.weighted_tilt ),
            "filetype" : self._default_choice( self.weighted_filetype ),
            "gradienttype" : self._default_choice( self.weighted_gradienttype ),
        } 
