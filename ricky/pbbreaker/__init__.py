from ricky.pb import Pb
from ricky.pbbreaker.params import Params


class PbBreaker(Pb):
    def __init__(self):
        super(PbBreaker, self).__init__()

    def params_init(self):
        new_params = Params()
        new_params.api = self
        return new_params
