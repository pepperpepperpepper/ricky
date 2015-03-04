#!/usr/bin/python2.7
import urllib
import urllib2
import simplejson as json
import random
import sys
from lib.utils import post_request

IMGRID_URL = "http://asdf.us/im/api/imgrid"

class ImGrid():
    def __init__(self):
        self._required_keys = [
            "width",
            "height",
            "linethickness",
            "opacity",
            "linecolor",
            "spacing",
            "vlines",
            "hlines",
            "shadow",
            "bgimage",
            "bgcolor",
            "imageinstead",
            "planebgcolor",
            "planebgimage",
            "swing",
            "tilt",
            "roll",
            "zoom",
            "skycolor",
            "transition",
            "trim",
            "format",
            "username"
        ] 
    def new(self, params):
        for k in self._required_keys:
            if not k in params:
                params[k] = "";
        self.params = params
        return json.loads(post_request(IMGRID_URL, self.params))
     
