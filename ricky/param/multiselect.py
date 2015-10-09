import random
from ricky.param import Param


class MultiSelect(Param):
    def __init__(self, **kwargs):
        super(MultiSelect, self).__init__(**kwargs)

    def value_get(self):
        return super(MultiSelect, self).value_get()

    def value_set(self, value):
        if not any([value == i['value'] for i in self._options]) and \
            value is not None:
            raise ValueError
        super(MultiSelect, self).value_set(value)

    value = property(value_get, value_set)

    def randomize(self):
        weights_total = sum(map(lambda x: x["weight"], self.options()))
        choice = random.randint(0, weights_total)
        position = 0
        for elem in self.options():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                break

