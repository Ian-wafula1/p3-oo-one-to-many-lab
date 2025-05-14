class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception()
        else:
            self.pet_type = pet_type
        
        if owner != None and not isinstance(owner, Owner):
            raise Exception()
        
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception()
    
    def get_sorted_pets(self):
        pets = self.pets()
        pets.sort(key=lambda x: x.name)
        return pets
        
owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)
print(owner.get_sorted_pets())