from ricky.pb import Pb
from ricky.pbbreaker.params import Params
from ricky.config import IMBREAK_URL


class PbBreaker(Pb):
    def __init__(self):
        super(PbBreaker, self).__init__()
        self.url = IMBREAK_URL

    def params_init(self):
        new_params = Params()
        # new_params = self.get_from_server()
        new_params.api = self
        return new_params
