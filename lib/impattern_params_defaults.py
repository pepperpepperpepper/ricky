#!/usr/bin/python2.7
import random
from config import USERNAME, TEST_URL
from lib.utils import Pb_Api_Params
PATTERN_URL_BASE =  "http://asdf.us/impattern/patterns"
class ImPatternParams_FromDefaults(Pb_Api_Params):
    def __init__(self):
        self.weighted_pattern_url = [
            { "value":"1.png", "weight":1 },
            { "value":"2.png", "weight":1 },
        ]
    def from_random(self, url=TEST_URL):
        return {
            "image_url" : url,
            "username" : USERNAME, 
            "pattern_url" : "{}/{}".format(PATTERN_URL_BASE, self._weighted_choice( self.weighted_pattern_url )),
        }
    def from_default(self, url=TEST_URL):
        return {
            "image_url" : url,
            "username" : USERNAME, 
            "pattern_url" : "{}/{}".format(PATTERN_URL_BASE, self._default_choice( self.weighted_pattern_url )),
        }
