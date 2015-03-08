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
from Pb_Api.Param.Bool import Pb_Api_Param_Bool

class Pattern_Url_Option(Pb_Api_Param_Option):
  def __init__(self, **kwargs):
    super(Pb_Api_Param_Option, self).__init__(**kwargs) 
  @classmethod
  def from_name(cls, **kwargs):
    formatted = "{}/{}.png".format(PATTERN_BASE_URL, kwargs["value"])
    return cls(weight=kwargs["weight"], value=formatted )

class Param_Zoom(Pb_Api_Param_NumberRange):
  def __init__(self, **kwargs):
    super(Pb_Api_Param_Option, self).__init__(**kwargs) 
    self.exclusion_range = kwargs['exclusion_range']

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
           Pb_Api_Param_Bool(name="vlines", required=0, options=vlines_options),
           Pb_Api_Param_Bool(name="hlines", required=0, options=hlines_options),
           Pb_Api_Param_Bool(name="trim", required=0, options=trim_options),
           Pb_Api_Param_Bool(name="shadow", required=0, options=shadow_options),
           Param_Zoom(name="zoom", required=0, options=zoom_options),
        ]
    def randomize(self):
        super(ImPattern_Params, self).randomize()
        p = self.params()
        if any([ 
          p['spacing'].value > p['width'].value,
          p['spacing'].value > p['height'].value,
          p['linethickness'] > p['width'].value,
          p['linethickness'] > p['height'].value ]):
          self.randomize()

skycolor_colors = Pb_Api_Param_Options(
  Pb_Api_Param_Option( value='black', weight=50 ), 
  Pb_Api_Param_Option( value='silver', weight=20 ), 
)

pattern_url_options = Pb_Api_Param_Options([  
  Pattern_Url_Option.from_name(weight=0, value=i) for i in range(1,100) ] + [
  Pattern_Url_Option.from_name(weight=0, value="a{}".format(i)) for i in range(0, 42) 
])

pattern_url_options.search("a10").weight = 20;
