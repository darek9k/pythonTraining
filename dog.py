class Dog:

    species = 'domestic dog'

    def __init__(self, race, name, age):
        self.race = race
        self.name = name
        self.age = age

    def bark(self):
        return "Hau! Hau!"

    def present(self):
        print("Race is" + self.race)
        print("Name is" + self.name)
        print("Age is" + str(self.age))


Lassie = Dog('Collie ', 'Lassie', 3)
print(Lassie.race)
print(Lassie.age)
print(Lassie.name)
print(Lassie.species)
print(Dog.species)

print(Lassie.bark())

Dog.present(Lassie)



