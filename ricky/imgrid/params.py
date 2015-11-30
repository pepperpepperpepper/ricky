import random
from ricky.params import Params
from ricky.param.username import Username
from ricky.param.imageurl import ImageUrl
from ricky.param.multiselect import MultiSelect
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


class Param_Zoom(ConstrainedNumber):
    def __init__(self, **kwargs):
        super(Param_Zoom, self).__init__(**kwargs)
        self.exclusion_range = kwargs['exclusion_range']

    def test_value(self):
        return not (
            (self.value > self.exclusion_range[0]) and
            (self.value < self.exclusion_range[1])
        )

    def randomize(self):
        weights_total = sum(
            map(lambda x: x["weight"], self.probabilities())
        ) + 10
        choice = random.randint(0, weights_total)
        position = 0
        for elem in self.probabilities():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                return
        max_tries = 10000
        while(max_tries):
            self.value = round(
                random.uniform(self.range_max, self.range_min), 2
            )
            if self.test_value:
                return
            max_tries -= 1
        raise ValueError

    @property
    def value(self):
        return super(MultiSelect, self).value_get()

    @value.setter
    def value(self, value):
        self._value = value
        if self._value is not None:
            self.is_ready = 1
        self.set_by_user = 1


class Param_Opacity(ConstrainedNumber):
    def __init__(self, **kwargs):
        super(Param_Opacity, self).__init__(**kwargs)

    def randomize(self):
        weights_total = sum(
            map(
                lambda x: x["weight"], self.probabilities()
            ) + self.range_max - self.range_min
        )
        choice = random.randint(0, weights_total)
        position = 0
        for elem in self.probabilities():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                return
        self.value = round(
            random.uniform(self.range_min, self.range_max), 2
        )


class ImGridParams(Params):
    def __init__(self):
        self._params = [
           Username(name="username", required=0),
           ImageUrl(name="bgimage", required=0),
           ImageUrl(name="imageinstead", required=0),
           ImageUrl(name="planebgimage", required=0),
           MultiSelect(
               name="format",
               required=False,
               options=_FILETYPE_OPTIONS
           ),
           MultiSelect(
               name="transition",
               required=1,
               options=_TRANSITION_OPTIONS
           ),
           Color(name="skycolor", required=False),
           Color(name="planebgcolor", required=False),
           Color(name="bgcolor", required=False),
           Color(name="linecolor", required=False),
           ConstrainedNumber(name="swing", required=False, min=-170, max=170),
           ConstrainedNumber(name="tilt", required=False, min=-170, max=170),
           ConstrainedNumber(name="roll", required=False, min=-170, max=170),
           ConstrainedNumber(name="width", required=False, min=100, max=800),
           ConstrainedNumber(name="height", required=False, min=100, max=800),
           ConstrainedNumber(
               name="linethickness",
               required=False,
               min=1,
               max=30
           ),
           ConstrainedNumber(name="opacity", required=False, min=0, max=1),
           ConstrainedNumber(name="spacing", required=False, min=2, max=100),
           Bool(name="vlines", required=False),
           Bool(name="hlines", required=False),
           Bool(name="trim", required=False),
           Bool(name="shadow", required=False),
           Param_Zoom(
               name="zoom",
               required=False,
               min=-12,
               max=12,
               exclusion_range=[-1.1, 1.1]
           )
        ]

    def test_values(self):
        return not any([
          (self.param('spacing').value > self.param('width').value),
          (self.param('spacing').value > self.param('height').value),
          (self.param('linethickness').value > self.param('width').value),
          (self.param('linethickness').value > self.param('height').value),
        ])

    def randomize(self):
        p = self.params
        for el in p:
            if el in ['spacing', 'linethickness']:
                continue
            el.randomize()
        for name in ['spacing', 'linethickness']:
            max_tries = 10000
            while(max_tries):
                self.param(name).randomize()
                if self.test_values():
                    return
                max_tries -= 1
            raise ValueError
