from Pb_Api.Param.Number import Pb_Api_Param_Number
import random
class Pb_Api_Param_Number(Pb_Api_Param): 
    def __init__(self, **kwargs):
      super(Pb_Api_Param_Number, self).__init__(**kwargs)  
      self._preferences = kwargs['preferences'] #ahhh if I name it preferences, then this can all just be number? yes
      self._max = kwargs['max']
      self._min = kwargs['min']
      self._ranges = kwargs['ranges']
      #now how do I add exclusions? well can add an array of ranges accepted instead of min/max, like:
# a bit more calulations that way, but more generic yeah lets do it so how does it read from the kwargs? just accept array, like options
#ahhh I think zoom is so different that it's a pain, it also requires float, where everything else  is an Int logic is same though, you can have Param_Number and Param_Float, probably if constructed properly one can inherit from another, but that's complications.
#ok so one thing that I'm learning is that inheritance does save code, but can be sort of the trickiest part of all OOP, 
#because it can be cnfusing having to plan out everything before you write, is that more or less true? yep
#so OOP without inheritance is ok, but just results in much more code? well yeah, it have more code, but you use OOP to not have much code than in prodcedural way, to avoid copy-pasting, and benefit from sort of collective changes of all classes then you add method to parent class. so 
#basically you almost always should use inheritance, unless it is just too difficult? no well it's not always necessary, but parameters like here it's should be with inhertance, becuase they are just all the same multiselect or select over virtual range of numbers.
#alright. I think I should take a break from this for a little while, read more code, and hopefully in about a week I'll understand it better
#already, I think Ive more ideas that are related to OOP, but do you think it's realistic to expect it to be a gradual process for me to 
#shift everything ovnker? or should I try to force it? just take it step by step, this project is a bit complicated, can be written in many ways one of then will use a lot of things from oop world, and can be hard to understand right from start, so just write it the way you get it and then we can optimize it more and more. Right, but primarily the way to learn is to USE libraries, and observe how they work, right? yes ok 
#part of the issue I think is that in my mind I'm thinking like a shell script, and that is bad for OOP because it seems like
#the shell really has nothing to do with any of this, calling the shell command on the terminal is ath bit different from calling a method here,
#or is that wrong? it's right but I should think that the shell itself is an object, and the commands are sort of the api for generating new 
#method calls? yeah if computer is an object with fs and all stuff, then shell is api for that object and calling commands is calling methods of this object, which change it's state (modify internal "variables"- files). ok cool, but the confusing thing about that is that the naming is
#all completely different from something like python or perl, right? yes ok cool I do understand, I  think this was just a little too ambitious.
#I'll work on some other code and come back to this next weekend. Thanks a lot for the help no problems

    def preferences(self):
      return self._preferences
    def randomize(self):
       weights_total = sum(map(lambda x: x["weight"], self.preferences()) + self._max - self._min 
       choice = random.randint(0, weights_total)
       position = 0i
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
