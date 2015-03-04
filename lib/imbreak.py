#!/usr/bin/python2.7
import urllib
import urllib2
import simplejson as json
import random
import sys
from lib.utils import post_request

IMBREAK_URL = "http://asdf.us/im/api/imbreak"

class ImBreak():
    def __init__(self):
        self._required_keys = [
            "url",
            "breaktype",
            "finalformat",
            "breakmode",
            "breakangle",
            "username",
            "expanded"
        ] 
    def new(self, params):
        for k in self._required_keys:
            if not k in params:
                params[k] = "";
        self.params = params
        return json.loads(post_request(IMBREAK_URL, self.params))
     
