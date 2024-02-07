class vehicle():
    def _init_(self):
        self.type = 'generic vehicle'
        
    def honk (self):
        return self._sound
    
    @property
    def wheels(self):
        return self.wheels
    
class motorcycle(vehicle):
    def _init_(self,make,model,year,color,sound):
        super()._init_(make,model,year)
        self._wheels = 4

class car(vehicle):
    def _init_(self, color, sound, make, model, year):
        super()._init_(make,model,year)
        self.color = color
        self._sound = sound
        self._wheels = 4

    
    
    
    
