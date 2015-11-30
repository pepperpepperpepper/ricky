import random
from ricky.param import Param


class MultiSelect(Param):
    def __init__(self, **kwargs):
        super(MultiSelect, self).__init__(**kwargs)
        self._options = kwargs.get('options') or []
        if len(self._options):
            self._validate_options()

    def options(self):
        return self._options

    def _validate_options(self):
        try:
            pass
        except Exception:
            raise ValueError('Unable to validate %s\n:' % self.name)

    def value_get(self):
        return super(MultiSelect, self).value_get()

    def value_set(self, value):
        if value not in self._options and value is not None:
            raise ValueError
        super(MultiSelect, self).value_set(value)

    value = property(value_get, value_set)

    def randomize(self):
        self.value_set(random.choice(self.options))
