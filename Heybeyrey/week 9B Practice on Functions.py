# # # in the first function we did in week 4 or 3, we defined and used the return statement. In this one, we are calling out the fuction ()
# # # any() is also a built-in function, same with Zip, sort,and,count, etc
# # # This means that when you write code within a function, you can use variable names and identifiers without worrying about whether they’re already used elsewhere outside the function. This helps minimize errors in code considerably.
# # # Both a function definition and a function call must always include parentheses, even if they’re empty.


# # # def market_list(q, p):    # I just defined a simple demand function. market_list is a function of Q and P parameters
# # #     dd = q*p
# # #     # q = 50           # so you can either define your arguments inside  the function, on the call function. But not ourside the function biko so that when calling the function, you are clear as to where the figures will pick from especially if they have the same variable name as other variables outside the function
# # #     # p =20
# # #     print(dd)
# # # market_list(50,20)    # note the indentatio of my call function

# # # Types/Ways of passing an Argument:

# # # 1. POSITIONAL ARGUMENTS
# # def market_list(q, p):    
# #     dd = q*p
# #     print(dd)
# # market_list(50,20)              #This is the position when calling a function

# # # With positional arguments, the arguments in the call and the parameters in the definition must agree not only in order but in number as well. That’s the reason positional arguments are also referred to as required arguments. You can’t leave any out when calling the function nor state more arguments than required. you'll get and error

# # # 2. KEYWORD ARGUMENTS
# # def market_list(q, p, name):    
# #     dd = q*p
# #     print(f'Ade\'s expense is ${dd}')        #use the backward slash to escape implication quotation marks
# # market_list(q =50,p=20,name ='ade')    # Referencing a keyword that doesn’t match any of the declared parameters generates an exception. Using keyword arguments lifts the restriction on argument order. Each keyword argument explicitly designates a specific parameter by name, so you can specify them in any order and Python will still know which argument goes with which parameter.


# # # 3. COMBINATION OF POSITIONAL AND KEYWORD ARGUMENTS
# # def market_list(q, p, name):    
# #     dd = q*p
# #     print(f'Ade\'s expense is ${dd}')        
# # market_list(50,25,name ='ade')   # When positional and keyword arguments are both present, all the positional arguments must come first, if not it'll give you an error. ie Once you’ve specified a keyword argument, there can’t be any positional arguments to the right of it.


# # # Types/Ways of writing parameters:
# # # 1. NORMAL WAY
# # def market_list(q, p, name):         # this is where we define the parameters of the function
# #     dd = q*p
# #     print(f'Ade\'s expense is ${dd}')        
# # market_list(50,25,name ='ade')


# # #2. ABNORMAL WAY         why would any normal person wanna go the abnormal way? I hate clogging my parameters. keep it as simple as possible and define every other thing insde the body of the function
# # def market_list(q=50, p=6, name='ade'):         
# #     dd = q*p
# #     print(f'Ade\'s expense is ${dd}')        
# # market_list(q=50, p=6, name='ade')

# # # When this version of f() is called, any argument that’s left out assumes its default value:
# # def market_list(q=50, p=6, name='ade'):         
# #     dd = q*p
# #     print(f'Ade\'s expense is ${dd}')        
# # market_list(q=50, p=6 )
 

# # # Default Parameters
# # # If a parameter specified in a Python function definition has the form <name>=<value>, then <value> becomes a default value for that parameter. Parameters defined this way are referred to as default or optional parameters. An example of a function definition with default parameters is shown below:

# # # >>> def f(qty=6, item='bananas', price=1.74):
# # # ...     print(f'{qty} {item} cost ${price:.2f}')
# # # ...
# # # When this version of f() is called, any argument that’s left out assumes its default value:

# # # >>> f(4, 'apples', 2.24)
# # # 4 apples cost $2.24
# # # >>> f(4, 'apples')
# # # 4 apples cost $1.74

# # # >>> f(4)
# # # 4 bananas cost $1.74
# # # >>> f()
# # # 6 bananas cost $1.74

# # # >>> f(item='kumquats', qty=9)
# # # 9 kumquats cost $1.74
# # # >>> f(price=2.29)
# # # 6 bananas cost $2.29

# # # subsequently, anywhere you call the function, it will answer you. # market_list(50, 50)
# # market_list(50, 50)

# # IT IS IMPOSSIBLE TO REPLACE THE PARAMETERS IN A FUNCTION. 
# # def f(fx):
# #     fx= 10
# # x= 5
# # f(x)          this is a new function callable such that x ==fx
# # print(x)

# # def f(fx):
# #     print('fx =', fx, '/ id(fx) = ', id(fx))
# #     fx = 10
# #     print('fx =', fx, '/ id(fx) = ', id(fx))
# # x = 5
# # print('x =', x, '/ id(x) = ', id(x))
# # # x = 5 / id(x) =  1357924048

# # f(x)           # running this replacement function will show that fx as 5 != fx as 10
# # # fx = 5 / id(fx) =  1357924048
# # # fx = 10 / id(fx) =  1357924128

# # print('x =', x, '/ id(x) = ', id(x))
# # x = 5 / id(x) =  1357924048

# # ANOTHER EXAMPLE: the connection between x and i here is lost
# # def f(x):
# #     x = 'foo'
# # for i in ( 40, dict(foo=1, bar=2), {1, 2, 3},'bar', ['foo', 'bar', 'baz']):
# #     f(i)    now you want x as foo to be replace with the values of i. the connection is lost already
# #     print(i)


