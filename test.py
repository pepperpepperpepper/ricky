#!/usr/bin/python2.7
from lib.dumpfm import DumpFmImageSearch
from lib.imbreak_params_defaults import ImBreakParams_FromDefaults
from lib.imgradient_params_defaults import ImGradientParams_FromDefaults
from lib.imgrid_params_defaults import ImGridParams_FromDefaults
from lib.impattern_params_defaults import ImPatternParams_FromDefaults
from lib.imbreak import ImBreak
from lib.impattern import ImPattern
from lib.imgradient import ImGradient
from lib.imgrid import ImGrid

imbreak = ImBreak()
imgradient = ImGradient()
imgrid = ImGrid()
impattern = ImPattern()
#p = ImBreakParams_FromDefaults() 
#image = imbreak.new(p.from_random())
#print image

#p = ImGradientParams_FromDefaults() 
#image = imgradient.new(p.from_random())
#print image

#p = ImGridParams_FromDefaults() 
#image = imgrid.new(p.from_random())
#print image

p = ImPatternParams_FromDefaults() 
image = impattern.new(p.from_random())
print image
