import random
from ricky.param import Param


class NumberRange(Param):
    def __init__(self, **kwargs):
        super(NumberRange, self).__init__(**kwargs)
        self.range_min = kwargs['min']
        self.range_max = kwargs['max']

    def randomize(self):
        weights_total = sum(
                map(lambda x: x["weight"], self.options())
            ) + self.range_max - self.range_min
        choice = random.randint(0, weights_total)
        position = 0
        for elem in self.options():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                return
        
        val = random.randint(self.range_min, self.range_max)
        self.value = val
        
    @property
    def value(self):
        return super(NumberRange, self).value_get()

    @value.setter
    def value(self, value):
        self._value = value
        if self._value and \
            (self._value < self.range_min or self._value > self.range_max):
            raise ValueError(
                "Value must be between %s and %s\n" % (
                    self.range_min, self.range_max
                )
            )
        if self._value is not None:
            self.is_ready = 1
        self.set_by_user = 1
