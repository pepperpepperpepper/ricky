#!/usr/bin/python2.7
import sys
from ricky.impattern import ImPattern
from ricky.imgrid import ImGrid
from ricky.imbreak import ImBreak
from ricky.imgradient import ImGradient
import pprint

#api = ImPattern()
#params = api.params_init()
#params.randomize()
#print params.as_hash()
#req = params.execute()
#print req

#api = ImGrid()
#params = api.params_init()
#params.randomize()
#print params.as_hash()
#req = params.execute()
#print req



#api = ImBreak()
#params = api.params_init()
#params.randomize()
#print params.as_hash()
#req = params.execute()
#print req

api = ImGradient()
params = api.params_init()
params.randomize()
print params.as_hash()
req = params.execute()
print req
