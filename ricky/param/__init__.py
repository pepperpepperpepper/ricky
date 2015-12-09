import pprint
import random


class Param(object):
    def __init__(
                 self,
                 required=False,
                 set_by_user=False,
                 name=None,
                 **kwargs
                ):
        self.name = name
        self.required = required
        self._value_default = kwargs.get("default") or None

        if not hasattr(self, "set_by_user"):
            self._set_by_user = set_by_user
        if hasattr(self, "value") and self.value is not None and \
                kwargs.get("value") is not None:
            self._value = kwargs.get("value")
        else:
            self._value = self._value_default or None  # maybe FIXME

    def as_dict(self):
        return {
            'type': self.__class__.__name__,
            'required': self.required,
            'name': self.name,
            'default': self.default,
            'value': self.value
        }

    def __str__(self):
        return pprint.pformat(self.as_dict())

    def value_get(self):
        if self._set_by_user:
            return self._value
        return self._value_default

    def value_set(self, value):
        self._value = value
        self._set_by_user = True

    value = property(value_get, value_set)

    def default_set(self, value):
        raise ValueError("Default must be set at instantiation")

    def default_get(self):
        return self._value_default

    default = property(default_get, default_set)

    def _choose_from_probabilities(self, probabilities):
        """
            if using weights, considers all weights as a percentage of
            100
        """
        choice = random.randint(0, 100)
        position = 0
        for elem in probabilities:
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                return True
        return False

    def randomize(self, probabilities=None):
        pass

    def from_normalized(self, value):
        pass

    def as_normalized(self):
        if self.value:
            return 1
        return 0
