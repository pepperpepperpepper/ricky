from ricky.api import Api
from ricky.imgrid.params import ImGridParams
from ricky.config import IMGRID_URL

class ImGrid(Api):
    def __init__(self):
        self.url = IMGRID_URL
    def params_init(self):
        new_params = ImGridParams()
        #new_params = self.get_from_server()
        new_params.api = self
        return new_params
