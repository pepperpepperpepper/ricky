#!/usr/bin/python2.7
from ricky.imgradient import ImGradient


api = ImGradient()
params = api.params_init()
print params
params.randomize()
print params['color1']
params['color1'].from_normalized(0.28187431585)
print params['color1']
# print params.as_dict()
# req = params.execute()
# print req
