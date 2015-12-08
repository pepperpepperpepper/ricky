from ricky.pb import Pb
from ricky.pbpattern.params import Params


class PbPattern(Pb):
    def __init__(self):
        pass

    def params_init(self):
        new_params = Params()
        new_params.api = self
        return new_params
