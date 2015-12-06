from ricky.im import Im
from ricky.imgrid.params import Params
from ricky.config import IMGRID_URL


class ImGrid(Im):
    def __init__(self):
        self.url = IMGRID_URL

    def params_init(self):
        new_params = Params()
        # new_params = self.get_from_server()
        new_params.api = self
        return new_params
