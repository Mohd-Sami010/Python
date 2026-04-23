class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking")
        
class Child(Father, Mother):
    def show(self):
        print("Child inherits skills")

obj = Child()
obj.show()
obj.skills()   # Method resolution order (MRO)