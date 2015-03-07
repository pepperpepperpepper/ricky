from Pb_Api.Param import Pb_Api_Param
import random
class Pb_Api_Param_Color(Pb_Api_Param): 
    def __init__(self, **kwargs):
      self._preferred_colors = kwargs['preferred_colors']
      super(Pb_Api_Param_Color, self).__init__(**kwargs)  

    @classmethod
    def from_rgb(cls, r,g,b):
      return cls(value="rgb({},{},{})".format(r,g,b))


    def preferred_colors(self):
      return self._preferred_colors
    
    def randomize(self):
       weights_total = sum(map(lambda x: x["weight"], self.preferred_angles()) +  (255 * 255 * 255)  #so this is the only thing that changes? yeah and 
       choice = random.randint(0, weights_total)
       position = 0
       for elem in self.options():
          position += elem["weight"] 
          if position >= choice:
              self.value = elem["value"]
              break
       self.value = "rgb({},{},{})".format(
         random.randint(0,255),
         random.randint(0,255),
         random.randint(0,255),
       )
    def _choose_heaviest(self):
       heaviest_idx = 0
       heaviest_weight = 0
       idx = 0
       for elem in self.options():
          if elem["weight"] > heaviest_weight:
              heaviest_weight = elem["weight"]
              heaviest_idx = idx;
          idx += 1
       return self.options()[heaviest_idx]["value"]
    def heaviest(self):
       self.value = self._get_heaviest()
