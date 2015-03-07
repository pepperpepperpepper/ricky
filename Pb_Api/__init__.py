import urllib
import urllib2
import sys
import random
import simplejson as json
import urllib2

class Pb_Api:
    def __init__(self):
        self._required_keys = []
        self.url = ""
    def new(self, params):
        for k in self._required_keys:
            if not k in params:
                params[k] = "";
        self.current_params = params
        return json.loads(post_request(self.url, self.current_params))
    def post_request(self, url, params):
        params = urllib.urlencode(params)
        sys.stderr.write(params)
        sys.stderr.write(url)
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36",
            "Accept": "text/plain"
        }
        try:
            req = urllib2.Request(url, params, headers)
            response = urllib2.urlopen(req)
            return response.read()
        except Exception as e:
            sys.stderr.write(str(e))
            raise 
    def call(self, params):  
        return json.loads(self.post_request(self.url, params.as_hash()))
