class Mammal:
    className = 'Mammal'


class Dog(Mammal):
    species = 'Canis lupus'


dog = Dog
print(dog.className)
print(dog.species)
