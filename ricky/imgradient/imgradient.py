from ricky.api import Api
from ricky.imgradient.params import ImGradientParams
from ricky.config import IMGRADIENT_URL

class ImGradient(Api):
    def __init__(self):
        self.url = IMGRADIENT_URL
    def params_init(self):
        new_params = ImGradientParams()
        #new_params = self.get_from_server()
        new_params.api = self
        return new_params
