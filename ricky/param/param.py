import pprint
import sys

class Param(object):
    def __init__(
            self,
            required=0,
            set_by_user=0,
            value=None,
            name=None,
            **kwargs):
        self._value_default = None
        self.name = name
        self.required = required
        self.is_ready = 0
        self._value = value
        self.set_by_user = set_by_user

    def __str__(self):
        return pprint.pformat(vars(self))

    def value_get(self):
        if self.set_by_user == 1:
            return self._value
        return self._value_default

    def value_set(self, value):
        self._value = value
        sys.stderr.write("trying to set %s: %s \n" % (self.name, value))
        if self._value:
            self.is_ready = 1
        self.set_by_user = 1

    value = property(value_get, value_set)

    def default(self, value):
        self._value_default = value

    @property
    def is_ready(self):
        return self._is_ready or not self.required

    @is_ready.setter
    def is_ready(self, n):
        self._is_ready = n

    def randomize(self):
        pass
