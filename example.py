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
for i in xrange(0,100):
    api = ImGradient()
    params = api.params_init()
    params.randomize()
    print params.as_dict()
    req = params.execute()
    print req

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

