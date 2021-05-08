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

def check_intersect(list_a, list_b):

    set_a = set(list_a) # convert lists to set in order to use intersect functionlity from sets
    set_b = set(list_b)

    intersect = set_a.intersection(set_b)
    print(intersect)
    print("A and B a have atleast 1 common values: ", bool(intersect))

check_intersect([1,2,3], [5, 6,7]) 