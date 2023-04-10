# Parent class: Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("The animal speaks.")

    def eat(self):
        print("The animal eats.")


# Child class: Dog, inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the __init__ method of the parent class using super()
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        print("The dog barks.")

    def fetch(self):
        print("The dog fetches.")


# Child class: Cat, inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Call the __init__ method of the parent class using super()
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        print("The cat meows.")

    def scratch(self):
        print("The cat scratches.")


# Create objects of the child classes
dog1 = Dog("Buddy", "Labrador")
cat1 = Cat("Fluffy", "White")

# Access attributes and methods of parent class and child classes
print(dog1.name)  # Output: Buddy
print(cat1.species)  # Output: Cat

dog1.speak()  # Output: The dog barks.
cat1.speak()  # Output: The cat meows.

dog1.fetch()  # Output: The dog fetches.
cat1.scratch()  # Output: The cat scratches.

dog1.eat()  # Output: The animal eats.
cat1.eat()  # Output: The animal eats.
