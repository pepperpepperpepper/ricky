from ricky.pb import Pb
from ricky.pbpattern.params import Params
from ricky.config import IMPATTERN_URL


class PbPattern(Pb):
    def __init__(self):
        self.url = IMPATTERN_URL

    def params_init(self):
        new_params = Params()
        new_params.api = self
        return new_params
