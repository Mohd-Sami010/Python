# WAP to invoke a method on an object without knowing the type of an object
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

# Function to invoke speak method without knowing the type
def make_animal_speak(animal):
    print(animal.speak())

# Create instances of different animal classes
dog = Dog()
cat = Cat()
bird = Bird()

# Invoke the speak method without knowing the type
make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(bird)