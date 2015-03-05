import pprint
class Pb_Api_Params(object):
    #so how do we need to change these?
    def param(self, name):
       for p in self.params: 
         if p.name == name:
           return p
       return None

    def __str__(self):
      return pprint.pformat({ "params": map(lambda x: vars(x), self.params) })

#do we need to add a simple __iter__ attribute to that class so that map will work, or is it already
#iterating? it is already



    def randomize(self):
       for el in self.params:
         if el.set_by_user:
           continue
         el.randomize()


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
