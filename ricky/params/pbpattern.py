from ricky.params import Params
from ricky.param.username import Username
from ricky.param.imageurl import PbageUrl
from ricky.param.enum import Enum
from ricky.config import PATTERN_URL_BASE, PBPATTERN_URL


class PbPattern(Params):
    def __init__(self):
        super(Params, self).__init__(
           Username(name="username", required=False),
           PbageUrl(name="image_url", required=True),
           Enum(
                name="pattern_url",
                required=True,
                options=self._get_pattern_urls()
           )
        )
        self._url = PBPATTERN_URL

    def _get_pattern_urls(self):
        return set(
            ["%s/img/%s.png" % (PATTERN_URL_BASE, i) for i in xrange(0, 97)] +
            ["%s/img/a%s.png" % (PATTERN_URL_BASE, i) for i in xrange(1, 42)]
        )
