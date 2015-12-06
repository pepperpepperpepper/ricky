from ricky.im import Im
from ricky.impattern.params import Params
from ricky.config import IMPATTERN_URL


class ImPattern(Im):
    def __init__(self):
        self.url = IMPATTERN_URL

    def params_init(self):
        new_params = Params()
        # new_params = self.get_from_server()
        new_params.api = self
        return new_params
