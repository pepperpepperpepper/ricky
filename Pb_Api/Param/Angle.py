from Pb_Api.Param import Pb_Api_Param
import random
from config import ANGLE_MAX, ANGLE_MIN
class Pb_Api_Param_Angle(Pb_Api_Param): 
    def __init__(self, **kwargs):
      self._preferred_angles = kwargs['preferred_angles']
      super(Pb_Api_Param_Angle, self).__init__(**kwargs)  

    @classmethod
    def from_rgb(cls, r,g,b):
      return cls(value="rgb({},{},{})".format(r,g,b))


    def preferred_angles(self):
      return self._preferred_angles
    def randomize(self):
       weights_total = sum(map(lambda x: x["weight"], self.preferred_angles()) + ANGLE_MAX - ANGLE_MIN   
       choice = random.randint(0, weights_total)
       position = 0
       for elem in self.options():
          position += elem["weight"] 
          if position >= choice:
              self.value = elem["value"]
              break
       self.value = random.randint(ANGLE_MIN,ANGLE_MAX),
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
