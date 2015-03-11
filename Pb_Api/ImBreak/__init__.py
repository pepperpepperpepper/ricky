#!/usr/bin/python2.7
from Pb_Api import Pb_Api
from Pb_Api.ImBreak.Params import ImBreak_Params
from config import IMBREAK_URL

class Pb_Api_ImBreak(Pb_Api):
    def __init__(self):
        self.url = IMBREAK_URL
    def params_init(self):
        new_params = ImBreak_Params()
        #new_params = self.get_from_server()
        new_params.api = self 
        return new_params 
