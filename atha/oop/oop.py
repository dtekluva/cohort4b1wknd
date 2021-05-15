# class Dog:
#     fur = "Dark" # class attribute

#     def __init__(self, name, age):
#         self.name = name   # instance attribute
#         self.age = age

#     def bark(self):
#         import time

#         print("woof")
#         time.sleep(1)
#         print("woof")
#         time.sleep(1)
#         print("woof")
#         time.sleep(1)
#         print(f"I am {self.name}")

# my_dog = Dog(name = "Busky", age = 34)
# my_dog2 = Dog(name = "Bingo", age = 34)
# # print(type(my_dog))
# print(my_dog.name)
# my_dog.bark()
# my_dog2.bark()

# base empty class with not functionality
# class Statement_Analyzer():
#     pass

# analyzer1 = Statement_Analyzer()
# print(analyzer1)

# # MORE FUNCTIONAL CLASS THAT REQUIRES ARGUMENT PATH
# class Statement_Analyzer():
    
#     def __init__(self, path):
#         self.path = path
#         self.file = open(path, "r")


# path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b1wknd\materials\statement2.csv"

# analyzer1 = Statement_Analyzer(path)
# print(analyzer1)
# print(analyzer1.path)
# print(analyzer1.file)

# MORE FUNCTIONAL CLASS THAT REQUIRES ARGUMENT PATH AND MORE METHODS
# class Statement_Analyzer():
    
#     def __init__(self, path):
#         self.path = path
#         self.file = open(path, "r")

#     def get_count_of_transaction(self, target_amount_min, target_amount_max, target_column, description_col):

#         statement_file = self.file.readlines()
#         header = statement_file.pop(0) #remove first element or row from read file
#         count_500 = 0
#         sum_of_target =0

#         withdrawal_list = [header]

#         for line in statement_file:

#             splitted_line = line.split(",")
#             withdrawal = splitted_line[target_column]
#             float_withdrawal = float(withdrawal)

#             description = splitted_line[description_col]

#             if float_withdrawal <= target_amount_max and float_withdrawal >= target_amount_min:
#                 print(float_withdrawal, description, sep = "                 ")
#                 count_500 += 1
#                 sum_of_target += float_withdrawal
#                 withdrawal_list.append(line)

#         print(f"Total target : ", count_500)
#         print(f"Sum of target : ", sum_of_target)

#         # return withdrawal_list




# path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b1wknd\materials\statement2.csv"

# analyzer1 = Statement_Analyzer(path)
# # print(analyzer1)
# # print(analyzer1.path)
# # print(analyzer1.file)
# print(analyzer1.get_count_of_transaction(500, 10000, 3, 6))



# class Human():

#     hands = 2
#     legs = 2
#     eyes = 2
#     nose = 2
#     fur = False

#     def describe(self):
#         print(f""" 
#                     Hello I have no name.
#                     But I have 
#                     {self.hands} hands,
#                     {self.eyes} eyes,
#                     {self.nose} nose,
#                     {self.fur} fur
#                 """)


# # ade = Human()
# # print(ade.describe())


# # INHERITED EVOLVED MAN

# class Mordern_Man(Human): # INHERITED CLASS IS PUT IN PARENTHESIS

#     def __init__(self, name):
#         self.name = name
    
# john = Mordern_Man(name = "John")
# john.describe()


# # INHERITED EVOLVED MAN EVOLVES MORE WITH THE ADDITION OF NAME TO THE DESCRIBE METHOD

# class Mordern_Man(Human): # INHERITED CLASS IS PUT IN PARENTHESIS
    
#     def __init__(self, name):
#         self.name = name

#     # DESCRIBE METHOD IS MORPHED TO ADD NAME ( POLYMORPHISM )
#     def describe(self):
#         print(f""" 
#                     Hello my name is {self.name}.
#                     But I have 
#                     {self.hands} hands,
#                     {self.eyes} eyes,
#                     {self.nose} nose,
#                     {self.fur} fur
#                 """)
    
# dele = Mordern_Man(name = "dele")
# dele.describe()

# mordern_men = ["Kunle",
#                 "Saheed",
#                 "Mummy"]

# for man in mordern_men:
#     person = Mordern_Man(name = man)
#     person.describe()

# CREATE A CLASS OF DOG WITH ATTRIBUTES BARK AND DESCRIBE
# INHERIT FROM THE CLASS WITH NEW SUB CLASSES BULLDOG AND TERRIER AND MORPH TO HAVE THE ATTRIBUTE BREED TYPE IN THE DESCRIPTION












