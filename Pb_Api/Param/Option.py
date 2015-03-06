class Pb_Api_Param_Option(dict):
  def __init__(self, **kwargs):
    super(Pb_Api_Param_Option, self).__init__(**kwargs)
    self.value = kwargs["value"]
    self.weight = kwargs["weight"]
  def __getattr__(self, attr):
       return self.get(attr)
  __setattr__= dict.__setitem__
  __delattr__= dict.__delitem__
