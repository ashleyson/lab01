#Animal Shelter
from Animal import Animal
class AnimalShelter:
    '''The AnimalShetler.py file will contatin the definition of what a
single AnimalShelter object is'''
    '''An AnimalShelter object will contain a dictioinary structure where
the keys of the dictioniary will be a str type representing an Animal's species
(All upper-case characters'''
    def __init__(self):
        self.dict = {}
        
    def addAnimal(self,animal):
        if animal.species in self.dict:
            self.dict[animal.species].append(animal)
        else:
            self.dict[animal.species] = [animal]
        
    def removeAnimal(self,animal):
        if animal in self.dict[animal.species]:
           self.dict[animal.species].remove(animal) 
           
    def getAnimalsBySpecies(self, species):
        x = ""
        species = species.upper()
        if species not in self.dict.keys(): 
            return x
        y = self.dict[species]
        for i in range(len(y)):
            if i == len(y)-1:
                x = x + y[i].toString() 
            else:
                x = x + y[i].toString() + "\n"
        return x
    
    def doesAnimalExist(self, animal):
        for i in self.dict.keys():
            if animal in self.dict[i]:
                return True
        return False
