from ricky.param.selection import Selection
import sys
class Selections:
  def __init__(self, *args):
    self._values = args
  def __iter__(self):
    return iter(self._values)
  def __len__(self):
    return len(self._values)
  def __str__(self):
    return str(self._values)
  def __getitem__(self, i):
    return self._values[i]
  def search(self, s):
    for i in self:
      if str(s) in i.value:
        return i
  @classmethod
  def from_dict(cls, *args):
    selections = map(lambda x: Selection(**x), args);
    return cls(*selections);
