import pprint
import sys

class Param(object):
    def __init__(
            self,
            required=0,
            set_by_user=0,
            value=None,
            name=None,
            **kwargs):
        self._value_default = None
        self.name = name
        self.required = required
        self.is_ready = 0
        self._value = value
        self.set_by_user = set_by_user
        self._selections = kwargs.get('selections') or []
        if len(self._selections):
            self._validate_selections()
            """default value is the selection with the heaviest weight"""
            self.default(self._choose_heaviest())

    def selections(self):
        return self._selections

    def _validate_selections(self):
        try:
            int(self._selections[0]['weight'])
            self._selections[0]['value']
        except Exception:
            raise ValueError('Unable to validate %s\n:' % self.name)

    def __str__(self):
        return pprint.pformat(vars(self))

    def value_get(self):
        if self.set_by_user == 1:
            return self._value
        return self._value_default

    def value_set(self, value):
        self._value = value
#        sys.stderr.write("trying to set %s - %s: %s \n" %
#            (
#                self.__class__.__name__,
#                self.name,
#                value
#            )
#        )
        if self._value:
            self.is_ready = 1
        self.set_by_user = 1

    value = property(value_get, value_set)

    def default(self, value):
        self._value_default = value

    @property
    def is_ready(self):
        return self._is_ready or not self.required

    @is_ready.setter
    def is_ready(self, n):
        self._is_ready = n

    def randomize(self):
        pass

    def _choose_heaviest(self):
        heaviest_idx = 0
        heaviest_weight = 0
        idx = 0
        if (len(self.selections())):
            for elem in self.selections():
                if elem["weight"] > heaviest_weight:
                    heaviest_weight = elem["weight"]
                    heaviest_idx = idx
                idx += 1
            return self.selections()[heaviest_idx]["value"]
        else:
            self.randomize()

    def heaviest(self):
        self.value = self._choose_heaviest()
