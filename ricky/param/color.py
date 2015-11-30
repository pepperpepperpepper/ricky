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

    def randomize(self):
        self.value = "rgb(%s,%s,%s)" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
