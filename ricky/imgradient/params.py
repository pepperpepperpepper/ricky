from ricky.params import Params as _Params
from ricky.param.username import Username
from ricky.param.multiselect import MultiSelect
from ricky.param.constrainednumber import ConstrainedNumber
from ricky.param.bool import Bool
from ricky.param.color import Color


_HALFTONE_OPTIONS = [
    "",
    "checkeredfade",
    "etchedtransition",
    "bendaydots",
    "smallerdots1",
    "smallerdots2",
    "flatstripes",
]

_BEVEL_OPTIONS = [
    "",
    "flatout",
    "flatinner",
    "evenlyframed",
    "biginner",
    "bigouter",
    "dramaticflatout",
    "dramaticflatinner",
]

_FILETYPE_OPTIONS = [
    "png",
    "jpg",
    "gif",
]

_GRADIENTTYPE_OPTIONS = [
    "canvas",
    "gradient",
    "radial",
    "colorspace",
    "plasmawash",
    "gradientwash",
    "mirrored",
    "noise",
]


class Params(_Params):
    def __init__(self):
        super(Params, self).__init__(
            Username(name="username", required=0),
            ConstrainedNumber(
                name="width",
                required=1,
                min=10,
                max=800
            ),
            ConstrainedNumber(
                name="height",
                required=1,
                min=10,
                max=800
            ),
            Color(name="color1", required=1),
            Color(name="color2", required=1),
            MultiSelect(
                name="filetype",
                required=0,
            ),
            MultiSelect(
                name="gradienttype",
                required=1,
                options=_GRADIENTTYPE_OPTIONS
            ),
            MultiSelect(
                name="halftone",
                required=0,
                options=_HALFTONE_OPTIONS
            ),
            MultiSelect(
                name="bevel",
                required=0,
                options=_BEVEL_OPTIONS
            ),
            ConstrainedNumber(
                name="stripenumber",
                required=0,
                min=0,
                max=400
            ),
            ConstrainedNumber(
                name="stripeintensity",
                required=0,
                min=0,
                max=5000
            ),

            ConstrainedNumber(
                name="blurriness",
                required=0,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="contrast",
                required=0,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="brightness",
                required=0,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="saturation",
                required=0,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="hue",
                required=0,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="percentbeveled",
                required=0,
                min=0,
                max=100
            ),
            ConstrainedNumber(
                name="rotate",
                required=0,
                min=0,
                max=360
            ),
            ConstrainedNumber(
                name="tilt",
                required=0,
                min=0,
                max=360
            ),
            Bool(
                name="flop",
                required=0,
            ),
            Bool(
                name="flip",
                required=0
            ),
        )
