import random
from ricky.param import Param
DEFAULT_RAND_MAX = 1000
DEFAULT_RAND_MIN = -1000


class ConstrainedNumber(Param):
    def __init__(self, **kwargs):
        self.range_min = kwargs.get('min')
        self.range_max = kwargs.get('max')
        self.forbidden = kwargs.get('forbidden')
        self.forbidden_range_min = kwargs.get('forbidden_range_min')
        self.forbidden_range_max = kwargs.get('forbidden_range_max')
        self.assert_int = kwargs.get('assert_int')
        if kwargs.get("default") is not None:
            self._default = kwargs.get("default")
        else:
            self.randomize()
            self._default = self._value
        super(ConstrainedNumber, self).__init__(**kwargs)

    @property
    def value(self):
        return super(ConstrainedNumber, self).value_get()

    @value.setter
    def value(self, value):
        if value is not None and (
            self._value < self.range_min or
            self._value > self.range_max
        ):
            raise ValueError(
                "Value must be between %s and %s\n" % (
                    self.range_min, self.range_max
                )
            )
        if value == self.forbidden:
            raise ValueError(
                "Value %s is forbidden" % value
            )
        if (self.forbidden_range_max or self.forbidden_range_max == 0) and \
                self.forbidden_range_max >= value:
                raise ValueError(
                    "In forbidden range: Value %s is below %s" %
                    (value, self.forbidden_range_max)
                )
        if (self.forbidden_range_min or self.forbidden_range_min == 0) and \
                self.forbidden_range_min <= value:
                raise ValueError(
                    "In forbidden range: Value %s is above %s" %
                    (value, self.forbidden_range_min)
                )
        if self.assert_int and type(value) != int:
            raise ValueError(
               "Value %s is not an int" % value
            )
        self._value = value

    def __str__(self):
        value_dict = {
           'value': self._value,
        }
        for attr in (
            'range_min', 'range_max', 'forbidden', 'forbidden_range_min',
            'forbidden_range_max', 'assert_int'
        ):
            attr_val = getattr(self, attr)
            if attr_val or attr_val == 0:
                value_dict[attr] = attr_val
        return "Constrained Number Range \"%s\":\n %s" % (self.name, value_dict)

    def _generate_random(self):
        value = random.uniform(DEFAULT_RAND_MIN, DEFAULT_RAND_MAX)
        if self.assert_int:
            value = int(value)
        self.value = value

    def randomize(self):
        tries = 0
        tries_max = 30
        try:
            self._generate_random()
        except ValueError:
            tries += 1
            if tries < tries_max:
                self._generate_random()
            else:
                raise ValueError(
                    "Unable to set random value on %s in %s tries"
                ) % (self.name, self.tries_max)
