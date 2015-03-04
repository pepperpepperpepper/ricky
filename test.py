#!/usr/bin/python2.7
from lib.dumpfm import DumpFmImageSearch

#ok so lib.dumpfm is completely different and I'll ask about that later


from Pb_Api.ImGradient import *
from Pb_Api.ImGrid import *

#ok how do I initialize and load params?

imgradient = Pb_Api_ImGradient() #this class name doesn't seem right though, is that what we named it? no, but should be about that, i'm using perl style, so path and class name basically same, we can't use dot in class name, so i'm using _. why can't we use the dot in the classname? i think it's syntax error. hmm should we test real quick? sure
params = imgradient.params()
params.param("gradienttype").value("mirror")
#params.randomize()
params.defaults() # if I want defaults? yep
result = imgradient.call(params)
# seomthing like this

#this is how they are getting imported...does it look a little bit weird?
#well it fine, what about all those services, imbreak, imgradient, can they be sort of merged together? not really
#they take very different parameters...that's the issue, but the service call, I made a master class for it
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
