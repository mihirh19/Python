class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


# Create objects of Animal, Dog, and Cat
animal = Animal()
dog = Dog()
cat = Cat()

# Call speak() method on Animal object
animal.speak()  # Output: Animal speaks

# Call speak() method on Dog object
dog.speak()  # Output: Dog barks

# Call speak() method on Cat object
cat.speak()  # Output: Cat meows
