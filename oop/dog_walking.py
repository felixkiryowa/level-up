class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Parent class Dog
class Dog:

    # Initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method walking 
    def walk(self):
        return f"{self.name} is walking!"


# GermanySpherd class (inherits from Dog class)
class GermanySpherd(Dog):
    pass

# Child class (inherits from Dog class)
class Bulldog(Dog):
    pass

# Create instances of dogs
dogs = [
    Bulldog("Tom", 6), 
    GermanySpherd("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pet class
pets = Pets(dogs)

pets.walk()