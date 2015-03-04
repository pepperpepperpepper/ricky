#!/usr/bin/python2.7
import random
from config import USERNAME, TEST_URL
from lib.utils import Pb_Api_Params

class ImBreakParams_FromDefaults(Pb_Api_Params):
    def __init__(self):
        self.weighted_breaktype = [
            {"value":"CLASSIC",         "weight": 1},
            {"value":"REDUX",           "weight": 1},
            {"value":"BLURRY_BREAK",    "weight": 1},
            {"value":"BLURRY_BREAK_2",  "weight": 1},
            {"value":"SWIPE",           "weight": 1},
            {"value":"RGB_WASH",        "weight": 1},
            {"value":"RGB_WASH_2",      "weight": 1},
            {"value":"NOISY_BREAK",     "weight": 1},
            {"value":"BROKEN_VIGNETTE", "weight": 1},
            {"value":"FAX_MACHINE",     "weight": 1},
            {"value":"STRIPES",         "weight": 1},
            {"value":"PHOTOCOPY",       "weight": 1}, 
        ]
        self.weighted_breakmode = [
            {"value":"extreme",  "weight": 1},
            {"value":"subtle",  "weight": 1},
        ]
        self.weighted_finalformat = [
            {"value":"png",  "weight": 5},
            {"value":"jpg",  "weight": 2},
            {"value":"gif",  "weight": 2},
        ]
        self.weighted_breakangle = [
            {"value":0,  "weight": 9},
            {"value":90,  "weight": 2},
            {"value":180,  "weight": 2},
            {"value":270,  "weight": 2},
            {"value":random.randint(0,360),  "weight": 4},
        ]
        self.weighted_expanded = [
            {"value": "" , "weight": 11 },
            {"value": 1, "weight": 2}
        ] 
    def from_random(self, url=TEST_URL):
        return {
            "url" : url,
            "username" : USERNAME, 
            "breakmode" : self._weighted_choice( self.weighted_breakmode ),
            "breaktype" : self._weighted_choice( self.weighted_breaktype ),
            "breakangle" : self._weighted_choice( self.weighted_breakangle ),
            "finalformat" : self._weighted_choice( self.weighted_finalformat ),
            "expanded" : self._weighted_choice( self.weighted_expanded ),
        }
    def from_default(self, url=TEST_URL):
        return {
            "url" : url,
            "username" : USERNAME, 
            "breakmode" : self._default_choice( self.default.breakmode ),
            "breaktype" : self._default_choice( self.default.breaktype ),
            "breakangle" : self._default_choice( self.default.breakangle ),
            "finalformat" : self._default_choice( self.default.finalformat ),
            "expanded" : self._default_choice( self.default.expanded ),
        } 
