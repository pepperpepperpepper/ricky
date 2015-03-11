#!/usr/bin/python2.7
from Pb_Api import Pb_Api
from Pb_Api.ImPattern.Params import ImPattern_Params
from config import IMPATTERN_URL

class Pb_Api_ImPattern(Pb_Api):
    def __init__(self):
        self.url = IMPATTERN_URL
    def params_init(self):
        new_params = ImPattern_Params()
        #new_params = self.get_from_server()
        new_params.api = self 
        return new_params 
