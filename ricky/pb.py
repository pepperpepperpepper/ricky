import os
import sys
import simplejson as json
from ricky.config import OFFLINE, PB_DATA_URL
import ricky.utils as utils


class Pb(object):
    def __init__(self):
        self.url = ""
        self._offline = OFFLINE

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
            utils.http_request(self.url, params=params.as_dict())
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
            print utils.http_request("%s?newfile=%s" % (PB_DATA_URL, newfile))
            raise NotImplementedError("Not yet implemented\n")
