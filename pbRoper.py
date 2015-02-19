#!/usr/bin/python
import sys
import commands
import imcolors
import random
import time
from genericrequest import request as apirequest
if __name__ == "__main__":
    searchterm1 = raw_input(" first term: ")
    searchterm2 = raw_input(" second term: ")
else:
    searchterm1 = "pyramid"
    searchterm2 = "grass"

TESTURL_1 = commands.getoutput('python DumpSearchScraper '+searchterm1)
TESTURL_2 = commands.getoutput('python DumpSearchScraper '+searchterm2)
BOOL = ['true','false']
DEGREES = [str(x) for x in xrange(0,359)] 
COLORS = [value for key, value in imcolors.rgbtohex.iteritems()]
REASONABLEPIXELVALUE = [str(x) for x in xrange(1, 4000)]
PERCENT = [str(x) for x in xrange(0,100)]
ZEROTOTWO = [str(x) for x in xrange(0,200)]
IMAGEFORMATS = ['png','gif','jpg']
NAME = 'richard_giovanni'
#The following script determines values to be used with the pbWrangler object
#essentially it is working out the values for the param lists of the 4 
#photoblaster apis
#
#NOTE ALL APIS TAKE AN OBJECT WITH VALUES IN STRINGS THAT CORRESPOND TO THE KEYS
#DESCRIBED BELOW
############################API USAGE REFERENCE############################
#444444444444444444444444---->PHOTOBLASTER (MAIN)......."http://asdf.us/cgi-bin/im/generate"44444444444444444
#------->PARAMS
pbmainAPI = "http://asdf.us/cgi-bin/im/generate"
pbmain = {}
#url (any valid image url), transparent ('true' or 'false'), flip ('true' or 'false'),#rotate(any value between '0' and '360'),  
pbmain['url'] = TESTURL_1#===========CHANGETHIS=====================
pbmain['transparent'] = BOOL; pbmain['flip'] = BOOL; pbmain['rotate'] = DEGREES;
#subtract (any color
#as string in hex including the pound symbol ie '#ffdead' or 'rgb(0,0,0)' unfort#unately not all colors work, all of the 'websafe colors' are good though...a fo#fourth paramater can be added for semi-transparency id eg. #ffdead0.5)
pbmain['subtract'] = COLORS
#fuzz(a string value between '0' and '100'),
pbmain['fuzz'] = [str(x) for x in xrange(0,10)]#PERCENT
#width(reasonable pixel value) height(same)
pbmain['width'] = '500'
pbmain['height'] = '500'
#black(color value as described), white(colorvalue as described)
pbmain['black'] = COLORS
#brightness(value between 0,200), 100 being the default...same goes for contrast and hue
pbmain['brightness'] = 100
pbmain['contrast'] = 100#ZEROTOTWO; 
pbmain['hue'] = 100#ZEROTOTWO
#bakground(any valid image url), compose(one of the following..
IM_COMPOSE_LIST = "ATop Dst_Over Dst_In Dst_Out Multiply Screen Divide Plus Difference Exclusion Lighten Darken Overlay Hard_Light Soft_Light Pegtop_Light Linear_Light Vivid_Light Pin_Light Linear_Dodge Linear_Burn Color_Dodge Color_Burn".split()
pbmain['background'] = TESTURL_2; pbmain['compose'] = IM_COMPOSE_LIST
#format('gif', 'jpg' or 'png')
pbmain['format'] = IMAGEFORMATS
#name(a username string)
pbmain['name'] = NAME
def probability(objectname, item, ratio="0:0"):
    parts = ratio.split(':')
    number = int(parts[0])
    outof = int(parts[1])+1
    theprobability = random.choice([x for x in xrange(number, outof)])    
    probabilitylist = [x for x in xrange(0, number+1)]
    if theprobability not in probabilitylist:
        del objectname[item]
probabilitydict = {'tilt':'1:3','rotate':'1:3','halftone':'2:3'}
tester = ""
def sendrandom(dict, api):
    sendobj = {}
    for key, value in dict.iteritems():
        if type(value) == list:
            thechoice = random.choice(value)
            print key, thechoice
            sendobj[key] = thechoice
        else:
            print key, value
            sendobj[key] = value
    for key in sendobj.keys():
        if key in probabilitydict.keys():
            probability(sendobj, key, probabilitydict[key])
        if key == 'gradienttype' and 'value' == 'noise':
            if random.choice([1,2,3]) == 1:
                'value' == 'gradient'
        try:
            print key, sendobj[key]
        except KeyError:
            continue

    sendit =  apirequest(api, sendobj) 
#------------->GRADIENT....http://asdf.us/cgi-bin/im/gradient
#flip("true" or "false") flop("true or false") tilt('0'-'360') rotate('0'-'360')
pbgradient = {}
pbgradientAPI = "http://asdf.us/cgi-bin/im/gradient"
pbgradient['tilt'] = DEGREES
pbgradient['rotate'] = DEGREES
pbgradient['flip'] = BOOL
pbgradient['flop'] = BOOL

pbgradient['width'] = '500'; pbgradient['height'] = '500';
pbgradient['color1'] = COLORS; pbgradient['color2'] = COLORS
#width(reasonable number eg '400') height(reasonable number)
pbgradient['width'] = '500'#
pbgradient['height'] = '700'#
#color1('any color value') color2('any color value')
pbgradient['color1'] = COLORS
pbgradient['color2'] = COLORS
#brightness, saturation, hue, contrast (any number '0'-'200', default is '100')
pbgradient['brightness'] = ZEROTOTWO
pbgradient['saturation'] = '100' #ZEROTOTWO
pbgradient['hue'] = ZEROTOTWO
pbgradient['contrast'] = '100'#ZEROTOTWO
#blurriness(any number between '0' and '20')
pbgradient['burriness'] = [str(x) for x in xrange(0,20)]
#gradeinttype...any from this list
GRADIENT_TYPE_LIST = "gradient plasma canvas radial colorspace plasmawash gradientwash mirrored noise".split()
pbgradient['gradienttype'] = GRADIENT_TYPE_LIST
#bevel...any from this list
BEVEL_LIST = "  flatout evenlyframed biginner bigouter dramaticflatout dramaticflatinner".split() 
pbgradient['bevel'] = BEVEL_LIST
#percentbeveled(any number value between '0' and '100'
pbgradient['percentbeveled'] = PERCENT
#halftone...any from this list
HALFTONE_LIST = "  checkeredfade etchedtrasnition bendaydots smallerdots1 smallerdots2 flatstripes".split()
pbgradient['halftone'] = HALFTONE_LIST
#stripes...('true' or 'false')
pbgradient['stripes'] = BOOL
#stripenumber('0' to '600')
pbgradient['stripenumber'] = [str(x) for x in xrange(0,20)]
#stripeintensity(0,2000) '1000' retains original color for the most part
pbgradient['stripeintensity'] = [str(x) for x in xrange(0,2000)]
#format ('gif','jpg' or 'png'
pbgradient['format'] = ['gif','jpg','png']
#name (username)
pbgradient['name'] = NAME

for x in xrange(0,20):
    sendrandom(pbgradient, pbgradientAPI)####
    #sendrandom(pbmain, pbmainAPI)#
    time.sleep(2)

