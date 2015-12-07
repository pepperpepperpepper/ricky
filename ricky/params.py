"""base class for all params"""
import pprint
import simplejson as json
import sys
import os
from ricky.config import PROBABILITIES_DIR


class Params(object):
    def __init__(self, *args):
        self._api = None
        self._params = args

    def __getitem__(self, name):
        """getter for the param by name"""
        for param in self._params:
            if param.name == name:
                return param
        raise ValueError("No param with name %s\n" % name)

    def __str__(self):
        """string representation"""
        return pprint.pformat(self.as_dict())

    def _load_probabilities_json(self, probabilities_file=None):
        if probabilities_file:
            filepath = probabilities_file
        else:
            filepath = os.path.join(
                PROBABILITIES_DIR,
                "%s.json" % (self.api.__class__.__name__)
            )
        try:
            f = open(filepath, 'r')
            data = f.read()
            f.close()
            return json.loads(data)
        except json.scanner.JSONDecodeError as e:
            sys.stderr.write("Invalid Json - Problem decoding %s\n" % filepath)
            sys.stderr.write("%s\n" % e)
            sys.exit(1)
        except IOError:
            sys.stderr.write(
                "Could not find probabilities file %s\n" % filepath)
            sys.exit(1)

    def randomize(
            self,
            probabilities=None,
            probabilities_local=False
            ):
        """assign random values to all params
        if using a probabilities.json file, weight is taken
        into account"""
        if probabilities:
            probabilities_dict = self._load_probabilities_json(probabilities)
        elif probabilities_local:
            probabilities_dict = self._load_probabilities_json()
        else:
            probabilities_dict = {}
        for param in self._params:
            param.randomize(probabilities=probabilities_dict.get(param.name))

    @property
    def api(self):
        """property setter for im api"""
        return self._api

    @api.setter
    def api(self, cls):
        """property getter for im api"""
        self._api = cls

    def execute(self):
        """calls the associated api"""
        return self.api.call(self)

    def as_dict(self):
        """displays the params names and values in dictionary form
           used by the api call
        """
        result = {}
        for param in self._params:
            result[param.name] = param.value
        return result

    def from_dict(self, params_dict):
        """set param values manually from a dictionary"""
        for param in self._params:
            if param.name in params_dict.keys():
                param.value_set(params_dict[param.name])
