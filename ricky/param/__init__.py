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
        self.set_by_user = set_by_user
        self._value_default = kwargs.get("default") or None

        if self.value is not None and \
                kwargs.get("value") is not None:
            self._value = kwargs.get("value")
        else:
            self._value = self._value_default or None  # maybe FIXME
        if not hasattr(self, "set_by_user"):
            self.set_by_user = set_by_user

    def __str__(self):
        return pprint.pformat(vars(self))  # FIXME needs to be more explicit

    def value_get(self):
        if self.set_by_user == 1:
            return self._value
        return self._value_default

    def value_set(self, value):
        self._value = value

    value = property(value_get, value_set)

    def default_set(self, value):
        raise ValueError("Default must be set at instantiation")

    def default_get(self, value):
        return self._value_default

    default = property(default_set, default_get)

    def randomize(self):
        pass
