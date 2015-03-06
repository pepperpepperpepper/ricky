class Pb_Api_Param_Options:
  def __init__(self, arr):
    self._values = arr
  def __iter__(self):
    return iter(self._values)
  def __str__(self):
    return str(self._values)
  def __getitem__(self, i):
    return self._values[i]
  def search(self, s):
    for i in self:
      if str(s) in i.value:
        return i
