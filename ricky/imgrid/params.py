from ricky.params import Params as _Params
from ricky.param.username import Username
from ricky.param.imageurl import ImageUrl
from ricky.param.enum import Enum
from ricky.param.constrainednumber import ConstrainedNumber
from ricky.param.color import Color
from ricky.param.bool import Bool

_TRANSITION_OPTIONS = [
    "background",
    "dither",
    "random",
    "tile",
    "edge"
]

_FILETYPE_OPTIONS = [
    "png",
    "jpg",
    "gif",
]


class Params(_Params):
    def __init__(self):
        self._params = (
           Username(name="username", required=False),
           ImageUrl(name="bgimage", required=False),
           ImageUrl(name="imageinstead", required=False),
           ImageUrl(name="planebgimage", required=False),
           Enum(
               name="format",
               required=False,
               options=_FILETYPE_OPTIONS
           ),
           Enum(
               name="transition",
               required=True,
               options=_TRANSITION_OPTIONS
           ),
           Color(name="skycolor", required=False),
           Color(name="planebgcolor", required=False),
           Color(name="bgcolor", required=False),
           Color(name="linecolor", required=False),
           ConstrainedNumber(
               name="swing",
               required=False,
               enforce_int=True,
               min=-170,
               max=170),
           ConstrainedNumber(
               name="tilt",
               required=False,
               enforce_int=True,
               min=-170,
               max=170),
           ConstrainedNumber(
               name="roll",
               required=False,
               enforce_int=True,
               min=-170,
               max=170),
           ConstrainedNumber(
               name="width",
               required=False,
               enforce_int=True,
               min=100,
               max=800),
           ConstrainedNumber(
               name="height",
               required=False,
               enforce_int=True,
               min=100,
               max=800),
           ConstrainedNumber(
               name="linethickness",
               required=False,
               enforce_int=True,
               min=1,
               max=30
           ),
           ConstrainedNumber(
               name="opacity", required=False, min=0, max=1, prec=2),
           ConstrainedNumber(
               name="spacing",
               enforce_int=True,
               required=False,
               min=2,
               max=100),
           Bool(name="vlines", required=False),
           Bool(name="hlines", required=False),
           Bool(name="trim", required=False),
           Bool(name="shadow", required=False),
           ConstrainedNumber(
               name="zoom",
               required=False,
               min=-12,
               max=12,
               forbidden_range_min=-1.1,
               forbidden_range_max=1.1,
               prec=1
           )
        )

    def _test_values(self):
        return not any([
          (self.__getitem__('spacing').value >
              self.__getitem__('width').value),
          (self.__getitem__('spacing').value >
              self.__getitem__('height').value),
          (self.__getitem__('linethickness').value >
              self.__getitem__('width').value),
          (self.__getitem__('linethickness').value >
              self.__getitem__('height').value),
        ])

    def randomize(self):
        p = self._params
        for el in p:
            if el in ['spacing', 'linethickness']:
                continue
            el.randomize()
        for name in ['spacing', 'linethickness']:
            max_tries = 10000
            while(max_tries):
                self.__getitem__(name).randomize()
                if self._test_values():
                    return
                max_tries -= 1
            raise ValueError
