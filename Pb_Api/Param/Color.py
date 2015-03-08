from Pb_Api.Param.MultiSelect import Pb_Api_Param_MultiSelect
import random
class Pb_Api_Param_Color(Pb_Api_Param_MultiSelect): 
    def __init__(self, **kwargs):
      super(Pb_Api_Param_Color, self).__init__(**kwargs)  

    @classmethod
    def from_rgb(cls, r,g,b):
      return cls(value="rgb({},{},{})".format(r,g,b))
    

    def randomize(self):
       weights_total = sum(map(lambda x: x["weight"], self.options()) +  (255 * 255 * 255) 
       choice = random.randint(0, weights_total)
       position = 0
       for elem in self.options():
          position += elem["weight"] 
          if position >= choice:
              self.value = elem["value"]
              return
       self.value = "rgb({},{},{})".format(
         random.randint(0,255),
         random.randint(0,255),
         random.randint(0,255),
       )
