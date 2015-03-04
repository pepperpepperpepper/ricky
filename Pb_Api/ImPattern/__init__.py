#!/usr/bin/python2.7
import urllib
import urllib2
import simplejson as json
import random
import sys
from lib.utils import post_request, Pb_Api

IMPATTERN_URL = "http://asdf.us/im/api/impattern"

#ok what about here?

class ImPattern(Pb_Api):
    def __init__(self):
        self.url = IMPATTERN_URL
    def params(self):
        return ImPattern_Params() 


