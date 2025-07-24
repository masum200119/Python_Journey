class A:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def display(self):
        print(f"Name: {self.__name}")
        print(f"Name (via getter): {self.get_name()}")

s1 = A("Alice")
s1.display()