from ricky.params import Params as _Params
from ricky.param.username import Username
from ricky.param.imageurl import PbageUrl
from ricky.param.enum import Enum
from ricky.param.constrainednumber import ConstrainedNumber
from ricky.param.bool import Bool
from ricky.config import PBBREAKER_URL

_BREAKTYPE_OPTIONS = [
    "CLASSIC",
    "REDUX",
    "BLURRY_BREAK",
    "BLURRY_BREAK_2",
    "SWIPE",
    "RGB_WASH",
    "RGB_WASH_2",
    "NOISY_BREAK",
    "BROKEN_VIGNETTE",
    "FAX_MACHINE",
    "STRIPES",
    "PHOTOCOPY"
]
_BREAKMODE_OPTIONS = [
    "extreme",
    "subtle",
]
_FINALFORMAT_OPTIONS = [
    "png",
    "jpg",
    "gif",
]


class Params(_Params):
    def __init__(self):
        super(Params, self).__init__(
           Username(name="username", required=False),
           PbageUrl(name="url", required=True),
           Enum(
                       name="finalformat",
                       required=False,
                       options=_FINALFORMAT_OPTIONS),
           Enum(
                       name="breaktype",
                       required=True,
                       options=_BREAKTYPE_OPTIONS),
           ConstrainedNumber(
                       name="breakangle",
                       required=False,
                       enforce_int=True,
                       min=-180,
                       max=180),
           Enum(
                       name="breakmode",
                       required=True,
                       options=_BREAKMODE_OPTIONS),
           Bool(name="expanded", required=False)
        )
        self._url = PBBREAKER_URL
