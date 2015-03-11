from Pb_Api.Param.Options import Pb_Api_Param_Options
format_options = Pb_Api_Param_Options.from_dict(
  { 'weight': 20, 'value': 'png' },
  { 'weight': 0, 'value': 'gif' },
  { 'weight': 0, 'value': 'jpg' },
)
transition_options = Pb_Api_Param_Options.from_dict(
  { "value" : "background", "weight": 1 },
  { "value" : "dither", "weight": 1 },
  { "value" : "random", "weight": 1 },
  { "value" : "tile", "weight": 1 },
  { "value" : "edge", "weight": 1 },
)
skycolor_colors = \
  bgcolor_colors = planebgcolor_colors = Pb_Api_Param_Options.from_dict(
  { "value" : "white", "weight" : 1 }, 
  { "value" : "silver", "weight" : 1 }, 
  { "value" : None, "weight" : 10 }, 
)

linecolor_colors = Pb_Api_Param_Options.from_dict(
  { "value" : "black", "weight" : 1 }, 
  { "value" : "white", "weight" : 1 }, 
  { "value" : "silver", "weight" : 1 }, 
)
swing_options = tilt_options = roll_options = Pb_Api_Param_Options.from_dict(
   {"value": "",  "weight": 2},
   {"value": 30,   "weight": 1},
   {"value": -30,   "weight": 1},
)
width_options = height_options = Pb_Api_Param_Options.from_dict(
   { "value" : 400, "weight" : 1 }, 
   { "value" : 600, "weight" : 1 }, 
)
linethickness_options = Pb_Api_Param_Options.from_dict(
   {"value":1,  "weight": 2},
   {"value":2,  "weight": 1},
)
opacity_options = Pb_Api_Param_Options.from_dict( 
   {"value":1,  "weight": 2},
   {"value":0.5,  "weight": 1},
)
spacing_options = Pb_Api_Param_Options.from_dict(
   {"value":10,  "weight": 1},
   {"value":15,  "weight": 1},
)
vlines_options = hlines_options = Pb_Api_Param_Options.from_dict(
   {"value":"",  "weight": 2},
   {"value":"true",   "weight": 1},
)
shadow_options = Pb_Api_Param_Options.from_dict(
   {"value":"",  "weight": 1},
   {"value":"true",   "weight": 1},
)
zoom_options = Pb_Api_Param_Options.from_dict(
    {"value": 0,  "weight": 3},
    {"value": 1.2,  "weight": 1},
    {"value": -1.2,  "weight": 1},
)
trim_options = Pb_Api_Param_Options.from_dict(
   {"value":"",  "weight": 1},
   {"value":"true",   "weight": 1},
)

