import sys
import pprint
class Params(object):
  def __init__(self):
    self._api = None
    self._params = []

  def param(self, name):
    for p in self._params:
      if p.name == name:
        return p
    return None

  def __str__(self):
    return pprint.pformat({ "params": map(lambda x: vars(x), self._params) })

  def randomize(self):
    for el in self._params:
      if el.set_by_user:
        continue
      el.randomize()

  @property
  def api(self):
    return self._api

  @api.setter
  def api(self, cls):
    self._api = cls


  def execute(self):
    return self.api.call(self)

  def is_ready(self):
    for p in self._params:
      if not p.is_ready and not p.default:
        sys.stderr.write("param not ready: {}".format(p))
        return 0
    return 1

  def __dict__(self):
    result = {}
    for p in self._params:
      result[p.name] = p.value
    return result

  def as_dict(self):
    return self.__dict__()
