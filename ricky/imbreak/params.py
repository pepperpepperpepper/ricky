import re, random
from ricky.params import Params
from ricky.param.option import Selection
from ricky.param.selections import Selections
from ricky.param.username import Username
from ricky.param.imageurl import ImageUrl
from ricky.param.multiselect import MultiSelect
from ricky.param.numberrange import NumberRange
from ricky.param.color import Color
from ricky.config import PATTERN_BASE_URL


breaktype_selections = Selections.from_dict(
    {"value":"CLASSIC",         "weight": 1},
    {"value":"REDUX",           "weight": 1},
    {"value":"BLURRY_BREAK",    "weight": 1},
    {"value":"BLURRY_BREAK_2",  "weight": 1},
    {"value":"SWIPE",           "weight": 1},
    {"value":"RGB_WASH",        "weight": 1},
    {"value":"RGB_WASH_2",      "weight": 1},
    {"value":"NOISY_BREAK",     "weight": 1},
    {"value":"BROKEN_VIGNETTE", "weight": 1},
    {"value":"FAX_MACHINE",     "weight": 1},
    {"value":"STRIPES",         "weight": 1},
    {"value":"PHOTOCOPY",       "weight": 1},
)
breakmode_selections = Selections.from_dict(
    {"value":"extreme",  "weight": 1},
    {"value":"subtle",  "weight": 1},
)
finalformat_selections = Selections.from_dict(
    {"value":"png",  "weight": 5},
    {"value":"jpg",  "weight": 2},
    {"value":"gif",  "weight": 2},
)
breakangle_selections = Selections.from_dict(
    {"value":0,  "weight": 9},
    {"value":90,  "weight": 2},
    {"value":-180,  "weight": 2},
    {"value":180,  "weight": 2},
)
expanded_selections = Selections.from_dict(
    {"value": "" , "weight": 11 },
    {"value": 1, "weight": 2}
)

class ImBreakParams(Params):
    def __init__(self):
        self._params = [
           Username(name="username", required=0),
           ImageUrl(name="url", required=1),
           MultiSelect(name="finalformat", required=0, selections=finalformat_selections),
           MultiSelect(name="breaktype", required=1, selections=breaktype_selections),
           NumberRange(name="breakangle", required=0, selections=breakangle_selections, min=-180, max=180),
           MultiSelect(name="breakmode", required=1, selections=breakmode_selections),
           MultiSelect(name="expanded", required=0, selections=expanded_selections),
        ]
