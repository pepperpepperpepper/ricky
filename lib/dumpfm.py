#!/usr/bin/python2.7
import urllib
import urllib2
import simplejson as json
import sys
import re
import os
urlencode = urllib.urlencode
urlopen = urllib2.urlopen
Request = urllib2.Request

DEFAULT_TERM = "pizza"

#{{{
def get_request(url):
  try:
    headers = {
      'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
      'Accept': '*/*'
      }
    req = Request(url, None, headers)
    response = urlopen(req)
    return response.read()
  except IOError, e:
    if hasattr(e, 'code'):
      sys.stderr.write( '%s - ERROR %s' % (url, e.code))
    else:
      sys.stderr.write(str(e))
    sys.exit(1)
#}}}
class Image_url():
    def __init__(self, result):
        self._url = result['url']
    def url(self):
        if self._url[0] == '/':
            return "{}{}".format('http://dump.fm/images', self._url)
        else :
            return "{}{}".format('http://', self._url)
class DumpFmImageSearch:
  def __init__(self):
    self._search_url = 'http://dump.fm/cmd/search/'
  def search(self, *args):  # something like this should work.
    if len(args) < 1:
        sys.stderr.write("Must provide search term");
        raise ValueError
    terms = "+".join(map(lambda x : urllib.quote(x), args));
    url = "{}{}".format(self._search_url, terms)
    resp = get_request(url);
    return map(        
        lambda x: Image_url(x),
        json.loads(resp)
    )
 
  
if __name__ == '__main__':
  term = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TERM
  s = DumpFmImageSearch()
  images = s.search(term)
  print images[0].url() 
