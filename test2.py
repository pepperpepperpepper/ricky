#!/usr/bin/python2.7 
from Pb_Api.ImPattern import Pb_Api_ImPattern
import pprint

p = Pb_Api_ImPattern()
params = p.params()
#params.param("image_url").value = "http://hello"
#print params
params.randomize()
pprint.pprint(params.as_hash()) 
print p.call(params.as_hash())
