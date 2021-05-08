# NAMESPACING

# import helpers # importing namespace as a whole
# from helpers import * # import all available values from names without namespace itself
# from helpers import helper1, helper2 # import just a specific value from namespace


# print(helpers.helper1) # use this if imported with first format
# print(helper1) # use this if imported with second format you actually have access to all variables from namespace
x = 50

# def ordinary(): # function creation
#     x = 30
#     print(x)

# ordinary() # function call
# # print(x)
# # print(x)

# def ordinary(y): # function creation wtith one parameter y
#     x = 30
#     print(x, y)

# ordinary(23) # function call
# # print(x)
# # print(x)

# def ordinary(y): # function creation wtith one parameter y
#     x = 30
#     print(x * y)

# y = 2
# ordinary(y+5) # function call
# print(x)
# print(x)

# def check_intersect(list_a, list_b):

#     set_a = set(list_a) # convert lists to set in order to use intersect functionlity from sets
#     set_b = set(list_b)

#     intersect = set_a.intersection(set_b)
#     print(intersect)
#     print("A and B a have atleast 1 common values: ", bool(intersect))

# check_intersect([1,2,3], [5, 6,7]) 

# string = "my text"
# def reverse_text(string):

#     reversed_str  = string[::-1]
#     print(reversed_str)

# reverse_text(string)

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor

# word = "Hello Mr Samuel Okon"

# upcases = 0
# lowercases = 0

# for char in word:
#     print(char, char.isupper(), char.islower())

#     if char.islower():
#         lowercases += 1
#     elif char.isupper():
#         upcases += 1

# print(upcases, lowercases)

# def case_counter(string):

#     upcases = 0
#     lowercases = 0

#     for char in string:
#         # print(char, char.isupper(), char.islower())

#         if char.islower():
#             lowercases += 1
#         elif char.isupper():
#             upcases += 1

#     print(upcases, lowercases)

# case_counter("How are you Bolade.")

# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b1wknd\materials\statement2.csv" #make to get you correspinding file path

# # statement_file = open(file=file_path, mode = "r") # calling open builtin function using keyword argument

# statement_file = open(file_path, "r")# calling open builtin function using positional argument

# statement = statement_file.readlines()# Reads line after line
# # statement = file.read()# reads character by character
# # print(statement)

# for line in statement:
#     print(line)
#     print("\n\n")


# # GOING FURTHERR TO PRINT JUST LODGEMENTS IN OPENED STATEMENT

# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b1wknd\materials\statement2.csv" #make to get you correspinding file path


# statement_file = open(file_path, "r")# calling open builtin function using positional argument

# for line in statement_file:

#     splitted_line = line.split(",")
#     lodgement = splitted_line[4]
#     description = splitted_line[6]
#     # print(line.split(",")[4])
#     # print("\n\n")
#     print(lodgement, description, sep = "            ")

# # GOING FURTHER TO COUNT AND PRINT JUST WITHDRAWALS OF N50

# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b1wknd\materials\statement2.csv" #make to get you correspinding file path


# statement_file = open(file_path, "r")# calling open builtin function using positional argument
# count_500 = 0

# for line in statement_file:

#     splitted_line = line.split(",")
#     withdrawal = splitted_line[3]
#     description = splitted_line[6]

#     if withdrawal == "50.00":
#         print(description)
#         count_500 += 1

# print(count_500)

# CONVERT TO A FUNCTION

file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b1wknd\materials\statement2.csv" #make to get you correspinding file path

def get_count_of_transaction(file_path, target_amount, target_column, description_col):

    statement_file = open(file_path, "r")# calling open builtin function using positional argument
    count_500 = 0

    for line in statement_file:

        splitted_line = line.split(",")
        withdrawal = splitted_line[target_column]
        description = splitted_line[description_col]

        if withdrawal == target_amount:
            print(description)
            count_500 += 1

    print(f"Total {target_amount} : ", count_500)

get_count_of_transaction(file_path, "500.00", 3, 6)