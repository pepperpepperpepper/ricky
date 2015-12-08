import sys
import urllib
import urllib2


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
