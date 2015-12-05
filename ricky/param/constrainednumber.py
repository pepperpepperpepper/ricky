import random
from ricky.param import Param
DEFAULT_RAND_MAX = 1000
DEFAULT_RAND_MIN = -1000


class ConstrainedNumber(Param):
    def __init__(self, **kwargs):
        self.range_min = kwargs.get('min', DEFAULT_RAND_MIN)
        self.range_max = kwargs.get('max', DEFAULT_RAND_MAX)
        self.forbidden = kwargs.get('forbidden')
        self.forbidden_range_min = kwargs.get('forbidden_range_min')
        self.forbidden_range_max = kwargs.get('forbidden_range_max')
        self.enforce_int = kwargs.get('enforce_int')
        self.prec = kwargs.get('prec')
        if "default" not in kwargs:
            self.randomize()
            kwargs["default"] = self._value
        super(ConstrainedNumber, self).__init__(**kwargs)

    @property
    def value(self):
        return super(ConstrainedNumber, self).value_get()

    @value.setter
    def value(self, value):
        if value is not None and (
            value < self.range_min or
            value > self.range_max
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
        if self.enforce_int and type(value) != int:
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
            'forbidden_range_max', 'enforce_int'
        ):
            attr_val = getattr(self, attr)
            if attr_val or attr_val == 0:
                value_dict[attr] = attr_val
        return "Constrained Number Range \"%s\":\n %s" % (self.name, value_dict)

    def _generate_random(self):
        value = random.uniform(self.range_min, self.range_max)
        if self.prec:
            value = round(value, self.prec)
        if self.enforce_int:
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
