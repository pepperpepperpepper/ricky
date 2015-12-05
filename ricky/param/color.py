from ricky.param import Param
import random


class Color(Param):
    def __init__(self, **kwargs):
        super(Color, self).__init__(**kwargs)

    @classmethod
    def from_rgb(cls, r, g, b):
        return cls(value="rgb({},{},{})".format(r, g, b))

    def randomize(self):
        self.value = "rgb(%s,%s,%s)" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
