from ricky.param.options import Options

width_options = Options.from_dict(
    {"value": 400, "weight": 3},
    {"value": 600, "weight": 1},
)
height_options = Options.from_dict(
    {"value": 400, "weight": 3},
    {"value": 600, "weight": 1},
)
color1_options = Options.from_dict(
    {"value": "", "weight": 0},
#    {"value": "black", "weight": 1},
#    {"value": "white", "weight": 2},
)
color2_options = Options.from_dict(
    {"value": "", "weight": 0},
#    {"value": "black", "weight": 2},
#    {"value": "white", "weight": 1},
)
stripes_options = Options.from_dict(
    {"value": "true", "weight": 3},
    {"value": "false", "weight": 1},
)
stripenumber_options = Options.from_dict(
    {"value": "", "weight": 0},
#    {"value": 1, "weight": 50},
#    {"value": 2, "weight": 50},
#    {"value": 2, "weight": 50},

)
#  contrast_options = \
stripeintensity_options = \
  brightness_options = \
  saturation_options = \
  hue_options = \
  Options.from_dict(
    {"value": "", "weight": 0},
#    {"value": "", "weight": 300},
)
halftone_options = Options.from_dict(
    {"value": "", "weight": 20},
    {"value": "checkeredfade", "weight": 1},
    {"value": "etchedtransition", "weight": 1},
    {"value": "bendaydots", "weight": 1},
    {"value": "smallerdots1", "weight": 1},
    {"value": "smallerdots2", "weight": 1},
    {"value": "flatstripes", "weight": 1},
)
bevel_options = Options.from_dict(
    {"value": "", "weight": 4},
    {"value": "flatout", "weight": 1},
    {"value": "flatinner", "weight": 1},
    {"value": "evenlyframed", "weight": 1},
#    {"value": "biginner", "weight": 1},
    {"value": "bigouter", "weight": 1},
    {"value": "dramaticflatout", "weight": 1},
#    {"value": "dramaticflatinner", "weight": 1},
)

blurriness_options = \
    percentbeveled_options = Options.from_dict(
    {"value": 30, "weight": 20},
    {"value": 10, "weight": 2},
    {"value": "", "weight": 100},
)
rotate_options = \
    tilt_options = Options.from_dict(
    {"value": 0, "weight": 200},
    {"value": 90,  "weight": 2},
    {"value": 180, "weight": 2},
    {"value": 270, "weight": 2},
)
flop_options = flip_options = Options.from_dict(
    {"value": "", "weight": 1},
    {"value": "true",  "weight": 1},
)

filetype_options = Options.from_dict(
    {"value": "png", "weight": 10},
    {"value": "jpg", "weight": 2},
    {"value": "gif", "weight": 2},
)
gradienttype_options = Options.from_dict(
    {"value": "canvas", "weight": 1},
    {"value": "gradient", "weight": 5},
    {"value": "radial", "weight": 1},
    {"value": "colorspace", "weight": 1},
    {"value": "plasmawash", "weight": 2},
    {"value": "gradientwash", "weight": 1},
    {"value": "mirrored", "weight": 1},
    {"value": "noise", "weight": 3},
)
