#!/usr/bin/python2.7 
from Pb_Api.ImPattern import Pb_Api_ImPattern

p = Pb_Api_ImPattern()
params = p.params()
params.param("image_url").value("http://hello")
pprint.pprint(params.as_hash()) 
# for now
#and then to call it, just below? yes are the params set, or do I pass them in?

#p.call(params) #something like this?
#and inside .call() you need to use .as_hash() to pass to post request. ok good
#alright I'll test this on my own time. sort of a lot. Thanks again no problems
