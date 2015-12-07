#!/usr/bin/python2.7
from ricky.pbgradient import PbGradient
from ricky.pbbreaker import PbBreaker
from ricky.pbgrid import PbGrid
from ricky.pbpattern import PbPattern


api = PbPattern()
params = api.params_init()
print params
params.randomize()
print params
#print params['color1']
#params['color1'].from_normalized(0.28187431585)
#print params['color1']
# print params.as_dict()
# req = params.execute()
# print req
