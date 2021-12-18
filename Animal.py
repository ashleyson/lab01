#Animal.py

class Animal:
    '''THe animal.py file will contain the definitioin of what an animal is'''
    
    def __init__(self, species = None, weight = None, age = None, name = None):
        if species == None:    
            self.species = species
        else:
            self.species = species.upper()
        self.weight = weight
        self.age = age
        if name == None:    
            self.name = name
        else: 
            self.name = name.upper()
#setter methods        
    def setSpecies(self, species):
        self.species = species.upper() 
        
    def setWeight(self, weight):
        self.weight = weight
        
    def setAge(self, age):
        self.age = age
        
    def setName(self, name):
        self.name = name.upper()
        
    def toString(self):
        x = "Species: {}, Name: {}, Age: {}, Weight: {}".format(self.species, self.name, self.age, self.weight)   
        return x
