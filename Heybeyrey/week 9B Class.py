# USER-DEFINED FUNCTIONS
# # you can import a workbook=worksheet = name space inside another namespace

# import helpers
# from helpers import helper1     # this is to import the sub-folder
# from helpers import *   # this is to import every variable in helpers ie the import asterisks
# print(helper1)           #use this if imported the sub-folder

# # ORRRR

# import helpers
# print (helpers. helper1)


# from helpers import helper1, helper2 


# The zen of Python: call up python, type import this and run
# to import namespace, all files must me in the same folder/path

import week_2_class       # the nomenclature must not have space
print (week_2_class.new_word)


x = 50
def ordinary ():           #function creation. ordinary = function name, () = parameter
    x=30
    print(x)
ordinary()       # untill ordinary is initialed/called upon, x = 30 and line 28 print(x) will not run. This is called a function call. Note the indentation of the ordinary. 
print(x)


def ordinary (y):           
    x=30
    print(x*y)
ordinary(20)       

def f():
    s = "-- Inside f()"
    print(s)
f()

    # so you can either define your arguments inside  the function, on the call function. But not ourside the function biko so that when calling the function, you are clear as to where the figures will pick from especially if they have the same variable name as other variables outside the function. Guess I didnt ge this knowledge in class when I did this.
 x = [1,2,3,4,5]                     
# y = [9,8,7,6,5]       
# Sx = set(x)
# Sy = set(y)
# def f(Sx,Sy):
#     intersect = Sx.intersection(Sy)
#     print(bool(intersect))
# f(Sx,Sy)


# ORRRR

def check_intersection (x,y):
    Sx = set(x)
    Sy = set(y)
    intersect = Sx.intersection(Sy)
    print(bool(intersect))
check_intersection([1,2,3,4,5], [9,8,7,6,5])    






































