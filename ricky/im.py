import urllib
import urllib2
import sys
import simplejson as json


class Im(object):
    def __init__(self):
        self._required_keys = []
        self.url = ""

    def post_request(self, url, params):
        params = urllib.urlencode(params)
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/40.0.2214.94 Safari/537.36"
            ),
            "Accept": "text/plain"
        }
        try:
            req = urllib2.Request(url, params, headers)
            response = urllib2.urlopen(req)
            return response.read()
        except urllib.error.HTTPError:
            sys.stderr.write("Post Request failed!")

    def call(self, params):
        return json.loads(
            self.post_request(self.url, params.as_dict())
        )
