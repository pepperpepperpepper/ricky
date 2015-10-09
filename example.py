#!/usr/bin/python2.7
import sys
from ricky.impattern import ImPattern
from ricky.imgrid import ImGrid
from ricky.imbreak import ImBreak
from ricky.imgradient import ImGradient
import pprint
import time

#ok we are 32 and we need a from_dict method
#ok we are 32 and we need a from_dict method
test_d = {'username': 'RICHARD_GIOVANNI', 'bevel': 'flatinner', 'saturation': '', 'rotate': 34, 'percentbeveled': 96, 'brightness': 79, 'stripenumber': 2, 'filetype': 'png', 'blurriness': 180, 'flip': '', 'height': 594, 'color1': 'rgb(191,125,24)', 'width': 536, 'color2': 'rgb(186,78,94)', 'gradienttype': 'mirrored', 'stripeintensity': 2515, 'tilt': 58, 'flop': '', 'halftone': 'etchedtransition', 'hue': 146}
#for i in xrange(0,100):
api = ImGradient()
params = api.params_init()
params.from_dict(test_d)
#params.randomize()
print params.as_dict()
req = params.execute()
print req
#if not (i % 5):
#   time.sleep(2)


#api = ImPattern()
#params = api.params_init()
#params.randomize()
#print params.as_dict()
#req = params.execute()
#print req

#api = ImGrid()
#params = api.params_init()
#params.randomize()
#print params.as_dict()
#req = params.execute()
#print req



#api = ImBreak()
#params = api.params_init()
#params.randomize()
#print params.as_dict()
#req = params.execute()
#print req

