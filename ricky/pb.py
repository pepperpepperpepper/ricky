import urllib
import urllib2
import sys
import simplejson as json
from ricky.config import OFFLINE


class Pb(object):
    def __init__(self):
        self._required_keys = []
        self.url = ""
        self._offline = OFFLINE

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
        except ValueError:
            sys.stderr.write(
                "Bad Post params or Url sent to photoblaster"
                "api.\n"
            )
        except urllib2.URLError:
            sys.stderr.write(
                "Could not complete post request to the given url:\n" +
                ("URL: %s\n" % url) +
                ("PARAMS: %s\n" % params)
            )

    def call(self, params):
        if self._offline:
            sys.path.append("./photoblaster")
            from photoblaster.modules import Pb
            from photoblaster.config import LOCAL as PBLOCAL
            for pbcls in Pb.__subclasses__():
                if pbcls.__name__ == self.__class__.__name__:
                    params_dict = params.as_dict()
                    instance = pbcls(**params_dict)
                    instance.create()
                    if not PBLOCAL:
                        instance.file_s3move()
                    return instance.file_dict()
        return json.loads(
            self.post_request(self.url, params.as_dict())
        )
