from ricky.param import Param
import random
import math
import decimal
import re


class Color(Param):
    def __init__(self, **kwargs):
        super(Color, self).__init__(**kwargs)

    @classmethod
    def from_rgb(cls, r, g, b):
        return cls(value="rgb({},{},{})".format(r, g, b), is_rgb=True)

    def as_hex(self):
        matched = re.match(
            r'rgb\(([0-9]+),([0-9]+),([0-9]+)\)',
            self.value,
            re.IGNORECASE
        )
        return ''.join(
            [hex(int(num)).split('x')[1] for num in matched.groups()]
        )

    def from_normalized(self, value):
        maximum = math.pow(16, 6) - 1
        hex_val = hex(int(round(maximum * value, 0)))
        matched = re.match('0x(..)(..)(..)', hex_val)
        vals = [int(num, 16) for num in matched.groups()]
        self.value = "rgb({},{},{})".format(vals[0], vals[1], vals[2])

    def as_normalized(self):
        maximum = math.pow(16, 6) - 1
        value = int(self.as_hex(), 16)
        return decimal.Decimal(value)/decimal.Decimal(maximum)

    def randomize(self):
        self.value = "rgb(%s,%s,%s)" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self._is_rgb = True
