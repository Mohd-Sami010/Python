class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
class Bird:
    def speak(self):
        return "Tweet!"
def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
bird = Bird()
make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(bird)