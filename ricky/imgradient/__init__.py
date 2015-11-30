"""class for the imgradient api handler"""
from ricky.im import Im
from ricky.imgradient.params import Params
from ricky.config import IMGRADIENT_URL


class ImGradient(Im):
    def __init__(self):
        super(ImGradient, self).__init__()
        self.url = IMGRADIENT_URL

    def params_init(self):
        new_params = Params()
        new_params.api = self
        return new_params
