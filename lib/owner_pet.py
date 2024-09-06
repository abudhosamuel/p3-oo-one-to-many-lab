class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet to the owner's list of pets if owner is specified
        if owner:
            owner.add_pet(self)

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet requires a Pet instance")
        if pet not in self._pets:
            self._pets.append(pet)
            pet.owner = self  # Set the owner attribute of the pet when adding

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
