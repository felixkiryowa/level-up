# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class GermanSpherd(Dog):
    pass


# Child class (inherits from Dog class)
class Bulldog(Dog):
    pass

# Create instances of dogs
dogs = [
    Bulldog("Tom", 6), 
    GermanSpherd("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
pets = Pets(dogs)

# Output
print("I have {} dogs.".format(len(pets.dogs)))
for dog in pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

are_the_dogs_hungry = True
for dog in pets.dogs:
    if dog.is_hungry:
        are_the_dogs_hungry = True

if are_the_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")