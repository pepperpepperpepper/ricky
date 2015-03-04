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
        ]
        self.weighted_stripes = [
            {"value":"true",  "weight": 1},
            {"value":"false",  "weight": 1},
        ]
        self.weighted_stripenumber = [
            {"value":1,  "weight": 1},
            {"value":2,  "weight": 1},
            {"value":random.randint(0,400),  "weight": 1},
        ]
        self.weighted_stripeintensity = [
            {"value": "",  "weight": 3},
            {"value": random.randint(0,2000),  "weight": 1},
        ]
        self.weighted_blurriness = [
            {"value": "",  "weight": 3},
            {"value": random.randint(0,20),   "weight": 1},
        ]
        self.weighted_contrast = [
            {"value": "",  "weight": 3},
            {"value": random.randint(0,20),   "weight": 1},
        ]
        self.weighted_brightness = [
            {"value": "",  "weight": 3},
            {"value": random.randint(0,200),  "weight": 1},
        ]
        self.weighted_saturation = [
            {"value": "",  "weight": 3},
            {"value": random.randint(0,200),  "weight": 1},
        ]
        self.weighted_hue = [
            {"value": "",  "weight": 3},
            {"value": random.randint(0,200),  "weight": 1},
        ]
        self.weighted_halftone = [
            { "value" : "checkeredfade", "weight": 1 },
            { "value" : "etchedtransition", "weight": 1 },
            { "value" : "bendaydots", "weight": 1 },
            { "value" : "smallerdots1", "weight": 1 },
            { "value" : "smallerdots2", "weight": 1 },
            { "value" : "flatstripes", "weight": 1 },
        ]
        self.weighted_bevel = [
            { "value" : "", "weight" : 4 }, 
            { "value" : "flatout", "weight" : 1 }, 
            { "value" : "flatinner", "weight" : 1 }, 
            { "value" : "evenlyframed", "weight" : 1 }, 
            { "value" : "biginner", "weight" : 1 }, 
            { "value" : "bigouter", "weight" : 1 }, 
            { "value" : "dramaticflatout", "weight" : 1 }, 
            { "value" : "dramaticflatinner", "weight" : 1 }, 
        ]
        self.weighted_percentbeveled = [
            { "value" : random.randint(0,99),  "weight": 1 },
            { "value" : "",  "weight": 4 },
        ]
        self.weighted_rotate = [
            {"value":"",    "weight": 9},
            {"value":90,   "weight": 2},
            {"value":180,  "weight": 2},
            {"value":270,  "weight": 2},
            {"value":random.randint(0,360),  "weight": 4},
        ]
        self.weighted_flop = [
            {"value":"",  "weight": 1},
            {"value":"true",   "weight": 1},
        ]
        self.weighted_flip = [
            {"value":"",  "weight": 1},
            {"value":"true",   "weight": 1},
        ]
        self.weighted_tilt = [
            {"value":"",    "weight": 9},
            {"value":90,   "weight": 2},
            {"value":180,  "weight": 2},
            {"value":270,  "weight": 2},
            {"value":random.randint(0,360),  "weight": 4},
        ]
        self.weighted_filetype = [
            {"value":"png",  "weight": 5},
            {"value":"jpg",  "weight": 2},
            {"value":"gif",  "weight": 2},
        ]
        self.weighted_gradienttype = [
            { "value" : "canvas", "weight" : 1 }, 
            { "value" : "gradient", "weight" : 3 }, 
            { "value" : "radial", "weight" : 1 }, 
            { "value" : "colorspace", "weight" : 1 }, 
            { "value" : "plasmawash", "weight" : 1 }, 
            { "value" : "gradientwash", "weight" : 1 }, 
            { "value" : "mirrored", "weight" : 1 }, 
            { "value" : "noise", "weight" : 1 }, 
        ]

#I just needed a place to encapsulate the params and the weights, and methods to access them. I guess I didn't really know the right answer
#as far as the structure, so I tried to just imagine something somewhat related to what you were talking about before.
#do I need separate classes for the two methods below?
#well lets dicusss this a bit more, so services each have own param set, they are sort of original from service itself, so i guess there should be a way to get
#"fresh" copy of parameters accepted by this service, instead of rewriting code each time. do you mean just a list of the keynames? yeah and thier values
#the keys don't have default values necessarily. they just each have a range of accepted values. Basically just html forms hmm sort of like
#writing a bot that fills in some forms on the internet, like a bot to brute force a credit card form or something, funny example, but I guess a good one
#each parameter has values that are within an accepted range, like First Name would need to come from a list of frist names, and CC number would need to bevel
#intelligible ints, the first four should correspond with a known bank, etc. you understand what I mean? yeah
ok so since all services are about same, just a bunch of parameters and known values we can make base class for parameteres. it would look like:


class ApiParams(object):
   def params():
   def randomize():
   def build():

class ImGradientParams(ApiParams):
   def __init__():
     self.params = {
       "width": # well here it's int i suppose, need somethig esle
       "gradienttype": [
         { "value "...}
       ]
     }
   
class ImGradientPb_Api():
   def params():
    return new ImGradientParams()
   def call(params):
    return image();


api = ImGradientPb_Api()
image_params = api.params()
image_params.gradient_type("mirror")
image_params.randomize()
image = api.call(image _params)
# something like this, yeah I think so...lol I tried to do something like this


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
