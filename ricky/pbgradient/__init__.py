"""class for the imgradient api handler"""
from ricky.pb import Pb
from ricky.pbgradient.params import Params
from ricky.config import IMGRADIENT_URL


class PbGradient(Pb):
    def __init__(self):
        super(PbGradient, self).__init__()
        self.url = IMGRADIENT_URL

    def params_init(self):
        new_params = Params()
        new_params.api = self
        return new_params
