import re
from Pb_Api.Params import Pb_Api_Params 
from Pb_Api.Param import Pb_Api_Param
from Pb_Api.Param.Option import Pb_Api_Param_Option
from Pb_Api.Param.Options import Pb_Api_Param_Options
from Pb_Api.Param.Username import Pb_Api_Param_Username
from Pb_Api.Param.Image_Url import Pb_Api_Param_Image_Url
from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect

class Pattern_Url_Option(Pb_Api_Param_Option):
  def __init__(self, **kwargs):
    super(Pb_Api_Param_Option, self).__init__(**kwargs) 
  @classmethod
  def from_name(cls, **kwargs):
    formatted = "{}/{}.png".format(PATTERN_BASE_URL, kwargs["value"])
    return cls(weight=kwargs["weight"], value=formatted )

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
           Pb_Api_Param_Angle(name="swing", required=0, preferred_angles=preferred_angles),
           Pb_Api_Param_Angle(name="tilt", required=0, preferred_angles=preferred_angles),
           Pb_Api_Param_Angle(name="roll", required=0, preferred_angles=preferred_angles),
        ]
#what about width and height, same as angle, just set a max and min? yeah can be that so should angle inherit from a number
#class? yes i would make Number class which doesn't have prefered numbers, and angle can inherit and add preferend number functionality
            "width" 
            "height" 

            "skycolor" 
            "planebgcolor" 
            "bgcolor" 
            "linecolor" 

#ok these are similar too, they have a limited range though
            "linethickness" 
            "opacity" 
            "spacing" 




            "vlines" 
            "hlines" 


            "trim" 
            "shadow" 

#ok swing tilt roll zoom is a number between -180 and 180
#but it would be nice to prefer 0, 90, etc?
#seems sort of similar to colors? yeah custom class basically the same logic as color? yeah can be same

            "swing" 
            "tilt" 
            "roll" 
#ok two more, the thing with this is that it has 
#a much smaller range than the others, and it can't be a number between 1 and -1
#very weird parameters I guess that's the last thing
            "zoom" 
#like that? yep ok next thing is this above
skycolor_colors = Pb_Api_Param_Options(
  Pb_Api_Param_Option( value='black', weight=50 ), 
  Pb_Api_Param_Option( value='silver', weight=20 ), 
)

pattern_url_options = Pb_Api_Param_Options([  
  Pattern_Url_Option.from_name(weight=0, value=i) for i in range(1,100) ] + [
  Pattern_Url_Option.from_name(weight=0, value="a{}".format(i)) for i in range(0, 42) 
])

pattern_url_options.search("a10").weight = 20;
