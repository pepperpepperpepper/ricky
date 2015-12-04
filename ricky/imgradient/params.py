from ricky.params import Params as _Params
from ricky.param.username import Username
from ricky.param.enum import Enum
from ricky.param.constrainednumber import ConstrainedNumber
from ricky.param.bool import Bool
from ricky.param.color import Color


_HALFTONE_OPTIONS = (
    "",
    "checkeredfade",
    "etchedtransition",
    "bendaydots",
    "smallerdots1",
    "smallerdots2",
    "flatstripes",
)

_BEVEL_OPTIONS = (
    "",
    "flatout",
    "flatinner",
    "evenlyframed",
    "biginner",
    "bigouter",
    "dramaticflatout",
    "dramaticflatinner",
)

_FILETYPE_OPTIONS = (
    "png",
    "jpg",
    "gif",
)

_GRADIENTTYPE_OPTIONS = (
    "canvas",
    "gradient",
    "radial",
    "colorspace",
    "plasmawash",
    "gradientwash",
    "mirrored",
    "noise",
)


class Params(_Params):
    def __init__(self):
        super(Params, self).__init__(
            Username(name="username", required=False),
            ConstrainedNumber(
                name="width",
                required=True,
                min=10,
                max=800
            ),
            ConstrainedNumber(
                name="height",
                required=True,
                min=10,
                max=800
            ),
            Color(name="color1", required=True),
            Color(name="color2", required=True),
            Enum(
                name="filetype",
                required=False,
            ),
            Enum(
                name="gradienttype",
                required=True,
                options=_GRADIENTTYPE_OPTIONS
            ),
            Enum(
                name="halftone",
                required=False,
                options=_HALFTONE_OPTIONS
            ),
            Enum(
                name="bevel",
                required=False,
                options=_BEVEL_OPTIONS
            ),
            ConstrainedNumber(
                name="stripenumber",
                required=False,
                min=0,
                max=400
            ),
            ConstrainedNumber(
                name="stripeintensity",
                required=False,
                min=0,
                max=5000
            ),
            ConstrainedNumber(
                name="blurriness",
                required=False,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="contrast",
                required=False,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="brightness",
                required=False,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="saturation",
                required=False,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="hue",
                required=False,
                min=0,
                max=200
            ),
            ConstrainedNumber(
                name="percentbeveled",
                required=False,
                min=0,
                max=100
            ),
            ConstrainedNumber(
                name="rotate",
                required=False,
                min=0,
                max=360
            ),
            ConstrainedNumber(
                name="tilt",
                required=False,
                min=0,
                max=360
            ),
            Bool(
                name="flop",
                required=False,
            ),
            Bool(
                name="flip",
                required=False
            )
        )
