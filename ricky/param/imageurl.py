from ricky.config import TEST_URL
from ricky.param.string import String


class PbageUrl(String):
    def __init__(self, *args, **kwargs):
        if 'default' not in kwargs:
            kwargs['default'] = TEST_URL
        super(PbageUrl, self).__init__(*args, **kwargs)
