#!/usr/bin/python2.7 
from Pb_Api.ImPattern import Pb_Api_ImPattern
import pprint

p = Pb_Api_ImPattern()
params = p.params()
params.param("image_url").value = "http://hello"
print params
params.randomize()
pprint.pprint(params.as_hash()) 
# well something like this how do you feel about it? seems right? yep looks good, need to go over ranomization and defaults a bit, but core is ready to use lets just look at randomization for a second? sure
# works, but i think need to reconsider default somehow, it should be something like set_by_user to make sure user set that, and not automated default, or something like that. why is it better to use set by user? well default doesn't say much about value, and in intialization we say that values passed is default, which is not really true. to find difference ( and make randomize() code clearer) it should be somehting like  if not el.set_by_user: el.randomize()
# yeahh ok
# well like this, but need to check randomization, keep selecting 1.png weird