# import time

# name ="kunle"

# name = str("kunle")

# class Person(object):

#     """
#         This is a Person class that did not help anybody. Thanks.!
#     """

#     name = "Atha" # CLASS ATTRIBUTES
#     age = 25 # CLASS ATTRIBUTES

#     def __init__(self, username):
#         self.address = "19, Kunle Afolabi, Somolu."
#         self.phone = "08031346306"
#         self.username = username

#     def walk(self):
#         print("I am walking...")
#         time.sleep(2)
#         print("I am walking...")
#         time.sleep(2)
#         print("I am walking...")

#     def __str__(self):
#         return self.name + "-" + self.username

# man = Person(username = "Lone_warior2x")
# man2 = Person(username = "tiger_roaring_like_a_goat")
# print(man.age)
# print(type(man))
# print(type(name))

# print("Man Object dict --> ", man.__dict__)
# print("Person Class dict --> ", Person.__dict__)

# print(man.username)
# print(man2.username)

# man.username = "xtreme_funmonger"
# print(man.username)
# print(Person.walk())  # BOUND METHOD CAN NOT BE ACCESSED FROM THE CLASS BUT ONLY FROM THE OBJECT
# print(Person("boluwizzy").walk()) 
# print(Person.username) 
# print(man)
# print(man2)


##############################################
###### SIMPLE DICE GAME WITH 2 PLAYERS #######
##############################################

# import random , time

# class Player():

#     def __init__(self, username):
#         self.username = username
#         self.score = 0

#     def roll_dice(self):
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)

#         self.score += die1
#         self.score += die2

#         print(f"{self.username} - Die1- {die1}, Die2- {die2}")

#     def __str__(self):
#         return self.username + " | Score -> " + str(self.score)

# class Game():

#     def __init__(self, player1, player2, max_score = 50):
#         self.max_score = max_score
#         self.player1 = player1
#         self.player2 = player2

#     def play(self):

#         while True:
#             for player in self.player1, self.player2:

#                 player.roll_dice()

#             if self.player1.score >= self.max_score:
#                 print(self.player1, " HAS WON THE GAME")

#                 print()
#                 print(self.player1, self.player2)

#                 break

#             elif self.player2.score >= self.max_score:
#                 print(self.player2, " HAS WON THE GAME")

#                 print()
#                 print(self.player1, self.player2)

#                 break
#             time.sleep(1)

    

# new_player = Player(username = "sekilala")
# new_player2 = Player(username = "kunleswagger")

# new_game = Game(new_player, new_player2)
# new_game.play()
# print(new_player)
# print(new_player2)

# __STR__ METHOD

# class Boy:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

# junior = Boy("junior")
# print((junior))

# class PayRoll():

#     def display_payroll(self, *employees):

#         total_salaries = 0

#         for employee in employees:

#             total_salaries += employee.get_salary()

#             print(employee.name.rjust(15), employee.get_salary())

#         print("\n\nTotal Salaries Due : ", total_salaries)

# class Employee():

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def get_salary(self):
#         return self.salary

# # kunle = Employee("kunle", 2000)
# # print(kunle.get_salary())

# class ManagementStaff(Employee):

#     def __init__(self, name, salary):
#         super().__init__(name, salary)

# class CleaningStaff(Employee):

#     def __init__(self, name, salary):
#         super().__init__(name, salary)

#     def get_salary(self):
#         self.salary = self.salary * 4
#         return super().get_salary()

# class Consultant(Employee):
    
#     def __init__(self, name, commision, qty_sold, salary = 0):

#         self.commision = commision
#         self.qty_sold = qty_sold
#         super().__init__(name, salary)

#     def get_salary(self):

#         self.salary = self.commision * self.qty_sold * 100000
#         return super().get_salary()

# sunbo = ManagementStaff("sunbo", 13000)
# # print(sunbo.get_salary())

# seki = CleaningStaff("seki", 5000)
# # print(seki.get_salary())

# ceci_williams = Consultant("ceci_williams", 0.2, 13)
# tokunbo = Consultant("tokunbo", 0.4, 50)
# # print(ceci_williams.get_salary())

# payroll_man = PayRoll()

# payroll_man.display_payroll(sunbo, seki, ceci_williams, tokunbo)
