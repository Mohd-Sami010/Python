# Create a custom iterator that returns squares of numbers up to N.

class Squares:
    def __init__(self, num):
        self.num = num
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.num:
            self.count+=1
            return self.count ** 2
        else:
            raise StopIteration

for i in Squares(20):
    print(i)