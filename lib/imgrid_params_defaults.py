#!/usr/bin/python2.7
import random
from config import USERNAME, TEST_URL
from lib.utils import Pb_Api_Params


class ImGridParams_FromDefaults(Pb_Api_Params):
    def __init__(self):
        self.weighted_width = [
            { "value" : 400, "weight" : 1 }, 
            { "value" : 600, "weight" : 1 }, 
        ]
        self.weighted_height = [
            { "value" : 400, "weight" : 1 }, 
            { "value" : 600, "weight" : 1 }, 
        ]
        self.weighted_colors = [
            { "value" : 
                "rgb({},{},{})".format(
                     random.randint(0,255),
                     random.randint(0,255),
                     random.randint(0,255),
                ),
                "weight" : 1 }, 
            { "value" : "black", "weight" : 1 }, 
            { "value" : "white", "weight" : 1 }, 
            { "value" : "silver", "weight" : 1 }, 
        ]
        self.weighted_linethickness = [
            {"value":1,  "weight": 2},
            {"value":2,  "weight": 1},
            {"value":random.randint(1,100),  "weight": 1},
            {"value":random.randint(1,200),  "weight": 1},
        ]
        self.weighted_opacity = [
            {"value":1,  "weight": 2},
            {"value":0.5,  "weight": 1},
            {"value":float(random.randint(0,10)/10.0),  "weight": 1},
        ]
        self.weighted_spacing = [
            {"value":10,  "weight": 1},
            {"value":random.randint(10,400),  "weight": 1},
            {"value":random.randint(10,100),  "weight": 1},
        ]
        self.weighted_vlines = [
            {"value":"",  "weight": 1},
            {"value":"true",   "weight": 1},
        ]
        self.weighted_hlines = [
            {"value":"",  "weight": 1},
            {"value":"true",   "weight": 1},
        ]
        self.weighted_shadow = [
            {"value":"",  "weight": 1},
            {"value":"true",   "weight": 1},
        ]
        self.weighted_stripeintensity = [
            {"value": "",  "weight": 3},
            {"value": random.randint(0,2000),  "weight": 1},
        ]
        self.weighted_swing = [
            {"value": "",  "weight": 3},
            {"value": random.randint(-180,180),   "weight": 1},
        ]
        self.weighted_tilt = [
            {"value": "",  "weight": 3},
            {"value": random.randint(-180,180),   "weight": 1},
        ]
        self.weighted_roll = [
            {"value": "",  "weight": 3},
            {"value": random.randint(-180,180),   "weight": 1},
        ]
        self.weighted_zoom = [
            {"value": 0,  "weight": 3},
            {"value": float(random.randint(1,12)/2.0),   "weight": 1},
            {"value": float(random.randint(-12,-1)/2.0),   "weight": 1},
        ]
        self.weighted_trim = [
            {"value":"",  "weight": 1},
            {"value":"true",   "weight": 1},
        ]
        self.weighted_transition = [
            { "value" : "background", "weight": 1 },
            { "value" : "dither", "weight": 1 },
            { "value" : "random", "weight": 1 },
            { "value" : "tile", "weight": 1 },
            { "value" : "edge", "weight": 1 },
        ]
        self.weighted_format = [
            {"value":"png",  "weight": 5},
            {"value":"jpg",  "weight": 2},
            {"value":"gif",  "weight": 2},
        ]
    def from_random(self, imageinstead="", bgimage="", planebgimage=""):
        return {
            "username" : USERNAME, 
            "width" : self._weighted_choice( self.weighted_width ),
            "height" : self._weighted_choice( self.weighted_height ),

            "skycolor" : self._weighted_choice( self.weighted_colors ),
            "planebgcolor" : self._weighted_choice( self.weighted_colors ),
            "bgcolor" : self._weighted_choice( self.weighted_colors ),
            "linecolor" : self._weighted_choice( self.weighted_colors ),

            "bgimage" : bgimage,
            "imageinstead" : imageinstead,
            "planebgimage" : planebgimage,

            "linethickness" : self._weighted_choice( self.weighted_linethickness ),
            "opacity" : self._weighted_choice( self.weighted_opacity ),
            "spacing" : self._weighted_choice( self.weighted_spacing ),
            "vlines" : self._weighted_choice( self.weighted_vlines ),
            "hlines" : self._weighted_choice( self.weighted_hlines ),
            "shadow" : self._weighted_choice( self.weighted_shadow ),

            "swing" : self._weighted_choice( self.weighted_swing ),
            "tilt" : self._weighted_choice( self.weighted_tilt ),
            "roll" : self._weighted_choice( self.weighted_roll ),
            "zoom" : self._weighted_choice( self.weighted_zoom ),
            "transition" : self._weighted_choice( self.weighted_transition ),
            "trim" : self._weighted_choice( self.weighted_trim ),
            "format" : self._weighted_choice( self.weighted_format ),
        }
    def from_default(self, imageinstead="", bgimage="", planebgimage=""):
        return {
            "username" : USERNAME, 
            "width" : self._default_choice( self.weighted_width ),
            "height" : self._default_choice( self.weighted_height ),

            "skycolor" : self._default_choice( self.weighted_colors ),
            "planebgcolor" : self._default_choice( self.weighted_colors ),
            "bgcolor" : self._default_choice( self.weighted_colors ),
            "linecolor" : self._default_choice( self.weighted_colors ),

            "bgimage" : bgimage,
            "imageinstead" : imageinstead,
            "planebgimage" : planebgimage,

            "linethickness" : self._default_choice( self.weighted_linethickness ),
            "opacity" : self._default_choice( self.weighted_opacity ),
            "spacing" : self._default_choice( self.weighted_spacing ),
            "vlines" : self._default_choice( self.weighted_vlines ),
            "hlines" : self._default_choice( self.weighted_hlines ),
            "shadow" : self._default_choice( self.weighted_shadow ),

            "swing" : self._default_choice( self.weighted_swing ),
            "tilt" : self._default_choice( self.weighted_tilt ),
            "roll" : self._default_choice( self.weighted_roll ),
            "zoom" : self._default_choice( self.weighted_zoom ),
            "transition" : self._default_choice( self.weighted_transition ),
            "trim" : self._default_choice( self.weighted_trim ),
            "format" : self._default_choice( self.weighted_format ),
        }
