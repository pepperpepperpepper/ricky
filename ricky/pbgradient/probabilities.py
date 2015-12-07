from ricky.param.probabilities import Probabilities

width_probabilities = Probabilities.from_dict(
    {"value": 40, "weight": 10},
)
height_probabilities = Probabilities.from_dict(
    {"value": 400, "weight": 100},
)
color1_probabilities = Probabilities.from_dict(
    {"value": "", "weight": 0},
#    {"value": "black", "weight": 1},
#    {"value": "white", "weight": 2},
)
color2_probabilities = Probabilities.from_dict(
    {"value": "", "weight": 0},
#    {"value": "black", "weight": 2},
#    {"value": "white", "weight": 1},
)
stripes_probabilities = Probabilities.from_dict(
    {"value": "true", "weight": 3},
    {"value": "false", "weight": 1},
)
stripenumber_probabilities = Probabilities.from_dict(
    {"value": 3, "weight": 10},
    {"value": 10, "weight": 10},
    {"value": 20, "weight": 10},
    {"value": 100, "weight": 10},
    {"value": 40, "weight": 10},
#    {"value": 1, "weight": 50},
#    {"value": 2, "weight": 50},
#    {"value": 2, "weight": 50},

)
stripeintensity_probabilities = Probabilities.from_dict(
  {"value": 1000, "weight": 10},
  {"value": 4, "weight": 10},
)
#  contrast_probabilities = \
brightness_probabilities = \
  saturation_probabilities = \
  hue_probabilities = \
  Probabilities.from_dict(
    {"value": "", "weight": 0},
#    {"value": "", "weight": 300},
)
halftone_probabilities = Probabilities.from_dict(
    {"value": "", "weight": 60},
    {"value": "checkeredfade", "weight": 10},
    {"value": "etchedtransition", "weight": 10},
    {"value": "bendaydots", "weight": 10},
    {"value": "smallerdots1", "weight": 10},
    {"value": "smallerdots2", "weight": 10},
    {"value": "flatstripes", "weight": 10},
)
bevel_probabilities = Probabilities.from_dict(
    {"value": "", "weight": 4},
    {"value": "flatout", "weight": 1},
    {"value": "flatinner", "weight": 0},
    {"value": "evenlyframed", "weight": 1},
#    {"value": "biginner", "weight": 1},
    {"value": "bigouter", "weight": 1},
    {"value": "dramaticflatout", "weight": 1},
#    {"value": "dramaticflatinner", "weight": 1},
)

blurriness_probabilities = \
    percentbeveled_probabilities = Probabilities.from_dict(
    {"value": 30, "weight": 10},
    {"value": 10, "weight": 10},
    {"value": 5, "weight": 10},
    {"value": 20, "weight": 10},
    {"value": 25, "weight": 10},
    {"value": 7, "weight": 10},
    {"value": "", "weight": 1},
)
rotate_probabilities = \
    tilt_probabilities = Probabilities.from_dict(
    {"value": 0, "weight": 200},
    {"value": 90,  "weight": 2},
    {"value": 180, "weight": 2},
    {"value": 270, "weight": 2},
)
flop_probabilities = flip_probabilities = Probabilities.from_dict(
    {"value": "", "weight": 1},
    {"value": "true",  "weight": 1},
)

filetype_probabilities = Probabilities.from_dict(
    {"value": "png", "weight": 10},
    {"value": "jpg", "weight": 2},
    {"value": "gif", "weight": 2},
)
gradienttype_probabilities = Probabilities.from_dict(
    {"value": "canvas", "weight": 1},
    {"value": "gradient", "weight": 5},
    {"value": "radial", "weight": 1},
    {"value": "colorspace", "weight": 1},
    {"value": "plasmawash", "weight": 2},
    {"value": "gradientwash", "weight": 1},
    {"value": "mirrored", "weight": 0},
    {"value": "noise", "weight": 1},
)
