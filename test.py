#!/usr/bin/python2.7 
from Pb_Api.ImPattern import Pb_Api_ImPattern
from Pb_Api.ImGrid import Pb_Api_ImGrid
from Pb_Api.ImBreak import Pb_Api_ImBreak
from Pb_Api.ImGradient import Pb_Api_ImGradient
import pprint

#api = Pb_Api_ImPattern()
#params = api.params_init()
#params.randomize()
#print params.as_hash()
#req = params.execute()
#print req

#api = Pb_Api_ImGrid()
#params = api.params_init()
#params.randomize()
#print params.as_hash()
#req = params.execute()
#print req



#api = Pb_Api_ImBreak()
#params = api.params_init()
#params.randomize()
#print params.as_hash()
#req = params.execute()
#print req

api = Pb_Api_ImGradient()
params = api.params_init()
params.randomize()
print params.as_hash()
req = params.execute()
print req
