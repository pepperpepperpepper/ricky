import urllib
import urllib2
import sys
import random
def post_request(url, params):
    params = urllib.urlencode(params)
    sys.stderr.write(params)
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

class Service:
    def __init__(self):
        self._required_keys = []
        self.url = ""
    def new(self, params):
        for k in self._required_keys:
            if not k in params:
                params[k] = "";
        self.current_params = params
        return json.loads(post_request(self.url, self.current_params))

class Pb_Api_Params:
    def _weighted_choice(self, param):
       weights_total = sum(map(lambda x: x["weight"], param))
       choice = random.randint(0, weights_total)
       position = 0
       for elem in param:
          position += elem["weight"]
          if position >= choice:
              return elem["value"]
    def _default_choice(self, param):
       heaviest_idx = 0
       heaviest_weight = 0
       idx = 0
       for elem in param:
          if elem["weight"] > heaviest_weight:
              heaviest_weight = elem["weight"]
              heaviest_idx = idx;
          idx += 1
       return param[heaviest_idx]["value"]
