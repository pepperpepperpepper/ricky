"""base class for all params"""
import pprint


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

    def randomize(
            self,
            probabilities=None,
            probabilities_local=False
            ):
        """assign random values to all params
        if using a probabilities.json file, weight is taken
        into account"""
        if probabilities:
            probabilities = self._load_probabilities(probabilities)
        else if probabilities_local:
            probabilities = self._load_probabilities(probabilities_local)
        else:
            probabilities = {}
        for param in self._params:
            param.randomize(probability=probabilities.get(param.name))

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
