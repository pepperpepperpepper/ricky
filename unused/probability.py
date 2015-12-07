class Probability(dict):
  def __init__(self, **kwargs):
    super(Probability, self).__init__(**kwargs)
    self.value = kwargs["value"]
    self.weight = kwargs["weight"]
  def __getattr__(self, attr):
       return self.get(attr)
  __setattr__= dict.__setitem__
  __delattr__= dict.__delitem__
