"""class for the imgradient api handler"""
from ricky.pb import Pb
from ricky.pbgradient.params import Params


class PbGradient(Pb):
    def __init__(self):
        super(PbGradient, self).__init__()

    def params_init(self):
        new_params = Params()
        new_params.api = self
        return new_params
