class Dog:
    fur = "Dark" # class attribute

    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

    def bark(self):
        import time

        print("woof")
        time.sleep(1)
        print("woof")
        time.sleep(1)
        print("woof")
        time.sleep(1)
        print(f"I am {self.name}")

my_dog = Dog(name = "Busky", age = 34)
my_dog2 = Dog(name = "Bingo", age = 34)
# print(type(my_dog))
print(my_dog.name)
my_dog.bark()
my_dog2.bark()