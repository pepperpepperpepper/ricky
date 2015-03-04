#!/usr/bin/python2.7
import urllib
import urllib2
import simplejson as json
import random
import sys
from lib.utils import post_request, Service

IMPATTERN_URL = "http://asdf.us/im/api/impattern"



class ImGradient(Service):
    def __init__(self):
        self.url = IMPATTERN_URL
        self._required_keys = [
            "pattern_url",
            "pattern_data",
            "username",
            "image_url",
        ] 
    def new(self, params):
        for k in self._required_keys:
            if not k in params:
                params[k] = "";
        self.params = params
        return json.loads(post_request(IMPATTERN_URL, self.params))
     
