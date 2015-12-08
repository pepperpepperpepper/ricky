import os
import urllib
import urllib2
import sys
import simplejson as json
from ricky.config import OFFLINE, PB_DATA_URL


class Pb(object):
    def __init__(self):
        self._required_keys = []
        self.url = ""
        self._offline = OFFLINE

    def http_request(self, url, params={}):
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
            if params:
                req = urllib2.Request(url, params, headers)
            else:
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
            from photoblaster.modules import Pb as _Pb
            from photoblaster.config import LOCAL as PBLOCAL
            for pbcls in _Pb.__subclasses__():
                if pbcls.__name__ == self.__class__.__name__:
                    params_dict = params.as_dict()
                    instance = pbcls(**params_dict)
                    instance.create()
                    if not PBLOCAL:
                        instance.file_s3move()
                    return instance.file_dict()
        return json.loads(
            self.http_request(self.url, params=params.as_dict())
        )

    def data_from_url(self, url):
        """
        retrieves image params from db using the url
        """
        newfile = os.path.split(url)[-1]
        if self._offline:
            sys.path.append("./photoblaster")
            from photoblaster.db.models.imcmd import ImCmd
            result = ImCmd.search(newfile=newfile).first()
            try:
                return {
                    "module": result.tag.split(":")[0],
                    "params": json.loads(result.dataobj)
                }
            except AttributeError:
                sys.stderr.write("No usable data found in db\n")
                return None
        else:
            print self.http_request("%s?newfile=%s" % (PB_DATA_URL, newfile))
            raise NotImplementedError("Not yet implemented\n")
