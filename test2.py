#!/usr/bin/python2.7 
from Pb_Api.ImPattern import Pb_Api_ImPattern
from Pb_Api.ImGrid import Pb_Api_ImGrid
import pprint

api = Pb_Api_ImPattern()
request = api.request_new()
request.randomize()
resp = request.execute()


