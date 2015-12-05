import pprint


class Param(object):
    def __init__(
                 self,
                 required=False,
                 set_by_user=False,
                 name=None,
                 **kwargs
                ):
        self._value_default = None
        self.name = name
        self.required = required
        self._value_default = kwargs.get("default") or None

        if not hasattr(self, "set_by_user"):
            self._set_by_user = set_by_user
        if self.value is not None and \
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

    def randomize(self):
        pass
