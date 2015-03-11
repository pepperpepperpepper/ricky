#!/usr/bin/python2.7
from Pb_Api import Pb_Api
from Pb_Api.ImGrid.Params import ImGrid_Params
from config import IMGRID_URL

class Pb_Api_ImGrid(Pb_Api):
    def __init__(self):
        self.url = IMGRID_URL
    def params_init(self):
        new_params = ImGrid_Params()
        #new_params = self.get_from_server()
        new_params.api = self 
        return new_params 
