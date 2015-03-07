#!/usr/bin/python2.7
from Pb_Api import Pb_Api
from Pb_Api.ImPattern.Params import ImGrid_params
from config import IMGRID_URL

class Pb_Api_ImPattern(Pb_Api):
    def __init__(self):
        self.url = IMGRID_URL
    def request_new(self):
        new_params = ImGrid_Params()
        #new_params = self.get_from_server()
        new_params.api = self 
        return new_params 
