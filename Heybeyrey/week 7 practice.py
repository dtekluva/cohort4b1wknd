# i = 100
# total_item = 0
# while i < 1000:
#     i+=1
#     mulp_i= i*3
#     istr = str(i)
#     lastcha = str(i)[2]
#     lastchaerr = str(lastcha*3)
#     if mulp_i == int(lastchaerr):
#         print(i, mulp_i, lastcha, lastchaerr)
#         total_item +=1
# print(total_item)     #this is to count the total number of items found
        
# #     # print(i, mulp_i)
# #     # print(mulp_i, lastcha)
# #     # lastcha = str(i)            #integer objects are not subscriptable, that's why we split them to string
# #     # lastchaind = lastcha[2]
# #     # print(lastchaind)
# #     # print(i, mulp_i, lastchaind)


# # # DICTIONARY COLLECTION
# # d = {"foo":1, "bar":2, "baz":3}
# # # print(d)        # this will print both the keys and values as is
# # # for x in d:
# #     # print(x)    #this will print only the keys    
# #     # print(d[x])    #this one will print only the values.....n/b but ONLY WITH SQUARE BRACKETS
# # # but to print values and items, I prefer to just use the .values() and the .item() function. They are easier
# # for x in d.values():    #this one will also give you the values ie using the .values() end function
# #     print(x)

# # for x in d.items():#just as .values() function prints only the values, .items() function prints both keys and values
# #     print(x)

# # #now we can see that we can use other sub-functions inside the for loop eg: reversed, .values(), .items(), range,etc

# # # for x in range(6):
# # #     print(x)

# # # for x in range(7):
# # #     print("* " * x)
# # # for x in range(7,0,-1):
# # #     print("* "*x)

# # for i in range (100, 401):
#     # if i%2==0:
#     #     print(i)
#     # i_str = str(i)     #just as in the exhaustive enumeration, to break an integer into subscrits, we convert to str
#     # i0 = int(i_str[0])   #if we didnt convert to str, we would get an error message not not all str were converted
#     # i1 = int(i_str[1])
#     # i2 = int(i_str[2])
#     # # if i0%2==0 and i1%2==0 and i2%2==0 and i2 !=0:
#     #     # print(i0,i1,i2, sep='-')
#     # mapping = map(lambda i: i0%2 == 0,i1%2 == 0,i2%2 == 0 [i0,i1,i2])
#     # if all(mapping):
#     #     print(i, end = ", ")
#         # print(i)
    

# #UNION OF @ SETS:...........now we have learnt how to use the .union function OR?AND the | center slash function
# x1 = {'foo', 'bar', 'baz'}
# x2 = {'baz', 'qux', 'quux'}

# print(x1.union(x2))
# # {'foo', 'qux', 'quux', 'baz', 'bar'}
# #ORRRRR
# print(x1 | x2)
# # {'foo', 'qux', 'quux', 'baz', 'bar'}

# # print(x1|x2|x3|x4) etc ie you can get the union common set of more than one variable
# # print(x1 & x2 & x3 & x4) etc ie you can get the intersection common set of more than one variable

# print(x1.intersection(x2))
# {'baz'}

# print(x1 & x2)       #this is the short form for intersection
# {'baz'}
# # example 2:
# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5}
# c = {3, 4, 5, 6}
# d = {4, 5, 6, 7}

# >>> a.intersection(b, c, d)    # for intersection
# {4}

# >>> a & b & c & d         # for intersection
# {4}


# >>> x1.difference(x2)
# {'foo', 'bar'}

# >>> x1 - x2
# {'foo', 'bar'}

# >>> x1 = {'foo', 'bar', 'baz'}
# >>> x2 = {'baz', 'qux', 'quux'}

# >>> x1.symmetric_difference(x2)
# {'foo', 'qux', 'quux', 'bar'}

# >>> x1 ^ x2         # The ^ operator also allows more than two sets:
# {'foo', 'qux', 'quux', 'bar'}

# # x1.isdisjoint(x2) returns True if x1 and x2 have no elements in common:

#  x1 = {1, 3, 5}
# >>> x2 = {2, 4, 6}

# >>> x1.isdisjoint(x2)
# True
# >>> x1 & x2     # There is no operator that corresponds to the .isdisjoint() method.
# set()

# # set is very wide ooo, just as it is in further maths. other functions includes subset and supersets of sets. refer to the line in readme for more on modifications of sets.

# # x.pop() removes items one after another while x.clear() removes all the elements from a set

# # frozen set is like normal set just that it does not carry out some set operations such as .pop(), .clear(), .add(), etc cos these functions have the capacity to alter the original frozen set and frozen sets don't change.

# >>> x = frozenset(['foo', 'bar', 'baz'])
# >>> x
# frozenset({'foo', 'baz', 'bar'})

# >>> len(x)
# 3

# >>> x & {'baz', 'qux', 'quux'}
# frozenset({'baz'})

# >>> x = frozenset(['foo', 'bar', 'baz'])

# >>> x.add('qux')
# Traceback (most recent call last):
#   File "<pyshell#127>", line 1, in <module>
#     x.add('qux')
# AttributeError: 'frozenset' object has no attribute 'add'

# >>> x.pop()
# Traceback (most recent call last):
#   File "<pyshell#129>", line 1, in <module>
#     x.pop()
# AttributeError: 'frozenset' object has no attribute 'pop'

# >>> x.clear()
# Traceback (most recent call last):
#   File "<pyshell#131>", line 1, in <module>
#     x.clear()
# AttributeError: 'frozenset' object has no attribute 'clear'

# >>> x
# frozenset({'foo', 'bar', 'baz'})


# >>> f = frozenset(['foo', 'bar', 'baz'])
# >>> s = {'baz', 'qux', 'quux'}

# >>> f &= s
# >>> f
# frozenset({'baz'})
# What gives?

# Python does not perform augmented assignments on frozensets in place. The statement x &= s is effectively equivalent to x = x & s. It isn’t modifying the original x. It is reassigning x to a new object, and the object x originally referenced is gone.


















































