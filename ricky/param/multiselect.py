import random
from ricky.param import Param


class MultiSelect(Param):
    def __init__(self, **kwargs):
        self._options = kwargs.get('options') or []
        super(MultiSelect, self).__init__(**kwargs)
        if len(self._options):
            self._validate_options()
            """default value is the option with the heaviest weight"""
            self.default(self._choose_heaviest())

    def options(self):
        return self._options

    def _validate_options(self):
        try:
            int(self._options[0]['weight'])
            self._options[0]['value']
        except Exception:
            raise ValueError('Unable to validate %s\n:' % self.name)

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

    def _choose_heaviest(self):
        heaviest_idx = 0
        heaviest_weight = 0
        idx = 0
        if (len(self.options())):
            for elem in self.options():
                if elem["weight"] > heaviest_weight:
                    heaviest_weight = elem["weight"]
                    heaviest_idx = idx
                idx += 1
            return self.options()[heaviest_idx]["value"]
        else:
            self.randomize()

    def heaviest(self):
        self.value = self._choose_heaviest()
