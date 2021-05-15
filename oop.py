class Dog:
    fur = "Dark" #CLASS ATTRIBUTES
    def __init__(self, name, age):
        self.name = name #INSTANCE ATTRIBUTE
        self.age = age

    def bark(self):
        import time

        print()


my_dog = Dog(name = "Busky", age = 34)
my_dog2 = Dog(name = "Busky", age = 34)
print(type(my_dog))
print(my_dog.name)
