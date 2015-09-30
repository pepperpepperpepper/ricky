from ricky.config import TEST_URL
from ricky.param.string import String

class ImageUrl(String):
    def __init__(self, *args, **kwargs):
      super(ImageUrl, self).__init__(*args, **kwargs)
      self.default(TEST_URL)
