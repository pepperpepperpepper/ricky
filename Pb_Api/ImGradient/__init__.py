#!/usr/bin/python2.7
import urllib
import urllib2
import simplejson as json
import random
import sys
from lib.utils import post_request, Pb_Api


IMGRADIENT_URL = "http://asdf.us/im/api/imgradient"
#from Api.ImGradient.Api import * 

class ImGradientApi(Pb_Api):
    def __init__(self):
        self.url = IMGRADIENT_URL
        self._required_keys = [
            "width", "height", 
            "color1", "color2", 
            "stripes",
            "stripenumber", "stripeintensity", 
            "blurriness", 
            "contrast", 
            "brightness", "saturation", "hue",
            "halftone", 
            "bevel", "percentbeveled",
            "rotate", "flip", "flop", "tilt", 
            "filetype",
            "gradienttype", 
            "username",
        ] 
