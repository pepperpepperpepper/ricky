#!/usr/bin/python2.7
from Pb_Api import Pb_Api
from Pb_Api.ImPattern.Params import ImPattern_Params

IMPATTERN_URL = "http://asdf.us/im/api/impattern"

class Pb_Api_ImPattern(Pb_Api):
    def __init__(self):
        self.url = IMPATTERN_URL
    def params(self):
        return ImPattern_Params() 
