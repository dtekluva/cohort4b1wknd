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