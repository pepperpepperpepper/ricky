import random
from ricky.param import Param


class Enum(Param):
    def __init__(self, options=None, **kwargs):
        self._options = options
        if not self._options:
            raise ValueError("Object must be initialized with options set")
        super(Enum, self).__init__(**kwargs)
        self._validate_options()

    def options(self):
        return self._options

    def _validate_options(self):
        try:
            pass
        except Exception:
            raise ValueError('Unable to validate %s\n:' % self.name)

    def value_get(self):
        return super(Enum, self).value_get()

    def value_set(self, value):
        if value not in self._options and value is not None:
            raise ValueError
        super(Enum, self).value_set(value)

    value = property(value_get, value_set)

    def randomize(self):
        self.value_set(random.choice(self._options))
