#!/usr/bin/python2.7
from ricky.params.pbgradient import PbGradient
from ricky.params.pbbreaker import PbBreaker
from ricky.params.pbgrid import PbGrid
from ricky.params.pbpattern import PbPattern
import ricky.utils as utils

params = PbGradient()
params.randomize()
params.execute()
print params
#print params
#print params
#print params.execute()
#data = utils.data_from_url(
#    "http://i.asdf.us/im/8f/PbGradientblue4-DarkGreen_1448917630.png"
#)
#params.from_dict(data['params'])
#print params
#print params['color1']
#params['color1'].from_normalized(0.28187431585)
#print params['color1']
# print params.as_dict()
# req = params.execute()
# print req
