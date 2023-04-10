# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Dog barks")


dog = Dog("Buddy", "Labrador")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Labrador
dog.speak()  # Output: Dog barks


# Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")


class Mammal(Animal):
    def speak(self):
        print("Mammal speaks")


class Dog(Mammal):
    def speak(self):
        print("Dog barks")


dog = Dog()
dog.speak()  # Output: Dog barks


# Multiple Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


class Pet(Dog, Cat):
    pass


pet = Pet()
pet.speak()  # Output: Dog barks


# Hybrid Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")


class Mammal(Animal):
    def speak(self):
        print("Mammal speaks")


class Bird(Animal):
    def speak(self):
        print("Bird chirps")


class Bat(Mammal, Bird):
    pass


bat = Bat()
bat.speak()  # Output: Mammal speaks


# Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows
