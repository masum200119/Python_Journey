class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name= name
        self.age =age
    
dog1=Dog("ally", 2)
dog2=Dog("bobby", 3)

dog1.name= "kukur"
Dog.species = "Canis lupus familiaris"
print(dog1.species)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)