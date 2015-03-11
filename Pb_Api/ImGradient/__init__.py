#!/usr/bin/python2.7
from Pb_Api import Pb_Api
from Pb_Api.ImGradient.Params import ImGradient_Params
from config import IMGRADIENT_URL

class Pb_Api_ImGradient(Pb_Api):
    def __init__(self):
        self.url = IMGRADIENT_URL
    def params_init(self):
        new_params = ImGradient_Params()
        #new_params = self.get_from_server()
        new_params.api = self 
        return new_params 
