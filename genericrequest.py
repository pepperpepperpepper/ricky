#!/usr/bin/python

import urllib
import urllib2
import simplejson
import sys
urlencode = urllib.urlencode
urlopen = urllib2.urlopen
Request = urllib2.Request

def request (url, data):
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Accept': '*/*'
        }
    try:
        data = urlencode(data)
        req = Request(url, data, headers)
        response = urlopen(req)
        try:
            thejson = response.read()
            response = simplejson.loads(thejson)    
        except ValueError:
            response = response.read()
        return response
    except IOError, e:
        if hasattr(e, 'code'):
            print '%s - ERROR %s' % (self.url, e.code)
            return None
        else:
            return response
    
