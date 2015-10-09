from ricky.param import Param
import random


class Color(Param):
    def __init__(self, **kwargs):
        super(Color, self).__init__(**kwargs)

    @classmethod
    def from_rgb(cls, r, g, b):
        return cls(value="rgb({},{},{})".format(r, g, b))

    @property
    def value(self):
        return super(Color, self).value_get()

    @value.setter
    def value(self, value):
        self._value = value
        if self._value is not None:
            self.is_ready = 1
        self.set_by_user = 1

    def randomize(self):
        weights_total = sum(
            map(lambda x: x["weight"], self.options())
        ) + (255 * 255 * 255)
        choice = random.randint(0, weights_total)
        position = 0
        for elem in self.options():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                return
        self.value = "rgb(%s,%s,%s)" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
