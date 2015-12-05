#!/usr/bin/python2.7
from ricky.imgradient import ImGradient


api = ImGradient()
params = api.params_init()
print params
params.randomize()
print params
# print params.as_dict()
# req = params.execute()
# print req
