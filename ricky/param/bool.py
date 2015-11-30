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
        if any in [
                   re.match(r'(true|1)', value, re.IGNORECASE),
                   value == 1,
                  ]:
            value = True
        elif any in [
                     re.match(r'(false|0)', value, re.IGNORECASE),
                     value == 0,
                    ]:
            value = False
        else:
            raise ValueError("Bad Value for Bool %s" % value)
        return value

    def randomize(self):
        self.value_set(random.choice([True, False]))
