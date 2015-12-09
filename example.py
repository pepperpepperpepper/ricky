#!/usr/bin/python2.7
import ricky.params
import ricky.utils as utils

params = ricky.params.PbGradient()
params.randomize()
print params.as_serialized()
#print params.execute()
#print params
#data = utils.data_from_url(
#    "/im/cache/PbGradientrgb-234,155,194-"
#    "-rgb-9,252,50-_1449620530_RICHARD_GIOVANNI.jpg"
#)
#print data
#for params_class in ricky.params.Params.__subclasses__():
#    if data['module'] == params_class.__name__:
#        params_instance = params_class()
#        print type(params_instance)
#        params_instance.from_dict(data['params'])
#        print params_instance.execute()
#        print params_instance.as_normalized()
