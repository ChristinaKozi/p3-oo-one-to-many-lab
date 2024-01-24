class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str) or not isinstance(pet_type, str):
            raise Exception("Invalid input types for Pet initialization")
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            Pet.all.append(self)
            print(f"Created pet: {self.name}")
        else:
            raise Exception("Invalid pet_type")


class Owner:
    def __init__(self,name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet,Pet) and pet.pet_type in Pet.PET_TYPES:
            pet.owner = self
        else:
            raise Exception("Invalid pet or pet type")

    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda pet: pet.name)

    
owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)