import pprint
class Pb_Api_Params(object):
  def __init__(self):
    self._api = None
  def param(self, name):
    for p in self.params: 
      if p.name == name:
        return p
    return None
  def __str__(self):
    return pprint.pformat({ "params": map(lambda x: vars(x), self.params) })


  def randomize(self):
    for el in self.params:
      if el.set_by_user:
        continue
      el.randomize()

  @property
  def api(self):
    return self._api 
  @api.setter
  def api(self, cls):
    self._api = cls

  #does this really have to be here in Pb_Api_Params? seems confusing though  yeah it has to be here because ImPattern inherits from it? impatter params 
  def execute(self):
    return self.api.call(self)

  def is_ready(self):
    for p in self.params:
      if not p.is_ready():
        return 0
    return 1
  def as_hash(self):
    result = {}
    for p in self.params:
      result[p.name] = p.value
    return result
