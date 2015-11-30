import re
from ricky.params import Params
from ricky.param import Param
from ricky.param.probability import Probability
from ricky.param.probabilities import Probabilities
from ricky.param.username import Username
from ricky.param.imageurl import ImageUrl
from ricky.param.multiselect import MultiSelect

from ricky.config import PATTERN_BASE_URL

class Pattern_UrlProbability(Probability):
  def __init__(self, **kwargs):
    super(Pattern_UrlProbability, self).__init__(**kwargs)
  @classmethod
  def from_name(cls, **kwargs):
    formatted = "{}/{}.png".format(PATTERN_BASE_URL, kwargs["value"])
    return cls(weight=kwargs["weight"], value=formatted )

class ImPatternParams(Params):
    def __init__(self):
        self._params = [
           Username(name="username", required=False),
           ImageUrl(name="image_url", required=True),
           MultiSelect(name="pattern_url", required=True, probabilities=pattern_url_probabilities)
        ]

pattern_url_probabilities = Probabilities(*[
  Pattern_UrlProbability.from_name(weight=0, value=i) for i in range(1,100) ] + [
  Pattern_UrlProbability.from_name(weight=0, value="a{}".format(i)) for i in range(0, 42)
])

pattern_url_probabilities.search("a10").weight = 20;
