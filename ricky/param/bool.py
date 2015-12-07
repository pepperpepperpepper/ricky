from ricky.param import Param
import re
import random


class Bool(Param):
    def __init__(self, **kwargs):
        super(Bool, self).__init__(**kwargs)

    def value_get(self):
        return super(Bool, self).value_get()

    def value_set(self, value):
        value = self._bool_correct(value)
        super(Bool, self).value_set(value)

    value = property(value_get, value_set)

    def _bool_correct(self, value):
        value = str(value)
        if any([
            re.match(r'(true|1)', value, re.IGNORECASE),
            value == 1
        ]):
            value = True
        elif any([
            re.match(r'(false|0)', value, re.IGNORECASE),
            value == 0
        ]):
            value = False
        else:
            raise ValueError("Bad Value for Bool %s" % value)
        return value

    def randomize(self, probabilities=None):
        if probabilities and self._choose_from_probabilities(probabilities):
            return
        self.value = random.choice([True, False])

    def from_normalized(self, value):
        value_as_int = int(round(value, 0))
        self.value = True if value_as_int else False

    def as_normalized(self):
        return 1 if self.value else 0
