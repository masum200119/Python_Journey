class A:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name:", self.name)
class B(A):
    def sound(self):
        print("Sound: Woof Woof")

class C(B):
    def guide(self):
        print("Guiding the owner")

class X:
    def fr(self):
        print("Friendly")

class GoldenRetriever(A, X):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

b= C("masum")
b.display()
b.sound()