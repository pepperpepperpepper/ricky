#!/usr/bin/python2.7
import random
from config import USERNAME, TEST_URL
from lib.utils import Pb_Api_Params
PATTERN_URL_BASE =  "http://asdf.us/impattern/patterns"
class ImPatternParams_FromDefaults(Pb_Api_Params):
#{{{ params
#            "pattern_url",
#            "pattern_data",
#            "username",
#            "image_url",
#}}}
    def __init__(self):
        self.weighted_pattern_url = [
#{{{pattern urls
            { "value":"1.png", "weight":1 },
            { "value":"10.png", "weight":1 },
            { "value":"11.png", "weight":1 },
            { "value":"12.png", "weight":1 },
            { "value":"13.png", "weight":1 },
            { "value":"14.png", "weight":1 },
            { "value":"15.png", "weight":1 },
            { "value":"16.png", "weight":1 },
            { "value":"17.png", "weight":1 },
            { "value":"18.png", "weight":1 },
            { "value":"19.png", "weight":1 },
            { "value":"2.png", "weight":1 },
            { "value":"20.png", "weight":1 },
            { "value":"21.png", "weight":1 },
            { "value":"22.png", "weight":1 },
            { "value":"23.png", "weight":1 },
            { "value":"24.png", "weight":1 },
            { "value":"25.png", "weight":1 },
            { "value":"26.png", "weight":1 },
            { "value":"27.png", "weight":1 },
            { "value":"28.png", "weight":1 },
            { "value":"29.png", "weight":1 },
            { "value":"3.png", "weight":1 },
            { "value":"30.png", "weight":1 },
            { "value":"31.png", "weight":1 },
            { "value":"32.png", "weight":1 },
            { "value":"33.png", "weight":1 },
            { "value":"34.png", "weight":1 },
            { "value":"35.png", "weight":1 },
            { "value":"36.png", "weight":1 },
            { "value":"37.png", "weight":1 },
            { "value":"38.png", "weight":1 },
            { "value":"39.png", "weight":1 },
            { "value":"4.png", "weight":1 },
            { "value":"40.png", "weight":1 },
            { "value":"41.png", "weight":1 },
            { "value":"42.png", "weight":1 },
            { "value":"43.png", "weight":1 },
            { "value":"44.png", "weight":1 },
            { "value":"45.png", "weight":1 },
            { "value":"46.png", "weight":1 },
            { "value":"47.png", "weight":1 },
            { "value":"48.png", "weight":1 },
            { "value":"49.png", "weight":1 },
            { "value":"5.png", "weight":1 },
            { "value":"50.png", "weight":1 },
            { "value":"51.png", "weight":1 },
            { "value":"52.png", "weight":1 },
            { "value":"53.png", "weight":1 },
            { "value":"54.png", "weight":1 },
            { "value":"55.png", "weight":1 },
            { "value":"56.png", "weight":1 },
            { "value":"57.png", "weight":1 },
            { "value":"58.png", "weight":1 },
            { "value":"59.png", "weight":1 },
            { "value":"6.png", "weight":1 },
            { "value":"60.png", "weight":1 },
            { "value":"61.png", "weight":1 },
            { "value":"62.png", "weight":1 },
            { "value":"63.png", "weight":1 },
            { "value":"64.png", "weight":1 },
            { "value":"65.png", "weight":1 },
            { "value":"66.png", "weight":1 },
            { "value":"67.png", "weight":1 },
            { "value":"68.png", "weight":1 },
            { "value":"69.png", "weight":1 },
            { "value":"7.png", "weight":1 },
            { "value":"70.png", "weight":1 },
            { "value":"71.png", "weight":1 },
            { "value":"72.png", "weight":1 },
            { "value":"73.png", "weight":1 },
            { "value":"74.png", "weight":1 },
            { "value":"75.png", "weight":1 },
            { "value":"76.png", "weight":1 },
            { "value":"77.png", "weight":1 },
            { "value":"78.png", "weight":1 },
            { "value":"79.png", "weight":1 },
            { "value":"8.png", "weight":1 },
            { "value":"80.png", "weight":1 },
            { "value":"81.png", "weight":1 },
            { "value":"82.png", "weight":1 },
            { "value":"83.png", "weight":1 },
            { "value":"84.png", "weight":1 },
            { "value":"85.png", "weight":1 },
            { "value":"86.png", "weight":1 },
            { "value":"87.png", "weight":1 },
            { "value":"88.png", "weight":1 },
            { "value":"89.png", "weight":1 },
            { "value":"9.png", "weight":1 },
            { "value":"90.png", "weight":1 },
            { "value":"91.png", "weight":1 },
            { "value":"92.png", "weight":1 },
            { "value":"93.png", "weight":1 },
            { "value":"94.png", "weight":1 },
            { "value":"95.png", "weight":1 },
            { "value":"96.png", "weight":1 },
            { "value":"a0.png", "weight":1 },
            { "value":"a1.png", "weight":1 },
            { "value":"a10.png", "weight":1 },
            { "value":"a11.png", "weight":1 },
            { "value":"a12.png", "weight":1 },
            { "value":"a13.png", "weight":1 },
            { "value":"a14.png", "weight":1 },
            { "value":"a15.png", "weight":1 },
            { "value":"a16.png", "weight":1 },
            { "value":"a17.png", "weight":1 },
            { "value":"a18.png", "weight":1 },
            { "value":"a19.png", "weight":1 },
            { "value":"a2.png", "weight":1 },
            { "value":"a20.png", "weight":1 },
            { "value":"a21.png", "weight":1 },
            { "value":"a22.png", "weight":1 },
            { "value":"a23.png", "weight":1 },
            { "value":"a24.png", "weight":1 },
            { "value":"a25.png", "weight":1 },
            { "value":"a26.png", "weight":1 },
            { "value":"a27.png", "weight":1 },
            { "value":"a28.png", "weight":1 },
            { "value":"a29.png", "weight":1 },
            { "value":"a3.png", "weight":1 },
            { "value":"a30.png", "weight":1 },
            { "value":"a31.png", "weight":1 },
            { "value":"a32.png", "weight":1 },
            { "value":"a33.png", "weight":1 },
            { "value":"a34.png", "weight":1 },
            { "value":"a35.png", "weight":1 },
            { "value":"a36.png", "weight":1 },
            { "value":"a37.png", "weight":1 },
            { "value":"a38.png", "weight":1 },
            { "value":"a39.png", "weight":1 },
            { "value":"a4.png", "weight":1 },
            { "value":"a40.png", "weight":1 },
            { "value":"a41.png", "weight":1 },
            { "value":"a5.png", "weight":1 },
            { "value":"a6.png", "weight":1 },
            { "value":"a7.png", "weight":1 },
            { "value":"a8.png", "weight":1 },
            { "value":"a9.png", "weight":1 },
#}}}
        ]
    def from_random(self, url=TEST_URL):
        return {
            "image_url" : url,
            "username" : USERNAME, 
            "pattern_url" : "{}/{}".format(PATTERN_URL_BASE, self._weighted_choice( self.weighted_pattern_url )),
        }
    def from_default(self, url=TEST_URL):
        return {
            "image_url" : url,
            "username" : USERNAME, 
            "pattern_url" : "{}/{}".format(PATTERN_URL_BASE, self._default_choice( self.weighted_pattern_url )),
        }