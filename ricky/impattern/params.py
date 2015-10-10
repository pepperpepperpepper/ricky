import re
from ricky.params import Params
from ricky.param import Param
from ricky.param.selection import Selection
from ricky.param.selections import Selections
from ricky.param.username import Username
from ricky.param.imageurl import ImageUrl
from ricky.param.multiselect import MultiSelect

from ricky.config import PATTERN_BASE_URL

class Pattern_UrlSelection(Selection):
  def __init__(self, **kwargs):
    super(Pattern_UrlSelection, self).__init__(**kwargs)
  @classmethod
  def from_name(cls, **kwargs):
    formatted = "{}/{}.png".format(PATTERN_BASE_URL, kwargs["value"])
    return cls(weight=kwargs["weight"], value=formatted )

class ImPatternParams(Params):
    def __init__(self):
        self._params = [
           Username(name="username", required=0),
           ImageUrl(name="image_url", required=1),
           MultiSelect(name="pattern_url", required=1, selections=pattern_url_selections)
        ]

pattern_url_selections = Selections(*[
  Pattern_UrlSelection.from_name(weight=0, value=i) for i in range(1,100) ] + [
  Pattern_UrlSelection.from_name(weight=0, value="a{}".format(i)) for i in range(0, 42)
])

pattern_url_selections.search("a10").weight = 20;
