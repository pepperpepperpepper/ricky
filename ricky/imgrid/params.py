import re, random
from ricky.params import Params
from ricky.param import Param
from ricky.param.option import Option
from ricky.param.options import Options
from ricky.param.username import Username
from ricky.param.imageurl import ImageUrl
from ricky.param.multiselect import MultiSelect
from ricky.param.numberrange import NumberRange
from ricky.param.color import Color

from ricky.imgrid.options import *

class Param_Zoom(NumberRange):
  def __init__(self, **kwargs):
    super(Param_Zoom, self).__init__(**kwargs)
    self.exclusion_range = kwargs['exclusion_range']
  def test_value(self):
    return not ((self.value > self.exclusion_range[0]) and (self.value < self.exclusion_range[1]))
  def randomize(self):
    weights_total = sum(map(lambda x: x["weight"], self.options())) + 10
    choice = random.randint(0, weights_total)
    position = 0
    for elem in self.options():
       position += elem["weight"]
       if position >= choice:
           self.value = elem["value"]
           return
    max_tries = 10000
    while(max_tries):
      self.value = round(random.uniform(self.range_max, self.range_min), 2)
      if self.test_value: return
      max_tries -= 1;
    raise ValueError

  @property
  def value(self):
    return super(MultiSelect, self).get_value()
  @value.setter
  def value(self, value):
    self._value = value
    if not self._value is None:
      self.is_ready = 1
    self.set_by_user = 1

class Param_Opacity(NumberRange):
  def __init__(self, **kwargs):
    super(Param_Opacity, self).__init__(**kwargs)
  def randomize(self):
    weights_total = sum(map(lambda x: x["weight"], self.options()) + self.range_max - self.range_min)
    choice = random.randint(0, weights_total)
    position = 0
    for elem in self.options():
       position += elem["weight"]
       if position >= choice:
           self.value = elem["value"]
           return
    self.value = round(random.uniform(self.range_min,range_max), 2),

class ImGridParams(Params):
    def __init__(self):
        self.params = [
           Username(name="username", required=0),
           ImageUrl(name="bgimage", required=0),
           ImageUrl(name="imageinstead", required=0),
           ImageUrl(name="planebgimage", required=0),
           MultiSelect(name="format", required=0, options=format_options),
           MultiSelect(name="transition", required=1, options=transition_options),
           Color(name="skycolor", required=0, options=skycolor_colors),
           Color(name="planebgcolor", required=0, options=planebgcolor_colors),
           Color(name="bgcolor", required=0, options=bgcolor_colors),
           Color(name="linecolor", required=0, options=linecolor_colors),
           NumberRange(name="swing", required=0, options=swing_options, min=-170, max=170),
           NumberRange(name="tilt", required=0, options=tilt_options, min=-170, max=170),
           NumberRange(name="roll", required=0, options=roll_options, min=-170, max=170),
           NumberRange(name="width", required=0, options=width_options, min=100, max=800),
           NumberRange(name="height", required=0, options=height_options, min=100, max=800),
           NumberRange(name="linethickness", required=0, options=linethickness_options, min=1, max=30),
           NumberRange(name="opacity", required=0, options=opacity_options, min=0, max=1),
           NumberRange(name="spacing", required=0, options=spacing_options, min=2, max=100),
           MultiSelect(name="vlines", required=0, options=vlines_options),
           MultiSelect(name="hlines", required=0, options=hlines_options),
           MultiSelect(name="trim", required=0, options=trim_options),
           MultiSelect(name="shadow", required=0, options=shadow_options),
           Param_Zoom(name="zoom", required=0, options=zoom_options, min=-12, max=12, exclusion_range=[-1.1, 1.1]),
        ]
    def test_values(self):
        p = self.params
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
          if el.set_by_user:
            continue
          el.randomize()
        for name in  ['spacing', 'linethickness']:
          max_tries = 10000
          while(max_tries):
            self.param(name).randomize()
            if self.test_values():
              return
            max_tries -= 1
          raise ValueError
