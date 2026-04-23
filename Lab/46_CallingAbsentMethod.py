class A:
    def show(self):
        print("Method in A")
class B:
    def display(self):
        print("Method in B")
def call_method(obj):
    if hasattr(obj, "show"):
        obj.show()
    else:
        print("Method 'show' not found in object")

a = A()
b = B()
call_method(a)
call_method(b)