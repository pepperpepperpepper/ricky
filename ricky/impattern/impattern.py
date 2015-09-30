from ricky.api import Api
from ricky.impattern.params import ImPatternParams
from ricky.config import IMPATTERN_URL

class ImPattern(Api):
    def __init__(self):
        self.url = IMPATTERN_URL
    def params_init(self):
        new_params = ImPatternParams()
        #new_params = self.get_from_server()
        new_params.api = self
        return new_params
