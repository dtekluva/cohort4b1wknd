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

def case_counter(string):

    upcases = 0
    lowercases = 0

    for char in string:
        # print(char, char.isupper(), char.islower())

        if char.islower():
            lowercases += 1
        elif char.isupper():
            upcases += 1

    print(upcases, lowercases)

case_counter("How are you Bolade.")