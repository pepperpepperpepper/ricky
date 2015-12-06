from ricky.config import TEST_URL
from ricky.param.string import String


class ImageUrl(String):
    def __init__(self, *args, **kwargs):
        if 'default' not in kwargs:
            kwargs['default'] = TEST_URL
        super(ImageUrl, self).__init__(*args, **kwargs)
