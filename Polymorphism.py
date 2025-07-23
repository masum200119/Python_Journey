class Dog:
    def sound(self):
        print("dog sound")

class A(Dog):
    def sound(self):
        print("A sound")

class B(Dog):
    def sound(self):
        print("B sound")
dog= [Dog(), A(), B()]
for d in dog:
    d.sound()

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c 

calc = Calculator()
print(calc.add(5, 10))
print(calc.add(5, 10, 15))