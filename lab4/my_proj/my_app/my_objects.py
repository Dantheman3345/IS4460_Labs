class Car:
    def __init__(self, color, sound,year,make,model):
        self.color = color
        self._sound = sound
        self._wheels = 4

    @property
    def honk (self):
        return self._sound
    
    @property
    def wheels(self):
        return self._wheels
    

class Vehicle:
    def __init__(self, make,model,year,color,sound):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._sound = sound
        self._wheels = None

    @property
    def honk (self):
        return self._wheels
    
    @property
    def wheels(self):
        return self._wheels
    

class Motorcycle(Vehicle):
    def __init__(self, make, model, year,color,sound):
        super().__init__(make,model,year,color,sound)

        self._wheels = 2

class Car(Vehicle):
    def __init__(self, make, model, year,color,sound):
        super().__init__(make,model,year,color,sound)

        self._wheels = 4

    