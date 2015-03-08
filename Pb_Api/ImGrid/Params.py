import re
from Pb_Api.Params import Pb_Api_Params 
from Pb_Api.Param import Pb_Api_Param
from Pb_Api.Param.Option import Pb_Api_Param_Option
from Pb_Api.Param.Options import Pb_Api_Param_Options
from Pb_Api.Param.Username import Pb_Api_Param_Username
from Pb_Api.Param.Image_Url import Pb_Api_Param_Image_Url
from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect
from Pb_Api.Param.NumberRange import Pb_Api_Param_NumberRange
from Pb_Api.Param.Color import Pb_Api_Param_Color

#ok so is there anything else a bit weird here?
class Pattern_Url_Option(Pb_Api_Param_Option):
  def __init__(self, **kwargs):
    super(Pb_Api_Param_Option, self).__init__(**kwargs) 
  @classmethod
  def from_name(cls, **kwargs):
    formatted = "{}/{}.png".format(PATTERN_BASE_URL, kwargs["value"])
    return cls(weight=kwargs["weight"], value=formatted )
#I made options optional

class Param_Zoom(Pb_Api_Param_NumberRange):
  def __init__(self, **kwargs):
    super(Pb_Api_Param_Option, self).__init__(**kwargs) 
    self.exclusion_range = kwargs['exclusion_range']
  def randomize(self):
    weights_total = sum(map(lambda x: x["weight"], self.options()) + 
      (self.range_max - self.range_min) - (self.exclusion_range[1] - self.exclusion_range[0])   
    choice = random.randint(0, weights_total)
    position = 0
    for elem in self.options():
       position += elem["weight"] 
       if position >= choice:
           self.value = elem["value"]
           return
    max_tries = 10000
    while(max_tries): 
      self.value = random.randint(self.range_max, self.range_min),
      if not (self.value > self.exclusion_range[0] or self.value < self.exclusion_range[1]):
        return
      max_tries -= 1;
    raise ValueError
#does this make any sense? yeah but can be improved a lot, so if you see you have a lot of ways to check if value is valid or not, and 
#those checks appear here and there, so it's time to just move that code into separate method like is_valid, so you could quickly check
#if newly generate value is valid. moreover, this loop with max_tries already used in several classes (and i suspect you plan to use that later too). instead, you can defined randomize() method to have this max_tries loop, and call something like randomize_do() in child class, so all classes will have ability to regenrate value if it's not valid. I get it, and I can do that. 
#thing is that so far this is only needed once, for one param. and the randomize thing below was applying to the params class, 
#sort of a different check, to see if all the randomized params work with one another, so I think maybe I should wait to move it into 
#the parent? alright, ideally max_tries loop will be in Params class only, and Params class will have is_valid too, so basically if one param is not valid (as seen from Params) you will start over again. ahh, if one param isn't valid, it can just call randomize again on that param (individually) not on all the others, right? yep yeah that's much better ok I'll change that tomorrow. 
   
class ImPattern_Params(Pb_Api_Params): 
    def __init__(self):
        self.params = [
           Pb_Api_Param_Username(name="username", required=0), 
           Pb_Api_Param_Image_Url(name="bgimage", required=0),
           Pb_Api_Param_Image_Url(name="imageinstead", required=0),
           Pb_Api_Param_Image_Url(name="planebgimage", required=0),
           Pb_Api_Param_MultiSelect(name="format", required=0, options=format_options),
           Pb_Api_Param_MultiSelect(name="transition", required=1, options=transition_options),
           Pb_Api_Param_Color(name="skycolor", required=0, preferred_colors=skycolor_colors),
           Pb_Api_Param_Color(name="planebgcolor", required=0, preferred_colors=planebgcolor_colors),
           Pb_Api_Param_Color(name="bgcolor", required=0, preferred_colors=bgcolor_colors),
           Pb_Api_Param_Color(name="linecolor", required=0, preferred_colors=linecolor_colors),
           Pb_Api_Param_NumberRange(name="swing", required=0, options=swing_options),
           Pb_Api_Param_NumberRange(name="tilt", required=0, options=tilt_options),
           Pb_Api_Param_NumberRange(name="roll", required=0, options=roll_options),
           Pb_Api_Param_NumberRange(name="width", required=0, options=width_options),
           Pb_Api_Param_NumberRange(name="height", required=0, options=height_options),
           Pb_Api_Param_NumberRange(name="linethickness", required=0, options=height_options),
           Pb_Api_Param_NumberRange(name="opacity", required=0, options=height_options),
           Pb_Api_Param_NumberRange(name="spacing", required=0, options=height_options),
           Pb_Api_Param_MultiSelect(name="vlines", required=0, options=vlines_options),# not defined yet? oh the thing is the options have a 
#predefined weight...that's what you're supposed to set here, anyway hm, that complicated thing if different bool values have different weigths, so it's better to keep them as is then, o rs change to multiselect 
           Pb_Api_Param_MultiSelect(name="hlines", required=0, options=hlines_options),
           Pb_Api_Param_MultiSelect(name="trim", required=0, options=trim_options),
           Pb_Api_Param_MultiSelect(name="shadow", required=0, options=shadow_options),
           Param_Zoom(name="zoom", required=0, options=zoom_options),
        ]
    def randomize(self):
        max_tries = 10000
        while(max_tries): 
          super(ImPattern_Params, self).randomize()
          p = self.params()
          if not any([ 
          p['spacing'].value > p['width'].value,
          p['spacing'].value > p['height'].value,
          p['linethickness'] > p['width'].value,
          p['linethickness'] > p['height'].value ]):
            return
          max_tries -= 1
        raise ValueError
##ok I think I get it, last thing is this Param_Zoom

skycolor_colors = Pb_Api_Param_Options(
  Pb_Api_Param_Option( value='black', weight=50 ), 
  Pb_Api_Param_Option( value='silver', weight=20 ), 
)

pattern_url_options = Pb_Api_Param_Options([  
  Pattern_Url_Option.from_name(weight=0, value=i) for i in range(1,100) ] + [
  Pattern_Url_Option.from_name(weight=0, value="a{}".format(i)) for i in range(0, 42) 
])

pattern_url_options.search("a10").weight = 20;
