class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of pets that belong to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to the owner, if the pet is an instance of Pet"""
        if not isinstance(pet, Pet):
            raise Exception("You can only add instances of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of pets by their names"""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self._pet_type = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner.")
        self._owner = value

    def __repr__(self):
        return f"<Pet {self.name}, Type: {self.pet_type}>"

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
