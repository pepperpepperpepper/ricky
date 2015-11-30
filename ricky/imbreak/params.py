from ricky.params import Params
from ricky.param.username import Username
from ricky.param.imageurl import ImageUrl
from ricky.param.multiselect import MultiSelect
from ricky.param.constrainednumber import ConstrainedNumber
from ricky.param.bool import Bool


breaktype_options = [
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
breakmode_options = [
    "extreme",
    "subtle",
]
finalformat_options = [
    "png",
    "jpg",
    "gif",
]


class ImBreakParams(Params):
    def __init__(self):
        self._params = [
           Username(name="username", required=0),
           ImageUrl(name="url", required=1),
           MultiSelect(
                       name="finalformat",
                       required=0,
                       options=finalformat_options),
           MultiSelect(
                       name="breaktype",
                       required=1,
                       options=breaktype_options),
           ConstrainedNumber(
                       name="breakangle",
                       required=0,
                       min=-180,
                       max=180),
           MultiSelect(
                       name="breakmode",
                       required=1,
                       options=breakmode_options),
           Bool(name="expanded", required=0)
        ]
