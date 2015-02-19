#!/usr/bin/python

GRADIENT_PARAM_LIST = "flip flop tilt rotate subtract width height color2 color1 brightness saturation blurriness hue contrast gradienttype bevel percentbeveled halftone stripes stripenumber stripeintensity format name"

GRID_PARAM_LIST = "width height linethickness opacity linecolor spacing vlines hlines shadow bgimage bgcolor imageinstead planebgcolor skycolor planebgimage transition swing tilt roll zoom trim format username"

BREAK_PARAM_LIST = "breakmode breaktype breakangle url username firsttime"

PB_PARAM_LIST = "url transparent flip flop rotate subtract fuzz width height black white brightness saturation hue contrast background compose format name"

class PBwrangler:
    def __init__(self, pb):
        self.pblist = {'imgradient':GRADIENT_PARAM_LIST, 'imgrid':GRID_PARAM_LIST, 'imbreak':BREAK_PARAM_LIST, 'im':PB_PARAM_LIST}
        self.paramlist = pblist[pb]
        for param in self.paramlist:
            setattr(self, param, "")
    def PBwrangle(self):
        
