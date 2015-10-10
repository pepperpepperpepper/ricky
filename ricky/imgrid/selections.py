from ricky.param.selections import Selections
format_selections = Selections.from_dict(
  { 'weight': 20, 'value': 'png' },
  { 'weight': 0, 'value': 'gif' },
  { 'weight': 0, 'value': 'jpg' },
)
transition_selections = Selections.from_dict(
  { "value" : "background", "weight": 1 },
  { "value" : "dither", "weight": 1 },
  { "value" : "random", "weight": 1 },
  { "value" : "tile", "weight": 1 },
  { "value" : "edge", "weight": 1 },
)
skycolor_colors = \
  bgcolor_colors = planebgcolor_colors = Selections.from_dict(
  { "value" : "white", "weight" : 1 },
  { "value" : "silver", "weight" : 1 },
  { "value" : None, "weight" : 10 },
)

linecolor_colors = Selections.from_dict(
  { "value" : "black", "weight" : 1 },
  { "value" : "white", "weight" : 1 },
  { "value" : "silver", "weight" : 1 },
)
swing_selections = tilt_selections = roll_selections = Selections.from_dict(
   {"value": "",  "weight": 2},
   {"value": 30,   "weight": 1},
   {"value": -30,   "weight": 1},
)
width_selections = height_selections = Selections.from_dict(
   { "value" : 400, "weight" : 1 },
   { "value" : 600, "weight" : 1 },
)
linethickness_selections = Selections.from_dict(
   {"value":1,  "weight": 2},
   {"value":2,  "weight": 1},
)
opacity_selections = Selections.from_dict(
   {"value":1,  "weight": 2},
   {"value":0.5,  "weight": 1},
)
spacing_selections = Selections.from_dict(
   {"value":10,  "weight": 1},
   {"value":15,  "weight": 1},
)
vlines_selections = hlines_selections = Selections.from_dict(
   {"value":"",  "weight": 2},
   {"value":"true",   "weight": 1},
)
shadow_selections = Selections.from_dict(
   {"value":"",  "weight": 1},
   {"value":"true",   "weight": 1},
)
zoom_selections = Selections.from_dict(
    {"value": 0,  "weight": 3},
    {"value": 1.2,  "weight": 1},
    {"value": -1.2,  "weight": 1},
)
trim_selections = Selections.from_dict(
   {"value":"",  "weight": 1},
   {"value":"true",   "weight": 1},
)

