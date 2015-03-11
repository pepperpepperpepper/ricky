import re, random
from Pb_Api.Params import Pb_Api_Params 
from Pb_Api.Param import Pb_Api_Param
from Pb_Api.Param.Option import Pb_Api_Param_Option
from Pb_Api.Param.Options import Pb_Api_Param_Options
from Pb_Api.Param.Username import Pb_Api_Param_Username
from Pb_Api.Param.Image_Url import Pb_Api_Param_Image_Url
from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect
from Pb_Api.Param.NumberRange import Pb_Api_Param_NumberRange
from Pb_Api.Param.Color import Pb_Api_Param_Color

from Pb_Api.ImGrid.options import *

class Param_Zoom(Pb_Api_Param_NumberRange):
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
    return super(Pb_Api_Param_MultiSelect, self).get_value()
  @value.setter
  def value(self, value):
    self._value = value
    if not self._value is None:
      self.is_ready = 1
    self.set_by_user = 1 

class Param_Opacity(Pb_Api_Param_NumberRange):
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
   
class ImGrid_Params(Pb_Api_Params): 
    def __init__(self):
        self.params = [
           Pb_Api_Param_Username(name="username", required=0), 
           Pb_Api_Param_Image_Url(name="bgimage", required=0),
           Pb_Api_Param_Image_Url(name="imageinstead", required=0),
           Pb_Api_Param_Image_Url(name="planebgimage", required=0),
           Pb_Api_Param_MultiSelect(name="format", required=0, options=format_options),
           Pb_Api_Param_MultiSelect(name="transition", required=1, options=transition_options),
           Pb_Api_Param_Color(name="skycolor", required=0, options=skycolor_colors),
           Pb_Api_Param_Color(name="planebgcolor", required=0, options=planebgcolor_colors),
           Pb_Api_Param_Color(name="bgcolor", required=0, options=bgcolor_colors),
           Pb_Api_Param_Color(name="linecolor", required=0, options=linecolor_colors),
           Pb_Api_Param_NumberRange(name="swing", required=0, options=swing_options, min=-170, max=170),
           Pb_Api_Param_NumberRange(name="tilt", required=0, options=tilt_options, min=-170, max=170),
           Pb_Api_Param_NumberRange(name="roll", required=0, options=roll_options, min=-170, max=170),
           Pb_Api_Param_NumberRange(name="width", required=0, options=width_options, min=100, max=800),
           Pb_Api_Param_NumberRange(name="height", required=0, options=height_options, min=100, max=800),
           Pb_Api_Param_NumberRange(name="linethickness", required=0, options=linethickness_options, min=1, max=30),
           Pb_Api_Param_NumberRange(name="opacity", required=0, options=opacity_options, min=0, max=1),
           Pb_Api_Param_NumberRange(name="spacing", required=0, options=spacing_options, min=2, max=100),
           Pb_Api_Param_MultiSelect(name="vlines", required=0, options=vlines_options),
           Pb_Api_Param_MultiSelect(name="hlines", required=0, options=hlines_options),
           Pb_Api_Param_MultiSelect(name="trim", required=0, options=trim_options),
           Pb_Api_Param_MultiSelect(name="shadow", required=0, options=shadow_options),
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

