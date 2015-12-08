import os
import sys
import urllib
import urllib2
import simplejson as json
from ricky.config import OFFLINE, PB_DATA_URL


def data_from_url(url):
    """
    retrieves image params from db using the url
    """
    newfile = os.path.split(url)[-1]
    if OFFLINE:
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
        print http_request("%s?newfile=%s" % (PB_DATA_URL, newfile))
        raise NotImplementedError("Not yet implemented\n")


def http_request(url, params={}):
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
