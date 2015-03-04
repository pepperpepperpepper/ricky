class Pb_Api_Params(object):
    def _weighted_choice(self, param):
       weights_total = sum(map(lambda x: x["weight"], param))
       choice = random.randint(0, weights_total)
       position = 0
       for elem in param:
          position += elem["weight"]
          if position >= choice:
              return elem["value"]
    def _default_choice(self, param):
       heaviest_idx = 0
       heaviest_weight = 0
       idx = 0
       for elem in param:
          if elem["weight"] > heaviest_weight:
              heaviest_weight = elem["weight"]
              heaviest_idx = idx;
          idx += 1
       return param[heaviest_idx]["value"]
    def randomize(self):
       for el in self.params:
         if el.manually_set:
           continue
         el.randomize()
    def is_ready(self):
       for p in self.params():
         if not p.is_ready():
           return 0
       return 1
    def params(self):
       return self._params
    def param(self, name):
       for p in self.params():
         if p.name() == name:
           return p
       return None
    def as_hash(self):
       result = {}
       for p in self.params():
         result[p.name()] = p.value()
       return result
