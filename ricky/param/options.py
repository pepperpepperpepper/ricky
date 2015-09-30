from ricky.param.option import Option
import sys
class Options:
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
    options = map(lambda x: Option(**x), args);
    return cls(*options);
