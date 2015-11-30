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
           Username(name="username", required=False),
           ImageUrl(name="url", required=True),
           MultiSelect(
                       name="finalformat",
                       required=False,
                       options=finalformat_options),
           MultiSelect(
                       name="breaktype",
                       required=True,
                       options=breaktype_options),
           ConstrainedNumber(
                       name="breakangle",
                       required=False,
                       min=-180,
                       max=180),
           MultiSelect(
                       name="breakmode",
                       required=True,
                       options=breakmode_options),
           Bool(name="expanded", required=False)
        ]
