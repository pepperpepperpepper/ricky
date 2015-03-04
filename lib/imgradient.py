#!/usr/bin/python2.7
import urllib
import urllib2
import simplejson as json
import random
import sys
from lib.utils import post_request, Service

IMGRADIENT_URL = "http://asdf.us/im/api/imgradient"



class ImGradient(Service):
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
    def new(self, params):
        for k in self._required_keys:
            if not k in params:
                params[k] = "";
        self.params = params
        return json.loads(post_request(IMGRADIENT_URL, self.params))
     