# # ONLY POSSIBLE SCENARIO; is to use x index to make a similar index replacement in my_list. lol, but why?
# # def f(x):
# #     x[0] = '---'
# # my_list = ['foo', 'bar', 'baz', 'qux']
# # f(my_list)          this means we want the value of x replaced with values of my_list
# # print(my_list)
# # # ['---', 'bar', 'baz', 'qux']


# # ONLY POSSIBLE SCENARIO 2; is to use x index to make a similar index replacement in my_lis
# def f(x):
#     x[2] = 56
# my_list = ['foo', 'bar', 'baz', 'qux']
# f(my_list)
# print(my_list)

# # example 3: here, we wanna replace an item in a dictionary
# def f(x):
#     x['bar'] = 22
# my_list = {'foo': 1, 'bar': 2, 'baz': 3}
# f(my_list)            # this means we want the value of x replaced with values of my_list
# print(my_list)
# # {'foo': 1, 'bar': 22, 'baz': 3}


# # Side Effects
# # So, in Python, it’s possible for you to modify an argument from within a function so that the change is reflected in the calling environment. But should you do this? This is an example of what’s referred to in programming lingo as a side effect.

# # More generally, a Python function is said to cause a side effect if it modifies its calling environment in any way. Changing the value of a function argument is just one of the possibilities.
# # When they’re hidden or unexpected, side effects can lead to program errors that are very difficult to track down. Generally, it’s best to avoid them.

# # So HOW THEN DO WE UPDATE ARGUMENTS??? ANS: BY USING THE RETURN FUNCTION!
# # First of all, A return statement in a Python function serves two purposes:
# # It immediately TERMINATE the function and passes execution control back to the caller.
# # It provides a mechanism by which the function can pass data back to the caller.

# # CASE 1: TO TERMINATE A FUNCTIO IF TRUE:
# def f(x):
#     if x < 0: 
#         return        # lol, this also works like the break function
#     if x > 100:
#         return
#     print(x)
# f(-5)                # first call
# f(65)                # second call



# # CASE 2: TO UPDATE ARGUMENTS AND PASS DATA BACK TO THE CALLER:
# def f():
#     return 'foo'  # this means return foo whenever they call f(x)
# s = f()    
# print(s)       # with this replacement, we have to print s and not to call on f() as we did in our dd function above


# # ANOTHER EXAMPLE:
def f():
    return dict(foo=1, bar=2, baz=3)   # with the use of the return statement, we have to print f() and not just call on f()
z = f()
print(z)
# # {'foo': 1, 'bar': 2, 'baz': 3}
# print(f()['baz'])
# # 3



# When no return value is given, a Python function returns the special Python value None:

# >>> def f():
# ...     return
# ...

# >>> print(f())
# None
# The same thing happens if the function body doesn’t contain a return statement at all and the function falls off the end:

# >>> def g():
# ...     pass
# ...

# >>> print(g())
# None

#ANOTHER EXAMPLE WITH MULTIPLICATION. BASICALLY JUST DEFINE A FUNCTION AND TELL IT WHAT IT SHOULD RETURN FOR YOU
# def double():
#     x=5
#     return x*2      # the return function does not use parathesis
# print(double())

#ORRRR

# def double(x):
#     return x*2
# x=5
# y = double(x)
# print(y)


# ANOTHER EXAMPLE:  (lo la cram la paste)
# def multiple(x):
#     r = []
#     for i in x:
#         r.append(i*2)
#     return r
# a = [1,2,3,4,5]
# a = multiple(a)
# print(a)

#ORRRRR
# def multiple(x):
#     i = 0
#     while i < len(x):
#         x[i]*= 2
#         i+=1
# x = [1,2,3,4,5]
# multiple(x)
# print(x)


# def multiple(x):
#     i = 0
#     while i < len(x):
#         x[i]*= x[i]
#         i+=1
# x = [1,2,3,4,5]
# multiple(x)
# print(x)

#VARIABLE LENGHT ARGUMENT LIST

# def avg(a,b,c):
#     average = (a+b+c)/3
#     print(average)
# avg(20,30,55)

# to do this for an unknown number of arguments

# def avg(x):
#     total = 0
#     for i in x:
#         total += i
#     return total/len(x)
# print(avg([1,2,3,4,5,5]))        #because this your parameter is what you are going to call.

# t = (2,3,4,5,9)
# print(avg(t))                  # so we can call up this function any time we need it. Great




# def avg(x):
#     total = 0
#     for i in x:
#         total += i
#         return total/len(x)    # this one did 1/3 cos the return is under the first round total
# print(avg([1,2,3]))

def avg(x):
    return sum(x)/len(x)
print(avg([1,2,3,4,7]))        # the [] is to convert the tuple to one positional argument

#ORRRRRR
# def avg(*x):                  # the * means pick everything = argument packing. So no [] nor * in calling the function. single asterisks is for list, tuple and set packing. Double asterisks ** is for dictionary packing ie pack both the keys and values.
#     return sum(x)/len(x)      # just as from helper import * = means import everything
# print(avg(1,2,3,4,7))

t = ([1,2,3,5,7.8,9.5])           #Call the function any where  and it will answer you.
print(avg(t))        # if you used return funftion then in calling the function, you'll have to print it. buy if no return function was used, then just call the function and it will answer you.

# single asterisks is for list, tuple and set packing. Double asterisks ** is for dictionary packing ie pack both the keys and values.

def f(a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')


d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)
# a = foo
# b = 25
# c = qux









































































































































































