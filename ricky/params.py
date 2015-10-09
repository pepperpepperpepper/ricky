"""base class for all params"""
import sys
import pprint


class Params(object):
    def __init__(self, *args):
        self._api = None
        self._params = args

    def define_from_list(self, definitions_list):
        self._params = definitions_list

    def param(self, name):
        """getter for the param by name"""
        for param in self._params:
            if param.name == name:
                return param
        return None

    def __str__(self):
        """string representation"""
        return pprint.pformat({"params": map(lambda x: vars(x), self._params)})

    def randomize(self):
        """assign random values to all params, taking into account weight"""
        for param in self._params:
            if param.set_by_user:
                continue
            param.randomize()


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

    def is_ready(self):
        """test to see if any params with required values are missing"""
        for param in self._params:
            if not param.is_ready and not param.default:
                sys.stderr.write("param not ready: %s\n" % param)
                return 0
        return 1

    def __dict__(self):
        result = {}
        for param in self._params:
            result[param.name] = param.value
        return result

    def as_dict(self):
        """alias for __dict__"""
        return self.__dict__()

    def from_dict(self, params_dict):
        """set param values manually from a dictionary"""
        for param in self._params:
            if param.name in params_dict.keys():
                param.value_set(params_dict[param.name])
