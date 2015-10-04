from ricky.api import Im
from ricky.imbreak.params import ImBreakParams
from ricky.config import IMBREAK_URL

class ImBreak(Im):
    def __init__(self):
        self.url = IMBREAK_URL
    def params_init(self):
        new_params = ImBreakParams()
        #new_params = self.get_from_server()
        new_params.api = self
        return new_params
