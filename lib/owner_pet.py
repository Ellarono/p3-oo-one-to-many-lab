class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner  # Assign owner if provided

        if owner:
            owner.add_pet(self)  # Automatically add this pet to the owner's list

        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets  # Return the list of pets

    def add_pet(self, pet):
        if isinstance(pet, Pet) and pet not in self._pets:
            self._pets.append(pet)
            pet.owner = self  # Assign this owner to the pet
        elif not isinstance(pet, Pet):
            raise ValueError("Can only add instances of Pet")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)  # Sort pets by name
