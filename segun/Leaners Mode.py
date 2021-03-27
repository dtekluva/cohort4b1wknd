# number = -20

# print("Original- :", number)
# print("Abs - ", abs(number))

# numbers = [2,4,1,7,2,2,10]
# print(min(numbers)) # 

# numbers = [2,4,1,7,2,2,10]
# print(max(numbers))

# # print(max("AsholankeP"))
# # print(max("Aa"))

# name = "           Adefarasin Adebayo"
# print(len(name))

# stuff = ["shoe", "bags", "belts", ["rice", "beans", "garri"]]
# print(len(stuff))

# file = open("atha/journal.txt", "r")
# # print(file) # returns a raw object that has not been read
# # # print(file.read())
# # print(type(file.read()))

# data =  file.read()
# print(len(data))

# val = "32"
# casted_val= int(val) # type casting in this case from string to integer

# print(val * 2)
# print(casted_val * 2)

# # TYPE CONVERSION OR TYPE CASTING

# from typing import Tuple


# number = "300"
# print(number * 4)

# converted_num = int(number)# RETURNS A WHOLE NUMBER OF CONVERTED NUMBER
# print(converted_num * 4)

# float_num = float(number) # RETURNS A DECIMAL OF CONVERTED NUMBER
# print(float_num * 4)

# # RANGE FUNCTION

# my_numbers = range(10,20) # RANGE TAKES IN THREE ARGUMENTS (START - STOP - STEP)
# print(my_numbers)  # RANGE BY DEFAULT RETURNS AN OBJECT SHOWING ITS RANGE BUT NOT THE ACTUALVALUES IN THE RANGE I.E A GENERATOR.
# print(list(my_numbers)) # THE RETURN VALUE OF RANGE HAS TO BE CONVERTED TO A LIST IN ORDER TO GET THE ACTUAL VALUES IN THE RANGE

# my_leap_years = range(1980, 2020, 4) # ADDING A THIRD ARGUMENT SETS A STEP TO BE TAKEN BY THE RANGE METHOD.
# print(list(my_leap_years))
# print(tuple(my_leap_years))
# print(set(my_leap_years))

# # REVERSED

# my_name = "mat"
# reversed_name = reversed(my_name)
# print(list(reversed_name))

# # ROUND 

# pi = 22/7
# print(pi)

# rounded_pi = round(pi, 2) # ROUND TAKES 2 PARAMETERS - A VALUE , - A DECIMAL PLACES
# print(rounded_pi)

# # SORTED

# numbers = [23,1,4,1,6,22,0,9]
# print(sorted(numbers))

# students = [["ade", 90], ["sam", 66], ["john", 99], ["lisa", 77]]
# print(sorted(students))


# # SUM
# # SUMS ALL VALUES OF AN ITERABLE

# numbers = [23,1,4,1,6,22,0,9]
# print(sum(numbers))

# # DICT

# # DICT TAKES KEYWORD ARGUMENTS AND CREATES A DICTIONARY OUT OF THEM

# my_students = dict(ali = 1000, kunle = 22111, sam = 90000, sola = 320100)
# print(my_students)
# print(my_students["ali"])

# BOOL BUILTIN FUNC

# BOOL -> BOOLEAN CONVERTS EVERYTHING INTO A BOOLEAN VALUE I.E TRUE OR FALSE

# print(bool(1))
# print(bool(-1))
# print(bool(10))
# print(bool(0))
# print(bool([]))
# print(bool(["ade"]))
# print(bool("ade"))
# print(bool(""))
# print(bool(" "))

# MAP

# MAP TAKES IN A FUNCTION AND AN ITERABLE AND CARRIES OUT THE FUNCTION ON EVERY MEMBER OF THE ITERABLE

# words = ["salami", "tunde", "salau", "winston", "john"]

# length_of_words = map(len, words)
# mapped_object = length_of_words
# unravelled_object = list(mapped_object)
# print(unravelled_object)

# reversed_words = map(reversed, words)

# def reverse_for_real(value):
#     return list(reversed(value))

# mapped_object = map(reverse_for_real, words)

# unravelled_object = list(mapped_object)
# print(unravelled_object)

# words = ["salami", "tunde", "salau", "winston", "john"]

# def add_salutation(name):

#     name_plus_salutation = "Mrs " + name.title()
    
#     return name_plus_salutation

# # saluted_name = add_salutation("ebere")

# # print(saluted_name)

# print(list(map(add_salutation, words)))


# def add_number(name):
#     return name + " -> " + str(len(name))

# print(list(map(add_number, words)))

# METHOD (STRING METHODS)

# string = "I am a boy and my name is john"
# string2 = "       Jonah   "
# csv= "a,b,c,d,e,f"

# lower_case_version = string.lower() # RETURNS LOWER CASE OF A STRING
# print(lower_case_version)

# upper_case_version = string.upper() # RETURNS LOWER CASE OF A STRING
# print(upper_case_version)

# print(string2)
# print(string2.strip())

# replaced_vers = string.replace("boy", "girl")
# print(replaced_vers)

# splitted_string = string.split(" ")
# print(splitted_string)

# splitted_csv = csv.split(",")
# print(splitted_csv)

# print(",".join(splitted_csv)) # joins a list of strings with a specified delimiter


# # join CAN BE USED TO JOIN A REVERSED STRING BACK INTO ITS NATURAL FORM (ONE LINER)

# print("".join(list(reversed("alade"))))

# join CAN BE USED TO JOIN A REVERSED STRING BACK INTO ITS NATURAL FORM (BROKEN DOWN)

# value_to_be_reversed = "alade"
# reversed_value = list(reversed("alade"))

# joined_value = "".join(reversed_value)
# print(joined_value)

# INPUT BUILTIN FUNCTION

# age = 32
# age = input("Please enter your age : ")
# print("Your age is ", age)


# print("Welcome to my string reverser. HAHAHAHA!!!.\n")
# value_to_be_reversed = input("Please enter text to be reversed : ")
# reversed_value = list(reversed(value_to_be_reversed))

# joined_value = "".join(reversed_value)
# print(joined_value)

# print("Welcome to my string splitter. HAHAHAHA!!!.\n")
# value_to_be_splited = input("Please enter text to be splitted : ")
# splitted_value = value_to_be_splited.split("-")


# print(",".join(splitted_value)) # joins a list of strings with a specified delimiter


# print("Welcome to my string splitter. HAHAHAHA!!!.\n")
# value_to_be_splited = input("Please enter text to be splitted : ")
# splitted_value = value_to_be_splited.split("-")


# print(splitted_value)
# print(splitted_value[0])
# print(splitted_value[1])

# year_of_birth = int(splitted_value[0])
# age = 2021 - year_of_birth
# print("Hello you are", age, "years old.")


# SIMPLE EXERCISES

# num1 = input("Please enter num-1 > ")
# num2 = input("Please enter num-2 > ")

# print(num1, num2)
# print(int(num1) + int(num2))
# print(int(num1) * int(num2))
# print(sum([int(num1),int(num2)]))
# input()